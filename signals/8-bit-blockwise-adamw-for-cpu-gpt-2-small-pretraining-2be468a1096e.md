# 8-bit Blockwise AdamW for CPU GPT-2 Small Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `8-bit-blockwise-adamw-for-cpu-gpt-2-small-pretraining-2be468a1096e`
Run ID: `8-bit-blockwise-adamw-for-cpu-gpt-2-small-pretraining-2be468a1096e-20260604T081405663696+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/0efddd0f401e

## What looked useful

8-bit blockwise AdamW moment storage on GPT-2-small-shaped tensors reduced optimizer state from 995.81 MB to 249.44 MB with 2048-element blocks and 252.84 MB with 256-element blocks. However, the 2048-block tiny-GPT run diverged by step 30, while a 256-block run avoided catastrophic divergence over 30 steps but remained only a short proxy. Quantization diagnostics showed high second-moment zero fractions with large blocks, supporting a concrete stability failure mechanism.

## Boundaries and scale limits

No full GPT-2-small forward/backward pretraining or validation-set convergence was run. Training quality evidence is limited to 30 steps on synthetic-token tiny GPT. GPT-2-small evidence covers optimizer-state memory and synthetic-gradient optimizer-step time only.

## Claim scope

Bounded CPU evidence from a tiny GPT training loop plus GPT-2-small-shaped optimizer-state and synthetic-gradient update benchmarks. The tested naive blockwise 8-bit AdamW implementation reduces optimizer-state memory by about 4x, but 2048-element absmax blocks are unstable in short-run tiny-GPT training and the PyTorch CPU implementation is slower than FP32 AdamW on GPT-2-small-shaped optimizer updates.

## Why it stopped

Proxy and direct optimizer evidence show useful memory compression but do not validate CPU GPT-2-small pretraining; the naive large-block implementation is an early falsification for stability, not a full-scale validation.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should replace absmax int8 second-moment quantization with a stable unsigned/log/nonlinear or error-feedback scheme and rerun the same tiny-GPT plus GPT-2-small-shaped benchmarks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stable second-moment quantization for CPU 8-bit AdamW
- Success threshold: No catastrophic loss divergence and final tiny-GPT loss within 2% of FP32 AdamW after 200 matched steps, with optimizer-state memory at least 3.5x smaller than FP32 AdamW and GPT-2-small-shaped optimizer-step mean time no more than 2x FP32 AdamW.
- Stop condition: Stop if the improved quantizer still diverges, exceeds 2x FP32 AdamW optimizer-step time on GPT-2-small-shaped tensors, or requires more than 30 minutes of CPU-only runtime for the bounded test.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-blockwise-adamw-for-cpu-gpt-2-small-pretraining-2be468a1096e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
