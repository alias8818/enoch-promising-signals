# Optimized exact cache path for GPT-2 intermediate-head self-speculation

Status: `useful_signal`
Project ID: `optimized-exact-cache-path-for-gpt-2-intermediate-head-sel-0692caf722`
Run ID: `optimized-exact-cache-path-for-gpt-2-intermediate-head-sel-0692caf722-20260516T173930604873+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Optimized exact cache path for GPT-2 intermediate-head self-speculation: internal_generated:optimized-exact-cache-path-for-gpt-2-intermediate-head-sel-0692caf722

## What looked useful

Exact lower-cache reuse improves the modeled latency versus a naive no-reuse self-speculation baseline, but the method remains below dense decoding for useful late layers. Layer 10 averaged 0.7865 token acceptance and 0.6615 gamma-2 block acceptance, yet only 0.9321x dense speed in the optimistic exact-cache model with 1.120x serial layer-token work. The best non-final apparent speedup was a non-practical 1.0042x at layer 0/gamma 2 with only 0.0879 token acceptance and 1.8384x serial work.

## Boundaries and scale limits

Validated locally on GPT-2-small only, with 3 fixed WikiText prompt-sampling seeds, 64 prompts per seed, 64 generated tokens per prompt, layers 0/2/5/8/9/10 plus final-layer sanity control, and gamma 2/4/8. Actual split-layer exact-cache kernels, trained auxiliary heads, larger GPT-2 variants, and broader datasets were not implemented.

## Claim scope

For pretrained GPT-2-small with tied intermediate LM heads on WikiText-2 generated-prefix greedy decoding, an optimized exact lower-cache reuse path for intermediate-head self-speculation does not provide a practical speedup over dense cached decoding under an optimistic analytic latency model.

## Why it stopped

Direct GPT-2-small generated-prefix validation with dense and no-reuse baselines did not support a practical speedup claim; evidence is sufficient for no-paper closure but not a universal full-scale negative.

## Recommended next action

Stop this follow-up campaign at depth 4: record the bounded negative/useful signal rather than launching another deepen/retry follow-up; only reopen if a separate implementation provides a trained intermediate head or real exact-cache kernel with a >1.10x dense-baseline target.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/optimized-exact-cache-path-for-gpt-2-intermediate-head-sel-0692caf722`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
