# Direct GPT-2-small canary-loss detection on natural text

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `direct-gpt-2-small-canary-loss-detection-on-natural-text-401ba99424`
Run ID: `direct-gpt-2-small-canary-loss-detection-on-natural-text-401ba99424-20260630T021830048357+0000`

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

- Parent run decision: Canary-Loss Cheat Detection in Volunteer GPT-2 Training: enoch://control-plane/projects/canary-loss-cheat-detection-in-volunteer-gpt-2-training-50e93ef414c2/runs/canary-loss-cheat-detection-in-volunteer-gpt-2-training-50e93ef414c2-20260629T180139010799+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/74f95ca5e0d1

## What looked useful

Maximum 16-token local loss provides a usable ranking signal for canary-like insertions (overall AUC 0.823), but direct loss is weak at a practical low-FPR operating point (overall TPR 0.200 at 5% empirical FPR; numeric-code TPR 0.075). Whole-passage mean loss is weaker (AUC 0.673).

## Boundaries and scale limits

400 total examples, 80 clean negatives, 80 benign inserted negatives, and 80 positives per canary type; no real training-data membership canaries, no finetuning, no larger models, and no held-out threshold calibration beyond the same bounded corpus.

## Claim scope

Frozen GPT-2-small loss on WikiText-2 natural passages with injected canary-like sentences and benign inserted-sentence controls.

## Why it stopped

Control-aware direct evidence shows useful ranking but poor low-FPR detection and no direct membership/memorization validation, so this is not publication-grade.

## Recommended next action

Stop as no-paper useful signal; a bounded follow-up should test loss-window ranking on known memorized canaries from a small finetuned GPT-2-small model with held-out threshold calibration.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Known-exposure GPT-2-small canary loss detection with held-out calibration
- Success threshold: At least 0.80 AUC and at least 0.50 TPR at 5% FPR for two or more canary types under held-out threshold calibration.
- Stop condition: Stop if local loss-window TPR remains below 0.30 at 5% FPR for all canary types after controlled finetuning exposure.

## Evidence references

- Artifact root: `<local-path>/projects/direct-gpt-2-small-canary-loss-detection-on-natural-text-401ba99424`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
