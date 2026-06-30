# Actual local model three-tier cascade with difficulty routing

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `actual-local-model-three-tier-cascade-with-difficulty-rout-7b0e97ef0d`
Run ID: `actual-local-model-three-tier-cascade-with-difficulty-rout-7b0e97ef0d-20260628T081040075801+0000`

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

- Parent run decision: Difficulty-Routed Three-Tier Local Cascade on GB10: enoch://control-plane/projects/difficulty-routed-three-tier-local-cascade-on-gb10-5856bed1640b/runs/difficulty-routed-three-tier-local-cascade-on-gb10-5856bed1640b-20260628T075457829943+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1e1b24b469b9

## What looked useful

Always-small scored 33.33% at 0.50 average cost, always-medium 63.89% at 1.50, always-large 72.22% at 3.00. The tuned serial confidence cascade scored 55.56% at 1.58, worse than always-medium while costing more. Oracle difficulty routing scored 66.67% at 1.67, still below always-large. Oracle-best reached 86.11% at 2.42, showing complementarity exists but was not captured by simple confidence/difficulty signals. Medium and large tiers were overconfident when wrong.

## Boundaries and scale limits

Small direct test only: compact multiple-choice next-token scoring, one fixed benchmark, relative parameter-cost accounting rather than production p95 serving, no trained router, no open-ended generation, and no 7B+ full serving validation.

## Claim scope

On a 36-question controlled multiple-choice benchmark using real local Qwen2.5 0.5B/1.5B/3B Instruct tiers, a simple tuned confidence/difficulty cascade did not preserve large-model accuracy at meaningfully lower cost.

## Why it stopped

Controlled small direct test failed the practical threshold for simple three-tier difficulty routing: the tuned cascade underperformed always-medium and always-large baselines, and best confidence thresholds only matched always-large accuracy at near always-large cost.

## Recommended next action

Stop this run as no-paper useful negative evidence; next bounded work should train or calibrate a router/verifier on held-out data and require it to beat always-medium cost-adjusted accuracy while approaching always-large accuracy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated verifier router for three-tier local model cascades
- Success threshold: On held-out tasks, the router achieves at least always-medium accuracy plus 5 percentage points at no more than 2.0 average relative cost, or reaches within 3 percentage points of always-large accuracy at least 20% lower average relative cost.
- Stop condition: Stop if calibrated routing cannot beat always-medium by 2 percentage points at cost <= 2.0 or if matching always-large accuracy requires average cost above 2.7.

## Evidence references

- Artifact root: `<local-path>/projects/actual-local-model-three-tier-cascade-with-difficulty-rout-7b0e97ef0d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
