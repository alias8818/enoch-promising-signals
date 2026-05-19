# Nonlinear Adapter Hidden-Volunteer Repetition Under Fresh-Volunteer Scarcity

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `nonlinear-adapter-hidden-volunteer-repetition-under-fresh-4fe051b828`
Run ID: `nonlinear-adapter-hidden-volunteer-repetition-under-fresh-4fe051b828-20260518T051339744054+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Nonlinear Adapter Hidden-Volunteer Repetition Under Fresh-Volunteer Scarcity: internal_generated:nonlinear-adapter-hidden-volunteer-repetition-under-fresh-4fe051b828

## What looked useful

Nonlinear repetition appears useful only in the tightest hidden-unit scarcity regime. Full-sweep mean paired MSE improvement was +24.99% vs fresh-only, +26.02% vs linear-repeat, and +6.70% vs dense at width 8; +15.23% and +15.61% vs fresh/linear at width 16 but -2.48% vs dense; approximately tied or worse at width 32; worse than every baseline at width 64.

## Boundaries and scale limits

Validated only on synthetic MLP teacher-student regression with input_dim 32, teacher_width 96, 5 seeds, widths 8/16/32/64, and 16384/4096/4096 train/validation/test samples. Not validated on natural language, vision, GPT-2-small-class models, or production adapter workloads.

## Claim scope

In a synthetic nonlinear teacher-student regression benchmark, nonlinear hidden-volunteer repetition helps under severe fresh-hidden-width scarcity: at width 8 it beats fresh-only, linear-repeat, and parameter-matched dense baselines across 5/5 seeds; at width 16 it beats fresh-only and linear-repeat but not dense. The claim does not extend to wider fresh budgets or real transformer adapters.

## Why it stopped

Bounded full synthetic validation found a scoped mechanism signal under severe scarcity, but the broader hypothesis is mixed: the nonlinear adapter loses to dense at width 16, loses/ties at width 32, and is worse than all baselines at width 64. This is not publication-grade direct evidence for the architecture.

## Recommended next action

Stop this run as no-paper useful signal; the only warranted next bounded action is a real-task deepen test at GPT-2-small or comparable adapter scale to check whether the severe-scarcity synthetic benefit survives against a parameter-matched dense adapter.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Task Severe-Scarcity Nonlinear Adapter Validation
- Success threshold: Across at least 3 seeds, nonlinear repetition improves the severe-width held-out metric by >=10% versus all three baselines and does not underperform the dense baseline at the wider control width.
- Stop condition: Stop as negative if nonlinear repetition fails to beat the dense parameter-matched baseline at the tightest real-task width or if the benefit appears only on synthetic teacher-student data.

## Evidence references

- Artifact root: `<local-path>/projects/nonlinear-adapter-hidden-volunteer-repetition-under-fresh-4fe051b828`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
