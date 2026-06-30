# 8-bit AdamW with sparse gradient checkpointing on CPU worker

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `8-bit-adamw-with-sparse-gradient-checkpointing-on-cpu-worker-daab3073dc62`
Run ID: `8-bit-adamw-with-sparse-gradient-checkpointing-on-cpu-worker-daab3073dc62-20260605T143558023829+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/33df213a6f69

## What looked useful

Sparse checkpoints gave 0.0202x dense file bytes at 1% density and 0.2002x at 10% density with zero restore error, but writes were 1.89x-3.08x slower than dense at those densities. AdamW8 reduced optimizer-state bytes to 0.2503x of fp32 but diverged to NaN by step 51 while AdamW32 reached holdout proxy MSE 0.00385 after 300 steps.

## Boundaries and scale limits

Synthetic sparse linear regression only; no PyTorch integration, no stabilized production 8-bit AdamW implementation, no GPT-2-small or larger training, no distributed checkpoints, and no optimized direct-IO sparse writer.

## Claim scope

On a NumPy CPU sparse-gradient proxy, int32-index/fp32-value sparse gradient checkpoints are exactly restorable and save file bytes below about 50% gradient density, but a naive blockwise int8 AdamW state diverges where fp32 AdamW converges.

## Why it stopped

Early proxy falsification: the directly tested naive blockwise int8 AdamW state was unstable on sparse gradients, so the combined idea is not viable in this form despite sparse checkpoint storage savings.

## Recommended next action

Stop this run as a no-paper useful signal; only revisit with a stabilized 8-bit AdamW variant that passes the documented 300-step sparse proxy thresholds before scaling.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stabilized 8-bit AdamW for sparse-gradient checkpoints
- Success threshold: All required evidence items pass on the bounded CPU proxy, especially no NaNs and MSE within 1.25x of fp32 AdamW while retaining at least 3x optimizer-state savings.
- Stop condition: Stop if stabilized AdamW8 diverges, exceeds 1.25x fp32 MSE after 300 steps, or cannot retain at least 3x optimizer-state savings.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-adamw-with-sparse-gradient-checkpointing-on-cpu-worker-daab3073dc62`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
