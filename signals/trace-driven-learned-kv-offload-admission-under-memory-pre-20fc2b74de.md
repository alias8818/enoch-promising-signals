# Trace-Driven Learned KV Offload Admission Under Memory Pressure

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `trace-driven-learned-kv-offload-admission-under-memory-pre-20fc2b74de`
Run ID: `trace-driven-learned-kv-offload-admission-under-memory-pre-20fc2b74de-20260519T035704139647+0000`

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

- Internal Enoch project: Trace-Driven Learned KV Offload Admission Under Memory Pressure: internal_generated:trace-driven-learned-kv-offload-admission-under-memory-pre-20fc2b74de

## What looked useful

Learned HGB admission improved weighted cost by 8.37% on average vs LRU across 45 eval cases and by 7.54% vs the best heuristic, with positive improvements in 45/45 cases. The no-pressure ablation matched or slightly exceeded the pressure-aware model, so the learned-admission mechanism is supported but the explicit memory-pressure feature is not isolated.

## Boundaries and scale limits

Synthetic traces and simulated transfer/latency costs only; no real vLLM/SGLang/TensorRT-LLM replay, GPU allocator telemetry, CUDA copy overlap, production request traces, or measured TTFT/TPOT.

## Claim scope

In a synthetic trace-driven KV-cache simulator with fixed train/eval seeds, three workload shapes, three memory budgets, and online baselines, learned admission reduced weighted simulated latency/offload cost versus admit-all LRU and heuristic admission policies.

## Why it stopped

Tier-2 simulator evidence supports a useful mechanism but remains no-paper because the traces and latency/offload costs are synthetic and the explicit memory-pressure feature was not independently validated.

## Recommended next action

Run the same admission API against an instrumented vLLM or SGLang KV-block replay using open long-context traces and report measured TTFT/TPOT, transfer volume, HBM pressure, and allocator events before considering a paper.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Instrumented Serving Replay for Learned KV Offload Admission
- Success threshold: Learned admission must improve measured weighted TTFT/TPOT or per-token latency cost by at least 5% versus the best heuristic baseline in at least 80% of replay cases, without increasing p99 latency or OOM/eviction failures.
- Stop condition: Stop if learned admission fails to beat the best heuristic by 2% mean measured latency/offload cost, if policy overhead erases the simulated gain, or if the no-pressure ablation fully explains the result and no pressure-specific mechanism remains.

## Evidence references

- Artifact root: `<local-path>/projects/trace-driven-learned-kv-offload-admission-under-memory-pre-20fc2b74de`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
