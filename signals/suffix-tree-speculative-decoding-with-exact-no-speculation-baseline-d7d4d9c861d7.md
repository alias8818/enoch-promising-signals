# Suffix-tree speculative decoding with exact no-speculation baseline

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-speculative-decoding-with-exact-no-speculation-baseline-d7d4d9c861d7`
Run ID: `suffix-tree-speculative-decoding-with-exact-no-speculation-baseline-d7d4d9c861d7-20260621T160519064438+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d9ddc8cc00d2

## What looked useful

Best exact-output theoretical verifier-call speedups were 16.000x on periodic synthetic text, 4.769x on repeated project-prompt text, 2.835x on bursty synthetic text, and 1.000x on random-vocabulary control.

## Boundaries and scale limits

Proxy-only CPU benchmark on 12k-token streams; no real transformer verifier, tokenizer effects, KV-cache behavior, GPU batching, serving latency, or production suffix-tree overhead measured.

## Claim scope

Online suffix-context speculative proposals can preserve exact target output and reduce theoretical verifier calls on repeated token streams; the effect disappears on random-control streams.

## Why it stopped

Proxy benchmark supports the mechanism only on repeated streams and does not provide direct model-serving evidence for a publication claim.

## Recommended next action

Stop this run as no-paper proxy evidence; next bounded action is a small real-model verifier experiment using the same exact acceptance policy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model suffix-index speculative decoding with exact baseline
- Success threshold: Exact output equality on all prompts, at least 1.25x end-to-end tokens/sec improvement and at least 1.5x verifier-call reduction on repeated/retrieval-heavy prompts, with no more than 5% slowdown on natural/control prompts.
- Stop condition: Stop if exact output diverges, if suffix-index overhead eliminates wall-clock gains despite verifier-call reductions, or if natural/control prompts show more than 5% slowdown.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculative-decoding-with-exact-no-speculation-baseline-d7d4d9c861d7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
