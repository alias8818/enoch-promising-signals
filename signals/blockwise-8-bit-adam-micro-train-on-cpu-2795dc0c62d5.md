# Blockwise 8-bit Adam micro-train on CPU

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `blockwise-8-bit-adam-micro-train-on-cpu-2795dc0c62d5`
Run ID: `blockwise-8-bit-adam-micro-train-on-cpu-2795dc0c62d5-20260607T011455528595+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/6b86760bd48b

## What looked useful

Blockwise 8-bit Adam state reduced optimizer-state memory to about 25-31% of FP32 AdamW, but the tested recurrent quantized-moment implementation diverged or substantially underperformed FP32 AdamW across three seeds. Best 8-bit setting reached 0.8146 mean validation accuracy versus 0.9995 for FP32 at lr=0.003 and 0.9984 for FP32 at lr=0.0003.

## Boundaries and scale limits

Toy CPU MLP only; not a fused production optimizer, not language-model training, and not tested with stabilization mechanisms such as stochastic rounding, clipping, delayed quantization, FP32 small-tensor fallback, or error feedback.

## Claim scope

A self-contained NumPy CPU MLP micro-train using naive blockwise 8-bit Adam moment storage on a deterministic two-class spiral task.

## Why it stopped

Early direct CPU micro-train falsification: memory compression worked, but convergence did not remain close to FP32 AdamW and larger-block variants produced non-finite losses.

## Recommended next action

Stop this naive implementation as a no-paper negative; only revisit with a bounded stabilized-optimizer follow-up that must first match FP32 AdamW within 1 percentage point on the same CPU micro-train.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stabilized blockwise 8-bit Adam CPU micro-train
- Success threshold: A stabilized 8-bit variant uses no more than 40% of FP32 optimizer-state bytes, has no non-finite losses, and finishes within 1 percentage point validation accuracy and 0.05 validation loss of the best FP32 AdamW control across 3 seeds.
- Stop condition: Stop if the best stabilized variant still loses more than 1 validation-accuracy point to FP32 AdamW or emits any non-finite loss on the 3-seed micro-train.

## Evidence references

- Artifact root: `<local-path>/projects/blockwise-8-bit-adam-micro-train-on-cpu-2795dc0c62d5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
