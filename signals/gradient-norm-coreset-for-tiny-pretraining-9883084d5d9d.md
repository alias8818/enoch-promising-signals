# Gradient-Norm Coreset for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `gradient-norm-coreset-for-tiny-pretraining-9883084d5d9d`
Run ID: `gradient-norm-coreset-for-tiny-pretraining-9883084d5d9d-20260525T210420972178+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c88017cb2969

## What looked useful

Raw high-gradient-norm selection had mean validation loss 6.9435 versus 3.3771 for random across 5 seeds, losing on every seed. It also caused large target-label distribution shift (KL 1.029 vs 0.028 for random). Label-stratified high-gradient selection controlled that obvious skew (KL 0.003) but still lost to random by +0.1515 validation loss on average, while label-stratified random slightly beat random.

## Boundaries and scale limits

Proxy-only tiny character LM, 3,000 candidate windows, 1,200 validation windows, 500 training updates per arm, no transformer/BPE/full-corpus or large-scale pretraining validation.

## Claim scope

On a 5-seed Tiny Shakespeare NumPy character-LM proxy with 25% subsets, fixed 500-step training budget, and held-out next-character loss, selecting examples by high probe gradient norm is worse than random; next-character-label stratification reduces distribution skew but still fails to beat random.

## Why it stopped

Early proxy falsification: the directly tested tiny LM objective showed high-gradient coreset selection is consistently worse than random, and the distribution-controlled high-gradient variant also fails; this is not a full transformer-scale validation.

## Recommended next action

Stop this project as a no-paper useful negative signal; only revisit if a direct small-transformer/BPE replication with the same distribution controls is explicitly budgeted.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/gradient-norm-coreset-for-tiny-pretraining-9883084d5d9d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
