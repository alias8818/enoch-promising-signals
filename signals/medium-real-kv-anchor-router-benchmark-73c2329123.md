# Medium real-KV anchor router benchmark

Status: `compute_scale_blocked`
Curation bucket: `compute_scale_blocked`
Curation score: `83`
Project ID: `medium-real-kv-anchor-router-benchmark-73c2329123`
Run ID: `medium-real-kv-anchor-router-benchmark-73c2329123-20260515T105622866571+0000`

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

- Internal Enoch project: Medium real-KV anchor router benchmark: internal_generated:medium-real-kv-anchor-router-benchmark-73c2329123

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Medium direct benchmark on real distilgpt2 WikiText K/V tensors found high attention-mass recovery but routed attention was slower than exact full attention, so the paper-level speed claim is unsupported.

## Recommended next action

Stop this run as no-paper: the medium real-KV benchmark supports anchor routing fidelity but directly fails the latency requirement at this scale; only a bounded optimized long-context follow-up could overturn the speed result.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Optimized long-context real-KV anchor router benchmark
- Success threshold: Across fixed seeds, optimized anchor routing must show >= 1.25x mean latency speedup versus exact full attention with cosine >= 0.95, attention mass >= 0.85, and no worse than 5% regression in top-token recall against the best non-oracle control at comparable selected-token budget.
- Stop condition: Stop negative if optimized routing remains <= 1.0x speedup versus exact full attention or if meeting the speed threshold requires cosine < 0.95 or attention mass < 0.85.

## Evidence references

- Artifact root: `<local-path>/projects/medium-real-kv-anchor-router-benchmark-73c2329123`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
