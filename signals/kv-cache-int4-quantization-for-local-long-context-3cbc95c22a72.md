# KV Cache INT4 Quantization for Local Long-Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-int4-quantization-for-local-long-context-3cbc95c22a72`
Run ID: `kv-cache-int4-quantization-for-local-long-context-3cbc95c22a72-20260628T213358448831+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/2731a9e81bfb

## What looked useful

Naive groupwise INT4 KV-cache quantization achieved 3.56x-3.76x estimated fp16-cache compression but produced substantial attention-output perturbation: at 8192 tokens, Gaussian INT4 group-64 mean output relative RMSE was 0.1547 and 1% outlier INT4 group-64 mean output relative RMSE was 0.5065, while the INT8 outlier control was 0.0336.

## Boundaries and scale limits

No real transformer weights, no perplexity/task-quality evaluation, no fused GPU/CPU kernel, no multi-layer accumulation, and no production paged-attention serving path. Timings are CPU NumPy directionality only.

## Claim scope

Synthetic NumPy attention probe of per-token/per-head groupwise symmetric INT4 KV-cache quantize-dequantize up to 8192 tokens, compared against fp16 attention and an INT8 control.

## Why it stopped

Bounded synthetic mechanism probe produced useful no-paper evidence: naive symmetric INT4 saves memory but perturbs attention too much, especially with outliers. This is not full validation of all INT4 KV-cache designs.

## Recommended next action

Do not write a paper from this run; run a bounded real-model KV-cache replay follow-up with outlier-aware INT4 methods and predefined quality thresholds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model KV-cache replay for outlier-aware INT4 quantization
- Success threshold: At least 3x effective KV-cache compression versus fp16 with less than 5% relative degradation on the chosen quality metric and no more than 10% decode throughput loss versus fp16 or an explicit memory-capacity win that offsets latency.
- Stop condition: Stop if the outlier-aware INT4 variant exceeds 10% quality degradation or cannot demonstrate a real memory-capacity benefit on the local model.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-int4-quantization-for-local-long-context-3cbc95c22a72`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
