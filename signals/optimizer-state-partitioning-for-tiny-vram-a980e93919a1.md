# Optimizer State Partitioning for Tiny VRAM

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `optimizer-state-partitioning-for-tiny-vram-a980e93919a1`
Run ID: `optimizer-state-partitioning-for-tiny-vram-a980e93919a1-20260612T215600756260+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/8016a2027f8b

## What looked useful

Optimizer-state partitioning appears mechanically viable as a tiny-VRAM enabler when persistent Adam moments and update temporaries dominate CUDA memory. In the 64M-parameter case, peak CUDA allocation fell from 1.664 GB to 272 MB with 4M chunks and 260 MB with 1M chunks, at 1.71x and 1.27x optimizer-step slowdown respectively.

## Boundaries and scale limits

Synthetic flat-vector optimizer benchmark only; no transformer forward/backward pass, no loss convergence, no dataloader, no checkpointing, no distributed sharding, no explicit tiny CUDA memory cap, and no discrete-VRAM PCIe GPU validation.

## Claim scope

On NVIDIA GB10 with PyTorch 2.12, a synthetic BF16 parameter/gradient optimizer-step benchmark shows that CPU-partitioned FP32 Adam state can reduce peak CUDA allocation by about 69-84% versus GPU-resident FP32 Adam state for 4M-64M parameters, with about 1.27-2.04x optimizer-step slowdown depending on chunk size and problem size.

## Why it stopped

Synthetic optimizer-state proxy supports the mechanism but is not direct publication-grade training evidence.

## Recommended next action

Stop this worker run as a no-paper useful signal; the next bounded test should run a small transformer under an explicit memory cap and compare loss parity plus throughput against GPU Adam.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Memory-capped transformer training with partitioned Adam state
- Success threshold: Partitioned Adam fits and trains under the cap where GPU Adam fails or uses at least 2x more CUDA memory, with loss within 2% of control and throughput at least 40% of the fitting baseline.
- Stop condition: Stop if partitioned Adam cannot maintain loss parity, has less than 25% baseline throughput after basic chunk tuning, or fails to fit under a cap that should admit param+grad+one chunk by accounting.

## Evidence references

- Artifact root: `<local-path>/projects/optimizer-state-partitioning-for-tiny-vram-a980e93919a1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
