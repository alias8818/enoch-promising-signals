# N-gram draft speculative decoding for local inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-draft-speculative-decoding-for-local-inference-d201d059639d`
Run ID: `n-gram-draft-speculative-decoding-for-local-inference-d201d059639d-20260607T144249442543+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ec992d4816f3

## What looked useful

On fixed structured traces, the best n=3 draft-length=16 setting reduced conservative target calls from 752 to 569 (24.3%, 1.32x upper-bound target-call speedup) with median per-trace reduction 25.3% and p10 0.0%. On GPT-2 generated traces, the same family of settings reached 70.6% reduction, but inspection showed repeated phrases, so this is a mechanism check rather than a serving claim.

## Boundaries and scale limits

No integrated decoder or serving engine was benchmarked; no wall-clock speedup claim is made. Model-generated traces were small and repetition-heavy, and the strongest distilGPT2 result was degenerate newline repetition. Fixed structured controls used tokenizer traces rather than target-model-generated text.

## Claim scope

Trace-replay evidence on small GPT-family greedy continuations and fixed structured code/config/SQL/runbook continuations shows that an autoregressive most-recent n-gram drafter can reduce conservative target verifier calls when outputs contain local repetition.

## Why it stopped

Trace-based proxy supports the mechanism but does not provide publication-grade or end-to-end local inference evidence; strongest model-generated effects are inflated by repetition.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is an integrated verifier benchmark that measures real wall-clock tokens/sec and output equivalence on non-degenerate local instruction-model prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Integrated n-gram speculative decoding benchmark for local instruction-model inference
- Success threshold: At least 10% median wall-clock tokens/sec improvement over baseline greedy decoding on structured/code-heavy prompts, no output mismatches, and no more than 5% slowdown on low-repetition controls.
- Stop condition: Stop as negative if integrated overhead erases target-call savings or if low-repetition controls show frequent slowdowns above 5%.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-draft-speculative-decoding-for-local-inference-d201d059639d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
