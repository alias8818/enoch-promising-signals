# Canary Probe Attribution for Volunteer Data Poisoning Detection

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `canary-probe-attribution-for-volunteer-data-poisoning-detection-4379a08fdf78`
Run ID: `canary-probe-attribution-for-volunteer-data-poisoning-detection-4379a08fdf78-20260628T180715490297+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/68f1afa29ba0

## What looked useful

Canary probes achieved MAP/AUC/top-k recall of 1.000 with no canary dropout, while no-canary ranking stayed near chance (MAP 0.088, AUC 0.500, top-k recall 0.037). With 50% canary dropout and 1 canary repeat, MAP increased from 0.137 at 2 poison examples to 0.427 at 8 poison examples, showing the mechanism is sensitive to canary coverage and poison volume.

## Boundaries and scale limits

No real volunteer data, no LLM or embedding fine-tuning, no adaptive attacker, no privacy/legal deployment analysis, and no long-horizon canary collision or forgetting test. Main run used 40 seeds, 960 trial/config rows, and a Naive Bayes text model.

## Claim scope

In a synthetic bag-of-words backdoor poisoning benchmark with 80 volunteer sources and 4 poisoners, per-source canary tokens provide strong source attribution when canaries appear reliably in source records; attribution degrades under 50% canary dropout at low poison volume.

## Why it stopped

Local synthetic mechanism test is complete and useful, but it is proxy evidence rather than direct production or paper-grade validation.

## Recommended next action

Run a bounded follow-up using a small transformer or embedding classifier on natural text with controlled canary insertion, adaptive attacker controls, and source-level false-positive thresholds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-text canary attribution under adaptive poisoning
- Success threshold: At least 0.80 source-level MAP and 0.90 ROC-AUC at a specified canary coverage, with false positives bounded against a no-canary baseline across at least 20 seeds.
- Stop condition: Stop if canary attribution does not exceed the no-canary baseline by at least 0.20 MAP under realistic canary coverage, or if adaptive dilution makes source attribution indistinguishable from chance.

## Evidence references

- Artifact root: `<local-path>/projects/canary-probe-attribution-for-volunteer-data-poisoning-detection-4379a08fdf78`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
