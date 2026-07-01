# Local MinHash Deduplication for Tiny Pretraining Gains

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `local-minhash-deduplication-for-tiny-pretraining-gains-bb1d1f6a8270`
Run ID: `local-minhash-deduplication-for-tiny-pretraining-gains-bb1d1f6a8270-20260520T075256466317+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/0189f03a7099

## What looked useful

MinHash dedup had no effect when no chunks were removed, and on contaminated corpora improved mean validation cross entropy by 0.0010 to 0.0091 nats across duplicate-fraction sweeps; the primary 0.35 duplicate-fraction setting improved by 0.00728 nats, about 0.21% relative. Effects were small relative to seed variance and not paper-ready.

## Boundaries and scale limits

Toy public corpus, synthetic near-duplicate injection, character n-gram LM rather than transformer pretraining, five seeds per condition, short CPU-only runs; no real web-corpus duplicate structure, downstream transfer, tokenizer effects, or large-scale training tested.

## Claim scope

On a Tiny Shakespeare character n-gram LM proxy with synthetic local near-duplicate contamination, local MinHash LSH deduplication removed verified high-Jaccard chunks and produced small mean held-out cross-entropy improvements under a fixed 800k-token training budget.

## Why it stopped

Proxy/early bounded result rather than full validation: evidence comes from a toy corpus with synthetic duplicates and an n-gram LM, so it cannot support a broad pretraining or paper-positive claim.

## Recommended next action

Stop this run as a no-paper useful-signal proxy result; the concrete next bounded test is a tiny transformer validation on a real duplicated text corpus with matched sequence-item budget and a predefined improvement threshold above seed noise.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny Transformer Validation of Local MinHash Deduplication
- Success threshold: Mean dedup validation loss improvement at least 0.01 nats and larger than the paired standard error, with no degradation in any no-removal control.
- Stop condition: Stop as negative if dedup fails to beat raw by 0.01 nats, reverses on two or more seeds, or the measured duplicate rate is too low for MinHash to remove at least 5% of train chunks.

## Evidence references

- Artifact root: `<local-path>/projects/local-minhash-deduplication-for-tiny-pretraining-gains-bb1d1f6a8270`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
