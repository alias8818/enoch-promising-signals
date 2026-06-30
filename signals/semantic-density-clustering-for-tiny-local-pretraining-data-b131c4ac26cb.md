# Semantic-density clustering for tiny local pretraining data

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `semantic-density-clustering-for-tiny-local-pretraining-data-b131c4ac26cb`
Run ID: `semantic-density-clustering-for-tiny-local-pretraining-data-b131c4ac26cb-20260528T072653353900+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/1290e91868e3

## What looked useful

The selector achieved higher semantic-density scores but reduced held-out lexical coverage and produced worse validation LM loss than every random baseline in the bounded full run: 3.7385 vs random losses 3.6198, 3.5361, and 3.4862.

## Boundaries and scale limits

Tested on local Markdown/text chunks, 6000 candidate documents, 750 selected documents, 1000 held-out documents, a shared word vocabulary, and a small GRU trained for 220 update steps. Not tested with neural sentence embeddings, GPT-2-class transformers, broad web/code corpora, convergence training, or downstream transfer.

## Claim scope

For a local documentation corpus, TF-IDF/SVD semantic-density cluster selection of central documents did not improve tiny word-level GRU language-model pretraining over matched random document selection.

## Why it stopped

Bounded direct proxy evidence falsified the simple semantic-density hypothesis: density increased, but held-out LM loss worsened and lexical coverage dropped versus random.

## Recommended next action

Stop the naive central-density selector; if continuing, test a diversity-constrained semantic selector against random on a small transformer before any scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Diversity-constrained semantic clustering for tiny pretraining data
- Success threshold: Diversity-constrained semantic selection beats the random mean held-out loss by at least 0.05 nats and beats every random seed or has non-overlapping confidence intervals, without reducing validation token coverage.
- Stop condition: Stop if diversity-constrained selection still underperforms the random mean or improves loss only by trading away lexical/topic coverage.

## Evidence references

- Artifact root: `<local-path>/projects/semantic-density-clustering-for-tiny-local-pretraining-data-b131c4ac26cb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
