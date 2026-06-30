# Sparse top-k Adam optimizer state for tiny-VRAM training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sparse-top-k-adam-optimizer-state-for-tiny-vram-training-31012fe3c029`
Run ID: `sparse-top-k-adam-optimizer-state-for-tiny-vram-training-31012fe3c029-20260609T022512835243+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/846f49dced2e

## What looked useful

Sparse top-k moment storage works mechanically and reduces measured optimizer-state bytes, but aggressive sparsity damages learning and higher density erodes the memory benefit. The result argues against plain top-k Adam state as a practical tiny-VRAM optimizer without additional mechanisms such as residual/error-feedback or a fused GPU implementation.

## Boundaries and scale limits

This run used a synthetic language-model task, 80-step medium runs, one seed, an inspectable Python/CPU-dictionary sparse-state prototype, and no true near-OOM tiny-VRAM boundary test. It does not validate GPT-2-small-class training, real-corpus perplexity, fused CUDA sparse kernels, or long-horizon convergence.

## Claim scope

On a 3.323M-parameter synthetic next-token Transformer benchmark, plain sparse top-k AdamW moment storage reduces optimizer-state bytes but creates an unfavorable tradeoff: 4-8x state reduction causes large short-horizon loss degradation, while 20% top-k narrows the loss gap but leaves only 1.6x state reduction and severe prototype throughput loss.

## Why it stopped

Bounded local evidence is negative for the plain sparse top-k AdamW state design: useful memory savings coincide with unacceptable loss degradation, and the higher-density recovery point gives too little memory reduction with large prototype slowdown.

## Recommended next action

Stop this run as no-paper useful evidence; a bounded adjacent test should evaluate whether error-feedback for non-selected gradients can recover convergence at 4x or better state reduction before any larger-scale validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Error-feedback sparse Adam state on the same tiny Transformer benchmark
- Success threshold: At 80-200 steps, final loss within 10% of AdamW's loss improvement over initialization, at least 4x lower optimizer-state bytes including residual buffers, and no more than 2x throughput slowdown in the prototype.
- Stop condition: Stop if residual/error-feedback still has more than a 0.5 absolute final-loss gap at 4x state reduction or if residual buffers erase the state-memory advantage.

## Evidence references

- Artifact root: `<local-path>/projects/sparse-top-k-adam-optimizer-state-for-tiny-vram-training-31012fe3c029`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
