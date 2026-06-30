# Priority-tiered context eviction for bounded queue depth

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `priority-tiered-context-eviction-for-bounded-queue-depth-cae4c6985fdc`
Run ID: `priority-tiered-context-eviction-for-bounded-queue-depth-cae4c6985fdc-20260614T071052776440+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/c69875551c26

## What looked useful

Priority labels can be useful eviction structure under bounded queue depth, but the mechanism depends strongly on label quality; reserve-based tiering was more robust at high noise while pure priority-LRU maximized clean-label critical retention.

## Boundaries and scale limits

Synthetic workload only; 12 seeds, 4000 steps per condition, hand-specified utility/reference process, no real LLM traces, no downstream task-quality measurement, no production latency/cost study.

## Claim scope

In a bounded synthetic context-queue simulator with capacities 32/64/128, priority-aware eviction improved true-utility-weighted reference retention and reduced critical-tier misses versus FIFO/LRU in most tested conditions, but benefits declined sharply with noisy priority labels.

## Why it stopped

Closed as no-paper useful signal because evidence is synthetic/proxy-only and not a full validation of deployed LLM context eviction.

## Recommended next action

Run a bounded deepen follow-up on real or realistic agent traces with external utility labels and downstream answer-quality scoring before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace replay of priority-tiered context eviction
- Success threshold: At equal token budget, priority-tiered eviction improves weighted retention by at least 10% relative over LRU and does not reduce downstream task quality by more than 1% absolute across at least two trace families.
- Stop condition: Stop if priority labels are unavailable/unreliable, weighted retention gain is under 5% relative versus LRU, or downstream quality regresses by more than 2% absolute.

## Evidence references

- Artifact root: `<local-path>/projects/priority-tiered-context-eviction-for-bounded-queue-depth-cae4c6985fdc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
