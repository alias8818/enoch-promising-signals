# Activation-Sparsity Data Pruning

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `activation-sparsity-data-pruning-c53a20966b9d`
Run ID: `activation-sparsity-data-pruning-c53a20966b9d-20260529T104920394617+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9c7d9b00b62d

## What looked useful

Activation-sparsity policies successfully selected low/high/mid sparsity subsets but were indistinguishable from random pruning: paired delta accuracy vs random was +0.00015 for low sparsity, -0.00045 for high sparsity, and +0.00025 for mid sparsity, all with 95% CIs crossing zero. High-loss retention was the best non-full policy.

## Boundaries and scale limits

Synthetic data, one-hidden-layer ReLU MLP, no transformer/LLM, no real corpus, no large-scale training, no hardware sparse-execution measurement.

## Claim scope

In a 40-seed controlled NumPy ReLU MLP binary-classification probe, pruning 50% of training examples by warmup activation sparsity did not improve over random 50% retention.

## Why it stopped

Early bounded falsification: in the directly tested small ReLU setting, activation-sparsity-only pruning did not beat random retention; this is not a full transformer-scale validation.

## Recommended next action

Stop this no-paper run; do not pursue activation-sparsity-only pruning without a stronger mechanism or a real-data transformer test that beats random and loss-based controls.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/activation-sparsity-data-pruning-c53a20966b9d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
