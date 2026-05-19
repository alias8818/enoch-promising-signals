# Router-Calibrated KV Adapter with Cache-Integrated Error Features

Status: `useful_signal`
Project ID: `router-calibrated-kv-adapter-with-cache-integrated-error-f-41199327e2`
Run ID: `router-calibrated-kv-adapter-with-cache-integrated-error-f-41199327e2-20260517T232653444779+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Router-Calibrated KV Adapter with Cache-Integrated Error Features: internal_generated:router-calibrated-kv-adapter-with-cache-integrated-error-f-41199327e2

## What looked useful

Error-feature routing reduced attention MSE by 25.27% and clean-logit KL by 29.44% versus corrupted cache; it beat the same-parameter no-error router on attention MSE and KL in all three seeds, but the incremental gain was modest (mean attention MSE improvement 0.000737 and KL improvement 0.0630).

## Boundaries and scale limits

Single pretrained model, one attention layer, one dataset, post-hoc adapter training, synthetic cache-pressure policy, short 96-token windows, no real serving kernel, no latency/throughput accounting, and no multi-layer or end-to-end generation validation.

## Claim scope

On distilgpt2 block-2 attention over Wikitext-2 with synthetic heterogeneous 2/3/4-bit KV-cache quantization, a low-rank MoE adapter routed by attention-weighted cache-error features modestly improves attention reconstruction and clean-logit KL over uncorrected cache, static low-rank adapter, and a same-structure no-error-feature router across three fixed seeds.

## Why it stopped

No-paper closure: Tier 2 evidence supports a bounded mechanism signal but the margin over the no-error router is small and the validation is too narrow for a publication claim.

## Recommended next action

Run one bounded deepen test with shuffled-error-feature controls and multiple layers/compression policies; stop if error features do not beat no-error routing by at least 2% relative attention MSE and 3% KL reduction on a majority of layer-policy pairs.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Shuffled-error and multi-layer validation for router-calibrated KV adapters
- Success threshold: True error-feature routing beats both no-error and shuffled-error routing by >=2% relative attention MSE and >=3% clean-logit KL on a majority of evaluated layer-policy pairs, with no mean CE regression versus no-error routing.
- Stop condition: Stop as unsupported if shuffled/no-error routing matches or beats true error-feature routing on most layer-policy pairs, or if CE regresses by more than 0.005 mean versus no-error routing.

## Evidence references

- Artifact root: `<local-path>/projects/router-calibrated-kv-adapter-with-cache-integrated-error-f-41199327e2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
