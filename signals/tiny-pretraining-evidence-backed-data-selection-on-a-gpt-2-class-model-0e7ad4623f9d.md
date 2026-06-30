# Tiny Pretraining: Evidence-Backed Data Selection on a GPT-2-Class Model

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `tiny-pretraining-evidence-backed-data-selection-on-a-gpt-2-class-model-0e7ad4623f9d`
Run ID: `tiny-pretraining-evidence-backed-data-selection-on-a-gpt-2-class-model-0e7ad4623f9d-20260610T181422071289+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/74bbef087b46

## What looked useful

The simple evidence-backed top-score rule failed the predeclared 3% improvement threshold against random selection: mean final validation PPL was 10.5446 for evidence versus 10.5263 for random, a -0.174% improvement. The same score did identify harmful low-evidence data: anti-selection PPL was 10.9624 and was worse than evidence in 5/5 seeds.

## Boundaries and scale limits

This is a small local direct pretraining test, not GPT-2-small-scale or web-corpus-scale validation. It uses byte tokens instead of GPT-2 BPE, one dataset, 800 update steps, and a lexical validation-domain selector rather than a learned data-quality model.

## Claim scope

On WikiText-2 with a byte-level 4-layer GPT-style causal transformer trained for 800 steps under a 900k selected-token budget, the tested TF-IDF validation-similarity plus repetition-quality selector did not improve validation perplexity over random selection across five seeds; anti-selection was consistently worse than evidence selection.

## Why it stopped

Five-seed direct local experiment failed the predeclared success threshold; this is an early bounded falsification of the top-score TF-IDF evidence selector, not a full-scale validation of all data-selection methods.

## Recommended next action

Stop this exact selector as no-paper evidence; a bounded follow-up should test whether a stronger selector that combines lexical evidence with independent quality filters can beat random by at least 3% on the same fixed-budget protocol.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Quality-Gated Evidence Selection for Tiny GPT Pretraining
- Success threshold: Combined selector mean validation perplexity at least 3% lower than random with evidence lower than random in at least 4/5 paired seeds and anti-selection worse than evidence.
- Stop condition: Stop if the combined selector fails to beat random by at least 1% mean validation perplexity after five seeds or if gains disappear on a separate held-out test split.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-pretraining-evidence-backed-data-selection-on-a-gpt-2-class-model-0e7ad4623f9d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
