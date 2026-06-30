# Suffix-Array Speculative Decoding on CPU for Local Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-array-speculative-decoding-on-cpu-for-local-inference-328f35f346f7`
Run ID: `suffix-array-speculative-decoding-on-cpu-for-local-inference-328f35f346f7-20260619T030732089479+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/2fb0acef370f

## What looked useful

Suffix-array drafting is feasible and non-random for repetitive local contexts, but this run does not show superiority over simpler exact-context tables or end-to-end CPU inference speedup.

## Boundaries and scale limits

No neural target verifier, no real local-LLM tokens/s measurement, small proxy corpora only, and n-gram table control is faster for the tested exact-context workloads.

## Claim scope

Bounded CPU-only mechanism probe: suffix-array exact-context drafting can produce accepted multi-token continuations on repeated local-document streams and modest accepted continuations on structured logs, under an explicit target-call cost model.

## Why it stopped

No-paper useful signal: this was a proxy mechanism benchmark, not full validation, and the n-gram baseline was faster while matching acceptance on the tested workloads.

## Recommended next action

Run a bounded real-verifier follow-up that plugs suffix-array and n-gram drafters into a small CPU autoregressive model loop and measures end-to-end tokens/s on repeated prompt workloads.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU verifier test for suffix-array speculative drafting
- Success threshold: At least 1.25x end-to-end tokens/s over no speculation on repeated local-document prompts, with suffix-array performance within 10% of or better than n-gram drafting, and no regression on non-repetitive controls beyond 5%.
- Stop condition: Stop if real verifier acceptance is below 0.25 mean accepted tokens or end-to-end speedup is below 1.05x on repeated workloads while n-gram drafting is equal or faster.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-speculative-decoding-on-cpu-for-local-inference-328f35f346f7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
