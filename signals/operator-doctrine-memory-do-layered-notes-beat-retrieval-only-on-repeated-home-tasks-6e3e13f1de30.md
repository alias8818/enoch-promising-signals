# Operator-Doctrine Memory: Do Layered Notes Beat Retrieval-Only on Repeated Home Tasks?

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `operator-doctrine-memory-do-layered-notes-beat-retrieval-only-on-repeated-home-tasks-6e3e13f1de30`
Run ID: `operator-doctrine-memory-do-layered-notes-beat-retrieval-only-on-repeated-home-tasks-6e3e13f1de30-20260629T101603777803+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1af9aa073b79

## What looked useful

Layered notes achieved 0.952 field accuracy and 0.903 exact task success versus 0.872 field accuracy and 0.710 exact task success for the strongest retrieval-only baseline in the main run. No-drift sensitivity nearly erased the gap, while high drift preserved a large advantage, indicating the mechanism is latest-doctrine consolidation under repeated changing tasks.

## Boundaries and scale limits

Synthetic symbolic tasks only; no real home-operator traces, no LLM planner, no noisy human feedback parsing, no privacy or note-maintenance cost evaluation, and no publication-grade external validation.

## Claim scope

In a deterministic synthetic benchmark of repeated home tasks across 32 homes and six task types, layered per-home operator-doctrine notes beat top-k retrieval-only memory, including a home-filtered recency-aware baseline, when task preferences can drift.

## Why it stopped

Proxy-only synthetic evidence supports the mechanism but is not direct/full validation of real operator-doctrine memory.

## Recommended next action

Stop this run as a synthetic useful signal; next run should test the same memory variants with an LLM agent on realistic repeated home-task transcripts before making any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-agent repeated home-task memory evaluation with layered notes versus retrieval-only
- Success threshold: Layered notes beat the strongest retrieval-only baseline by at least 5 percentage points exact task success with non-overlapping bootstrap 95% confidence intervals and no more than 20% higher context/token cost.
- Stop condition: Stop if layered notes fail to improve exact task success by 2 percentage points over recency-aware retrieval or if note-update errors/stale doctrine erase the synthetic advantage.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-do-layered-notes-beat-retrieval-only-on-repeated-home-tasks-6e3e13f1de3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
