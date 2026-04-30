---
adr_id: "0007"
comments:
    - author: Danielle McCool
      comment: "1"
      date: "2026-04-30 19:11:46"
    - author: Danielle McCool
      comment: "2"
      date: "2026-04-30 19:11:46"
links:
    precedes: []
    succeeds:
        - "0003"
status: decided
tags:
    - uploads
    - streaming
    - memory-safety
    - file-api
title: Stream PayloadFile uploads end-to-end and never materialize to a path
---

## <a name="question"></a> Context and Problem Statement

The FlowBuilder upload pipeline receives PayloadFile (an AsyncFileAdapter wrapping a browser File via FileReaderSync). The previous materialize_file() helper read the entire file into Python memory then wrote it to Pyodide's in-memory /tmp to produce a path string for downstream extractors. This calls FileReaderSync.readAsArrayBuffer() against the entire blob, which fails with NotReadableError for files above the DOM File API's ~2 GiB ArrayBuffer cap, independent of available RAM. SURF Research Cloud (SRC) no longer requires PayloadString/WORKERFS support, so the dual-payload plumbing introduced in feldspar/AD0003 can be retired. How should the upload pipeline handle PayloadFile to avoid this failure mode and stay aligned with upstream's streaming design?

## <a name="options"></a> Considered Options
1. <a name="option-1"></a> Pass AsyncFileAdapter directly to zipfile.ZipFile and other consumers; delete materialize_file
2. <a name="option-2"></a> Stream materialize_file in chunks to /tmp
3. <a name="option-3"></a> Mount the browser Blob via WORKERFS and return a path string

## <a name="criteria"></a> Decision Drivers
DOM File API caps readAsArrayBuffer at ~2 GiB; full-file reads fail above that limit regardless of available RAM
Upstream eyra/feldspar PR #482 (2025-11-03) explicitly designed AsyncFileAdapter to avoid full-file reads — must preserve that intent
Empirical reproduction on next.eyra.co with a 2.5 GiB Facebook fixture produced NotReadableError, confirming this code path is broken in production (see issue #61)
SRC no longer needs PayloadString; dual-payload plumbing can collapse to a single payload type, shrinking the failure surface
Multi-GiB takeouts (YouTube, Facebook) are routine; the upload path must not impose a ceiling lower than the documented safety check
### Pros and Cons

**Pass AsyncFileAdapter directly to zipfile.ZipFile and other consumers; delete materialize_file**
* Good, because it is the upstream PR #482 design — proven and aligned with eyra/feldspar
* Good, because AsyncFileAdapter already implements the file-like protocol zipfile.ZipFile requires (read, seek, tell, readable, seekable, context-manager)
* Good, because zipfile chunks reads at its own discretion (≤ 1 MiB typical), well below the FileReaderSync cap
* Good, because deleting materialize_file removes the failure surface entirely — no path-producing function exists for a future refactor to call
* Good, because the size check (FileTooLargeError, ChunkedExportError) can move upstream to use adapter.size (JS metadata, no read), so it fires before any byte transfer
* Neutral, because researcher forks still on the WORKERFS path must migrate before consuming this version

**Stream materialize_file in chunks to /tmp**
* Good, because it avoids the FileReaderSync cap by reading slices ≤ chunk size
* Bad, because /tmp is Pyodide's in-memory filesystem — the file is still copied into worker heap, defeating the memory benefit
* Bad, because it preserves the materialize step as a permanent feature, leaving a path-producing function the next refactor can misuse
* Bad, because it adds latency for no extraction benefit — zipfile would re-read /tmp lazily anyway

**Mount the browser Blob via WORKERFS and return a path string**
* Good, because consumers continue to receive a path string (no API change downstream)
* Good, because reads happen lazily from the Blob via the filesystem layer
* Bad, because it routes through a filesystem mechanism the codebase no longer needs (SRC compat dropped) — adds a layer instead of removing one
* Bad, because it preserves PayloadString plumbing that feldspar/AD0003 marked as deprecated, blocking closure of that deprecation window


## <a name="outcome"></a> Decision Outcome
We decided for [Option 1](#option-1) because: Option 1 restores the upstream PR #482 design. AsyncFileAdapter is already a complete file-like object; downstream consumers (zipfile.ZipFile, ZipArchiveReader, validate.validate_zip, parsers) accept it without modification because Python's zipfile takes any seekable binary file-like. Deleting materialize_file removes the failure surface — there is no path-producing function in the upload pipeline left to call. The size guard moves upstream to operate on adapter.size (a JS metadata attribute, no read required), so oversize files are rejected before any byte transfer rather than after a 2 GiB read attempt that the API will refuse. Defense in depth: type tightening on consumer signatures (str → seekable binary protocol) is enforced at the Pyright layer, and a behavioral regression test asserts that AsyncFileAdapter.read is never called with size=-1 from upload-path code. Consequences: the 2 GiB upload ceiling is removed for the read path; mono's HTTP body limit (200 MB default, env-overridable) remains a separate downstream concern for extracted JSON; researcher forks still on the WORKERFS path must migrate to PayloadFile before consuming this version, closing the deprecation window opened by feldspar/AD0003.

## <a name="comments"></a> Comments
<a name="comment-2"></a>2. (2026-04-30 19:11:46) Danielle McCool: More Information:
Succeeds extraction/AD0003 (which placed the size check after materialize, the buggy ordering this ADR corrects). The original AD0003 ownership decision (FlowBuilder owns upload safety, before validation/extraction) remains correct; only the placement of the size check changes. See feldspar/AD0003 for the PayloadFile migration whose intent this ADR enforces. Production reproduction and full diagnosis: https://github.com/d3i-infra/data-donation-task/issues/61. Upstream design: https://github.com/eyra/feldspar/pull/482.
