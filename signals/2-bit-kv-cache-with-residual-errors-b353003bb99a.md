# 2-bit KV cache with residual errors

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-kv-cache-with-residual-errors-b353003bb99a`
Run ID: `2-bit-kv-cache-with-residual-errors-b353003bb99a-20260525T030741013212+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/d6ad506a8a39

## What looked useful

At <=4.0 effective bitmask bits/element, the best residual-corrected 2-bit setting missed the p95 output-relative-RMSE <=0.05 threshold: 0.1286 on AR(1), 0.4150 on Gaussian, 0.4602 on heavy-tail, and 0.4636 on outlier-mix caches. Meeting the 0.05 threshold required 80% residual retention, costing 15.8 bits/element and erasing the intended fp16 memory advantage.

## Boundaries and scale limits

No real pretrained transformer activations, perplexity, generation-quality, trained adaptation, GPU kernel, or serving-latency validation was run. Synthetic tensors used heads=8, sequence length=256, dimension=64, 20 trials per distribution, and four distribution families.

## Claim scope

Bounded NumPy attention simulations over synthetic KV cache distributions show that naive 2-bit K/V quantization plus sparse fp16 residual-error correction does not preserve attention outputs at about 4x fp16 compression.

## Why it stopped

Proxy/direct-attention evidence falsified the tested bounded success threshold, but it is not a full real-model validation.

## Recommended next action

Stop this run as a proxy early falsification; if continuing the idea, run a bounded real-activation GPT-2-small-class evaluation with exact memory accounting for the residual representation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-activation check for 2-bit KV residual correction
- Success threshold: At <=4 effective bits/element, p95 attention-output relative RMSE <=0.05 and validation loss/perplexity degradation no worse than a 4-bit KV baseline on the same examples.
- Stop condition: Stop if real activations still require >4 effective bits/element to meet the error threshold or if loss/perplexity degradation is worse than a simple 4-bit KV baseline.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-kv-cache-with-residual-errors-b353003bb99a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
