# N-gram Cache Speculative Decoding on GB10

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-cache-speculative-decoding-on-gb10-bed808c00b5d`
Run ID: `n-gram-cache-speculative-decoding-on-gb10-bed808c00b5d-20260609T170611151508+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/ef764dcfdc55

## What looked useful

The n-gram cache mechanism produced exact greedy-equivalent outputs while reducing target forwards from 768 to 314 at gamma 4 with 82.62% draft acceptance and a 2.52x local reference wall-time ratio; gamma 8 reduced forwards to 252 with lower 72.68% acceptance.

## Boundaries and scale limits

One 135M model, six hand-written prompts, 128 generated tokens per prompt, reference full-context verification rather than optimized KV-cache serving, no batched serving, no larger-model or corpus-scale validation.

## Claim scope

On a GB10 using HuggingFaceTB/SmolLM2-135M and six fixed short prompts, a longest-match n-gram cache can draft tokens for greedy-equivalent speculative decoding and reduce target forward calls by 39.45% to 67.19% across gamma 2/4/8.

## Why it stopped

This run produced a useful small real-model signal, but the evidence is too scoped and reference-implementation-specific for a paper claim.

## Recommended next action

Run a bounded KV-cache-aware implementation on a repeated-context/code/chat benchmark and compare against greedy plus a standard prompt-lookup or learned-draft baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache-aware n-gram speculative decoding on repeated-context workloads
- Success threshold: At least 1.25x tokens/s improvement over greedy and no output mismatches on the repeated-context subset, with target forwards/token reduced by at least 25% versus greedy.
- Stop condition: Stop if KV-cache maintenance overhead eliminates tokens/s gains or exact greedy equivalence fails under partial acceptance/rejection.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-cache-speculative-decoding-on-gb10-bed808c00b5d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
