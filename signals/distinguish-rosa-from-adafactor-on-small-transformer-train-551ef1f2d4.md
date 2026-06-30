# Distinguish ROSA from Adafactor on Small Transformer Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `distinguish-rosa-from-adafactor-on-small-transformer-train-551ef1f2d4`
Run ID: `distinguish-rosa-from-adafactor-on-small-transformer-train-551ef1f2d4-20260520T112444195076+0000`

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

- Parent run decision: Rank-1 Optimizer State Accumulators (ROSA) for Sub-Quadratic Optimizer Memory: enoch://control-plane/projects/rank-1-optimizer-state-accumulators-rosa-for-sub-quadratic-optimizer-memory-0ca15ae1f2ac/runs/rank-1-optimizer-state-accumulators-rosa-for-sub-quadratic-optimizer-memory-0ca15ae1f2ac-20260520T111109951590+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/4bf726152d4b

## What looked useful

Adafactor reached mean final validation loss 2.4305, while tuned ROSA rank 16 and rank 4 remained at 3.4501 and 3.4500. ROSA rank 16 exceeded the predeclared thresholds with 41.95% higher validation loss and +0.2796 median update-cosine gap versus Adafactor.

## Boundaries and scale limits

Synthetic token stream, tiny model, CPU run, 3 seeds, fixed random subspace ROSA only; does not establish behavior on natural language, GPT-2-small-class models, larger training budgets, adaptive/refreshed ROSA variants, or publication-grade robustness.

## Claim scope

Tier 1 controlled small direct test: on a 2-layer tiny causal Transformer trained for 1000 steps on a deterministic learnable synthetic token stream across 3 seeds, fixed random-subspace ROSA rank 4 and rank 16 are empirically distinguishable from PyTorch Adafactor by validation loss, and rank 16 is also distinguishable by median update-gradient cosine.

## Why it stopped

Tier 1 direct evidence met the distinguishability threshold, but the evidence is toy-scale and variant-limited, so it is useful no-paper evidence rather than publication readiness.

## Recommended next action

Run a bounded deepen follow-up testing refreshed ROSA subspaces plus an LR/rank grid on the same learnable stream and one small real character corpus; do not write a paper from this toy-only result.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Test whether refreshed ROSA subspaces close the small-Transformer gap to Adafactor
- Success threshold: Refreshed ROSA reaches within 5% relative final validation loss of Adafactor on both tasks while maintaining a median update-cosine gap of at least 0.10 from Adafactor.
- Stop condition: Stop if refreshed ROSA remains more than 15% worse than Adafactor on validation loss across both tasks after the LR/rank grid, or if it requires unstable learning rates to improve.

## Evidence references

- Artifact root: `<local-path>/projects/distinguish-rosa-from-adafactor-on-small-transformer-train-551ef1f2d4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
