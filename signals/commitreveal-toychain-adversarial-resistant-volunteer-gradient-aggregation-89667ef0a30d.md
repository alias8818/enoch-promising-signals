# CommitReveal ToyChain: Adversarial-Resistant Volunteer Gradient Aggregation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `commitreveal-toychain-adversarial-resistant-volunteer-gradient-aggregation-89667ef0a30d`
Run ID: `commitreveal-toychain-adversarial-resistant-volunteer-gradient-aggregation-89667ef0a30d-20260610T014701902234+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b7d69054757c

## What looked useful

Commit-reveal changed plain-mean cosine under adaptive_oppose from -0.958 without commit to 0.794 with commit-reveal, eliminating negative-cosine attack success in the medium run. It produced essentially no benefit against static_true_direction Byzantine updates, where plain mean stayed near -0.949 and robust aggregation supplied the actual defense. A 20% non-reveal churn check showed reveal liveness can degrade robust aggregation if membership and trimming are not adjusted.

## Boundaries and scale limits

CPU-only synthetic simulation; no real model training, no real volunteer network, no Sybil economics, no consensus latency/fee modeling, and no large-scale distributed validation.

## Claim scope

Synthetic toychain gradient aggregation with 32 honest and 8 Byzantine volunteers over 128-dimensional gradients. Commit-reveal was tested as a timing barrier against direction-blind adaptive last-mover attacks and as a non-solution against precommitted true-direction Byzantine updates.

## Why it stopped

Moderate synthetic evidence supports commit-reveal as a timing defense but falsifies the stronger claim that it alone is adversarial-resistant gradient aggregation.

## Recommended next action

Stop this run as no-paper useful signal; a bounded deepen follow-up should test liveness-aware commit-reveal plus robust aggregation on a real small model training task.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Liveness-aware commit-reveal robust aggregation on a small real training task
- Success threshold: Commit-reveal plus liveness-aware robust aggregation keeps final validation accuracy within 2 percentage points of clean training and reduces adaptive attack success by at least 80% relative to no-commit under at least 20% missing reveals.
- Stop condition: Stop if commit-reveal variants fail to beat robust aggregation without commit under adaptive attacks, or if missing reveals cause more than a 5 percentage point accuracy loss after quorum-aware adjustment.

## Evidence references

- Artifact root: `<local-path>/projects/commitreveal-toychain-adversarial-resistant-volunteer-gradient-aggregation-89667ef0a30d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
