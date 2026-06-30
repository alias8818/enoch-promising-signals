# Answer-divergence instruction data selection benchmark

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `87`
Project ID: `adg-answer-divergence-data-selection-20260628`
Run ID: `adg-answer-divergence-data-selection-20260628-20260629T063237122388+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `87`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 12}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- external source URL present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Exa/arXiv frontier AI scout shortlist: frontier-ai-scout-exa-arxiv-20260628
- Linear ALI-208 frontier research issue: linear-ALI-208
- Answer-divergence instruction data selection benchmark: https://arxiv.org/abs/2604.10448v1
- Answer-divergence instruction data selection benchmark: https://github.com/WisdomShell/ADG

## What looked useful

High answer divergence is a repeatable hard-example targeting signal (+2.31 percentage points hard accuracy vs random, normal 95% CI +1.53 to +3.09 points, 24/30 seed wins), but naive high-divergence selection slightly underperforms random on overall accuracy (-0.66 points). Mid-divergence selection gives only a small uncertain overall gain (+0.29 points, CI -0.44 to +1.03).

## Boundaries and scale limits

Synthetic prompts, simulated weak answerers, binary answers, small engineered-feature/text MLP student, 500 selected examples per policy, 30 seeds; not evidence for real LLM instruction tuning, natural instruction distributions, open-ended grading, or large pretrained models.

## Claim scope

In a synthetic yes/no instruction-selection benchmark with exact labels, five simulated weak answerers, and a small CUDA-trained MLP student, highest answer-divergence selection improves hard-subset accuracy but does not improve overall heldout accuracy versus random selection.

## Why it stopped

No-paper proxy result: synthetic evidence is mixed and does not support the broad claim that answer-divergence selection generally beats random instruction data selection, though it identifies a narrower hard-example targeting mechanism.

## Recommended next action

Run a bounded real-data deepen test using actual teacher/model answer divergence on an instruction dataset and compare equal-token fine-tuning against random and difficulty controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-teacher answer-divergence instruction selection
- Success threshold: High-divergence or diversity-constrained divergence beats random by at least 1.5 percentage points overall and at least 2.0 percentage points on the hard slice across at least 5 seeds without increasing selected-label noise.
- Stop condition: Stop if high/mid/diversity-constrained divergence fails to beat random on both overall and hard-slice metrics after 5 paired seeds, or if teacher divergence is dominated by answer-format noise rather than semantic disagreement.

## Evidence references

- Artifact root: `<local-path>/projects/adg-answer-divergence-data-selection-20260628`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
