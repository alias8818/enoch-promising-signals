# Grouped-Head KV Eviction on GPT-2-Small-Class with Real VRAM and Downstream Metrics

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `grouped-head-kv-eviction-on-gpt-2-small-class-with-real-vram-and-downstream-metrics-4278df384036`
Run ID: `grouped-head-kv-eviction-on-gpt-2-small-class-with-real-vram-and-downstream-metrics-4278df384036-20260620T055602103794+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/09b091fae8ea

## What looked useful

Head assignment matters: naive grouped policies were worse than uniform64, but the rotation `64,32,32,128` reached PPL 1759.19 versus uniform64 PPL 2530.14 at the same 18,874,368 stored KV bytes, while full cache remained far better at PPL 34.45.

## Boundaries and scale limits

Inference-only, 384-token sequences, 3,072 evaluated tokens, GPT-2 small only, WikiText-2 next-token metrics only, unoptimized per-group attention, and no production paged-cache or downstream task validation.

## Claim scope

On GPT-2 small with an explicit CUDA KV cache and a 3,072-token WikiText-2 validation probe, grouped-head KV eviction can reduce stored KV bytes by 83.3% versus full cache; one contiguous head-window assignment beat uniform eviction at the same average 64-token KV budget, while other assignments were worse.

## Why it stopped

Mixed bounded evidence: grouped-head eviction produced real KV memory savings and one better-than-uniform assignment, but results were assignment-sensitive, small-slice, inference-only, and not enough for publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded deepen follow-up that scores GPT-2 heads by eviction sensitivity and allocates longer windows to the most context-sensitive heads, then compare against uniform windows at identical KV bytes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Head-Sensitivity-Guided Grouped KV Eviction for GPT-2 Small
- Success threshold: Sensitivity-guided grouping improves mean NLL by at least 5% versus uniform eviction at the same KV byte budget on held-out text for two of three tested average-window budgets without increasing stored KV bytes.
- Stop condition: Stop if sensitivity-guided grouping fails to beat uniform eviction on held-out text for at least two budgets, or if quality remains within 1% of uniform while adding grouped-attention runtime overhead.

## Evidence references

- Artifact root: `<local-path>/projects/grouped-head-kv-eviction-on-gpt-2-small-class-with-real-vram-and-downstream-metrics-4278df384036`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
