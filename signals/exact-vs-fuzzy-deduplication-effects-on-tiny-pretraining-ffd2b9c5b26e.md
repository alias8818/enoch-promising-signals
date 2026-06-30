# Exact vs Fuzzy Deduplication Effects on Tiny Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-vs-fuzzy-deduplication-effects-on-tiny-pretraining-ffd2b9c5b26e`
Run ID: `exact-vs-fuzzy-deduplication-effects-on-tiny-pretraining-ffd2b9c5b26e-20260613T221038840582+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8c652a0ea698

## What looked useful

Fuzzy dedup removed about half of the exact-deduped corpus but improved evaluation loss over exact dedup by only about 0.002. Both exact and fuzzy dedup improved near-duplicate held-out loss versus no dedup, but worsened clean held-out loss in all three seeds.

## Boundaries and scale limits

Synthetic corpus only; no real web corpus, no production MinHash/LSH pipeline, no tokenizer/model scaling, and no long training schedule. The result is a proxy useful signal, not a broad validation of deduplication policy for real pretraining.

## Claim scope

Controlled synthetic tiny character-level Transformer pretraining with known exact and fuzzy duplicate clusters, three seeds, 500 optimizer steps per condition.

## Why it stopped

No-paper proxy result: the synthetic experiment produced a useful mixed signal, but fuzzy-vs-exact deltas were too small and the setup too artificial for publication-grade claims.

## Recommended next action

Stop this worker run; the next bounded action is a real-corpus confirmation on WikiText/TinyStories-scale data with a practical fuzzy deduper and a training-token-matched control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus token-matched exact vs fuzzy dedup tiny pretraining
- Success threshold: Fuzzy dedup must improve clean held-out loss over exact dedup by at least 0.02 nats or reduce near-duplicate/canary memorization by at least 10% without worsening clean held-out loss by more than 0.01 nats across three seeds.
- Stop condition: Stop if fuzzy-vs-exact clean-loss changes remain within +/-0.01 nats and memorization metrics improve by less than 5%, or if dedup effects reverse across seeds.

## Evidence references

- Artifact root: `<local-path>/projects/exact-vs-fuzzy-deduplication-effects-on-tiny-pretraining-ffd2b9c5b26e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
