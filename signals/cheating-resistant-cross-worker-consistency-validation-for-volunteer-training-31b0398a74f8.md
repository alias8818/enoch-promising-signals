# Cheating-Resistant Cross-Worker Consistency Validation for Volunteer Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cheating-resistant-cross-worker-consistency-validation-for-volunteer-training-31b0398a74f8`
Run ID: `cheating-resistant-cross-worker-consistency-validation-for-volunteer-training-31b0398a74f8-20260527T193843191469+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/038bddab746a

## What looked useful

Private hidden gold plus gold-qualified anchor consensus reached AUROC 0.9255 versus 0.7392 for naive pairwise agreement across 28,800 synthetic worker rows. When colluders could identify all gold tasks, the proposed hybrid collapsed to AUROC 0.4449, showing that the design is not broadly cheating-resistant under gold leakage.

## Boundaries and scale limits

No real volunteers, no natural-language rubric scoring, no production incentives, and no adaptive human adversaries. The gold-aware colluder stress test is synthetic but directly probes a key cheating-resistance failure mode.

## Claim scope

Synthetic binary volunteer-labeling simulation with randomized overlap, hidden gold tasks, careless workers, and coordinated colluders. Private hidden-gold anchor consensus improved bad-worker detection over naive pairwise agreement, but the proposed hybrid did not outperform anchor consensus alone.

## Why it stopped

Proxy simulation produced mixed evidence and an early falsification of broad cheating-resistance under gold-aware colluders; this is not a full validation.

## Recommended next action

Stop as a no-paper useful signal; any next test should use real or semi-real volunteer responses with concealed gold rotation and an adaptive colluder protocol rather than scaling this synthetic simulator alone.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive Colluder Evaluation with Rotating Hidden Gold
- Success threshold: Maintain AUROC at least 0.80 and average precision at least 0.70 for bad-worker detection under partial gold leakage, with honest-worker false-positive rate below 10% at the selected review threshold.
- Stop condition: Stop if adaptive colluders with partial gold knowledge reduce AUROC below 0.70 or require more hidden gold than is operationally plausible for volunteer training.

## Evidence references

- Artifact root: `<local-path>/projects/cheating-resistant-cross-worker-consistency-validation-for-volunteer-training-31b0398a74f8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
