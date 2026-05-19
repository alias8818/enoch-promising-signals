# KV-Cache Suffix Array Drafting for VRAM-Free Speculative Decoding

Status: `compute_scale_blocked`
Curation bucket: `compute_scale_blocked`
Curation score: `83`
Project ID: `kv-cache-suffix-array-drafting-for-vram-free-speculative-decoding-503b4aedb46f`
Run ID: `kv-cache-suffix-array-drafting-for-vram-free-speculative-decoding-503b4aedb46f-20260514T161335024139+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Compute-scale blocked
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/408ce29cffcd

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Corpus and BPE-token proxy tests show exact suffix drafting has useful coverage only for very short, low-accuracy suffixes, while reliable longer suffixes are too rare; this is not full validation but is sufficient to reject paper readiness.

## Recommended next action

Stop this run as an early proxy falsification; only a bounded real-LLM trace and end-to-end latency test could overturn the low BPE-token suffix yield observed here.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real LLM Trace Validation for Exact KV-Cache Suffix Drafting
- Success threshold: At L >= 4, demonstrate at least 1.15x wall-clock tokens/s over no-draft decoding on real generated traces, with median accepted length above 0 and no domain-specific prompt leakage.
- Stop condition: Stop if generated-trace BPE accepted tokens per position is below 0.15 for L >= 4 or if end-to-end timing fails to exceed 1.05x after overheads.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-suffix-array-drafting-for-vram-free-speculative-decoding-503b4aedb46f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
