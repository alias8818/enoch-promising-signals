# GPT-2-small-class bounded checkpointing confirmation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gpt-2-small-class-bounded-checkpointing-confirmation-9309963b81`
Run ID: `gpt-2-small-class-bounded-checkpointing-confirmation-9309963b81-20260608T035610698977+0000`

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

- Parent run decision: Bounded Gradient Checkpointing for Home Training: enoch://control-plane/projects/bounded-gradient-checkpointing-for-home-training-d3f169d4fb1a/runs/bounded-gradient-checkpointing-for-home-training-d3f169d4fb1a-20260607T224415227824+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/fec5ab3734c4

## What looked useful

Checkpointing reduced 12-layer GPT-2-small-class peak-over-baseline memory by 48.64% at seq_len 1024 with loss/gradient agreement, and layer scaling at seq_len 1024 was much flatter under checkpointing. At seq_len 512 the reduction was only 4.90%, below the operational 20% material-benefit threshold.

## Boundaries and scale limits

Batch size 1 only; random tokens and random initialization only; no optimizer state, no real-corpus training curve, no repeated timing statistics, no distributed setting, and no publication-grade ablations.

## Claim scope

In a controlled one-step random-initialized GPT-2-small-class causal LM on NVIDIA GB10, activation checkpointing preserves deterministic loss/selected gradient aggregates and materially reduces peak GPU allocation over baseline at sequence length 1024, but not at sequence length 512.

## Why it stopped

Controlled Tier 1 evidence supports the mechanism at longer context but is mixed against the material-reduction threshold and is not full validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded work should add optimizer-inclusive replicated memory attribution across batch sizes and sequence lengths before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Optimizer-inclusive replicated GPT-2-small checkpointing memory attribution
- Success threshold: Checkpointing must reduce optimizer-inclusive peak-over-baseline memory by at least 20% in the largest tested feasible settings, preserve loss within 1e-5 and selected gradient aggregates within 1e-4, and show a lower memory-growth slope with sequence length or layer count than the standard baseline.
- Stop condition: Stop if checkpointing fails to reach 20% memory reduction in all optimizer-inclusive GPT-2-small-class settings up to seq_len 1024, or if memory attribution shows fixed non-activation costs dominate the claimed envelope.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-class-bounded-checkpointing-confirmation-9309963b81`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
