# Anchor-verified compression on real lane-work traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchor-verified-compression-on-real-lane-work-traces-a0d62928e4`
Run ID: `anchor-verified-compression-on-real-lane-work-traces-a0d62928e4-20260612T071155469894+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Semantic State Compression with Anchor Verification for Bounded Lane Work: enoch://control-plane/projects/semantic-state-compression-with-anchor-verification-for-bounded-lane-work-bb56e8a32c40/runs/semantic-state-compression-with-anchor-verification-for-bounded-lane-work-bb56e8a32c40-20260612T014421752358+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f0e02bdbdc90

## What looked useful

Anchor-verified lossy trace compression is mechanically viable on a small real Enoch worker trace: it beats gzipped raw logs by about 51% while retaining verifiable source anchors and detecting source mutation.

## Boundaries and scale limits

Only 2 source files and 26 anchors from a single project/run were tested. This does not validate many worker lanes, long traces, heterogeneous schemas, retrieval quality, or publication-grade robustness.

## Claim scope

On one local real Enoch lane-work trace corpus from this worker run, a compact event-summary package with byte-range SHA-256 anchors compressed to 6.32% of raw bytes with zstd-19, verified all 26 anchors, and detected a one-byte tamper control.

## Why it stopped

Tier 1 direct mechanism test completed successfully, but the evidence is too small and single-run to support a paper.

## Recommended next action

Run a bounded deepen test on at least 50 real lane-work trace files from multiple projects, requiring 100% anchor verification, tamper detection, and anchor-package zstd size below 60% of raw gzip while preserving command/status/output-excerpt retrieval.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchor-verified compression across a multi-project real lane-work trace corpus
- Success threshold: Aggregate anchor-package zstd-19 size below 60% of raw gzip, 100% pre-tamper anchor verification, and 100% detection of injected one-byte tamper cases across the sampled corpus.
- Stop condition: Stop if aggregate package size is at least raw gzip size, any untampered anchor verification fails, or compact summaries omit required command/status/output fields for more than 5% of command events.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-verified-compression-on-real-lane-work-traces-a0d62928e4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
