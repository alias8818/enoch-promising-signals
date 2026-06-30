# Query-Sensitivity Router for Mixed-Precision Local Cascade

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `query-sensitivity-router-for-mixed-precision-local-cascade-865d4752a641`
Run ID: `query-sensitivity-router-for-mixed-precision-local-cascade-865d4752a641-20260526T085511148222+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/3d1fad879a66

## What looked useful

The routing mechanism is conditionally useful: uncertainty routing beat random escalation on digits and synthetic multiclass tasks, but failed on breast_cancer where the high model underperformed the quantized low model. A mixed-precision local cascade needs an expected-correction or validated-dominance guardrail, not uncertainty alone.

## Boundaries and scale limits

CPU-only sklearn proxy using small tabular/image datasets; not a real LLM cascade, not GPU serving, not full mixed-precision deployment evidence, and not publication-grade validation.

## Claim scope

On small local classification proxies, low-model uncertainty can improve matched-budget escalation when the high model is better, but it can reduce accuracy when the high model is worse on the routed slice.

## Why it stopped

Proxy evidence is mixed and not paper-ready: the mechanism helps only when the high model dominates and can harm accuracy otherwise.

## Recommended next action

Stop this run as a proxy useful-signal result; next test should compare uncertainty-only routing against an expected-correction guardrail on a local quantized LLM workload.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Expected-Correction Guardrail for Mixed-Precision Local Cascades
- Success threshold: At 10-25% high-model call rate, expected-correction routing must outperform uncertainty-only routing and random routing on quality without reducing accuracy below always-low on any evaluated slice.
- Stop condition: Stop if the expected-correction guardrail cannot beat random routing at matched call rates or if calibration requires labels/resources unavailable in local deployment.

## Evidence references

- Artifact root: `<local-path>/projects/query-sensitivity-router-for-mixed-precision-local-cascade-865d4752a641`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
