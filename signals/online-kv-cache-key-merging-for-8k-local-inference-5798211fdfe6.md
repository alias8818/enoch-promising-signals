# Online KV-Cache Key Merging for 8k Local Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `online-kv-cache-key-merging-for-8k-local-inference-5798211fdfe6`
Run ID: `online-kv-cache-key-merging-for-8k-local-inference-5798211fdfe6-20260531T195815513175+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8d9c62e110b1

## What looked useful

Key-only online merging compressed repeated/value-consistent 8k traces from 8192 to 512 retained slots with median relative L2 error about 0.000253, but a near-collision trace with high-cosine keys and opposite values produced median relative L2 error about 0.998 and output cosine about 0.069 despite retained-key attention KL near 5e-7.

## Boundaries and scale limits

No real decoder model, perplexity, generation-quality, or production-serving validation was run. Evidence is limited to controlled PyTorch traces at seq_len=8192, dim=64, 256 queries, two seeds, and synthetic correlated/heterogeneous/near-collision scenarios.

## Claim scope

8k synthetic attention mechanism probe for online count-weighted key-cosine KV-cache merging versus exact attention and retention baselines.

## Why it stopped

Synthetic 8k evidence found both a favorable regime and a mechanism-level counterexample, so key-only merging is not reliable enough for a paper-positive claim without a guarded variant and real-model validation.

## Recommended next action

Stop this run as a no-paper useful signal; next run should test a value-aware or query-sensitive merge guard on the same 8k traces plus captured KV tensors from a small local decoder model.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Value-Aware Guard for Online KV-Cache Key Merging
- Success threshold: Guarded merging keeps correlated-trace retained slots at or below 1024/8192 with relative L2 error below 0.01, reduces near_collision relative L2 error by at least 5x versus key-only merging, and does not worsen small-model next-token KL by more than 1% versus full cache on a bounded 8k prompt set.
- Stop condition: Stop if the guard either fails to reduce near_collision relative L2 below 0.2 or loses most compression benefit by retaining more than 4096/8192 slots on correlated traces.

## Evidence references

- Artifact root: `<local-path>/projects/online-kv-cache-key-merging-for-8k-local-inference-5798211fdfe6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
