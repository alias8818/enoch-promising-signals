# Lookahead-Jacobi Decoding with N-Gram Pool (CPU)

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `lookahead-jacobi-decoding-with-n-gram-pool-cpu-462c0aab1d50`
Run ID: `lookahead-jacobi-decoding-with-n-gram-pool-cpu-462c0aab1d50-20260629T132712831482+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c3f67e44b264

## What looked useful

N-gram-pool Jacobi block-8 achieved 1.481x mean model-round speedup over sequential greedy across five seeds, versus 1.140x for naive Jacobi, with a 1.299x mean relative gain over the best naive variant and zero exact-match failures observed.

## Boundaries and scale limits

Synthetic CPU-only proxy; no real transformer, no GPU or batched serving latency, no natural-language benchmark, and no KV-cache or production inference-engine measurements.

## Claim scope

On a deterministic synthetic n-gram language-model proxy, lookahead-Jacobi greedy decoding with an n-gram proposal pool preserved exact sequential greedy outputs and reduced model rounds more than a naive Jacobi proposal across five seeds.

## Why it stopped

Reproducible mechanism signal was obtained, but it is a synthetic CPU proxy rather than direct transformer-serving evidence, so it is not paper-ready.

## Recommended next action

Stop this run as useful no-paper evidence; next bounded test should implement the same verifier against a small open transformer and measure real acceptance, exact-match preservation, and wall-clock latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer lookahead-Jacobi n-gram pool validation
- Success threshold: At least 1.2x wall-clock latency improvement over sequential greedy and at least 1.15x improvement over naive Jacobi on the same prompts with exact output match rate 1.0.
- Stop condition: Stop if exact output match falls below 1.0, n-gram acceptance is not better than naive Jacobi, or verification overhead eliminates wall-clock speedup.

## Evidence references

- Artifact root: `<local-path>/projects/lookahead-jacobi-decoding-with-n-gram-pool-cpu-462c0aab1d50`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
