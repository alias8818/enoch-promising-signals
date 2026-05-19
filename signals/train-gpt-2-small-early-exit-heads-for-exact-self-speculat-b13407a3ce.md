# Train GPT-2-small early-exit heads for exact self-speculative acceptance

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `train-gpt-2-small-early-exit-heads-for-exact-self-speculat-b13407a3ce`
Run ID: `train-gpt-2-small-early-exit-heads-for-exact-self-speculat-b13407a3ce-20260516T122203002671+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/d3ba195640b7

## What looked useful

Training early-exit heads directly against the final GPT-2-small greedy decisions produced a clear local mechanism signal: later-layer heads crossed 50% exact one-token acceptance and substantially outperformed applying the frozen final LM head to intermediate activations.

## Boundaries and scale limits

Single model family and checkpoint, WikiText-2 only, one seed, 64 training batches, deterministic greedy one-token acceptance as the primary metric, teacher-forced block diagnostics only, no autoregressive draft rollout, no stochastic exact acceptance-ratio test, and no wall-clock throughput benchmark.

## Claim scope

In a controlled small GPT-2-small/WikiText-2 run, frozen-model linear early-exit heads trained on intermediate hidden states improved exact greedy next-token agreement with the final GPT-2-small argmax by 11.8 to 26.0 percentage points over the tied LM-head control, reaching 58.9% at layer 10 and 61.2% at layer 11 on 16,256 validation positions.

## Why it stopped

No-paper closure: this run provides direct small-scale mechanism support, but it lacks end-to-end speculative decoding and throughput evidence required for a publishable claim.

## Recommended next action

Run a bounded end-to-end GPT-2-small self-speculative decoder test using the trained-head objective, measuring autoregressive draft acceptance, exact final-model verification, output equivalence, and wall-clock tokens/sec against vanilla GPT-2-small decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end GPT-2-small self-speculative decoding with trained early-exit heads
- Success threshold: On at least 1,000 held-out prompts, preserve exact greedy output equality, achieve at least 1.15x wall-clock tokens/sec versus vanilla GPT-2-small greedy decoding, and maintain at least 35% accepted tokens for a draft length of 2 or more.
- Stop condition: Stop if exact output equality fails, accepted-token rate is below 25% for draft length 2, or measured throughput is not above vanilla decoding after implementation overhead is included.

## Evidence references

- Artifact root: `<local-path>/projects/train-gpt-2-small-early-exit-heads-for-exact-self-speculat-b13407a3ce`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
