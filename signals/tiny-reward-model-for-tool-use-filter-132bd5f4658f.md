# Tiny Reward Model for Tool-Use Filter

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiny-reward-model-for-tool-use-filter-132bd5f4658f`
Run ID: `tiny-reward-model-for-tool-use-filter-132bd5f4658f-20260524T193749310364+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/a9550f8d4233

## What looked useful

Tiny learned tool-use filters are not automatically better than heuristics; hard-negative training is necessary in this probe and materially improves adversarial no-tool rejection, but the tested model is too brittle for a paper or deployment claim because OOD tool-needed recall fell to 5.4%.

## Boundaries and scale limits

Synthetic templates only; no real agent traces, human labels, large-model state features, production cost model, or broad multi-tool routing validation. Main run was five CPU seeds and completed in 7.53 seconds.

## Claim scope

On a synthetic tool-use filtering task over user request plus candidate action text, a 16k-parameter hashed n-gram logistic filter without hard negatives failed adversarial no-tool rejection; adding hard-negative training improved held-out adversarial no-tool accuracy to 85.6% but still missed the <=10% false-positive threshold and collapsed on OOD tool-needed recall.

## Why it stopped

Proxy synthetic run produced a useful but mixed signal and failed the predefined success threshold, so this is not a full validation or paper-ready result.

## Recommended next action

Run one bounded deepen test on real or human-labeled tool-use traces with hard-negative training and threshold calibration; stop if OOD tool-needed recall remains below 80% at <=10% no-tool false-positive rate.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hard-negative tiny tool filter on real tool-use traces
- Success threshold: On held-out real or human-labeled traces, achieve >=80% tool-needed recall and <=10% no-tool false-positive rate while beating the best heuristic by >=5 percentage points in balanced accuracy.
- Stop condition: Stop if the calibrated tiny filter cannot reach >=80% tool-needed recall at <=10% no-tool false-positive rate, or if gains over the best heuristic are under 5 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-reward-model-for-tool-use-filter-132bd5f4658f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
