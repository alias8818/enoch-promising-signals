# Medium KV-cache validation of n-gram fallback speculative decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `medium-kv-cache-validation-of-n-gram-fallback-speculative-48993b0331`
Run ID: `medium-kv-cache-validation-of-n-gram-fallback-speculative-48993b0331-20260609T214957369993+0000`

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

- Parent run decision: SpecDec with n-gram fallback for low-VRAM speculative decoding: enoch://control-plane/projects/specdec-with-n-gram-fallback-for-low-vram-speculative-decoding-401323b3d1c0/runs/specdec-with-n-gram-fallback-for-low-vram-speculative-decoding-401323b3d1c0-20260609T172035282114+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/2176f6fda42a

## What looked useful

Exact greedy new-token match held for all 3/3 GPT-2-medium cases. Rejection-path cache validation ran 9 fresh-prefix comparisons with max next-logit delta 0.0018291473388671875. Mean production target-call reduction was 53.85%; mean measured speed ratio was 2.40x on this small prompt suite.

## Boundaries and scale limits

One GPT-2-medium model, three hand-written prompts, 64 generated tokens per prompt, greedy decoding only, single-process CUDA inference. No batched serving, sampling, long-context, multi-model, corpus-level, modern DynamicCache, or production-kernel validation.

## Claim scope

Tier 1 controlled direct test: on cached gpt2-medium with three short prompts and greedy decoding, n-gram fallback speculative decoding preserved exact generated tokens and maintained usable KV-cache state across accepted and rejected drafts while reducing production target calls.

## Why it stopped

Tier 1 direct validation succeeded but remains small-scale mechanism evidence rather than publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up on a larger prompt corpus and at least two model families, using both greedy and sampling verification, before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Corpus-level KV-cache validation for n-gram speculative fallback
- Success threshold: Exact greedy token equivalence on 100% of prompts; no sampling distribution mismatch beyond test tolerance; cache-vs-fresh diagnostics never change argmax tokens; at least 20% mean production target-call reduction on high-repetition prompts; no more than 10% production target-call overhead on low-repetition controls.
- Stop condition: Stop if any exactness violation or cache-truncation token instability is found, or if high-repetition prompts fail to achieve 20% mean production target-call reduction under the fixed harness.

## Evidence references

- Artifact root: `<local-path>/projects/medium-kv-cache-validation-of-n-gram-fallback-speculative-48993b0331`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
