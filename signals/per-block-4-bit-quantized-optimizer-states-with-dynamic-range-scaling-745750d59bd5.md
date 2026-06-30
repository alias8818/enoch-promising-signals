# Per-Block 4-bit Quantized Optimizer States with Dynamic Range Scaling

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `per-block-4-bit-quantized-optimizer-states-with-dynamic-range-scaling-745750d59bd5`
Run ID: `per-block-4-bit-quantized-optimizer-states-with-dynamic-range-scaling-745750d59bd5-20260531T164440935365+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f092b61d322c

## What looked useful

Full 4-bit AdamW moment-state quantization diverged to NaN across block sizes 64 and 256 in the 500-step medium run, with accuracy near chance, despite 7.1x-7.8x modeled state compression. First-moment-only 4-bit quantization stayed at 1.0 validation accuracy with about 1.77x modeled state compression but higher final loss than AdamW.

## Boundaries and scale limits

Small synthetic dataset, small MLP, 3 medium-run seeds, no bit-packed production kernel, no language-model or large-benchmark validation; modeled state bytes rather than measured production optimizer memory.

## Claim scope

Bounded GPU PyTorch probe on synthetic MLP classification: linear per-block dynamic 4-bit quantization of both AdamW first and second moments was unstable, while 4-bit first-moment-only quantization with FP32 second moment remained stable and reduced modeled optimizer-state bytes.

## Why it stopped

Early bounded falsification of the full linear per-block 4-bit AdamW moment-state design, not a full-scale validation; the second-moment quantizer caused NaN divergence on the local direct optimizer probe.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded follow-up testing stabilized second-moment quantization such as log-scale or lower-bounded per-block scales against the same AdamW controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stabilized 4-bit second-moment quantization for AdamW
- Success threshold: No NaNs, validation loss within 2x AdamW on the synthetic probe, accuracy matching AdamW, and at least 3x modeled optimizer-state compression versus AdamW.
- Stop condition: Stop if the stabilized second-moment variant still diverges or loses more than 5 percentage points of accuracy versus AdamW on the synthetic probe across 3 seeds.

## Evidence references

- Artifact root: `<local-path>/projects/per-block-4-bit-quantized-optimizer-states-with-dynamic-range-scaling-745750d59bd5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
