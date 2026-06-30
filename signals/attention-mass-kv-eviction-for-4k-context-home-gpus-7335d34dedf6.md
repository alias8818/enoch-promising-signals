# Attention-Mass KV Eviction for 4k-Context Home GPUs

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `attention-mass-kv-eviction-for-4k-context-home-gpus-7335d34dedf6`
Run ID: `attention-mass-kv-eviction-for-4k-context-home-gpus-7335d34dedf6-20260530T021447639469+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/36b9f72c1481

## What looked useful

Pure cumulative attention-mass eviction has a cold-start failure mode: newly added local tokens have near-zero received mass and are evicted before they can be useful. A recency-protected variant improved over pure mass but still lost to recency in 0/30 scenario-seed-budget comparisons.

## Boundaries and scale limits

No trained LLM perplexity, task accuracy, multi-layer/head real attention traces, or production inference throughput was measured. Results are proxy evidence from generated attention matrices and CPU-side online policy simulation after GPU trace generation.

## Claim scope

Synthetic 4k-token causal attention traces on NVIDIA GB10 did not support cumulative attention-mass KV eviction, with or without a recency protection window, over recency or streaming-sink recency baselines at cache budgets 256, 512, and 1024.

## Why it stopped

Proxy early falsification: synthetic 4k attention traces showed attention-mass eviction underperforming simple recency on retained attention mass and output reconstruction error, but this is not full model-serving validation.

## Recommended next action

Stop this no-paper run; if continuing, run a bounded real-LM follow-up that measures perplexity from actual decoder attention traces before implementing any GPU KV-cache kernel.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-LM Perplexity Check for Recency-Protected Attention-Mass KV Eviction
- Success threshold: At least a 5% perplexity or NLL reduction versus recency at one or more budgets without worse results at the other budgets, plus less than 10% per-token eviction bookkeeping overhead.
- Stop condition: Stop if recency-protected attention mass fails to beat recency on perplexity/NLL at all tested budgets or if bookkeeping overhead exceeds 10% without a quality win.

## Evidence references

- Artifact root: `<local-path>/projects/attention-mass-kv-eviction-for-4k-context-home-gpus-7335d34dedf6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
