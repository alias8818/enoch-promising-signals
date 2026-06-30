# Deduplication Threshold Sweep for Local Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `deduplication-threshold-sweep-for-local-pretraining-d6ee02231b43`
Run ID: `deduplication-threshold-sweep-for-local-pretraining-d6ee02231b43-20260611T165430181036+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/33572c430bc7

## What looked useful

Across three seeds, threshold 0.72 retained 334/432 documents on average, improved clean eval loss by 0.0226 versus no dedup on average, and worsened exact-duplicate eval loss by 0.0126 and near-duplicate eval loss by 0.0150. The effect direction supports a dedup tradeoff mechanism, but seed variance and synthetic data make it no-paper evidence.

## Boundaries and scale limits

Synthetic corpus only; tiny model; 260 training steps per threshold; three seeds; no tokenizer-scale, web-corpus, GPT-2-small-class, or long pretraining validation.

## Claim scope

On a controlled synthetic near-duplicate corpus with a tiny 3-layer character-level causal Transformer, lowering shingled-Jaccard deduplication thresholds from no-dedup to 0.72 removed duplicate-family material and produced a duplicate-evaluation versus clean-evaluation tradeoff. The clean-loss optimum was not stable enough across three seeds to justify a general threshold recommendation.

## Why it stopped

Bounded synthetic evidence found a plausible mechanism but not a stable, publication-grade threshold result; this is not a full validation.

## Recommended next action

Stop this worker run as no-paper useful signal; next bounded action is a direct medium-scale run on a real small text corpus with GPT-2-small-class or parameter-matched baseline and at least five seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus dedup threshold sweep with GPT-2-small-class baseline
- Success threshold: A non-no-dedup threshold improves clean held-out loss by at least 1% relative while reducing duplicate memorization diagnostics, with confidence intervals excluding zero or an equivalent pre-registered stability criterion.
- Stop condition: Stop if retained-token loss explains the effect, confidence intervals overlap no-dedup after five seeds, or all non-no-dedup thresholds worsen clean held-out loss by at least 1%.

## Evidence references

- Artifact root: `<local-path>/projects/deduplication-threshold-sweep-for-local-pretraining-d6ee02231b43`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
