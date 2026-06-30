# Real small-agent rollback harness for evidence-ledger memory

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-small-agent-rollback-harness-for-evidence-ledger-memo-f5cec002e5`
Run ID: `real-small-agent-rollback-harness-for-evidence-ledger-memo-f5cec002e5-20260527T095713228991+0000`

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

- Parent run decision: Evidence-ledger rollback for small local CPU agents: enoch://control-plane/projects/evidence-ledger-rollback-for-small-local-cpu-agents-b5f2001881ad/runs/evidence-ledger-rollback-for-small-local-cpu-agents-b5f2001881ad-20260526T024931004654+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/77620b22bbc3

## What looked useful

Rollback directly repaired contaminated derived memory after delayed invalidation, yielding 100% accuracy and 0.0 residual poison mass in the Tier 1 run, while append-only summaries retained 5.2 mean poison mass and reached 83.7% accuracy. A secondary severity sweep crossed the 20 point lift threshold only at stronger poison weights of 3.0 and 3.4.

## Boundaries and scale limits

Synthetic 300-case CPU-only harness; no real LLM, real tool provenance system, vector memory, multi-agent workflow, or long-horizon deployment trace was tested. Active read-time recomputation matched rollback in this simple setting.

## Claim scope

In a deterministic small-agent harness with delayed invalidation of poisoned tool observations, rollback-ledger memory eliminated residual poison from durable summary state and improved final-label accuracy versus an append-only summary baseline; at the pre-set default poison severity the accuracy lift was 16.3 percentage points, below the 20 point threshold.

## Why it stopped

Closed as no-paper useful signal because the main pre-set Tier 1 threshold was not met at default poison severity and the evidence is a controlled synthetic harness rather than publication-grade validation.

## Recommended next action

Run one bounded deepen test using a real small LLM or trace-replay agent with natural-language summaries, comparing rollback against append-only and invalidation-aware repair baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Rollback ledger against repairable memory in real small-agent trace replay
- Success threshold: Rollback achieves at least a 10 percentage point accuracy lift over append-only, residual contamination no worse than active recompute or explicit repair, and replay overhead below 2x wall-clock on the bounded trace set.
- Stop condition: Stop if rollback fails to beat append-only by 5 percentage points, leaves higher residual contamination than repair/recompute controls, or requires more than 2x replay overhead without accuracy benefit.

## Evidence references

- Artifact root: `<local-path>/projects/real-small-agent-rollback-harness-for-evidence-ledger-memo-f5cec002e5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
