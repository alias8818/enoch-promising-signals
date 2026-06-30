# Commit-Reveal Gradient Timing to Block Look-Ahead Cheating

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `commit-reveal-gradient-timing-to-block-look-ahead-cheating-689ef2596e0f`
Run ID: `commit-reveal-gradient-timing-to-block-look-ahead-cheating-689ef2596e0f-20260628T101346523708+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e90d34308059

## What looked useful

Strict early commit-reveal accepted 0.000 look-ahead gradients across the main run; no-commit and late commit controls accepted 1.000; a tight jitter deadline leaked 0.263; post-commit mutation was rejected at 1.000.

## Boundaries and scale limits

40 seeds, 1200 rounds per seed, 64-dimensional linear regression, local single-process timing model; no distributed worker clocks, network jitter, secure batch release, or large-model training validation.

## Claim scope

In a synthetic online linear-regression protocol model, commit-reveal blocks accepted look-ahead gradient submissions when the commit deadline precedes future batch visibility; late or jitter-leaky deadlines do not block the attack.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic protocol acceptance evidence, not direct distributed training validation.

## Recommended next action

Build a small distributed coordinator/worker harness with explicit clock skew, network jitter, and batch-prefetch controls before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Distributed commit-reveal gradient timing under clock skew and batch prefetch
- Success threshold: Accepted look-ahead rate below 1% for strict guarded commit-reveal and at least 50% lower than tight/late controls across 20 or more seeds.
- Stop condition: Stop if realistic batch-prefetch or clock-skew conditions make future information visible before commit in 5% or more of guarded rounds, or if look-ahead submissions do not produce any measurable advantage in controls.

## Evidence references

- Artifact root: `<local-path>/projects/commit-reveal-gradient-timing-to-block-look-ahead-cheating-689ef2596e0f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
