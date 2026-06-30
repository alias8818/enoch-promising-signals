# Pretrained GPT-2 robustness benchmark for per-head INT8 K/V cache

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `pretrained-gpt-2-robustness-benchmark-for-per-head-int8-k-50e560357e`
Run ID: `pretrained-gpt-2-robustness-benchmark-for-per-head-int8-k-50e560357e-20260531T112750931023+0000`

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

- Parent run decision: Int8 per-head KV cache for CPU inference: enoch://control-plane/projects/int8-per-head-kv-cache-for-cpu-inference-e4a33fa97a79/runs/int8-per-head-kv-cache-for-cpu-inference-e4a33fa97a79-20260530T004503528887+0000
- Parent run decision: Real-model CPU decode validation for per-head INT8 K/V cache: enoch://control-plane/projects/real-model-cpu-decode-validation-for-per-head-int8-k-v-cac-3293af5b42/runs/real-model-cpu-decode-validation-for-per-head-int8-k-v-cac-3293af5b42-20260530T045803587088+0000

## What looked useful

Across 2,048 scored tokens per variant, per-head INT8 had PPL 80.7690 vs fp32 80.5407 (+0.2835% relative), KL to fp32 0.000653, top-1 agreement 97.51%, and estimated cache reduction 74.97%. Per-layer INT8 was slightly worse on aggregate, and per-head INT4 degraded to +5.41% relative PPL with 78.17% top-1 agreement.

## Boundaries and scale limits

Only pretrained GPT-2 small was tested; contexts were 16-token prompt plus 32 scored continuation tokens; corpus was fixed local prose rather than a standard benchmark; cache quantization was simulated on CPU by dequantizing before each model step, not implemented as a packed serving kernel; no larger models, long contexts, task-level generation evaluation, or real serving speedups were validated.

## Claim scope

On a local fixed-text GPT-2 small cached next-token benchmark with two fixed corpus-window seeds, simulated per-head symmetric INT8 K/V cache storage preserved perplexity within 0.29% relative to fp32 while reducing estimated K/V cache bytes by about 75%.

## Why it stopped

The run reached Tier 2-style local confirmation with fixed seeds, real fp32 baseline, per-layer INT8 control, and INT4 ablation, but the evidence is too narrow and partly simulated for publication readiness.

## Recommended next action

Stop this run as no-paper useful signal; next bounded deepen test should evaluate the same per-head INT8 cache on a standard held-out benchmark with longer contexts and a packed-cache implementation before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Standard-benchmark long-context GPT-2 per-head INT8 K/V cache validation
- Success threshold: Per-head INT8 relative PPL delta <=0.5% vs fp32, KL <=0.0015, top-1 agreement >=97%, and measured packed K/V memory reduction >=70% across the standard benchmark and context sweep.
- Stop condition: Stop if per-head INT8 exceeds 1% relative PPL degradation, top-1 agreement drops below 95%, packed-cache implementation cannot reproduce simulated logits within tolerance, or runtime would require datacenter-scale resources beyond this deployment.

## Evidence references

- Artifact root: `<local-path>/projects/pretrained-gpt-2-robustness-benchmark-for-per-head-int8-k-50e560357e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
