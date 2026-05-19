# Coverage-Constrained Variance Selection on Real Tiny-LM Text

Status: `useful_signal`
Project ID: `coverage-constrained-variance-selection-on-real-tiny-lm-te-e88a0676c3`
Run ID: `coverage-constrained-variance-selection-on-real-tiny-lm-te-e88a0676c3-20260517T203728808829+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/277817e856cd

## What looked useful

The coverage constraint worked as intended on the selected data distribution (cluster KL to pool 0.00018 versus 0.47324 for unconstrained top-variance), but validation NLL worsened: coverage_variance mean 2.3643, top_variance 2.3542, random 2.2287. The mechanism appears to select high-variance examples that fit training better but generalize worse in this setup.

## Boundaries and scale limits

Small direct test only: 1200 train blocks, 320 validation blocks, 128-character sequences, character-level GRU, simple content-feature clusters, one probe trajectory, three final-training seeds. Not evidence about GPT-2-small-class subword Transformers, semantic coverage labels, larger corpora, or long training runs.

## Claim scope

In a Tier 1 direct test on WikiText-2 raw text with a tiny character-level GRU LM, selecting 240 of 1200 training blocks by probe-loss variance with proportional content-cluster coverage did not improve held-out next-character validation NLL versus random or unconstrained top-variance selection.

## Why it stopped

Direct Tier 1 falsification of the operational success threshold: coverage_variance was +0.13565 NLL worse than random and +0.01015 NLL worse than top_variance, despite successful coverage enforcement.

## Recommended next action

Stop this run as a controlled small direct negative; any overturning evidence should test the same selector on a subword Transformer with at least 3 seeds and require coverage_variance to beat both random and top_variance on held-out NLL.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/coverage-constrained-variance-selection-on-real-tiny-lm-te-e88a0676c3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
