# Trapdoor-Batch Cheating Detector for Volunteer Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `trapdoor-batch-cheating-detector-for-volunteer-training-189a56b83f56`
Run ID: `trapdoor-batch-cheating-detector-for-volunteer-training-189a56b83f56-20260629T223522022228+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/0e54a04d551a

## What looked useful

Trapdoor batches are promising as a detector for careless random cheating only when enough hidden answer-key items are present; they are brittle when cheaters can identify or infer trapdoors.

## Boundaries and scale limits

No real volunteer data, production UI telemetry, subjective annotation tasks, collusion, or adaptive trapdoor discovery process was tested. Evidence is simulator-only and should not be treated as field validation.

## Claim scope

Synthetic binary volunteer-labeling batches with hidden answer-key trapdoors: 8 trapdoors per 80-item batch caught careless/random cheaters at mean recall 0.860 with mean false-positive rate 0.005, but 4 trapdoors and trapdoor-aware cheaters failed.

## Why it stopped

Synthetic proxy produced a useful mechanism signal but also a decisive adaptive-cheater failure mode, so this run is no-paper rather than a full validation.

## Recommended next action

Run a bounded real-data or high-fidelity replay study with hidden trapdoors, independent cheating labels, and an explicit trapdoor-detectability check before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay trapdoor-batch detection on realistic volunteer-labeling traces
- Success threshold: Mean recall >= 0.80 and false-positive rate <= 0.05 on careless cheating, plus an explicit measurement of trapdoor-aware failure or improvement from auxiliary features.
- Stop condition: Stop if trapdoors are identifiable above chance, if recall remains below 0.80 at FPR <= 0.05 with 8 or more trapdoors, or if realistic data cannot provide independent cheating labels.

## Evidence references

- Artifact root: `<local-path>/projects/trapdoor-batch-cheating-detector-for-volunteer-training-189a56b83f56`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
