# Round-Trip Paraphrase Augmentation for Scarce Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `round-trip-paraphrase-augmentation-for-scarce-pretraining-48fe85094864`
Run ID: `round-trip-paraphrase-augmentation-for-scarce-pretraining-48fe85094864-20260530T073203458439+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/38af9342d8d1

## What looked useful

Across train sizes 32, 64, and 128, round-trip-like paraphrase augmentation improved original-test perplexity versus duplicate controls by mean relative reductions of 19.44%, 16.45%, and 12.55%, and improved paraphrased-test perplexity by 31.65%, 31.24%, and 28.81%.

## Boundaries and scale limits

This is not neural pretraining and not a real machine-translation round-trip paraphraser. It uses one public-domain English book, 32-128 training paragraphs, five seeds, and a small n-gram model, so it supports only a local mechanism signal.

## Claim scope

In a bounded word-trigram language-model proxy on scarce Alice in Wonderland paragraphs, deterministic round-trip-like paraphrase augmentation reduced held-out original and paraphrased perplexity relative to no augmentation, exact duplication, and noisy augmentation controls.

## Why it stopped

Closed as no-paper useful signal: the local proxy supports the augmentation mechanism but is not direct publication-grade evidence for scarce neural pretraining.

## Recommended next action

Run a bounded neural follow-up using a small transformer or GPT-2-small-class model with an actual neural paraphrase/backtranslation pipeline on a small real corpus before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural Scarce-Pretraining Test of Round-Trip Paraphrase Augmentation
- Success threshold: At least 5% mean held-out perplexity reduction versus the strongest equal-token control, with no degradation on original held-out perplexity, across at least three seeds.
- Stop condition: Stop if round-trip paraphrase augmentation fails to beat exact duplication/noise controls by 5% or if gains appear only on paraphrased evaluation while original held-out perplexity worsens.

## Evidence references

- Artifact root: `<local-path>/projects/round-trip-paraphrase-augmentation-for-scarce-pretraining-48fe85094864`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
