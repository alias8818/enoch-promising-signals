# Dynamic Cascade Confidence Thresholding

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `dynamic-cascade-confidence-thresholding-b242e6b25458`
Run ID: `dynamic-cascade-confidence-thresholding-b242e6b25458-20260529T230701498630+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ba9392f21335

## What looked useful

Dynamic thresholding raised normalized cost from 0.1569 to 0.1670 and improved overall accuracy only from 0.2217 to 0.2276, while noisy-block accuracy was unchanged at 0.1054. The cheap model was overconfident and the static threshold saturated at 0.995, leaving little useful signal for raw confidence dynamics.

## Boundaries and scale limits

Small CPU-only image-classification proxy; not tested on LLM cascades, production request streams, calibrated neural confidence, real serving latency/cost, or multi-expert cascades.

## Claim scope

On sklearn digits with a weak overconfident GaussianNB first-stage classifier, an RBF SVC fallback, Gaussian corruption stream shift, and a fixed cost model, a rolling confidence dynamic threshold did not improve noisy-block robustness over a static clean-validation threshold.

## Why it stopped

Proxy early falsification: the tested dynamic rule produced no noisy-shift accuracy gain over static thresholding and increased cost; this is not a full large-model validation.

## Recommended next action

Stop this raw-confidence dynamic-threshold variant as an early proxy negative; next bounded work should test calibrated/conformal or OOD-aware gates rather than only rolling mean confidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated OOD-Aware Cascade Gates Under Corruption Shift
- Success threshold: Noisy-block accuracy improves by >=0.05 absolute over static confidence thresholding with normalized cost increase <=0.10 and wins in at least 8/10 seeds.
- Stop condition: Stop if calibrated/OOD-aware gates fail to improve noisy-block accuracy by >=0.02 absolute over static in a 10-seed bounded run or require always-expensive-like escalation.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-cascade-confidence-thresholding-b242e6b25458`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
