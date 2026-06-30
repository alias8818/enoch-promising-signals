# Tiny Transformer Real-Corpus Dedup Boundary Test

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `tiny-transformer-real-corpus-dedup-boundary-test-7ced90dfa4`
Run ID: `tiny-transformer-real-corpus-dedup-boundary-test-7ced90dfa4-20260610T010631866409+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: MinHash vs Exact 5-gram Deduplication for Tiny Pretraining: enoch://control-plane/projects/minhash-vs-exact-5-gram-deduplication-for-tiny-pretraining-abc3d9c4a05e/runs/minhash-vs-exact-5-gram-deduplication-for-tiny-pretraining-abc3d9c4a05e-20260609T204209956848+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e1d7582ea778

## What looked useful

Across seeds 7, 11, and 23, mean duplicate-trained boundary advantage was 0.0243 nats versus a 0.05-nat threshold, and mean boundary-minus-interior advantage was 0.0103 nats versus a 0.03-nat threshold. No seed met both criteria.

## Boundaries and scale limits

Three seeds, 500 optimizer steps per condition, 40 evaluated boundaries per seed, character-level modeling, small WikiText-derived corpus slice, exact duplicates only; not a tokenizer-level, GPT-2-small-class, large-corpus, long-training, or near-duplicate validation.

## Claim scope

In a Tier 1 small direct test using matched tiny character-level Transformer language models trained on WikiText-derived real text, retained exact duplicate documents did not produce a boundary-specific loss advantage meeting the predeclared threshold at late duplicate-document starts.

## Why it stopped

Small direct real-corpus test did not meet the predeclared boundary-specific success threshold; this is an early falsification, not a full validation of all deduplication or memorization regimes.

## Recommended next action

Stop this run as a Tier 1 early falsification of the stated boundary-specific threshold; only revisit with a tokenizer-level, longer-trained bounded follow-up if the controller wants to test whether the small generic duplicate advantage grows under stronger modeling.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tokenizer-Level Duplicate Boundary Confirmation
- Success threshold: Mean duplicate-trained boundary loss advantage at least 0.05 nats and boundary-minus-interior advantage at least 0.03 nats across seeds, with no seed showing a reversed boundary-specific effect.
- Stop condition: Stop as unsupported if aggregate boundary advantage remains below 0.05 nats or boundary-minus-interior advantage remains below 0.03 nats after the planned seeds.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-transformer-real-corpus-dedup-boundary-test-7ced90dfa4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
