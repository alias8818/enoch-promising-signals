# Residual Channel Quantization for GB10 VRAM Reduction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-channel-quantization-for-gb10-vram-reduction-1f7e73299a93`
Run ID: `residual-channel-quantization-for-gb10-vram-reduction-1f7e73299a93-20260605T200919088180+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/0f4cbfc2649e

## What looked useful

Per-channel int8 was nearly lossless at 1.99x compression; per-channel int4 reached 3.97x compression with 98.34% logit top-1 agreement and KL 0.3935; mixed RCQ at 25% int8 and 75% int4 reached 3.17x compression with 98.83% top-1 agreement and KL 0.1879, supporting channel-selective precision as a plausible memory-quality tradeoff.

## Boundaries and scale limits

Single small model, final hidden state only, no packed CUDA runtime, no end-to-end KV-cache or activation replacement, no dataset perplexity evaluation, and PyTorch allocation counters rather than nvidia-smi VRAM reporting on GB10 UMA.

## Claim scope

On a GB10 CUDA host, a bounded distilgpt2 final-hidden-state probe showed that channel-wise mixed int8/int4 residual quantization can estimate more than 3x fp16 tensor storage reduction while preserving next-token logit top-1 agreement above 98% on 8 repeated prompts at sequence length 128.

## Why it stopped

Closed as no-paper useful signal because the current evidence is a bounded final-hidden tensor proxy with estimated packed bytes, not direct end-to-end GB10 VRAM reduction.

## Recommended next action

Implement a packed per-channel int4/int8 activation or KV-cache path in one transformer block and compare end-to-end peak PyTorch CUDA allocation, throughput, and perplexity against per-channel int8 and per-channel int4 baselines on a small text dataset.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Packed RCQ Transformer Block Memory Probe
- Success threshold: At least 25% lower peak CUDA allocation than per-channel int8, at least 10% lower logit/perplexity degradation than per-channel int4 at comparable compression, and no more than 15% throughput loss versus the uncompressed fp16 block.
- Stop condition: Stop if packed RCQ does not reduce peak allocation relative to per-channel int8, if perplexity/logit drift is worse than per-channel int4 at similar compression, or if packing overhead causes more than 15% throughput loss.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-quantization-for-gb10-vram-reduction-1f7e73299a93`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
