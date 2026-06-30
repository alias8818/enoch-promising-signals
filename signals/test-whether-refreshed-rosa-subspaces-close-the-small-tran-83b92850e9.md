# Test whether refreshed ROSA subspaces close the small-Transformer gap to Adafactor

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `68`
Project ID: `test-whether-refreshed-rosa-subspaces-close-the-small-tran-83b92850e9`
Run ID: `test-whether-refreshed-rosa-subspaces-close-the-small-tran-83b92850e9-20260520T113505189766+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `68`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Distinguish ROSA from Adafactor on Small Transformer Training: enoch://control-plane/projects/distinguish-rosa-from-adafactor-on-small-transformer-train-551ef1f2d4/runs/distinguish-rosa-from-adafactor-on-small-transformer-train-551ef1f2d4-20260520T112444195076+0000
- Parent run decision: Rank-1 Optimizer State Accumulators (ROSA) for Sub-Quadratic Optimizer Memory: enoch://control-plane/projects/rank-1-optimizer-state-accumulators-rosa-for-sub-quadratic-optimizer-memory-0ca15ae1f2ac/runs/rank-1-optimizer-state-accumulators-rosa-for-sub-quadratic-optimizer-memory-0ca15ae1f2ac-20260520T111109951590+0000

## What looked useful

Refresh frequency matters: ROSA refresh-10 reduced 220-step mean validation loss from 1.5789 for static ROSA to 0.9916, but Adafactor reached 0.3078. In a 1000-step persistence check, refresh-10 remained 0.2474 nats/token behind Adafactor despite using more optimizer state in this implementation.

## Boundaries and scale limits

No natural-language corpus, GPT-2-small-class model, GPU kernel study, rank schedule, or structured subspace variant was tested. The conclusion is bounded to small CPU Transformer training with synthetic data.

## Claim scope

In a 65k-parameter, 2-layer causal Transformer trained on a deterministic synthetic autoregressive LM task with fixed seeds 11/22/33, rank-8 refreshed ROSA improves substantially over static ROSA but remains well behind a real Adafactor baseline.

## Why it stopped

Tier-2 direct small-Transformer evidence falsified the close-gap threshold: best refreshed ROSA was not within 0.03 nats/token of Adafactor at 220 steps or 1000 steps.

## Recommended next action

Stop this branch as no-paper evidence; only revisit if testing a materially different ROSA design such as structured/high-rank refreshed subspaces with an explicit memory-matched threshold.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/test-whether-refreshed-rosa-subspaces-close-the-small-tran-83b92850e9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
