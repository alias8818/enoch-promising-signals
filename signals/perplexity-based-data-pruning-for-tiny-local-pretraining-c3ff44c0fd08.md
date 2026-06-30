# Perplexity-based data pruning for tiny local pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `perplexity-based-data-pruning-for-tiny-local-pretraining-c3ff44c0fd08`
Run ID: `perplexity-based-data-pruning-for-tiny-local-pretraining-c3ff44c0fd08-20260529T070041715082+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/53c39b28019d

## What looked useful

Naive low/mid/high reference-perplexity document pruning underperformed random selection on mean validation loss across three tiny-pretraining seeds; low_ppl beat random in only 1/3 seeds and was worse on average by +0.0139 validation loss.

## Boundaries and scale limits

Tested 900 candidate training documents, 220 validation documents, three seeds, 90k selected-document token target, 337,920 processed training tokens per arm, and a 3-layer 192-hidden GPT-style model. Did not test larger corpora, GPT-2-small-class or larger targets, downstream transfer, long convergence, or non-perplexity quality filters.

## Claim scope

In a bounded Wikitext-2 tiny local pretraining experiment, document-level perplexity-band pruning with a distilgpt2 scorer did not robustly improve held-out validation loss versus random document selection at the same token/update budget.

## Why it stopped

Bounded direct evidence failed to support the hypothesis; this is not a full-scale validation, but it is enough to reject naive perplexity-band pruning as promising in the tested tiny local setup.

## Recommended next action

Stop this run as a no-paper useful negative; only revisit with a medium direct experiment that compares perplexity pruning against multiple random subsets on a larger corpus and model.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-based-data-pruning-for-tiny-local-pretraining-c3ff44c0fd08`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
