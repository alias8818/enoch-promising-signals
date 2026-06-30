# 1-Bit Draft with FP16 Residual Channel for Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `1-bit-draft-with-fp16-residual-channel-for-speculative-decoding-75b92c6c3c19`
Run ID: `1-bit-draft-with-fp16-residual-channel-for-speculative-decoding-75b92c6c3c19-20260523T031254466886+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8780efafda6d

## What looked useful

A channel-style FP16 residual is worth a bounded follow-up: 5% residual channels improved mean acceptance overlap from 0.2148 to 0.6719 at an estimated 8.83x LM-head compression, and 10% channels reached 0.7209 at 6.10x. Naive sparse residual entries are a negative path under this proxy.

## Boundaries and scale limits

Only the final LM projection was quantized; no full 1-bit draft transformer was trained, no end-to-end speculative decoding loop or custom kernel was benchmarked, and the evidence is limited to GPT-2-small and WikiText-2 contexts.

## Claim scope

Bounded proxy on GPT-2-small LM-head quantization over 2,048 WikiText-2 target positions: whole-channel FP16 residuals materially improve exact speculative acceptance overlap over a row-scaled 1-bit head, while sparse per-row FP16 residual entries worsen acceptance despite reducing weight error.

## Why it stopped

Stopped after a proxy useful-signal result: the mechanism is promising for channel residuals but not validated as a full draft model, while sparse residual-entry selection is early-falsified by the LM-head acceptance probe.

## Recommended next action

Run a bounded direct follow-up that trains or calibrates a complete GPT-2-small-class 1-bit draft with whole-channel FP16 residuals and measures end-to-end speculative acceptance and throughput against dense and int8 draft controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end GPT-2-small draft with 1-bit weights and FP16 residual channels
- Success threshold: At least 0.60 mean one-step acceptance overlap and a measured end-to-end speculative throughput gain over the best dense or int8 local draft baseline at comparable memory/runtime budget.
- Stop condition: Stop if calibrated full-draft acceptance remains below 0.40 mean overlap or if mixed 1-bit plus FP16-channel execution is slower than an int8 draft at matched acceptance.

## Evidence references

- Artifact root: `<local-path>/projects/1-bit-draft-with-fp16-residual-channel-for-speculative-decoding-75b92c6c3c19`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
