# Residual-Head KV-Cache: 2-bit KV with FP8 Attention Residual Heads

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-head-kv-cache-2-bit-kv-with-fp8-attention-residual-heads-542be01f8764`
Run ID: `residual-head-kv-cache-2-bit-kv-with-fp8-attention-residual-heads-542be01f8764-20260531T225051494859+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/fa735c67db63

## What looked useful

At 25% residual heads, mixed 2-bit/FP8 KV used 3.5 bits per scalar (21.875% of FP16 KV). Across 6 heterogeneous synthetic seeds, sensitivity-selected residual heads improved attention-output relative MSE by 100.63x over all-2-bit, while random residual heads improved only 1.35x. Across uniform seeds, selected residual heads improved only 1.37x, showing the method depends on real head-sensitivity concentration.

## Boundaries and scale limits

No trained language model, real calibration corpus, perplexity/generation metric, long-context workload, fused mixed-KV kernel, or serving throughput measurement was tested. Results are synthetic and proxy-only.

## Claim scope

Synthetic CUDA attention-output probe: sensitivity-selected FP8 residual heads can sharply reduce relative MSE versus all-2-bit KV when head quantization sensitivity is concentrated; the same mechanism gives only modest gains under uniform synthetic heads.

## Why it stopped

Proxy-only useful signal; the mechanism is supported synthetically but not validated in a trained model or kernel benchmark, so this is not paper-ready.

## Recommended next action

Run a bounded deepen test on a trained GPT-2-small-class decoder: calibrate sensitive heads on real text, evaluate perplexity/generation degradation for 2-bit, 4-bit, FP8, and mixed 2-bit/FP8 KV, and compare against equal-memory baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trained Decoder Residual-Head KV Cache Validation
- Success threshold: Selected mixed 2-bit/FP8 KV must beat all-2-bit and random-residual mixed KV by at least 20% relative perplexity-degradation reduction at the same residual budget, without exceeding the declared KV memory budget.
- Stop condition: Stop if calibrated residual heads do not outperform random residual allocation on perplexity/generation metrics, or if the sensitivity ranking is unstable across calibration/evaluation splits.

## Evidence references

- Artifact root: `<local-path>/projects/residual-head-kv-cache-2-bit-kv-with-fp8-attention-residual-heads-542be01f8764`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
