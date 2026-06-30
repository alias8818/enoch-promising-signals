# Chunked 8-bit AdamW for GPT-2-Small on GB10

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `chunked-8-bit-adamw-for-gpt-2-small-on-gb10-919e719c68f0`
Run ID: `chunked-8-bit-adamw-for-gpt-2-small-on-gb10-919e719c68f0-20260611T065049906795+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f3e4b47678f8

## What looked useful

The memory mechanism works, but naive per-chunk linear uint8 second-moment quantization is numerically unsafe: relative RMS parameter drift versus torch.optim.AdamW reached about 4.2% after 3 synthetic steps and about 8.7-11.2% after 10 steps across tested chunk sizes and dtypes. At 124M bf16 parameters, optimizer state fell from 496,001,024 bytes to 248,016,384 bytes, while update time increased from 24.33 ms to 312.88 ms.

## Boundaries and scale limits

Evidence covers synthetic AdamW update equivalence up to 1,048,576 parameters for 10 steps, GPT-2-small-sized synthetic optimizer update timing for 124,000,000 parameters over 3 measured steps, and one scratch GPT-2-small-shaped forward/backward/update smoke step at batch 1 sequence 64. It does not cover dataset training, validation perplexity, long-horizon convergence, or fused CUDA/Triton optimizer kernels.

## Claim scope

On GB10 with PyTorch 2.12/CUDA 13, a pure-PyTorch chunked AdamW prototype that stores first moment as per-chunk signed int8 and second moment as per-chunk linear uint8 reduces optimizer-state memory by about 2x for bf16 GPT-2-small-sized parameters, but it does not preserve AdamW update fidelity and is much slower than torch.optim.AdamW in update-only benchmarks.

## Why it stopped

Proxy and target-shape smoke evidence showed unacceptable optimizer drift and large update overhead, so a longer GPT-2-small run would not be a valid use of GB10 time for this exact design.

## Recommended next action

Stop this tested design as an early proxy falsification; the next bounded test should replace the second-moment quantizer before any longer GPT-2 training run.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stable second-moment quantization for chunked 8-bit AdamW
- Success threshold: At least 2x optimizer-state memory reduction versus torch.optim.AdamW for bf16 parameters, less than 1% relative RMS parameter drift after 100 controlled steps, finite GPT-2-small microtraining loss, and no more than 2x optimizer-step time overhead unless a fused-kernel path is explicitly planned.
- Stop condition: Stop if the revised quantizer exceeds 1% relative RMS drift after 100 controlled steps, produces non-finite loss in GPT-2-small microtraining, or remains more than 5x slower than torch.optim.AdamW without a credible kernel-fusion path.

## Evidence references

- Artifact root: `<local-path>/projects/chunked-8-bit-adamw-for-gpt-2-small-on-gb10-919e719c68f0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
