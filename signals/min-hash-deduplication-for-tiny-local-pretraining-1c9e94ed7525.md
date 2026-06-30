# Min-Hash Deduplication for Tiny Local Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `min-hash-deduplication-for-tiny-local-pretraining-1c9e94ed7525`
Run ID: `min-hash-deduplication-for-tiny-local-pretraining-1c9e94ed7525-20260605T045904090913+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/05124460a93a

## What looked useful

MinHash found about 68.9% of synthetic duplicate documents with 0 labeled false drops. Plain MinHash dedup worsened clean NLL (2.8811 vs raw 2.8568), but token-budget-matched MinHash improved clean NLL by 0.0173 nats/token and raised duplicate-probe NLL by 0.1837 nats/token, indicating less memorization.

## Boundaries and scale limits

Synthetic generated documents, 5 seeds, 1900 raw documents per seed, 64-permutation MinHash LSH, and a trigram LM proxy. No real web corpus, tokenizer, neural LM optimizer dynamics, downstream tasks, or large-scale pretraining were tested.

## Claim scope

On a controlled synthetic near-duplicate corpus with a count-based trigram tiny-pretraining proxy, MinHash deduplication reduced near-duplicate memorization and improved clean held-out NLL only when the deduplicated corpus was resampled to match the raw token budget; training on fewer deduplicated tokens hurt clean NLL.

## Why it stopped

Closed as no-paper useful signal because current evidence is synthetic/proxy-only and shows a conditional effect rather than publication-grade validation.

## Recommended next action

Run a bounded real-corpus tiny neural LM confirmation with matched tokenizer, matched token/step budget, raw and exact-dedup controls, MinHash threshold ablations, validation NLL, and memorization probes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus token-budget-matched MinHash dedup for tiny neural LM pretraining
- Success threshold: Budget-matched MinHash improves validation NLL versus raw and exact-dedup controls in at least 3 seeds while reducing memorization probe likelihood, without material false-positive deletion of non-duplicate documents.
- Stop condition: Stop if budget-matched MinHash does not beat raw or exact-dedup validation NLL, or if MinHash false-positive deletion exceeds 1% of manually/labeled non-duplicate samples.

## Evidence references

- Artifact root: `<local-path>/projects/min-hash-deduplication-for-tiny-local-pretraining-1c9e94ed7525`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
