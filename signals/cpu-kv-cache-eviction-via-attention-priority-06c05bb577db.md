# CPU KV-Cache Eviction via Attention Priority

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `cpu-kv-cache-eviction-via-attention-priority-06c05bb577db`
Run ID: `cpu-kv-cache-eviction-via-attention-priority-06c05bb577db-20260613T115001952312+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/808d12a99b4d

## What looked useful

Pure attention-priority and decayed attention-priority lost to LRU in every tested workload. Overall hit rate was 0.3097 for attention_priority and 0.3096 for attention_priority_decay versus 0.7725 for LRU. The mechanism retained more random-old entries but sacrificed many recent and anchor hits.

## Boundaries and scale limits

No real transformer serving, generated text quality, per-layer/per-head attention trace, allocator overhead, or CPU memory bandwidth measurement was performed; this is not publication-grade validation.

## Claim scope

Bounded synthetic CPU trace proxy for pure online attention-priority KV-cache eviction at 12% cache capacity across stationary locality, recurring anchor, and topic-shift workloads.

## Why it stopped

Proxy early falsification: in controlled traces where attention-priority should have helped on recurring anchors, pure attention-priority underperformed LRU by a large margin and did not win any workload.

## Recommended next action

Stop the pure-priority path; if continuing, run a bounded direct follow-up using actual small-transformer attention traces to test a hybrid LRU plus attention-score guard against LRU at matched KV budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hybrid LRU plus attention guard on real small-transformer KV traces
- Success threshold: Hybrid LRU-attention improves target retention or task accuracy by at least 5% relative over LRU at the same KV budget with less than 10% CPU overhead across at least two seeds and two workloads.
- Stop condition: Stop if hybrid policy fails to beat LRU on direct model traces or exceeds 10% CPU overhead at matched cache budget.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-kv-cache-eviction-via-attention-priority-06c05bb577db`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
