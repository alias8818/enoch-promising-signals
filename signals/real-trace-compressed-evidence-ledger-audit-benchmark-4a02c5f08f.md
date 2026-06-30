# Real-trace compressed evidence ledger audit benchmark

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-trace-compressed-evidence-ledger-audit-benchmark-4a02c5f08f`
Run ID: `real-trace-compressed-evidence-ledger-audit-benchmark-4a02c5f08f-20260523T030724663942+0000`

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

- Parent run decision: Compressed Agent Evidence Ledger: enoch://control-plane/projects/compressed-agent-evidence-ledger-29c1b399cf1c/runs/compressed-agent-evidence-ledger-29c1b399cf1c-20260523T022605364766+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b356e38b90fa

## What looked useful

The Tier 1 direct mechanism threshold was met: both ledgers verified, all tested tamper modes were detected, and raw trace storage fell by 71.25-73.05%. The ledger remained 1.99-2.55x larger than plain gzip, so the result supports auditability with compression but not a paper-positive compression-efficiency claim.

## Boundaries and scale limits

Only two local strace workloads were tested; binary ledger size is estimated from compressed payload bytes plus compact metadata rather than a standalone binary file format; no public trace corpus, signed external root, semantic audit queries, large-scale throughput test, or adversarial root-substitution model was evaluated.

## Claim scope

On two controlled local real syscall traces, a 64-event chunked zlib evidence ledger with per-chunk hash-chain links verified untampered traces, detected payload mutation, chunk deletion, and chunk reordering, and reduced binary ledger storage by at least 71.247% versus raw trace text.

## Why it stopped

Tier 1 useful mechanism signal achieved, but evidence is too narrow and gzip overhead too high for paper-positive closure.

## Recommended next action

Run a bounded deepen benchmark with a real binary serializer on a small public trace corpus and require both audit tamper detection and ledger size no more than 1.3x gzip before considering a paper path.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Binary evidence ledger corpus benchmark against gzip and zstd controls
- Success threshold: Across all trace families, untampered verification succeeds, all tamper classes except explicit full-root recomputation are detected, storage is at least 70% below raw, and ledger size is no more than 1.3x the best gzip/zstd compression-only baseline.
- Stop condition: Stop negative if any trace family exceeds 1.5x the best compression-only baseline or if any non-root-substitution tamper class is not detected.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-compressed-evidence-ledger-audit-benchmark-4a02c5f08f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
