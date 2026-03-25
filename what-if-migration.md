# what-if-migration — handover and status

Branch: `what-if-migration`

This document records what was done, the decisions made, and what remains.
The migration plan that guided this work is in [what-if-migration-plan.md](what-if-migration-plan.md).
The upstream v2 migration guide for downstream forks is in [MIGRATION.md](MIGRATION.md).

---

## What was migrated

Five platforms (`Instagram`, `Facebook`, `X/Twitter`, `TikTok`, `YouTube`) were migrated
from the `donation_flows/` pattern in `what-if-data-donation` to the `FlowBuilder`
architecture in `data-donation-task` v2.

Each platform in `packages/python/port/platforms/` now follows this structure:

- **`DDP_CATEGORIES`** — defines known zip members for validation (replaces the old
  `has_file_in_zip("*.json")` check that accepted any zip with a JSON file)
- **`extract_tables(file, validation, errors)`** — generator that yields
  `PropsUIPromptConsentFormTableViz` objects, with a shared `errors: Counter[str]`
- **`XxxFlow(FlowBuilder)`** — `validate_file()` delegates to `validate.validate_zip()`;
  `extract_data()` creates the counter, calls `extract_tables`, returns
  `ExtractionResult(tables=tables, errors=errors)`

See [MIGRATION.md](MIGRATION.md) ("If you have a custom script.py") for the canonical
description of this pattern.

---

## Commits

| Commit | What |
|--------|------|
| `01f2768` | Instagram: wired to `IG_ENTRIES`, deleted `donation_flows/instagram.py` |
| `50c832f` | Instagram: removed `donation_table` wrapper, direct `PropsUIPromptConsentFormTableViz` |
| `4fc2d38` | Facebook: wired to `FB_ENTRIES`, deleted `donation_flows/facebook.py` |
| `dcf8721` | Facebook: linter formatting |
| `8d3664c` | X/Twitter: wired to `X_ENTRIES`, deleted `donation_flows/twitter.py` |
| `472eb65` | TikTok: wired to `TIKTOK_ENTRIES`, deleted `donation_flows/tiktok.py` |
| `b3a9ea1` | TikTok: added JSON fallback in `validate_file` (TikTok exports as plain JSON or zip) |
| `a333aa0` | YouTube: wired to `YT_ENTRIES`, deleted `donation_flows/youtube.py` |
| `5e6a3c8` | Deleted `donation_flows/` directory and `helpers/donation_flow.py` |
| `ca9cdd9` | Inlined `readers.py` into `parsers.py`, deleted `readers.py` |
| `a9ae353` | `ZipArchiveReader`: added `js()` method and NFC Unicode normalisation |
| `ca86c8c` | All zip platforms: pass shared `ZipArchiveReader` to `create_table()` (zip opened once) |
| `f015428` | Instagram: handle paginated `post_comments_N.json` exports (plan §3.5) |
| `18313e0` | TikTok: wire `errors` counter through `extract_tables` (was silently dropped) |

---

## Decisions made

### Keep all `*_ENTRIES` tables (plan §4.2)

Rather than cherry-picking tables from the Excel sheet, all tables defined in
`IG_ENTRIES` / `FB_ENTRIES` / etc. are carried forward. These dicts are generated from
the master Excel sheet, so every entry already represents a deliberate research choice.

### Keep the structure donation table (plan §4.1, option B)

The old `donation_flows/` code donated a schema snapshot — every JSON file in the zip
with values replaced by type names. This was kept as a table (`id="placeholder"`,
title "Data structure") in each platform's `extract_tables()`. It has research value for
tracking how platform export formats evolve over time without collecting participant data.

### `IG_ENTRIES`-based extraction, not per-table functions (plan §3.10)

The migration plan suggested writing a dedicated `*_to_df()` function per table (the
style used in the upstream reference implementation). We instead retained the
`IG_ENTRIES` / `create_table()` data-driven approach, which is already how
`what-if-data-donation` worked. This avoids rewriting ~80 extractor functions per
platform and keeps the Excel sheet as the single source of truth for table definitions.

### TikTok: no `ZipArchiveReader` (plan §3.3)

TikTok's DDP is a single JSON file (`user_data.json`), not a zip archive.
`ZipArchiveReader` is not used for TikTok; `create_table([file], entries)` reads the
file directly. This is correct and intentional.

### Donation key (plan §4.4)

`FlowBuilder` automatically uses `{session_id}-{platform_name.lower()}` as the donation
key. If backend storage or analysis scripts depend on the old bare `{session_id}` key,
those need to be updated before going live with this build.

### Logging (plan §3.8)

`DataFrameHandler` and the `{session_id}-log` donation calls are gone. Python
`logging.*` output is now browser-console only. `FlowBuilder.start_flow()` emits
structured `emit_log` milestones at every major step (file received, validation,
extraction summary, consent, donation result), so no additional `emit_log` calls were
added. Researchers who relied on server-side log donations for debugging should use
browser DevTools instead.

---

## What remains

### New Instagram export format — `label_values` (plan §3.6) — TODO

Instagram changed its export JSON structure around 2023–2024. The current extractors
only handle the old `string_map_data` format. Participants with newer exports will get
empty tables for affected files.

The format difference:

```
# Old format (string_map_data)
{
  "impressions_history_ads_seen": [
    {"title": "...", "string_map_data": {"Author": {"value": "..."}, "Time": {"timestamp": ...}}}
  ]
}

# New format (label_values)
[
  {"label_values": [{"label": "Author", "value": "..."}, {"label": "Time", "timestamp": ...}]}
]
```

This affects **27 files** across the Instagram DDP — not just `ads_viewed.json` but also
`posts_viewed.json`, `videos_watched.json`, `post_comments_1.json`, `saved_posts.json`,
`personal_information.json`, and more. Any file whose `IG_ENTRIES` tree uses a
`('string_map_data', ...)` path is at risk.

**To check whether a DDP uses the new format:**
```bash
unzip -p your_export.zip ads_viewed.json | python3 -c \
  "import json,sys; d=json.load(sys.stdin); print(type(d), list(d[0].keys()) if isinstance(d, list) else list(d.keys()))"
```
New format prints `<class 'list'>` with `label_values`; old format prints `<class 'dict'>`.

**Blocked on:** obtaining a post-2023 Instagram DDP to test against. Once available,
the fix is to add `label_values` branch handling in the affected extractor paths,
following the helpers described in plan §3.6 (`_extract_owner_details`,
`_first_present`).

### Integration test with real DDPs (plan §5, step 9)

`pnpm test` passes (74/74). `pnpm start` with real DDPs per platform has not been
verified end-to-end. Run with `VITE_PLATFORM=Instagram` (etc.) and check:
- Tables are populated
- Donation key format is `{session_id}-instagram` (not bare `{session_id}`)
- No `*-log` donations appear in server-side data
