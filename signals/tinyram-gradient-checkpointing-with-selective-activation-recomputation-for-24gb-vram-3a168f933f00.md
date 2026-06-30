# TinyRAM gradient checkpointing with selective activation recomputation for 24GB VRAM

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tinyram-gradient-checkpointing-with-selective-activation-recomputation-for-24gb-vram-3a168f933f00`
Run ID: `tinyram-gradient-checkpointing-with-selective-activation-recomputation-for-24gb-vram-3a168f933f00-20260611T140907258967+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/329924fa12c8

## What looked useful

Selective recomputation reduced a 4 GiB proxy peak from 9.2815 GiB to 4.2815 GiB, and with a 3 GiB reserve reduced the 24 GiB target proxy from 30.9379 GiB to 23.9379 GiB while checkpointing 7/28 layers. A naive 1 GiB reserve missed the 24 GiB target at 25.9379 GiB, showing that overhead calibration is required. Full checkpointing reached 3.9379 GiB and was slightly faster in the synthetic 24 GiB proxy, so the speed-memory tradeoff is not paper-ready.

## Boundaries and scale limits

This was not a real Transformer/GPT-2 training run and not a discrete 24GB VRAM GPU measurement. The workload excludes attention, optimizer state, datasets, convergence, and full training throughput. Full checkpointing was not slower than selective in this proxy.

## Claim scope

On a GB10 PyTorch CUDA proxy with activation-heavy residual blocks, calibrated selective activation recomputation can reduce peak CUDA allocation and fit a 24 GiB peak-allocation target while preserving the computed loss.

## Why it stopped

Proxy evidence supports calibrated memory control but does not support a paper-ready advantage over full checkpointing or real 24GB model-training behavior.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should use a real Transformer or GPT-2-small-class training benchmark with a calibrated 24 GiB memory target.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated selective recomputation on a real Transformer under a 24 GiB target
- Success threshold: Selective recomputation must fit within 24 GiB peak allocation, match loss/gradient checks within tolerance, and improve median measured step time by at least 10% versus full checkpointing on the same real Transformer workload.
- Stop condition: Stop as negative if selective misses the 24 GiB target after reserve calibration, fails loss/gradient checks, or is less than 10% faster than full checkpointing.

## Evidence references

- Artifact root: `<local-path>/projects/tinyram-gradient-checkpointing-with-selective-activation-recomputation-for-24gb-vram-3a168f933f0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
