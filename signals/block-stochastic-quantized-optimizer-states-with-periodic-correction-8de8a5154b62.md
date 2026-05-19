# Block-Stochastic Quantized Optimizer States with Periodic Correction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `block-stochastic-quantized-optimizer-states-with-periodic-correction-8de8a5154b62`
Run ID: `block-stochastic-quantized-optimizer-states-with-periodic-correction-8de8a5154b62-20260516T044429630982+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/6eeb1383b126

## What looked useful

Pure blockwise stochastic int8 optimizer states were stable at lr=3e-4 across 5/5 seeds with validation loss 0.791117 versus AdamW 0.793245 and estimated optimizer-state memory ratio 0.254. At lr=1e-3, quantized variants diverged in 1-2/5 seeds while AdamW stayed finite. Periodic correction matched plain stochastic int8 loss but used 0.754x Adam state memory and was slower in the prototype.

## Boundaries and scale limits

Evidence is limited to small synthetic neural regression, 5 seeds, 1000 optimizer steps, Python-level implementation, estimated optimizer-state memory, and no fused kernels or packed production storage. It does not validate large language models, long-horizon training, distributed optimizers, or datacenter-scale throughput.

## Claim scope

On a 102,928-parameter synthetic teacher-regression MLP proxy, blockwise int8 Adam optimizer states with stochastic rounding can match full AdamW validation loss at a reduced learning rate while estimating about 25.4% of fp32 Adam optimizer-state memory. The tested periodic fp16 error-feedback correction did not improve loss or stability over plain stochastic int8 states.

## Why it stopped

Proxy evidence does not support the periodic-correction mechanism: it adds residual-memory and runtime overhead, does not improve loss, and does not prevent lr=1e-3 divergence. This is an early bounded falsification of the correction component, not a full-scale optimizer validation.

## Recommended next action

Stop this project as no-paper useful signal; if continuing locally, test second-moment floor or log-domain v quantization against plain stochastic int8 before any larger model run.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Second-moment stabilization for blockwise stochastic int8 Adam states
- Success threshold: The stabilized variant must have 5/5 finite runs at lr=1e-3, validation loss within 1% of AdamW, estimated optimizer-state memory no more than 30% of fp32 Adam states, and no more than 20% prototype steps/s regression versus plain stochastic int8.
- Stop condition: Stop if stabilized variants still diverge in any seed, exceed 30% optimizer-state memory, or fail to match AdamW validation loss within 1% on the proxy.

## Evidence references

- Artifact root: `<local-path>/projects/block-stochastic-quantized-optimizer-states-with-periodic-correction-8de8a5154b62`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
