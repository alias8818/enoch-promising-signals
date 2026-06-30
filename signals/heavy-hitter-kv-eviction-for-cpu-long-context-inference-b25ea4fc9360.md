# Heavy-hitter KV eviction for CPU long-context inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `heavy-hitter-kv-eviction-for-cpu-long-context-inference-b25ea4fc9360`
Run ID: `heavy-hitter-kv-eviction-for-cpu-long-context-inference-b25ea4fc9360-20260522T113507855013+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/10b0868b9e9f

## What looked useful

Heavy-hitter eviction retained all synthetic anchors and increased retained full-attention mass on the needle workload, but mean output MSE versus full attention was 4.38x worse than sliding-window at 4096+512 tokens. This cautions that retained attention mass or anchor retention alone is not a safe metric for KV eviction quality.

## Boundaries and scale limits

Synthetic single-layer attention proxy only; no trained LLM perplexity, task accuracy, multi-head/layer behavior, or optimized CPU runtime integration was tested. Wall-clock timings reflect a Python/NumPy prototype and should be interpreted as overhead-risk evidence, not production throughput.

## Claim scope

On deterministic synthetic autoregressive attention traces up to 4096 prompt tokens plus 512 decode tokens with a 512-token KV budget, vanilla cumulative-attention heavy-hitter eviction preserves old anchor tokens but does not reliably improve output fidelity versus sliding-window eviction, and can be substantially worse after attention renormalization.

## Why it stopped

Moderate proxy evidence found a mechanism-level failure: the policy preserves heavy tokens but can worsen full-attention output fidelity versus sliding-window, so this is not paper-ready and should not be claimed as validated CPU long-context inference improvement.

## Recommended next action

Stop vanilla heavy-hitter eviction as a standalone paper direction; only continue with a bounded real-model CPU test of a normalization- or value-aware variant if that variant directly addresses the observed output drift.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Normalization-aware heavy-hitter KV eviction on a small CPU transformer
- Success threshold: Corrected heavy-hitter must beat sliding-window by at least 10% on quality loss versus full cache at equal KV budget on a retrieval-heavy workload, remain no worse than sliding on a recency-control workload, and add less than 10% CPU overhead after optimized cache maintenance.
- Stop condition: Stop if corrected heavy-hitter is not better than sliding-window on quality loss in the retrieval workload or if cache maintenance overhead exceeds 10% in the optimized CPU prototype.

## Evidence references

- Artifact root: `<local-path>/projects/heavy-hitter-kv-eviction-for-cpu-long-context-inference-b25ea4fc9360`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
