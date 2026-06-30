# Curriculum Ordering by Readability for Tiny Local Pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `curriculum-ordering-by-readability-for-tiny-local-pretraining-0cae0d192016`
Run ID: `curriculum-ordering-by-readability-for-tiny-local-pretraining-0cae0d192016-20260601T061740805294+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/aa233e0bb664

## What looked useful

Random ordering was best at 3.67216 mean validation BPC. Easy-to-hard was worse by +0.00343 BPC and lost to random in 5/5 paired seeds; hard-to-easy was worse by +0.01899 BPC. Readability ordering can affect optimization, but this probe does not support the proposed easy-to-hard curriculum advantage.

## Boundaries and scale limits

Proxy model only: char bigram, 5 seeds, 2 epochs, public-domain book paragraphs, no transformer/GPT-2-class model and no large-corpus long-run validation.

## Claim scope

In a CPU-local NumPy character-level online softmax bigram LM trained on cached Project Gutenberg paragraphs, readability easy-to-hard ordering did not improve final validation bits per character over random ordering under matched token budgets.

## Why it stopped

Proxy early falsification: the directly tested ordering intervention failed on the local tiny-LM proxy, but full validation would require a neural/transformer LM and larger corpus.

## Recommended next action

Stop this run as a proxy early falsification; a bounded follow-up should test a small neural LM/transformer on the same paragraph-order protocol before any scale-up claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small neural LM readability-curriculum confirmation
- Success threshold: Easy-to-hard must beat random in at least 4/5 paired seeds and improve mean validation loss by at least 0.5% without worse early-token efficiency.
- Stop condition: Stop if easy-to-hard fails to beat random in at least 3/5 seeds or if the gain is below 0.2% mean validation loss after matched token budgets.

## Evidence references

- Artifact root: `<local-path>/projects/curriculum-ordering-by-readability-for-tiny-local-pretraining-0cae0d192016`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
