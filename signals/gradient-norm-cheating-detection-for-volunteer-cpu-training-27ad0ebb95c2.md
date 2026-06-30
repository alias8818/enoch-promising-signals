# Gradient-norm cheating detection for volunteer CPU training

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `gradient-norm-cheating-detection-for-volunteer-cpu-training-27ad0ebb95c2`
Run ID: `gradient-norm-cheating-detection-for-volunteer-cpu-training-27ad0ebb95c2-20260629T080401914995+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9aa549c948d0

## What looked useful

Gradient norm is useful as a malformed-update sanity check but is not viable as a standalone cheating detector because attackers can choose plausible norms and honest non-IID clients widen norm variance. Across five seeds, matched-norm random-direction attacks had norm AUROC about 0.46-0.50 and TPR@5%FPR about 0.03-0.06; IID sign-flip norm AUROC stayed near 0.50 while a direction-aware diagnostic separated it.

## Boundaries and scale limits

Synthetic logistic regression only; 100 clients, 30 sampled per round, 120 rounds per seed, five seeds, no real volunteer network, no deep model, no asynchronous runtime, and no private production traces.

## Claim scope

In a bounded synthetic CPU federated logistic-training simulation, robust gradient-norm-only scoring detects zero and obvious IID scale attacks but fails matched-norm and sign-flip cheating modes, especially under non-IID clients.

## Why it stopped

Synthetic early falsification of gradient-norm-only cheating detection as a robust volunteer CPU training detector; this is not full real-world validation.

## Recommended next action

Stop this norm-only path as no-paper evidence; a bounded follow-up should test direction-aware and validation-loss detectors on a small real federated benchmark with adaptive matched-norm attackers.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direction-aware detection for matched-norm volunteer training cheaters
- Success threshold: Direction-aware or validation-loss detector improves matched-norm and sign-flip TPR@5%FPR by at least 0.30 absolute over norm-only without doubling false positives on honest non-IID clients.
- Stop condition: Stop if matched-norm or sign-flip TPR@5%FPR remains below 0.30 in non-IID settings or if honest non-IID false positives exceed the fixed 5% target after calibration.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-norm-cheating-detection-for-volunteer-cpu-training-27ad0ebb95c2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
