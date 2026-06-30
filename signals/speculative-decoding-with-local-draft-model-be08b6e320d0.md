# Speculative decoding with local draft model

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-decoding-with-local-draft-model-be08b6e320d0`
Run ID: `speculative-decoding-with-local-draft-model-be08b6e320d0-20260605T150735333592+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/0eb48d708acf

## What looked useful

Acceptance rate was 80.73% in the confirmation run and target-call reductions were substantial, but draft overhead dominated: best speculative setting was 0.82x baseline throughput. This suggests local draft speculative decoding needs a much cheaper/optimized draft path or a larger target model before it becomes practically useful.

## Boundaries and scale limits

Small-model, short-prompt, greedy-only benchmark: 4 prompts, 48 new tokens each, draft windows 1/2/4. The implementation is inspectable but not a production KV-cache serving stack, and it does not test large target models, batch serving, sampling, quantized drafts, long contexts, or separate CPU/GPU placement.

## Claim scope

On a GB10 GPU with gpt2 target and distilgpt2 local draft, a simple greedy speculative decoder preserved exact greedy outputs and reduced target forward calls by up to 64.58%, but did not improve wall-clock throughput over the greedy target baseline.

## Why it stopped

Bounded local confirmation found a mixed mechanism/practical result: target-call reduction worked, but wall-clock speedup was negative in the tested setup.

## Recommended next action

Stop this worker run as a no-paper useful signal; the bounded next test is a cache-aware optimized speculative decoder on a larger target model with the same exact-output checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cache-aware speculative decoding with larger target and cheap local draft
- Success threshold: At least 1.2x sustained tokens/sec over warmed greedy baseline with 100% exact greedy-output match and no increase above available memory limits.
- Stop condition: Stop if optimized speculative throughput remains below 1.0x baseline after target-call reduction exceeds 40%, or if exact-output validation fails.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-with-local-draft-model-be08b6e320d0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
