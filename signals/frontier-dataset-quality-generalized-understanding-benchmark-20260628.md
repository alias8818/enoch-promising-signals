# Dataset quality benchmark for generalized understanding beyond scale

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `frontier-dataset-quality-generalized-understanding-benchmark-20260628`
Run ID: `frontier-dataset-quality-generalized-understanding-benchmark-20260628-20260629T064245391541+0000`

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

- Linear ALI-208 frontier research issue: linear-ALI-208
- Jeremy frontier AI research intake: DSpark, post-training, dataset quality: user-frontier-ai-research-tracks-20260628

## What looked useful

Quality mattered within fixed-size comparisons: high/medium quality beat low quality by +0.0167 to +0.0653 held-out-pair accuracy and +0.0995 to +0.3062 IID accuracy. However, dataset size correlated more strongly with OOD accuracy than the aggregate quality score, and large_low_quality still beat small_high_quality on held-out-pair and longer-program accuracy.

## Boundaries and scale limits

Synthetic task only; four dataset regimes; three seeds; one small transformer; local GB10 CUDA run under two minutes for the longest confirmation; no natural-language, multimodal, frontier-scale, or multi-architecture validation.

## Claim scope

A controlled synthetic compositional arithmetic benchmark with one tiny transformer shows that dataset quality metrics improve matched-size IID and held-out-pair accuracy, but do not beat a 10x raw size increase on held-out compositional or longer-program splits.

## Why it stopped

No-paper useful signal: this is a local synthetic proxy and early falsification of the broad quality-beats-scale claim, not a full validation of generalized understanding datasets.

## Recommended next action

Run a bounded deepen follow-up that equalizes unique-example count and ablates duplication, label noise, primitive coverage, and compositional-pair coverage one factor at a time.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Factorized quality ablation with equalized unique-example count
- Success threshold: At least one isolated quality factor improves held-out pair accuracy by 0.05 absolute or more over its matched control with non-overlapping seed-level confidence intervals, while raw duplicate-inflated size fails to produce the same gain.
- Stop condition: Stop if isolated quality-factor gains are below 0.02 absolute on held-out pair accuracy or if effects reverse across seeds.

## Evidence references

- Artifact root: `<local-path>/projects/frontier-dataset-quality-generalized-understanding-benchmark-20260628`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
