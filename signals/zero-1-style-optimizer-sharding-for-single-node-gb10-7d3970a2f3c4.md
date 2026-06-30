# ZeRO-1 Style Optimizer Sharding for Single Node gb10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `zero-1-style-optimizer-sharding-for-single-node-gb10-7d3970a2f3c4`
Run ID: `zero-1-style-optimizer-sharding-for-single-node-gb10-7d3970a2f3c4-20260612T215057380466+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/8016a2027f8b

## What looked useful

Optimizer-state placement outside the CUDA allocator can materially reduce CUDA allocator pressure on GB10 UMA, but it shifts pressure to host RSS/MemAvailable and introduces a clear optimizer-step slowdown. This is useful for deciding whether a direct bounded transformer-training follow-up is worth running.

## Boundaries and scale limits

This was an isolated optimizer-step benchmark, not full model training. It did not include transformer forward/backward compute, activation memory, dataloading, loss convergence, production optimizer kernels, or true multi-rank ZeRO-1 sharding. The host exposes one CUDA GPU and nvidia-smi memory accounting is unsupported on GB10, so CUDA allocator metrics and MemAvailable were used.

## Claim scope

On a single NVIDIA GB10 using synthetic bf16 parameter and gradient tensors from 5M to 500M scalars, moving AdamW first/second moments from CUDA tensors to chunked CPU/UMA tensors reduced PyTorch peak CUDA allocator use by about 77% while slowing isolated optimizer steps by about 1.5x to 3.0x.

## Why it stopped

Bounded synthetic optimizer-state evidence supports allocator relief but not a full ZeRO-1 or model-training claim.

## Recommended next action

Stop this no-paper run; the next bounded action is a direct GPT-2-small-class training comparison with matched tokens/batch, loss parity, step breakdown, CUDA allocator peaks, and MemAvailable telemetry.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Transformer Training Test for GB10 Optimizer-State Offload
- Success threshold: Demonstrate either a strictly larger feasible batch/model at matched loss behavior or at least 40% CUDA allocator peak reduction with less than 3x end-to-end tokens/s slowdown over several hundred transformer training steps.
- Stop condition: Stop if loss parity fails, end-to-end slowdown exceeds 3x without enabling a larger feasible configuration, or memory pressure approaches unsafe GB10 MemAvailable limits.

## Evidence references

- Artifact root: `<local-path>/projects/zero-1-style-optimizer-sharding-for-single-node-gb10-7d3970a2f3c4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
