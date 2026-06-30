# KV Cache Quantization with Runtime Accuracy Monitoring

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-quantization-with-runtime-accuracy-monitoring-ced7fa214163`
Run ID: `kv-cache-quantization-with-runtime-accuracy-monitoring-ced7fa214163-20260605T112134360554+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/4368a712410f

## What looked useful

Int8 KV quantization gave 1.94x storage compression and sub-1% mean output drift on benign synthetic cache states, but failed the accuracy threshold on heavy-tail and recent-drift distributions. Cheap sampled recomputation monitoring missed many int8 high-error rows; default 32/192 samples recalled only 18.2% on heavy-tail and 7.7% on drifted-recent. Int4 gave 3.76x compression but high drift in every tested case.

## Boundaries and scale limits

No real LLM KV traces, no perplexity/task/generation evaluation, no serving latency measurement, and no long-context production workload. Results are limited to batch=16, heads=12, seq_len=512, dim=64 single-token attention tensors.

## Claim scope

Bounded tensor-level GB10 probe of per-group symmetric int8/int4 KV-cache quantization on synthetic attention K/V distributions with a simple runtime monitor based on quantization stress plus sampled fp16 recomputation.

## Why it stopped

Bounded synthetic/tensor evidence supports compression on benign states but falsifies the cheap-monitor success threshold for int8 tail and drift cases; this is a proxy early falsification of the monitoring mechanism, not a full validation of KV quantization in deployed LLM serving.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded work should test a stronger per-row monitor or adaptive fallback on real small-model KV traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real KV Trace Monitor for Int8 Tail Risk
- Success threshold: On real small-model traces, recall >= 0.90 for high-error events, precision >= 0.70, retained KV compression >= 1.8x, and next-token KL/perplexity degradation within a predeclared tolerance versus fp16.
- Stop condition: Stop if the stronger monitor cannot exceed 0.75 recall at <=25% fallback/recompute rate or if int8 KV traces show unacceptable next-token degradation even with adaptive fallback.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-quantization-with-runtime-accuracy-monitoring-ced7fa214163`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
