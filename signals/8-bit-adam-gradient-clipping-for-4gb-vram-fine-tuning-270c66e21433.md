# 8-bit Adam + gradient clipping for 4GB VRAM fine-tuning

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `8-bit-adam-gradient-clipping-for-4gb-vram-fine-tuning-270c66e21433`
Run ID: `8-bit-adam-gradient-clipping-for-4gb-vram-fine-tuning-270c66e21433-20260610T100131214351+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/c722187ae2f8

## What looked useful

In a 1,000,000-parameter, 3-seed synthetic spike-stress test, clipped fp32 Adam reached final loss 0.0004527 mean with 8,000,000 optimizer-state bytes, while clipped naive 8-bit Adam used 2,001,960 state bytes but ended at final loss 105,403 mean. Global clipping improved the 8-bit failure magnitude relative to no clipping, but did not make the naive blockwise quantized optimizer viable.

## Boundaries and scale limits

No CUDA-visible GPU was available. The run did not fine-tune a transformer, did not test bitsandbytes kernels, did not measure real 4 GiB GPU residency, and excludes activations, frozen weights, allocator fragmentation, dataloading, and model-specific gradients.

## Claim scope

CPU-only synthetic optimizer proxy: blockwise 8-bit Adam moments with block size 4096 reduce optimizer-state memory to about 25% of fp32 Adam, but global norm clipping does not restore convergence under sparse gradient spikes.

## Why it stopped

Proxy early falsification of the simple drop-in claim: the tested naive 8-bit Adam plus global clipping saved memory but failed convergence badly under sparse gradient spikes, so this is not publication-grade positive evidence or a viable standalone recipe.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should replace naive blockwise quantization with an outlier-robust 8-bit moment scheme and require convergence within 2x of clipped fp32 Adam on the same spike stress test before attempting real 4 GiB fine-tuning.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Outlier-robust 8-bit Adam moment quantization under sparse gradient spikes
- Success threshold: At least one outlier-robust 8-bit variant reaches final loss no worse than 2x clipped fp32 Adam mean final loss across 3 seeds while using no more than 35% of fp32 Adam optimizer-state memory.
- Stop condition: Stop if all tested robust quantization variants remain worse than 10x clipped fp32 Adam final loss or require more than 35% of fp32 Adam optimizer-state memory.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-adam-gradient-clipping-for-4gb-vram-fine-tuning-270c66e21433`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
