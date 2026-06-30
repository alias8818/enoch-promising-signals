# CPU N-Gram Speculative Decoding for Tiny Transformers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-speculative-decoding-for-tiny-transformers-eb2e967fc66c`
Run ID: `cpu-n-gram-speculative-decoding-for-tiny-transformers-eb2e967fc66c-20260604T062145594166+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/06693430aed3

## What looked useful

CPU n-gram drafting is very effective for exact repeated spans (up to 15.5x target-call reduction in the repetitive control) but weak on natural text (best 1.065x target-call reduction, about 79.6% no-draft iterations), making it unlikely to be a general tiny-transformer CPU accelerator without workload repetition.

## Boundaries and scale limits

No real tiny-transformer runtime was installed under Python 3.14, no KV-cache or vectorized verification path was measured, and results are limited to 256-token generations with 1024-token prompts on one CPU worker.

## Claim scope

Bounded proxy benchmark of CPU history n-gram speculative drafting over Tiny Shakespeare and a repetitive control corpus; measures exact-match acceptance and implied target-call reduction, not real transformer wall-clock speed.

## Why it stopped

Proxy evidence is mixed and not paper-positive: strong on repetitive control, weak on natural-text acceptance, and no direct transformer latency validation.

## Recommended next action

Stop as no-paper useful signal; the only justified next step is a bounded direct CPU tiny-transformer wall-clock benchmark in a compatible runtime.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU tiny-transformer n-gram speculative decoding benchmark
- Success threshold: At least 1.2x end-to-end tokens/s improvement on copy-heavy prompts with no more than 2% slowdown on ordinary prompts and exact output equivalence to greedy decoding.
- Stop condition: Stop if natural or copy-heavy prompts fail to exceed 1.05x end-to-end speedup after a correct vectorized verification implementation.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-speculative-decoding-for-tiny-transformers-eb2e967fc66c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
