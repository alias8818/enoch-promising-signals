# Gradient-Norm Coresets for Half-Data GPT-2 Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-norm-coresets-for-half-data-gpt-2-pretraining-e670fb19fcc1`
Run ID: `gradient-norm-coresets-for-half-data-gpt-2-pretraining-e670fb19fcc1-20260531T154510250781+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8d9c62e110b1

## What looked useful

Top-gradient half averaged only 0.003 validation-loss points better than random half with paired differences changing sign across seeds; bottom-gradient half was consistently worse than random by 0.046 validation-loss points on average.

## Boundaries and scale limits

3 seeds, 384 training sequences, 256 scored candidates, 96 optimizer steps per variant, 3-layer/96-width GPT-style model, Wikitext-2 only; not GPT-2-small/full-corpus/web-scale evidence.

## Claim scope

Small GPT-2-style causal Transformer pretraining on Wikitext-2 token blocks: initial embedding/LM-head gradient-norm top-half selection was not a reliable improvement over a random half subset under a fixed update budget, while bottom-gradient half selection was consistently worse.

## Why it stopped

Bounded proxy/early falsification: the direct small-scale pretraining test did not support a robust initial top-gradient half-data advantage over random half-data selection.

## Recommended next action

Stop this run as a no-paper useful signal; if continuing locally, test whether warmup-step gradient norms produce a larger and more stable top-half advantage than initialization gradient norms.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Warmup Gradient-Norm Coresets for Small GPT Pretraining
- Success threshold: Warmup top-gradient half beats random half by at least 0.02 validation-loss points on mean paired difference with no more than one losing seed out of five.
- Stop condition: Stop if warmup top-gradient mean paired improvement is <= 0.005 or if paired differences still change sign across more than two of five seeds.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-norm-coresets-for-half-data-gpt-2-pretraining-e670fb19fcc1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
