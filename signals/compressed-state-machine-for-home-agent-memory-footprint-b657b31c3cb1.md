# Compressed State Machine for Home Agent Memory Footprint

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `compressed-state-machine-for-home-agent-memory-footprint-b657b31c3cb1`
Run ID: `compressed-state-machine-for-home-agent-memory-footprint-b657b31c3cb1-20260607T143749394709+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/7a69b6f68e37

## What looked useful

Compressed FSM serialized size was 208 bytes at 100k events and 212 bytes at 1M events while raw logs grew to 7.22 MB and 73.2 MB respectively, with 100% current-state query accuracy. Python deep object size was slightly larger than a belief dictionary, and episodic recall was zero.

## Boundaries and scale limits

Synthetic traces only; no real smart-home logs, natural-language retrieval evaluation, multi-day persistence test, privacy/audit constraints, or LLM-agent integration. Scale probe reached 1M events on one seed and is not a production workload validation.

## Claim scope

On deterministic synthetic home-agent event traces, a typed compressed FSM preserves exact current-state query answers while making serialized memory effectively constant-size relative to raw episodic logs; it does not preserve event history and is not always smaller than a normalized belief dictionary in Python resident object size.

## Why it stopped

Synthetic/proxy evidence supports a bounded mechanism but is insufficient for paper writing and exposes a material history-recall tradeoff plus a belief-dictionary resident-memory baseline that narrows the claim.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded deepen follow-up on real or replayed home-agent traces using a hybrid FSM plus episodic ring buffer and compare memory, latency, current-state accuracy, and natural-language history-query success against raw-log and belief-dict baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hybrid FSM plus episodic ring buffer on replayed home-agent traces
- Success threshold: Hybrid FSM plus ring buffer achieves >=95% labeled query success, 100% current-state accuracy, and >=10x resident-memory reduction versus raw logs on the replayed workload.
- Stop condition: Stop if history-sensitive query success falls below 90% at all ring-buffer sizes that still provide >=10x memory reduction, or if the belief-dictionary plus window baseline dominates the hybrid on both memory and accuracy.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-state-machine-for-home-agent-memory-footprint-b657b31c3cb1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
