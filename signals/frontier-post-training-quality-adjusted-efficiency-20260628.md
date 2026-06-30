# Post-training quality-adjusted efficiency experiment matrix

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `frontier-post-training-quality-adjusted-efficiency-20260628`
Run ID: `frontier-post-training-quality-adjusted-efficiency-20260628-20260629T075351976896+0000`

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

- Linear ALI-207 frontier research issue: linear-ALI-207
- Jeremy frontier AI research intake: DSpark, post-training, dataset quality: user-frontier-ai-research-tracks-20260628

## What looked useful

Across 108 CUDA cells, DPO improved mean true greedy reward by 0.059959 with 25/27 positive cells and mean QAE per 1k pairs of 0.042700. KTO-lite improved by 0.021924 with 26/27 positive cells. SFT and weighted SFT had negative mean quality deltas at higher label noise, especially at 4096 pairs, indicating that chosen-only training can turn extra noisy preference data into lower true reward.

## Boundaries and scale limits

Synthetic reward and preference labels only; tiny MLP policies rather than language models; no human labels, no real text generation, no 7B+ or frontier-scale training, no reward-model overoptimization study, and no long-run robustness validation.

## Claim scope

In a small synthetic contextual preference task with known ground-truth reward, a quality-adjusted efficiency matrix can distinguish post-training objectives: DPO produced the strongest mean quality gain and pair-normalized efficiency, KTO-lite was consistently positive but smaller, and chosen-only SFT variants became harmful under higher label noise and larger noisy pair budgets.

## Why it stopped

Closed as no-paper useful signal: the local result is reproducible and mechanism-informative, but it is synthetic/proxy evidence rather than direct post-training evidence on language models or human preference data.

## Recommended next action

Run a bounded direct-evidence follow-up on a GPT-2-small-class language model with an open preference dataset, matching update budgets and reporting quality gain per GPU-second and per preference token.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small preference matrix for quality-adjusted post-training efficiency
- Success threshold: DPO or another reference-relative objective must beat chosen-only SFT by at least 10% in quality gain per preference token and per GPU-second while preserving nonnegative held-out quality across noise/disagreement strata.
- Stop condition: Stop if all reference-relative objectives fail to exceed chosen-only SFT on both quality-normalized efficiency metrics or if held-out text quality degrades for every objective at matched budget.

## Evidence references

- Artifact root: `<local-path>/projects/frontier-post-training-quality-adjusted-efficiency-20260628`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
