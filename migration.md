# Migration analysis: what-if-data-donation → data-donation-task v2

This document analyses the differences between the extraction logic in
`what-if-data-donation` and the current `data-donation-task` v2 architecture, and
lists the concrete steps needed to migrate successfully. The migration covers all
five platforms: Instagram, Facebook, TikTok, Twitter, and YouTube. Instagram is
used as the worked example throughout.

---

## 1. What we are migrating from

The old repo (`what-if-data-donation`) has one active implementation per platform,
all living under `donation_flows/`:

| File | Role |
|------|------|
| `donation_flows/instagram.py` | Active; wired into `script.py`; data-driven via `IG_ENTRIES` |
| `donation_flows/facebook.py` | Active; wired into `script.py`; same pattern |
| `donation_flows/tiktok.py` | Active; wired into `script.py`; same pattern |
| `donation_flows/twitter.py` | Active; wired into `script.py`; same pattern |
| `donation_flows/youtube.py` | Active; wired into `script.py`; same pattern |

The repo also contains a `platforms/` directory with partial FlowBuilder rewrites,
but these are lingering artefacts from a previous migration attempt and are not used.
They can be ignored entirely.

---

## 2. Architectural differences

### 2.1 Driver script

| Dimension | Old `script.py` | New `script.py` |
|-----------|----------------|----------------|
| Platform selection | Runtime radio-button UI if `platform` arg is absent | Compile-time registry; `VITE_PLATFORM` env var for single-platform builds |
| Dispatch | `if platform == "Instagram": ...` chains | Registry loop with lazy `import_module()` |
| File payload type | `PayloadString` (WORKERFS path) | `PayloadFile` (browser File object, written to `/tmp` by `ScriptWrapper`) |
| Logging to host | All Python `logging` output collected by `DataFrameHandler` and donated as `{session_id}-log` | Only explicit `yield from ph.emit_log(...)` calls; no raw log messages leave the browser |
| Donation key | `{session_id}` | `{session_id}-{platform_name.lower()}` |
| End of script | `yield ph.exit(0, "Success")` | `yield ph.render_end_page()` |
| Error handling | Unhandled exceptions propagate to JS | `ScriptWrapper` catches all exceptions, routes through `error_flow` with participant consent before reporting traceback |

### 2.2 Validation

| Dimension | Old `donation_flows/` | New `platforms/` |
|-----------|----------------------|-----------------|
| Mechanism | `has_file_in_zip(path, "*.json")` — any `.json` file present | `validate.validate_zip(DDP_CATEGORIES, path)` |
| Threshold | Presence of a single file | >5% of `known_files` found |
| Archive members cached | No | Yes, in `ValidateInput.archive_members` |

The old `donation_flows/` validation accepts any zip that contains a `.json` file —
including completely wrong archives. The new `DDPCategory` approach correctly rejects
zips that do not match the expected platform structure.

### 2.3 File access

| Dimension | Old `donation_flows/` | New `platforms/` |
|-----------|----------------------|-----------------|
| Zip handling | `find_file_in_zip()` per file (re-opens zip every call) | Single `ZipArchiveReader` passed to all functions |
| Member list | Re-enumerated every call | Cached from validation step, never re-enumerated |
| Member resolution | `fnmatch` glob pattern | Exact match first; path-boundary suffix fallback; multi-match → None + error |

In the new code, all extractor functions receive a shared `reader: ZipArchiveReader`
and `errors: Counter` — the zip is opened and enumerated only once per run.

### 2.4 Error handling

| Dimension | Old `donation_flows/` | New `platforms/` |
|-----------|----------------------|-----------------|
| Per-function exceptions | `logging.exception(...)` | `logger.error(...)` + `errors[type(e).__name__] += 1` |
| Caller visibility | None (error is swallowed) | `ExtractionResult.errors` Counter propagated to FlowBuilder |
| Host visibility | Via `DataFrameHandler` log donation (includes message text — potential PII) | Type name + count only, via `emit_log` (PII-safe) |

### 2.5 Return type of `extract_data()`

