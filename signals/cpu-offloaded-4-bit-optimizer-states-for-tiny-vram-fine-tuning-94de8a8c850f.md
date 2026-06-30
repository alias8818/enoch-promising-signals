# CPU-Offloaded 4-bit Optimizer States for Tiny-VRAM Fine-tuning

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `cpu-offloaded-4-bit-optimizer-states-for-tiny-vram-fine-tuning-94de8a8c850f`
Run ID: `cpu-offloaded-4-bit-optimizer-states-for-tiny-vram-fine-tuning-94de8a8c850f-20260527T135914318825+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/33375f50b68e

## What looked useful

Naive signed-int4 Adam states collapsed on the calibrated proxy despite 7.1x optimizer-state compression. A uint4 second-moment variant with 16-element blocks matched fp32 on 2 of 5 seeds but catastrophically diverged on 3 of 5, giving mean loss delta +14.19 and mean accuracy delta -0.435 versus fp32. The memory mechanism works, but convergence robustness is insufficient.

## Boundaries and scale limits

No CUDA runtime or nvidia-smi was available, so GPU VRAM residency, CPU-GPU transfer cost, UMA behavior, and real language-model fine-tuning were not directly tested. The largest training proxy used 4096 synthetic examples, 240 steps, and 3264 trainable low-rank parameters.

## Claim scope

Bounded CPU-only NumPy proxy: packed blockwise 4-bit AdamW optimizer states on a synthetic LoRA-style fine-tuning task reduce state memory by 5.3x-7.1x but do not robustly preserve convergence across seeds.

## Why it stopped

Proxy early falsification: the directly tested NumPy 4-bit optimizer-state mechanism reduced memory but failed multi-seed convergence robustness, so it should not be scaled or presented as validated tiny-VRAM fine-tuning.

## Recommended next action

Stop this naive implementation as a no-paper useful negative; the only concrete next step is a bounded safeguarded-quantization follow-up with second-moment floors or log-domain uint4 quantization before any GPU scale test.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Safeguarded 4-bit Adam second-moment quantization for stable low-rank fine-tuning
- Success threshold: Across 5 seeds, no catastrophic divergence, mean final-loss delta <= 0.05 versus fp32, mean accuracy delta >= -0.02, optimizer-state storage at least 5x smaller than fp32 Adam states including all scales or residuals, and step throughput at least 40% of fp32 on CPU proxy.
- Stop condition: Stop as negative if any safeguarded 4-bit variant diverges on more than 1 of 5 seeds, loses more than 0.10 mean final loss versus fp32, or needs residual/fallback storage that reduces compression below 4x.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-offloaded-4-bit-optimizer-states-for-tiny-vram-fine-tuning-94de8a8c850f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
