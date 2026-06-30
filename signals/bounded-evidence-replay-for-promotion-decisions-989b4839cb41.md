# Bounded Evidence Replay for Promotion Decisions

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-evidence-replay-for-promotion-decisions-989b4839cb41`
Run ID: `bounded-evidence-replay-for-promotion-decisions-989b4839cb41-20260619T214611874286+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5b2f9aeee881

## What looked useful

Impact-selected bounded evidence is a useful compact audit signal for stable high-margin decisions, reaching 98.89% far-from-threshold match at 12.5% storage and 99.89% at 25% storage, but near-threshold match stayed low at 58.08% and 61.03% respectively; false negatives among promoted candidates remained high under partial-evidence threshold replay.

## Boundaries and scale limits

Synthetic CPU-only simulation with 10 seeds, 20,000 candidates per seed, 64 evidence events, and additive linear evidence. No real promotion logs, human decisions, non-additive policy models, privacy analysis, or production-scale retention system were tested.

## Claim scope

On synthetic additive promotion traces, bounded top-impact evidence capsules replay high-margin decisions well and outperform random/recent capsules at equal storage, but they do not faithfully replay near-threshold or promoted decisions when the original full-evidence threshold is reused.

## Why it stopped

Synthetic bounded replay produced a mixed useful signal, not a publication-grade positive: impact capsules beat controls, but near-threshold fidelity and promoted-candidate recall were too weak for the general replay claim.

## Recommended next action

Stop this run as no-paper useful signal; next run should test residual-calibrated bounded replay that stores top-impact evidence plus a small signed remainder summary and must beat 95% overall match and 85% near-threshold match at 25% storage on the same benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual-Calibrated Bounded Evidence Replay
- Success threshold: At 25% evidence-event storage plus no more than one scalar residual per candidate, achieve at least 95% overall decision match, at least 85% near-threshold match, and at least a 3x reduction in promoted false negatives relative to impact-only replay.
- Stop condition: Stop if residual-calibrated replay fails to exceed 90% overall match or 75% near-threshold match at 25% storage across 10 seeds, because the bounded replay mechanism remains too lossy for promotion-decision audit replay.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-evidence-replay-for-promotion-decisions-989b4839cb41`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
