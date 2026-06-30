# Micro-audit gradient validation for volunteer training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `micro-audit-gradient-validation-for-volunteer-training-1d2388e5c9a4`
Run ID: `micro-audit-gradient-validation-for-volunteer-training-1d2388e5c9a4-20260604T074740840916+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/be144912c7ce

## What looked useful

Targeted disagreement micro-audit improved label accuracy by 2.46 percentage points, validation accuracy by 0.49 percentage points, and gradient L2 error to the clean gradient by 0.0184, and beat random audit on gradient cosine in 90.9% of paired settings. It failed the direct pre-set gradient-cosine threshold versus raw majority vote with mean delta -0.03345.

## Boundaries and scale limits

No real volunteers, real audit rubric, multi-class task, LLM/RLHF setting, or full-scale model training was tested; evidence is limited to 50-seed synthetic sweeps.

## Claim scope

Synthetic binary logistic-regression proxy with 3 noisy volunteer labels per example and a 25% fixed-budget disagreement-targeted micro-audit.

## Why it stopped

Proxy/early falsification of the headline gradient-cosine validation claim: targeted micro-audit did not improve gradient cosine over raw majority vote despite improving labels, validation accuracy, and gradient L2 distance.

## Recommended next action

Stop as a no-paper useful signal; a bounded follow-up should test the metric conflict on a real or richer volunteer-label dataset before any scale-up claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Realistic metric-conflict audit for volunteer micro-audits
- Success threshold: Targeted audit must improve downstream validation by at least 1 percentage point and gradient L2 error by at least 0.01 versus raw majority, while explaining or resolving any gradient-cosine degradation across noise regimes.
- Stop condition: Stop if targeted audit fails to beat raw majority on downstream validation or gradient L2 error in the richer dataset, or if cosine degradation remains unexplained.

## Evidence references

- Artifact root: `<local-path>/projects/micro-audit-gradient-validation-for-volunteer-training-1d2388e5c9a4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
