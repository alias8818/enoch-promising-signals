# 2-Bit Residual Optimizer States for Home Fine-Tuning

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-residual-optimizer-states-for-home-fine-tuning-e5f7fd879be4`
Run ID: `2-bit-residual-optimizer-states-for-home-fine-tuning-e5f7fd879be4-20260527T110551668902+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9544abdcc655

## What looked useful

Residual error feedback can make 2-bit moment quantization train in a bounded proxy, but the useful variant is not a pure 2-bit state method because fp16 residual buffers dominate the memory footprint. Pure 2-bit states were unsupported.

## Boundaries and scale limits

Toy MLP task only; no real LLM fine-tuning, no packed production kernels, no large-model memory pressure, short 160-step runs, and tuned learning rates differed by optimizer.

## Claim scope

On a small CUDA MLP teacher-student classification proxy, pure 2-bit Adam moment storage was unstable or low quality, while 2-bit block-quantized moments plus fp16 residual error buffers recovered 94.6% of AdamW validation accuracy with an estimated 56.4% of AdamW optimizer-state memory.

## Why it stopped

Closed as no-paper useful signal: the local proxy supports a mechanism worth direct follow-up, but it is not full validation of home fine-tuning and pure 2-bit optimizer states were not viable here.

## Recommended next action

Run a bounded small-language-model or LoRA fine-tuning follow-up comparing AdamW, a mature 8-bit optimizer, pure 2-bit states, and 2-bit plus residual buffers with actual memory allocation measurements.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-LM Fine-Tuning Test of 2-Bit Residual Adam States
- Success threshold: 2-bit residual reaches at least 95% of AdamW validation quality and beats the 8-bit control on memory without more than 10% throughput loss; pure 2-bit is separately reported even if it fails.
- Stop condition: Stop if 2-bit residual requires fp16/full residual buffers above 60% of AdamW state memory or falls below 90% of AdamW validation quality after bounded LR tuning.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-residual-optimizer-states-for-home-fine-tuning-e5f7fd879be4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
