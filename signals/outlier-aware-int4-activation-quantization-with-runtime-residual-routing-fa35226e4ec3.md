# Outlier-Aware INT4 Activation Quantization with Runtime Residual Routing

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `outlier-aware-int4-activation-quantization-with-runtime-residual-routing-fa35226e4ec3`
Run ID: `outlier-aware-int4-activation-quantization-with-runtime-residual-routing-fa35226e4ec3-20260629T235631939209+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d9402cc56d81

## What looked useful

At <=1% routed density, mean relative output-L2 error fell by 65.4% for lognormal channel spikes and 64.9% for Student-t df=3 activations versus plain per-token INT4. Gaussian reached only 26.5%, and token-burst outliers reached only 28.3% at 1% routing, though token-burst crossed 50% at 2% routing.

## Boundaries and scale limits

Synthetic activations, random linear layers, 128 tokens, 1024 hidden dimension, 1024 output dimension, 3 seeds, CPU NumPy dense proxy. No real transformer activations, perplexity, task quality, optimized INT4 kernel, sparse index overhead, or serving latency validation.

## Claim scope

Bounded NumPy matrix-layer proxy: routing the largest activation elements before per-token INT4 quantization substantially reduces output error for heavy-tailed/global outlier synthetic activations at <=1% routed density, but not for Gaussian activations or bursty token-local outliers under the same route budget.

## Why it stopped

No-paper closure: this is a synthetic CPU proxy with mixed distribution results, useful for deciding the next direct model-trace experiment but insufficient for a paper or full validation.

## Recommended next action

Run a bounded deepen follow-up on real GPT-2-small-class activation traces, measuring projection output error and perplexity/task deltas for fixed versus adaptive residual routing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real transformer activation trace validation for INT4 residual routing
- Success threshold: At <=2% routed density, reduce mean projection output error by >=50% versus plain INT4 on traced real activations and keep end-to-end perplexity degradation at least 30% lower than plain INT4.
- Stop condition: Stop if real activation traces show <25% output-error reduction at 2% routing or if residual metadata/compute overhead exceeds the estimated benefit for small-batch inference.

## Evidence references

- Artifact root: `<local-path>/projects/outlier-aware-int4-activation-quantization-with-runtime-residual-routing-fa35226e4ec3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
