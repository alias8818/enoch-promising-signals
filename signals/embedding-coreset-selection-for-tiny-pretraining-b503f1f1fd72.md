# Embedding Coreset Selection for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `embedding-coreset-selection-for-tiny-pretraining-b503f1f1fd72`
Run ID: `embedding-coreset-selection-for-tiny-pretraining-b503f1f1fd72-20260526T012813323279+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/6fe9efb9df68

## What looked useful

K-means over hashed document embeddings improved an embedding coverage diagnostic but produced mixed validation-loss results: worse than all random controls in seed 1 and only modestly better than the random mean in seed 2. Farthest-point embedding selection biased toward shorter/outlier documents and failed to beat random in both seeds.

## Boundaries and scale limits

This was a small local proxy using hashed lexical embeddings, WikiText-2, two seeds, and a tiny byte-level Transformer; it does not test neural sentence embeddings, GPT-2-small-class tokenized pretraining, downstream tasks, or large web-corpus scaling.

## Claim scope

On WikiText-2 with 240-document, 87065-byte selected subsets and a tiny byte-level Transformer trained for 1500 steps, hashed-TFIDF embedding coreset selection did not consistently improve validation loss over same-byte random subset controls.

## Why it stopped

Early proxy/midpoint falsification: embedding coverage improved in the k-means diagnostic, but the direct tiny-pretraining validation-loss metric did not consistently beat random same-byte controls.

## Recommended next action

Stop this run as no-paper useful evidence; a bounded follow-up should test neural document embeddings with the same random and length controls before any larger-scale claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural embedding coreset selection for tiny GPT-style pretraining
- Success threshold: Neural embedding coreset selection must reduce validation loss by at least 1 percent versus the random mean and beat the best non-neural control in at least 3 of 4 seeds at the same token budget.
- Stop condition: Stop if neural embedding selection does not beat the random mean by at least 0.5 percent after two seeds, or if selected length/topic artifacts explain the gain without an embedding-specific effect.

## Evidence references

- Artifact root: `<local-path>/projects/embedding-coreset-selection-for-tiny-pretraining-b503f1f1fd72`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
