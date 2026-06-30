# Tiny neural LM validation of perplexity-ranked CPU data selection

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `tiny-neural-lm-validation-of-perplexity-ranked-cpu-data-se-a95c4cdaa9`
Run ID: `tiny-neural-lm-validation-of-perplexity-ranked-cpu-data-se-a95c4cdaa9-20260531T120830926148+0000`

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

- Parent run decision: Perplexity-based Data Selection for CPU Tiny Pretraining: enoch://control-plane/projects/perplexity-based-data-selection-for-cpu-tiny-pretraining-c039d264832a/runs/perplexity-based-data-selection-for-cpu-tiny-pretraining-c039d264832a-20260530T070431078286+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/07d3425a146e

## What looked useful

The selector separated target-domain from out-of-domain text and high-perplexity selection was consistently harmful, but random selection beat both low_ppl and mid_ppl in all three neural seeds. Mean validation bpc was random 3.3145, mid_ppl 3.3411, low_ppl 3.4605, and high_ppl 3.7520, directly missing the prior follow-up success threshold of at least 3% improvement over random.

## Boundaries and scale limits

Tiny character RNN only; 3 seeds; 500 steps per arm; Tiny Shakespeare target domain; Alice as the only real out-of-domain source; character-level modeling only; no transformer, tokenizer, web corpus, downstream task, clean-only neural control, or long training schedule.

## Claim scope

In a controlled Tier 1 CPU experiment with a NumPy 64-hidden-unit character RNN trained for matched 500-step runs on 32,768 selected characters, proxy perplexity ranking over Tiny Shakespeare plus Alice candidates did not improve held-out Tiny Shakespeare validation perplexity versus random selection.

## Why it stopped

The required Tier 1 direct tiny-neural validation falsified the stated success threshold: low_ppl and mid_ppl did not beat random, and random was best in every seed.

## Recommended next action

Stop this follow-up as a no-paper direct negative/useful-signal result; do not escalate the perplexity-ranked data-selection claim without a separate larger transformer-style robustness study that first explains why the tiny neural result reverses the n-gram proxy signal.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/tiny-neural-lm-validation-of-perplexity-ranked-cpu-data-se-a95c4cdaa9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
