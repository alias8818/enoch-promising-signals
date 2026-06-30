# Local Training Proofs via Gradient Range Certification

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `local-training-proofs-via-gradient-range-certification-a17d7763f885`
Run ID: `local-training-proofs-via-gradient-range-certification-a17d7763f885-20260605T065109741058+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/5be133f499a0

## What looked useful

Interval gradient enclosures contained all sampled gradient ranges in 300 initialization-grid cases and 195 training-path cases. Descent certification was 100% through radius 1e-2, but degraded at larger radii: the initialization grid fell to 52% descent certification at radius 1e-1, and the training-path probe at radius 3e-2 fell to 20% descent certification by step 60.

## Boundaries and scale limits

Only synthetic regression, one hidden layer, widths up to 32 on the initialization grid, width 8 on the training-path probe, one-step local certificates, and short local training trajectories were tested. No real dataset, deeper model, transformer, GPT-2-small-class baseline, or composed multi-step proof was validated.

## Claim scope

For small one-hidden-layer ReLU regression models on synthetic teacher data, simple interval gradient range certification can give valid non-vacuous one-step local descent certificates at parameter-box radii up to about 1e-2, including along a short 60-step gradient-descent path.

## Why it stopped

The evidence is a bounded proxy showing non-vacuous small-radius local descent certificates and clear moderate-radius failure, not a full local training proof or publication-grade validation.

## Recommended next action

Stop this run as a no-paper useful signal; next, run a bounded deepen test comparing interval bounds to affine or CROWN-style gradient bounds on the same training-path certificate task.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Sharper Gradient Range Bounds for Persistent Local Training Certificates
- Success threshold: At radius 3e-2, certify descent for at least 80% of evaluated training-path states through step 60 while retaining sampled-gradient containment and staying under 15 minutes CPU runtime.
- Stop condition: Stop if the sharper bound fails sampled-gradient containment, exceeds the 15-minute CPU-only budget, or improves radius 3e-2 step-60 descent certification by less than 20 percentage points over the interval baseline.

## Evidence references

- Artifact root: `<local-path>/projects/local-training-proofs-via-gradient-range-certification-a17d7763f885`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
