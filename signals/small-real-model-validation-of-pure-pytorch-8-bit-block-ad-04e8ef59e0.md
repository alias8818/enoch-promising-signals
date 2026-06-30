# Small real-model validation of pure PyTorch 8-bit block AdamW

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `small-real-model-validation-of-pure-pytorch-8-bit-block-ad-04e8ef59e0`
Run ID: `small-real-model-validation-of-pure-pytorch-8-bit-block-ad-04e8ef59e0-20260525T022701023651+0000`

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

- Parent run decision: Pure PyTorch 8-bit Block-wise AdamW for CPU: enoch://control-plane/projects/pure-pytorch-8-bit-block-wise-adamw-for-cpu-250ea26310ba/runs/pure-pytorch-8-bit-block-wise-adamw-for-cpu-250ea26310ba-20260525T015641074514+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/dc70f9f6e915

## What looked useful

Block8 reduced persistent optimizer-state bytes to 861640 vs AdamW 3373696 bytes (25.54% of AdamW) but failed the primary drop-in convergence threshold at lr=3e-4 because 2 of 5 seeds diverged. A lower matched lr=2e-4 check was stable across 5 seeds with Block8 final validation loss 0.9937x AdamW and the same state-byte ratio, suggesting tunability but not paper-ready stability.

## Boundaries and scale limits

Small single-task CPU run only; no GPT-2-scale model, no long training horizon, no GPU/kernel runtime validation, and no robustness across datasets. Primary AdamW-LR run diverged in 2 of 5 Block8 seeds; lower matched LR was stable but slower-converging and remains a bounded check.

## Claim scope

Tier 1 CPU validation of a pure PyTorch blockwise 8-bit AdamW on a 2-layer 128-dim character Transformer trained on Tiny Shakespeare for 120 steps across 5 seeds, compared with torch.optim.AdamW.

## Why it stopped

Primary direct Tier 1 validation produced a mixed/negative result: memory savings met the threshold, but the drop-in stability threshold was falsified by 2 of 5 Block8 seeds diverging while AdamW stayed stable.

## Recommended next action

Stop this run as no-paper useful signal; next bounded deepen test should add stability controls and require 5/5 non-divergent seeds at AdamW-matched or predeclared tuned schedule before considering larger validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stability-controlled pure PyTorch 8-bit block AdamW on small real models
- Success threshold: 5/5 non-divergent Block8 seeds, final validation loss <=1.03x AdamW mean on each tested task, persistent optimizer state <=0.35x AdamW, and CPU throughput no worse than 0.75x AdamW for the pure PyTorch prototype.
- Stop condition: Stop as negative if any tested configuration still diverges in more than 1 of 5 seeds or requires memory above 0.35x AdamW to remain stable.

## Evidence references

- Artifact root: `<local-path>/projects/small-real-model-validation-of-pure-pytorch-8-bit-block-ad-04e8ef59e0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
