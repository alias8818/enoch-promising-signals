# Rare N-gram Density Selection for Tiny CPU Pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `rare-n-gram-density-selection-for-tiny-cpu-pretraining-16ed849b4e5a`
Run ID: `rare-n-gram-density-selection-for-tiny-cpu-pretraining-16ed849b4e5a-20260607T105539214257+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/051d97438448

## What looked useful

Pure rare-trigram-density top-k selection was consistently worse than random on the intended rare-context slice: rare_top - random rare NLL was +0.0387 at 50k tokens, +0.0234 at 100k, and +0.0121 at 200k, with bootstrap confidence intervals above zero. Overall NLL also worsened by +0.1658, +0.1206, and +0.0764 respectively.

## Boundaries and scale limits

This run did not train a neural LM, did not use BPE/subword tokenization, and did not test larger corpora, downstream tasks, curricula, or rare-density mixtures with random/background text. It is an early proxy falsification of pure top-density selection, not a full neural pretraining validation.

## Claim scope

On a WikiText-2 CPU proxy using an interpolated count n-gram language model, selecting only highest rare-trigram-density 128-token chunks worsened held-out loss versus random selection at 50k, 100k, and 200k token budgets, including on rare-trigram target positions.

## Why it stopped

Early proxy falsification: the directly tested count-LM setup showed rare-density top-k selection worsening both all-token and rare-context held-out loss versus random; direct neural pretraining evidence would be required to overturn the scoped result.

## Recommended next action

Stop this run as a no-paper proxy falsification; the next bounded test should train a small neural LM with matched random, middle-density, pure rare-top, and rare-plus-random mixture samplers before any larger-scale claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny Neural LM Check for Rare-Density and Mixed Sampling
- Success threshold: Rare-plus-random mixture improves rare-context NLL by at least 0.02 over random without increasing all-token NLL by more than 0.01; pure rare-top should be separately reported and not averaged into the mixture claim.
- Stop condition: Stop if pure rare-top and all rare-plus-random mixtures fail to beat random on rare-context NLL, or if any rare-context gain is accompanied by an all-token NLL penalty above 0.01.

## Evidence references

- Artifact root: `<local-path>/projects/rare-n-gram-density-selection-for-tiny-cpu-pretraining-16ed849b4e5a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
