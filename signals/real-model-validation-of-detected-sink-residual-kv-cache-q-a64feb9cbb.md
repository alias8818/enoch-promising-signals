# Real-model validation of detected-sink residual KV-cache quantization

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-model-validation-of-detected-sink-residual-kv-cache-q-a64feb9cbb`
Run ID: `real-model-validation-of-detected-sink-residual-kv-cache-q-a64feb9cbb-20260621T031959524443+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Attention-Sink Residual KV-Cache Quantization: enoch://control-plane/projects/attention-sink-residual-kv-cache-quantization-af7f78d91eaf/runs/attention-sink-residual-kv-cache-quantization-af7f78d91eaf-20260621T030942352798+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c4961ff9efce

## What looked useful

Detected-sink residual reduced mean KL-to-FP from 0.00077845 for all-int8 to 0.00035958, a 53.8% relative reduction, with estimated 3.37x KV-cache compression. It beat random residual but only tied fixed-first residual within noise, so the detector advantage is not established.

## Boundaries and scale limits

Small model, four prompts, short continuations, simulated int8 quantize/dequantize cache tensors, no real compressed-cache serving implementation, no throughput measurement, no long-context or multi-model robustness.

## Claim scope

On a bounded distilgpt2 CPU teacher-forced evaluation with four short prompts, preserving four attention-detected sink KV-cache positions in full precision reduces int8 cache quantization drift versus all-int8 and random residual baselines at equal estimated cache bytes.

## Why it stopped

Tier 1 direct test produced useful mechanism support but not publication-grade evidence; fixed-first residual nearly matched detected-sink residual.

## Recommended next action

Run a deepen follow-up on longer prompts and at least two GPT-2-small-class or larger models, requiring detected-sink residual to beat both random and fixed-first residual at equal cache bytes before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Long-context multi-model check of detected-sink residual KV-cache quantization
- Success threshold: Detected-sink residual lowers mean KL-to-FP by at least 20% versus both fixed-first and random residual baselines at equal estimated cache bytes on both models, without reducing top-1 match versus the best control.
- Stop condition: Stop as no-paper if detected-sink residual does not beat fixed-first residual by at least 20% KL on either model or if detected sinks remain dominated by the first positions across the long-context set.

## Evidence references

- Artifact root: `<local-path>/projects/real-model-validation-of-detected-sink-residual-kv-cache-q-a64feb9cbb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
