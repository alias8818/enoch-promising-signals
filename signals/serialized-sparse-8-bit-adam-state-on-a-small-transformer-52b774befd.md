# Serialized sparse 8-bit Adam state on a small transformer or CNN convergence task

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `serialized-sparse-8-bit-adam-state-on-a-small-transformer-52b774befd`
Run ID: `serialized-sparse-8-bit-adam-state-on-a-small-transformer-52b774befd-20260522T104934530037+0000`

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

- Parent run decision: Stabilized sparse 8-bit Adam state with real small-model convergence check: enoch://control-plane/projects/stabilized-sparse-8-bit-adam-state-with-real-small-model-c-410cdc6d22/runs/stabilized-sparse-8-bit-adam-state-with-real-small-model-c-410cdc6d22-20260522T102304594496+0000
- Parent run decision: CPU-Offloaded Dynamic Sparse 8-bit Optimizer: enoch://control-plane/projects/cpu-offloaded-dynamic-sparse-8-bit-optimizer-f3035350a459/runs/cpu-offloaded-dynamic-sparse-8-bit-optimizer-f3035350a459-20260522T093044403740+0000

## What looked useful

Dense 8-bit Adam-state converged at 25.0% of fp32 Adam moment bytes. Serialized sparse 8-bit Adam-state at 50% density converged with mean accuracy 0.9733 versus fp32 Adam 0.9724 and mean serialized state 51,494 bytes versus fp32 estimate 306,256 bytes. A 25% density ablation cut state to 30,274 bytes but reduced mean accuracy to 0.9627 with higher variance.

## Boundaries and scale limits

Only a small CPU CNN/digits task was tested. No transformer language model, large image dataset, GPU kernel, optimizer offload bandwidth, distributed restart, or long training run was evaluated. The sparse Python implementation is slower than fp32 Adam.

## Claim scope

On scikit-learn digits with a small 2-conv CNN over five fixed seeds, a 50% density serialized sparse 8-bit Adam-state optimizer matched fp32 Adam mean test accuracy while using 16.8% of estimated fp32 Adam moment-state bytes.

## Why it stopped

Tier 2 small-CNN evidence supports the mechanism but is too narrow and too implementation-specific for publication readiness.

## Recommended next action

Stop this run as no-paper useful evidence; deepen next with a bounded local dataset/model expansion and checkpoint-resume validation before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Serialized sparse 8-bit Adam density sweep with checkpoint-resume on larger local CNN and tiny transformer tasks
- Success threshold: At least one CNN task and one tiny transformer task finish within 0.5 absolute accuracy points or equivalent validation-loss tolerance of fp32 Adam while using less than 25% fp32 Adam optimizer-state bytes, with no checkpoint-resume divergence beyond numerical tolerance.
- Stop condition: Stop if 50% and 75% density both miss the convergence threshold on either task, if checkpoint-resume changes the next-step trajectory materially, or if wall-clock overhead exceeds 5x fp32 Adam without a plausible implementation path.

## Evidence references

- Artifact root: `<local-path>/projects/serialized-sparse-8-bit-adam-state-on-a-small-transformer-52b774befd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
