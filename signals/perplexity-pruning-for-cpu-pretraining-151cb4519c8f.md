# Perplexity Pruning for CPU Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `perplexity-pruning-for-cpu-pretraining-151cb4519c8f`
Run ID: `perplexity-pruning-for-cpu-pretraining-151cb4519c8f-20260525T035830960543+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/6fb2eb850244

## What looked useful

Default condition: pruning was worse than full mixed by +0.0734 bpc but better than random-drop (+0.0944 bpc). High-noise condition: pruning was only +0.0144 bpc worse than full mixed while random-drop was +0.1310 bpc worse, and pruning reduced measured n-gram training time by about 74% versus full mixed.

## Boundaries and scale limits

Small corpus, character n-gram model, synthetic noise included, no neural transformer optimization, no tokenizer effects, no web-scale corpus, no downstream task evaluation, and no datacenter-scale training.

## Claim scope

In a standard-library CPU character n-gram LM probe on small literary/code/noise mixtures, high proxy-perplexity pruning enriched target-like chunks and beat random dropping under the same retained-character budget, especially in a high-contamination condition, but did not beat training on the full mixed corpus for held-out validation perplexity.

## Why it stopped

Early proxy falsification of the strong claim: high-perplexity pruning did not improve validation perplexity over full mixed CPU pretraining in the tested n-gram setting, although it did beat random dropping as a compute-saving filter.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should be a neural tiny-LM equal-wall-clock experiment on a real mixed-quality corpus to check whether the pruning efficiency tradeoff survives learned optimization.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural Equal-Wall-Clock Test of Perplexity-Tail Pruning
- Success threshold: ppl_prune_high_tail has validation bpc no worse than full_mixed by 0.01 bpc under equal wall-clock, and at least 0.05 bpc better than random_drop under equal retained-token budget across at least 3 seeds.
- Stop condition: Stop if pruning is worse than full_mixed by more than 0.05 bpc and not at least 0.03 bpc better than random_drop after the planned seeds.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-pruning-for-cpu-pretraining-151cb4519c8f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
