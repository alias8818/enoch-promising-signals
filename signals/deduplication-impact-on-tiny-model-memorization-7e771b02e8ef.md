# Deduplication impact on tiny model memorization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `deduplication-impact-on-tiny-model-memorization-7e771b02e8ef`
Run ID: `deduplication-impact-on-tiny-model-memorization-7e771b02e8ef-20260609T073213503155+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/482d9398fb58

## What looked useful

Exact duplicate canary repetition caused reliable verbatim memorization in a tiny local LM; exact dedup removed greedy exact extraction across three seeds, though rank-based exposure remained high and insensitive.

## Boundaries and scale limits

Synthetic corpus, five canaries, exact duplicates only, character-window neural LM rather than transformer, no natural-text corpus, no subword tokenizer, no large-scale training, and rank exposure saturated under unique prompts.

## Claim scope

In a three-seed synthetic NumPy tiny character-window language model probe, exact-line deduplication reduced verbatim greedy canary reconstruction from 5/5 to 0/5 and increased target canary NLL by 2.74 nats/char on average.

## Why it stopped

No-paper closure: this is a controlled synthetic proxy with a useful mechanism signal, not full validation for realistic tiny transformers or natural corpora.

## Recommended next action

Run a bounded tiny-transformer follow-up on a natural-text corpus with inserted canaries, duplicate-count dose response, exact/fuzzy dedup controls, and the same extraction metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny-transformer deduplication canary dose-response
- Success threshold: Deduplication reduces greedy exact canary extraction by at least 50% and increases target canary NLL without worsening held-out validation loss by more than 5% across at least three seeds.
- Stop condition: Stop if a smoke-sized transformer cannot learn the corpus above a trivial baseline, or if deduplication shows no consistent reduction in extraction or canary likelihood across seeds.

## Evidence references

- Artifact root: `<local-path>/projects/deduplication-impact-on-tiny-model-memorization-7e771b02e8ef`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
