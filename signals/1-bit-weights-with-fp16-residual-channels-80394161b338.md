# 1-Bit Weights with FP16 Residual Channels

Status: `useful_signal`
Project ID: `1-bit-weights-with-fp16-residual-channels-80394161b338`
Run ID: `1-bit-weights-with-fp16-residual-channels-80394161b338-20260516T151804202570+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3b8b513aeb52

## What looked useful

Rank-8 residual channels improved mean best validation loss from 2.1225 to 2.1078 versus pure binary across three seeds, while dense remained much better at 1.9483. One-seed rank ablation improved monotonically through rank 32 but still trailed dense.

## Boundaries and scale limits

Tested only a 2-layer 128-embedding character model for 2,000 steps, with three seeds for rank 8 and one-seed rank ablation. No GPT-2-small-class tokenized corpus, no packed 1-bit kernels, no large-scale training, and no production inference benchmark were run.

## Claim scope

In a tiny-GPT character language-model benchmark on Tiny Shakespeare, low-rank FP16 residual channels added to straight-through 1-bit linear weights modestly improve validation loss over pure 1-bit weights, but do not approach dense FP32 quality and incur storage/throughput costs.

## Why it stopped

Medium local proxy evidence supports a small residual-channel mechanism but not a publication-grade architecture claim; the dense quality gap remains large and the current implementation lacks packed 1-bit kernels.

## Recommended next action

Stop this run as a no-paper useful signal; next run should perform a storage-matched GPT-2-small-class or at least larger tokenized-corpus rank/placement ablation with packed-kernel-aware throughput measurement.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Storage-matched residual-channel binary transformer ablation
- Success threshold: Residual-channel binary model beats the best storage-matched non-residual binary control by at least 0.03 validation loss and closes at least 25% of the binary-to-dense loss gap without worse throughput than the storage-matched control.
- Stop condition: Stop if residual channels fail to beat storage-matched binary controls by 0.01 validation loss after the planned seeds, or if packed/residual throughput overhead removes the expected binary efficiency advantage.

## Evidence references

- Artifact root: `<local-path>/projects/1-bit-weights-with-fp16-residual-channels-80394161b338`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
