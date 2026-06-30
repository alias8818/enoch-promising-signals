# 4-Bit Quantized Adam for 355M Training on 10GB

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `4-bit-quantized-adam-for-355m-training-on-10gb-257292643cec`
Run ID: `4-bit-quantized-adam-for-355m-training-on-10gb-257292643cec-20260528T000400992967+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8e6317e9d84d

## What looked useful

Packed 4-bit Adam moments provide an approximately 8x optimizer-state reduction, but packed state alone is not enough: the naive optimizer diverged or reached NaN at lr 1e-3, 3e-4, and 1e-4 on tiny LM probes, and its synthetic optimizer update peaked at 33.0 CUDA-allocated bytes per parameter due to full fp32 dequantization temporaries. It was stable only at 3e-5 and 1e-5 where learning progress was very small.

## Boundaries and scale limits

No full 355M training run was performed, no 10 GiB hard memory cap was enforced, and the optimizer is a Python prototype that dequantizes full tensors rather than a fused/blockwise production kernel. Results exclude activation memory, allocator fragmentation, dataloader memory, checkpointing policy, and real corpus convergence.

## Claim scope

Local proxy evidence for a naive blockwise packed 4-bit Adam optimizer: persistent m/v state is about 1.0 bytes per parameter and analytically reduces 355M mixed-precision persistent parameter/gradient/master/optimizer memory from 5.68 GB to 3.20 GB, but short toy-LM runs show numerical brittleness at practical AdamW learning rates.

## Why it stopped

Proxy experiments found a clear split: persistent state compression works, but the naive 4-bit moment quantizer is unstable at useful learning rates and has excessive temporary memory, so the evidence does not justify paper writing or a full 355M validation run.

## Recommended next action

Stop this run as a proxy early falsification of the naive 4-bit Adam practical-training claim; the next bounded test should replace full-tensor dequantization with a fused/blockwise update and add stability safeguards before any 355M-scale run.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused blockwise stable 4-bit Adam for toy-LM convergence
- Success threshold: At lr 1e-4 and 3e-4, no NaNs over at least 300 toy-LM steps, final loss delta at least 95% of AdamW's loss delta, persistent state <= 1.5 bytes/parameter, and synthetic optimizer-update peak <= 8 bytes/parameter.
- Stop condition: Stop if the stabilized/blockwise variant still diverges, reaches NaN, or requires learning rates below 3e-5 to remain stable, or if bounded update memory remains above 8 bytes/parameter.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-quantized-adam-for-355m-training-on-10gb-257292643cec`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
