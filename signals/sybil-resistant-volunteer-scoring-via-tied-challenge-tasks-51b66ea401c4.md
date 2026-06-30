# Sybil-Resistant Volunteer Scoring via Tied Challenge Tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sybil-resistant-volunteer-scoring-via-tied-challenge-tasks-51b66ea401c4`
Run ID: `sybil-resistant-volunteer-scoring-via-tied-challenge-tasks-51b66ea401c4-20260628T225202606114+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/4b5657fb2df5

## What looked useful

Tied-error cluster capping reduced 40 copied Sybils' weight share from 0.2659568684 to 0.0099335385 and reduced a 100-Sybil copied attack's ordinary task error from 0.9775 to 0.0, with no honest clustering in the simulation. The same cap failed against dispersed independent cohorts, leaving Sybil weight essentially unchanged at about 0.269.

## Boundaries and scale limits

Evidence is synthetic only: 80 honest volunteers, 10-100 Sybils, 60 challenge families, 300 ordinary tasks per replicate, 8 adversary scenarios, and 80 seeds per scenario. It does not validate real volunteer behavior, non-binary outputs, challenge leakage resistance, adaptive online adversaries, or production identity/cost/graph defenses.

## Claim scope

In a bounded synthetic binary-label volunteer scoring simulation, tied hidden challenge tasks with known answers can expose copied or near-copied Sybil accounts through shared rare error fingerprints, and cluster-capping those fingerprints can sharply reduce aggregate copied-Sybil influence.

## Why it stopped

No-paper useful signal: the synthetic evidence supports the copied-account fingerprint mechanism but also shows tied challenge tasks alone are insufficient against dispersed Sybil strategies.

## Recommended next action

Run a bounded adaptive follow-up where Sybil cohorts choose copy probability and splitting after observing scores, and compare tied-error capping against identity/cost/graph baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive tied-challenge Sybil scoring with cohort-splitting adversaries
- Success threshold: Across at least 80 seeds per adaptive scenario, the best local mechanism keeps Sybil weight share below 0.10 and ordinary weighted decision error below 0.01 while clustering fewer than 2% of honest volunteers.
- Stop condition: Stop if adaptive dispersed cohorts keep Sybil weight share above 0.20 in two threshold-calibrated variants or if honest clustering exceeds 5% at thresholds required for Sybil recall.

## Evidence references

- Artifact root: `<local-path>/projects/sybil-resistant-volunteer-scoring-via-tied-challenge-tasks-51b66ea401c4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
