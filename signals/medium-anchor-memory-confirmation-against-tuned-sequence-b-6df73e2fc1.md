# Medium Anchor-Memory Confirmation Against Tuned Sequence Baselines

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `medium-anchor-memory-confirmation-against-tuned-sequence-b-6df73e2fc1`
Run ID: `medium-anchor-memory-confirmation-against-tuned-sequence-b-6df73e2fc1-20260520T031707746711+0000`

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

- Parent run decision: Differentiable Finite-State Memory for Exact Anchors: enoch://control-plane/projects/differentiable-finite-state-memory-for-exact-anchors-3bccd6b518cb/runs/differentiable-finite-state-memory-for-exact-anchors-3bccd6b518cb-20260519T225409227894+0000
- Parent run decision: Trainable FSM Anchor Memory Versus Parameter-Matched Sequence Models: enoch://control-plane/projects/trainable-fsm-anchor-memory-versus-parameter-matched-seque-828de5c847/runs/trainable-fsm-anchor-memory-versus-parameter-matched-seque-828de5c847-20260520T030706953086+0000

## What looked useful

Main 900-step matrix: FSM mean ID/long accuracy 0.525/0.524; best long sequence baseline was LSTM at 0.451, giving only a 0.072 mean margin versus the required 0.10, with one seed reversal and ID accuracy below the required 0.80. The no-write-gate ablation dropped long accuracy to 0.423, supporting a real memory-mechanism contribution. An FSM-only lr=0.01 check improved mean ID/long to 0.700/0.696 but still missed the 0.80 ID threshold.

## Boundaries and scale limits

Synthetic-only benchmark; no natural language, no GPT-2-small-class decoder integration, no broad hyperparameter sweep, no larger-cardinality full run beyond smoke/calibration, and CPU-only local training. The main evidence uses 900 training steps, with one targeted FSM learning-rate check.

## Claim scope

On a medium synthetic last-value anchor retrieval benchmark with 12 anchors, 8 values, train length 64, eval length 192, and five fixed seeds, the trainable FSM anchor memory showed a bounded long-sequence advantage over tuned GRU/LSTM/Transformer baselines but failed the declared Tier 2 success threshold.

## Why it stopped

The Tier 2 direct threshold was not met: the FSM's default mean long margin was below 0.10, one seed reversed, and both default and targeted learning-rate checks failed the required 0.80 in-distribution accuracy.

## Recommended next action

Stop as no-paper mixed useful signal; if pursued, run a separate vectorized optimization-depth follow-up that tests whether the FSM reaches >=0.80 ID accuracy at 12x8 without losing its long-sequence margin against equally extended baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Optimization-Depth Test for Medium FSM Anchor Memory
- Success threshold: FSM mean in-distribution accuracy >=0.80 and mean long-sequence accuracy at least 0.10 above the best tuned sequence baseline, with no seed reversal and the write-gate ablation at least 0.05 below the full FSM on mean long accuracy.
- Stop condition: Stop if the FSM remains below 0.75 mean in-distribution accuracy after the documented longer budget, if any tuned baseline closes the long-sequence gap below 0.05, or if the ablation performs within 0.02 of the full FSM.

## Evidence references

- Artifact root: `<local-path>/projects/medium-anchor-memory-confirmation-against-tuned-sequence-b-6df73e2fc1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
