# Real-Text 50M Dedup Threshold Sweep With Small-LM Validation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-text-50m-dedup-threshold-sweep-with-small-lm-validati-e4dade649d`
Run ID: `real-text-50m-dedup-threshold-sweep-with-small-lm-validati-e4dade649d-20260629T022359173116+0000`

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

- Parent run decision: Dedup Threshold Sweep at 50M Tokens: enoch://control-plane/projects/dedup-threshold-sweep-at-50m-tokens-dfdd5249ea2b/runs/dedup-threshold-sweep-at-50m-tokens-dfdd5249ea2b-20260629T015657805100+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3f57fe012b74

## What looked useful

Threshold choice materially changed duplicate recall (about 0.51 at 0.55, 0.31 at 0.70, 0.13 at 0.85, near zero at 0.95+) with almost no false positives. Small-LM validation differences were only about 0.001-0.003 nats, with 0.70 best on mean but not best for every seed.

## Boundaries and scale limits

Not a 50M-token or full-corpus validation. Primary runs used 2807 contaminated training documents and 264 held-out validation documents per seed, fixed 220-step character-GRU training, and controlled injected duplicates rather than naturally occurring web-scale duplication.

## Claim scope

On a bounded Gutenberg real-text paragraph corpus with injected near-duplicates, shingle-Jaccard dedup threshold 0.70 gave the best mean small character-GRU validation loss across three seeds while maintaining near-perfect duplicate removal precision; the effect was small and seed-sensitive.

## Why it stopped

Bounded proxy produced a useful threshold-ranking signal but did not produce robust 50M-scale or publication-grade validation.

## Recommended next action

Run a medium direct follow-up on an actual about-50M-token real-text corpus with fixed held-out validation, natural plus injected duplicate labels, and at least five LM seeds; stop if the best threshold fails to beat no-dedup by a predeclared margin exceeding seed noise.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium 50M-token real-text dedup threshold validation with repeated small-LM seeds
- Success threshold: A threshold in 0.70-0.85 beats no-dedup and 0.55 by at least 0.01 validation nats or an equivalent predeclared effect larger than the 95% seed-noise interval, while preserving duplicate-removal precision above 0.98 on labeled duplicates.
- Stop condition: Stop as no-paper if validation-loss differences remain within seed noise or if duplicate labels show precision below 0.98 at the candidate threshold.

## Evidence references

- Artifact root: `<local-path>/projects/real-text-50m-dedup-threshold-sweep-with-small-lm-validati-e4dade649d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
