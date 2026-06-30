# Per-Head KV Quantization with Block-wise Scaling

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `per-head-kv-quantization-with-block-wise-scaling-197ab8d7f399`
Run ID: `per-head-kv-quantization-with-block-wise-scaling-197ab8d7f399-20260604T064304307265+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/368bec57e31c

## What looked useful

Per-head block scaling consistently improved attention-output relative RMSE across homogeneous, heterogeneous, and outlier-head synthetic scenarios. In the heterogeneous case it reduced K rel-RMSE by 49.88% for int4 and 65.09% for int8, and reduced attention-output relative RMSE by 21.83% for int4 and 23.26% for int8.

## Boundaries and scale limits

Synthetic tensors only; no real transformer activation capture, fused serving kernel, decode latency benchmark, perplexity, or generation-quality evaluation. Medium shape was batch=2, heads=32, seq=2048, dim=128, queries=64, block=64, trials=8 on NVIDIA GB10.

## Claim scope

On synthetic GPU KV-cache tensors with controlled per-head range variation, per-head block-wise scales reduce K/V reconstruction error and attention-output drift versus a shared sequence-block scale, with less than 0.05% extra fp16 scale metadata relative to packed int4 payload for the tested medium shape.

## Why it stopped

Closed as no-paper useful signal because the mechanism was directly supported only on synthetic KV tensors; real activation and model-quality evidence is still missing.

## Recommended next action

Run a deepen test using captured KV caches from a real transformer layer and add task-level quality or perplexity checks before considering a bounded paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Activation Per-Head KV Quantization Replay
- Success threshold: For int4 on real activations, per-head block scales reduce attention-output relative RMSE by at least 10% versus shared block scales and do not worsen model-level quality proxy beyond the shared-scale baseline, with scale metadata below 0.1% of packed KV payload.
- Stop condition: Stop if real-activation attention-output relative RMSE improves by less than 5% in most tested layers/prompts or if model-level quality is no better than shared block scaling.

## Evidence references

- Artifact root: `<local-path>/projects/per-head-kv-quantization-with-block-wise-scaling-197ab8d7f399`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
