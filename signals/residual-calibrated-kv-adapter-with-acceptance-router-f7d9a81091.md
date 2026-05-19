# Residual-Calibrated KV Adapter with Acceptance Router

Status: `useful_signal`
Project ID: `residual-calibrated-kv-adapter-with-acceptance-router-f7d9a81091`
Run ID: `residual-calibrated-kv-adapter-with-acceptance-router-f7d9a81091-20260517T232123411448+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b29b30c8532f

## What looked useful

Residual calibration showed consistent attention-context error reduction, while the acceptance router failed the Tier 1 target: only about 5-6% acceptance and 34-39% mean accepted relative error versus a 30% acceptance and <=10% accepted-error threshold.

## Boundaries and scale limits

Small direct activation-only test on distilgpt2 layers 0, 2, and 4; PCA KV bottlenecks proxy a real deployable KV adapter; no autoregressive cache integration, latency measurement, perplexity evaluation, generation-quality evaluation, or larger-model validation.

## Claim scope

On held-out distilgpt2 attention activations from Wikitext-2 text, a residual MLP can reduce compressed-KV attention-context error by roughly 21-26%, but the tested validation-calibrated acceptance router does not find a practically useful low-error accepted subset.

## Why it stopped

Controlled small direct activation tests did not satisfy the acceptance-router threshold; this is not a full serving validation, but it is enough to reject paper readiness for the current mechanism.

## Recommended next action

Stop this run as a no-paper useful signal; a bounded deepen follow-up should test whether stronger router uncertainty features and a deployable cache-style adapter can reach >=30% accepted tokens at <=10% accepted relative attention error.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Router-Calibrated KV Adapter with Cache-Integrated Error Features
- Success threshold: At least 30% router acceptance with accepted mean relative attention-context error <=10%, no more than 1% perplexity regression versus exact KV on the bounded text set, and a measured KV memory or attention-step latency reduction.
- Stop condition: Stop if the router cannot reach 20% acceptance below 15% accepted relative attention error on validation, or if perplexity regresses by more than 2% at any acceptance threshold that yields measurable memory or latency savings.

## Evidence references

- Artifact root: `<local-path>/projects/residual-calibrated-kv-adapter-with-acceptance-router-f7d9a81091`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
