# GPT-2-small preference matrix for quality-adjusted post-training efficiency

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gpt-2-small-preference-matrix-for-quality-adjusted-post-tr-5f5c72e1fe`
Run ID: `gpt-2-small-preference-matrix-for-quality-adjusted-post-tr-5f5c72e1fe-20260629T081214067683+0000`

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

- Parent run decision: Post-training quality-adjusted efficiency experiment matrix: enoch://control-plane/projects/frontier-post-training-quality-adjusted-efficiency-20260628/runs/frontier-post-training-quality-adjusted-efficiency-20260628-20260629T075351976896+0000
- Linear ALI-207 frontier research issue: linear-ALI-207
- Jeremy frontier AI research intake: DSpark, post-training, dataset quality: user-frontier-ai-research-tracks-20260628

## What looked useful

A small preference matrix can expose category-dependent post-training efficiency on GPT-2-small: reasoning-clarity pairs produced the strongest decision-level held-out effect, instruction-following produced the strongest margin-per-second effect, and factual-specificity was consistently weakest.

## Boundaries and scale limits

Only 8 handcrafted training pairs and 4 handcrafted held-out pairs, 40 DPO steps per variant, no public human preference dataset, no generated-output judging, no SFT baseline, no LoRA/control trainer comparison, and only GPT-2-small.

## Claim scope

Bounded local GPT-2-small DPO probe on a handcrafted 4-category preference matrix: reasoning-clarity pairs were the only subset that consistently flipped held-out preference win rate from 0.25 to 0.50 across 3 seeds, while balanced mixing was not more efficient than the best single-category subsets.

## Why it stopped

The result is a direct but tiny proxy probe with handcrafted preferences; it supports a mechanism-level signal but is not broad or rigorous enough for paper-positive closure.

## Recommended next action

Run a bounded deepen follow-up using a small public preference dataset, GPT-2-small SFT and DPO controls, generated-output judging, and at least 3 seeds; stop this run as no-paper useful signal.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Public-data GPT-2-small preference matrix with SFT/DPO controls
- Success threshold: A category-stratified matrix must beat balanced/random mixtures by at least 5 percentage points held-out preference accuracy or generated-output win rate, while matching or improving quality gain per GPU-second across at least 3 seeds.
- Stop condition: Stop if category-stratified variants do not beat balanced/random controls on either held-out preference accuracy or generated-output judging, or if gains disappear across seeds.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-preference-matrix-for-quality-adjusted-post-tr-5f5c72e1fe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