The old `donation_flows/` functions return a `PropsUIPromptConsentFormViz` (the full
consent form prompt, assembled by `donation_flow()`). The new `FlowBuilder` expects
`extract_data()` to return an `ExtractionResult(tables, errors)` and assembles the
consent form itself. Generators are also supported — FlowBuilder checks
`isinstance(raw_result, Generator)` and calls `yield from` if needed.

### 2.6 Instagram export format support

Instagram changed its export JSON structure around 2023–2024. The old
`donation_flows/` code was built against the older format; the new code handles both.

| Format | Old `donation_flows/` | New `platforms/` |
|--------|----------------------|-----------------|
| Old: dict with `string_map_data` per item | Yes (via `IG_ENTRIES` path definitions) | Yes |
| New: top-level list with `label_values` | No | Yes (via `_extract_owner_details`) |
| Bilingual keys (`"Author"` / `"Auteur"`, `"Time"` / `"Tijd"`) | Partially (hardcoded paths in `IG_ENTRIES`) | Yes (via `_first_present(data, ["Author", "Auteur"])`) |

The same format shift applies to Facebook and other platforms — check each one.

### 2.7 `post_comments` pagination (Instagram)

| Old `donation_flows/` | New `platforms/` |
|----------------------|-----------------|
| Not handled in `IG_ENTRIES` (single-file entry) | `reader.json_all(r"(^|/)post_comments(?:_\d+)?\.json$")` |
| Misses paginated exports (`post_comments_1.json`, `_2.json`, ...) | Matches all pages including no-suffix variant |

### 2.8 Table coverage

| Source | Tables extracted |
|--------|----------------|
| Old `donation_flows/instagram.py` (via `IG_ENTRIES`) | ~80+ tables defined in the master Excel sheet; `IG_ENTRIES` is its generated output |
| New `platforms/instagram.py` | 12 tables (followers, following, ads viewed, posts viewed, videos watched, post comments, liked comments, liked posts, profile searches, story likes, threads viewed, saved posts) |

The other four platforms follow the same pattern — each has its own `*_ENTRIES` dict
generated from the same Excel sheet.

