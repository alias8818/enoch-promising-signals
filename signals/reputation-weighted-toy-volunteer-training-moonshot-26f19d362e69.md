# Reputation-Weighted Toy Volunteer Training (Moonshot)

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `reputation-weighted-toy-volunteer-training-moonshot-26f19d362e69`
Run ID: `reputation-weighted-toy-volunteer-training-moonshot-26f19d362e69-20260613T130052017609+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f83ebaa4f43d

## What looked useful

Reputation weighting improved independent-noise accuracy from 0.7157 to 0.7228 mean accuracy, close to the clean-label 0.7258 control. Under subgroup bias, random audit reputation improved subgroup accuracy from 0.7825 to 0.7992 but remained below stratified audit reputation at 0.8229 and clean labels at 0.8299.

## Boundaries and scale limits

Toy logistic regression only; synthetic volunteers and labels; no real volunteer data, no strategic behavior, no LLM fine-tuning, no large-model or multi-node training evidence.

## Claim scope

In a deterministic synthetic binary-classification simulation, audit-estimated reputation weighting improves training from independently noisy volunteer labels, while subgroup-aware auditing is needed when volunteers have correlated subgroup-specific bias.

## Why it stopped

Synthetic proxy evidence supports a narrow mechanism and exposes a failure mode, but it is not direct/full validation of volunteer training at scale.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is a deeper subgroup-aware audit policy test on semi-real or higher-fidelity volunteer-label data.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Subgroup-aware reputation audits for biased volunteer labels
- Success threshold: At equal audit budget, subgroup-aware or active reputation auditing improves subgroup accuracy by at least 2 percentage points over random global reputation without reducing overall accuracy by more than 0.5 percentage points.
- Stop condition: Stop if subgroup-aware auditing does not beat random global reputation by at least 1 percentage point on subgroup accuracy across two audit budgets, or if real/semi-real gold labels are unavailable.

## Evidence references

- Artifact root: `<local-path>/projects/reputation-weighted-toy-volunteer-training-moonshot-26f19d362e69`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
