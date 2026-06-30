# MinHash Dedup vs Random Sampling for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `minhash-dedup-vs-random-sampling-for-tiny-pretraining-22d11530147b`
Run ID: `minhash-dedup-vs-random-sampling-for-tiny-pretraining-22d11530147b-20260619T183542293217+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/86b6ef8f5ec2

## What looked useful

MinHash reduced duplicate rate from 0.3115 to 0.0348 and increased unique source docs from 87.67 to 120.00 at the same budget; validation NLL changed from 2.3328 to 2.3294 on average, with one seed worse.

## Boundaries and scale limits

One source book, injected near-duplicate pressure, three seeds, about 45k selected characters per strategy, and a tiny character-context neural LM; not evidence for web-scale transformer pretraining.

## Claim scope

In a bounded CPU-only probe using a duplicate-injected public-domain text corpus and a tiny NumPy character language model, MinHash near-dedup selection substantially increased unique-source coverage and shingle diversity under a fixed character budget, with only a tiny mixed average validation-loss benefit over random sampling.

## Why it stopped

Proxy-only tiny-LM evidence supports the dedup/diversity mechanism but is mixed on held-out loss and is not full validation of tiny transformer pretraining.

## Recommended next action

Stop this run as no-paper useful signal; deepen with a small-transformer fixed-token-budget comparison on a naturally duplicate-heavy public corpus.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer MinHash dedup vs random sampling on natural near-duplicates
- Success threshold: Across at least three seeds, MinHash must improve unique-source coverage by at least 20% and reduce near-duplicate retention by at least 50% while matching or improving held-out loss by at least 0.5% relative to random sampling.
- Stop condition: Stop if MinHash fails to improve diversity by 20%, or if diversity improves but held-out loss regresses by more than 1% in at least two of three seeds.

## Evidence references

- Artifact root: `<local-path>/projects/minhash-dedup-vs-random-sampling-for-tiny-pretraining-22d11530147b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