The `donation_flows/` approach also donates a **structure table** — every JSON file
in the zip with values replaced by type names (`"string"`, `"number"`, etc.). This
has no equivalent in the new code and is a genuinely unique feature worth deciding
on explicitly during migration (see [section 4](#4-decisions-to-make)).

### 2.9 Logging

The most significant behavioural difference is how logging reaches the researcher's
server.

**Old approach:** A `DataFrameHandler` is attached to Python's root logger at module
import time in `script.py`. Every `logging.info(...)` / `logging.error(...)` call
across the entire codebase is captured into a DataFrame and donated to the server as
`{session_id}-log` (and `-log1`, `-log2` around the main donation). These messages
include file paths, exception text, and byte counts — potential PII.

**New approach:** Standard `logging.getLogger(...)` output stays in the browser
DevTools console only (Pyodide worker stderr). Only explicit `yield from
ph.emit_log(level, message)` calls leave the browser, and by convention those must
be PII-free (platform name, counts, outcome labels only).

This is not just a refactor — it is a privacy-boundary change. After migration,
researchers who relied on the server-side log donations for debugging will need to
use browser DevTools instead, or introduce structured `emit_log` calls for the
specific milestones they want to observe server-side.

---

## 3. Migration checklist

Each item below is a concrete code change required. They are ordered from
foundational to detail-level.

### 3.1 `extract_data()` — return type

**Required.** Change the return type of `extraction()` from
`list[PropsUIPromptConsentFormTableViz]` to `ExtractionResult`.

```python
# Before (old platforms/)
def extraction(instagram_zip: str) -> list[d3i_props.PropsUIPromptConsentFormTableViz]:
    tables = [...]
    return [table for table in tables if not table.data_frame.empty]

# After (new)
def extraction(instagram_zip: str, validation) -> ExtractionResult:
    errors = Counter()
    reader = ZipArchiveReader(instagram_zip, validation.archive_members, errors)
    tables = [...]
    return ExtractionResult(
        tables=[table for table in tables if not table.data_frame.empty],
        errors=errors,
    )
```

### 3.2 `extract_data()` — signature

**Required.** The new `FlowBuilder.extract_data()` signature is:

```python
def extract_data(self, file: str, validation: validate.ValidateInput) -> ExtractionResult:
```

The `validation` argument must be passed through to `ZipArchiveReader` so it can use
the cached `archive_members` from the validation step rather than re-enumerating the
zip.

### 3.3 Extractor functions — switch to `ZipArchiveReader`

**Required.** The old `donation_flows/` approach uses `find_file_in_zip()` / `read_json()`
via the `readers.py` helpers. Replace these with `reader.json(filename)` from
`ZipArchiveReader`. The same applies to CSV files (`reader.csv()`) and raw/binary
files (`reader.raw()`).

```python
# Before (donation_flows pattern via readers.py)
def ads_viewed_to_df(file_input: list[str]) -> pd.DataFrame:
    data = read_json(file_input, ["ads_viewed.json"])
    ...

# After
def ads_viewed_to_df(reader: ZipArchiveReader, errors: Counter) -> pd.DataFrame:
    result = reader.json("ads_viewed.json")
    if not result.found:
        return pd.DataFrame()
    data = result.data
    ...
```

All functions must accept `reader: ZipArchiveReader` and `errors: Counter`. The
`errors` Counter is shared — pass the same instance to every function, and
`ZipArchiveReader` will also write to it internally when member resolution fails.

### 3.4 Error handling — add `errors` counting

**Required.** In every `except` block, add the error counter increment:

```python
# Before
except Exception as e:
    logger.error("Exception caught: %s", e)

# After
except Exception as e:
    logger.error("Exception caught: %s", e)
    errors[type(e).__name__] += 1
```

### 3.5 `post_comments` — fix pagination (Instagram)

**Required.** The old `donation_flows/` `IG_ENTRIES` defines a single entry for
`post_comments.json` and does not handle the paginated `post_comments_1.json`,
`post_comments_2.json`, ... variants. Use `reader.json_all()` with a regex:

```python
# After
results = reader.json_all(r"(^|/)post_comments(?:_\d+)?\.json$")
if not results:
    return pd.DataFrame()
for result in results:
    data = result.data
    items = data if isinstance(data, list) else data.get("comments_media_comments", [])
    ...
```

Check whether equivalent pagination issues exist in other platforms (TikTok, YouTube,
etc.) and apply the same fix where needed.

### 3.6 New Instagram export format support

**Recommended.** The old extractor functions only handle the `string_map_data` format.
Participants with newer Instagram exports will get empty tables. Add handling for the
`label_values` format in at minimum `ads_viewed_to_df`, `posts_viewed_to_df`, and
`videos_watched_to_df`. The new `data-donation-task` implementation of these
functions is the reference.

Key helpers to copy from the new `platforms/instagram.py`:
- `_extract_owner_details(label_values)` — recursive tree walker for the new format
- `_first_present(data, keys)` — tries multiple dict keys for bilingual support

### 3.7 `DDP_CATEGORIES` — define `known_files` per platform

**Required.** The old `donation_flows/` code does not use `DDPCategory` at all — it
accepts any zip containing a `.json` file. The new architecture requires a
`DDP_CATEGORIES` list for each platform, used by `validate.validate_zip()` to check
whether the uploaded zip is likely the right DDP.

For Instagram, the new `data-donation-task` `DDP_CATEGORIES` contains 39 known
files. Use it as the starting point and extend it if your Excel sheet defines tables
from files not yet in the list. Do the same for each of the other four platforms —
each needs its own `DDP_CATEGORIES`.

### 3.8 Logging — replace `DataFrameHandler`

**Required.** The `DataFrameHandler` and the three `ph.donate(...-log...)` calls in
`script.py` have no equivalent in the new architecture and must be removed. They will
not work because:
- `script.py` no longer drives individual platforms; each platform has its own flow
- The new `ScriptWrapper` in `main.py` is the exception boundary; any exception that
  previously would have been logged is now routed through `error_flow`

For server-side observability, introduce explicit `emit_log` calls in your
`InstagramFlow` at the milestones you care about. `FlowBuilder.start_flow()`
already emits logs at every major step (file received, validation, extraction
summary, consent, donation result), so no additional calls may be needed.

### 3.9 `session_id` type

**Minor.** The new `FlowBuilder` takes `session_id: str`. Check whether the host
passes an int or a string and update accordingly.

### 3.10 Tables — write one extractor function per table per platform

**Required.** For each platform, the Excel sheet defines which tables to extract.
Each table needs a dedicated `*_to_df(reader, errors)` function and a corresponding
`PropsUIPromptConsentFormTableViz` entry in `extraction()`. This replaces the
`IG_ENTRIES` / `create_table()` mechanism entirely. The new `platforms/instagram.py`
in `data-donation-task` is the reference implementation for how these functions
should be structured.

---

## 4. Decisions to make

### 4.1 Structure donation

`donation_flows/instagram.py` donates a schema snapshot — every JSON file in the zip
with values replaced by their type names. This has research value for tracking how
Instagram's export format evolves over time without collecting participant data.

**Options:**

A. **Drop it.** Accept that you lose the structural metadata. Simplest migration path.

B. **Keep it as a separate table.** Add a `structure_to_df()` function to
   `platforms/instagram.py` that calls `structure_from_zip()` and wraps the result
   in a DataFrame. Include it in the `extraction()` table list.

C. **Keep it as a separate donation.** Override `start_flow()` in `InstagramFlow` or
   add a post-donation step to `extract_data()` that yields a separate
   `CommandSystemDonate` for the structure data.

### 4.2 `IG_ENTRIES` tables not in `platforms/`

The `donation_flows/` extractor covers many tables the curated `platforms/` version
does not: Archived Posts, Blocked Profiles, Emoji Sliders, Countdowns, Consents,
Ad Interests, Story Reactions, etc.

**Decide per table:** is this data scientifically relevant to your study? If yes,
write a dedicated extractor function for it and add it to `extraction()`. If no,
leave it out. `IG_ENTRIES` is generated from the curated master Excel sheet — that
sheet is the specification, and any table defined there represents a deliberate
research choice. When deciding what to carry forward, consult the Excel sheet rather
than reading `entries_data.py` directly.

### 4.3 Tables in the Excel sheet not in the new reference implementation

The master Excel sheet may define tables that the new `data-donation-task` reference
implementation does not include (e.g. `accounts_you're_not_interested_in`,
`posts_you're_not_interested_in` for Instagram, or platform-specific tables for
Facebook, TikTok, Twitter, YouTube). These need to be written as new extractor
functions — they have no ready-made equivalent to copy from.

### 4.4 Donation key

The old code uses `{session_id}` as the key (same for all platforms). The new code
uses `{session_id}-instagram`. If your backend storage or analysis scripts depend on
the old key format, update them before or alongside the migration.

---

## 5. Migration order

A suggested safe order that lets you test incrementally. Work one platform at a time;
Instagram is the natural first one given it is the worked example here.

1. **Decisions first** (section 4) — resolve the open questions before writing code,
   especially the structure donation and which Excel-sheet tables to carry forward
2. **`DDP_CATEGORIES`** (3.7) — define `known_files` for the platform; verify
   validation passes on a real DDP and rejects a wrong zip
3. **Scaffold `extraction()`** (3.1, 3.2, 3.10) — create the `ExtractionResult`
   skeleton with a `ZipArchiveReader` and empty table list; confirm `FlowBuilder`
   accepts it end-to-end
4. **Write extractor functions** (3.3, 3.4) — one `*_to_df(reader, errors)` per
   table from the Excel sheet; add `errors` counting to every `except` block
5. **Pagination** (3.5) — fix any multi-file tables (at minimum `post_comments` for
   Instagram); check other platforms for the same issue
6. **New export format** (3.6) — add `label_values` handling; test with a newer DDP
7. **Logging cleanup** (3.8) — remove `DataFrameHandler` and log donation calls
8. **Repeat for remaining platforms** — Facebook, TikTok, Twitter, YouTube
9. **Integration test** — run `pnpm start` with a real DDP per platform; verify
   tables, donation keys, and that no log donations appear in server-side data
