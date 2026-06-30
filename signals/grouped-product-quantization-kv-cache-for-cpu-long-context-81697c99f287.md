# Grouped Product-Quantization KV Cache for CPU Long Context

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `grouped-product-quantization-kv-cache-for-cpu-long-context-81697c99f287`
Run ID: `grouped-product-quantization-kv-cache-for-cpu-long-context-81697c99f287-20260621T220446510815+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/2852c88656c4

## What looked useful

Aggressive grouped PQ reached 14.22x-15.75x compression versus FP16 KV but had attention output relative L2 of 0.8901-0.9893 and top-32 overlap of 0.245-0.261. A lower-compression ablation reached 5.33x-7.53x compression with improved but still high output relative L2 of 0.4524-0.5341; grouped sharing did not improve fidelity versus per-head PQ.

## Boundaries and scale limits

No real LLM KV traces, no downstream language-model quality metrics, no compressed-domain attention kernel, no 7B+ model, and no production serving benchmark. Results apply only to the implemented NumPy grouped-PQ reconstruction proxy.

## Claim scope

Bounded CPU proxy over synthetic 2048-4096 token KV tensors: naive grouped PQ codebook sharing across KV heads does not preserve retrieval-style attention well enough to justify a paper claim, and grouping provides only marginal compression over per-head PQ.

## Why it stopped

Proxy evidence falsifies the naive grouped-PQ mechanism for attention fidelity at useful compression levels; this is an early bounded falsification, not a full-scale validation.

## Recommended next action

Stop this run as no-paper useful evidence; if continuing, run a bounded real-trace follow-up using a small pretrained transformer layer and compare grouped PQ against per-head PQ plus scalar KV quantization baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace grouped PQ KV-cache comparison on a small transformer
- Success threshold: Grouped PQ is worth further scaling only if it achieves at least 6x compression versus FP16 KV with attention-output relative L2 below 0.10 and top-32 attention overlap above 0.90 while matching or beating per-head PQ and scalar/asymmetric baselines.
- Stop condition: Stop if grouped PQ misses either fidelity threshold or fails to beat per-head PQ at matched compression on real traces.

## Evidence references

- Artifact root: `<local-path>/projects/grouped-product-quantization-kv-cache-for-cpu-long-context-81697c99f287`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
