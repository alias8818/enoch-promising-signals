# 4-bit AdamW with error-feedback at 124M GPT-2 on GB10

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `4-bit-adamw-with-error-feedback-at-124m-gpt-2-on-gb10-e0451689ac6f`
Run ID: `4-bit-adamw-with-error-feedback-at-124m-gpt-2-on-gb10-e0451689ac6f-20260610T043935411866+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f223a98363ea

## What looked useful

EF4bit reproduced immediate instability at smoke and GPT-2-small scale: GPT-2-small loss went 203.0 to 58,720,256.0 in two steps versus AdamW 203.0 to 116.5. The EF4bit state was larger than bf16 AdamW in this implementation, 620,503,272 versus 494,856,784 bytes, because fp16 error-feedback residuals outweighed packed 4-bit moment savings. Diagnostics showed 92.3% of GPT-2-small second-moment quantized entries were zero after two steps.

## Boundaries and scale limits

Only two target-scale synthetic steps were run, with random-token data and a Python reference optimizer rather than a fused CUDA implementation. This does not rule out other low-bit Adam designs or longer real-corpus training after mechanism fixes.

## Claim scope

A transparent packed 4-bit AdamW variant with fp16 error-feedback residuals was tested on GB10 using smoke-scale and 123.7M-parameter GPT-2-small-class synthetic causal-LM steps. In this bounded setting it was not a viable drop-in replacement for PyTorch bf16 AdamW.

## Why it stopped

Proxy/early falsification: the bounded smoke and GPT-2-small synthetic tests directly showed immediate instability and unfavorable memory tradeoff, but did not perform full real-data training.

## Recommended next action

Stop this implementation path; only revisit with a redesigned second-moment quantizer/error-feedback scheme that demonstrates low zero-fraction and lower measured state memory before any longer real-corpus run.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Second-moment-safe 4-bit AdamW error-feedback probe
- Success threshold: On GPT-2-small-class GB10 runs, the redesigned optimizer keeps loss finite and within 25% of AdamW after 100 steps while using less measured optimizer-state memory than bf16 AdamW.
- Stop condition: Stop if second-moment zero fraction remains above 10%, optimizer state is not below AdamW, or loss explodes/NaNs in the first 20 target-scale steps.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-adamw-with-error-feedback-at-124m-gpt-2-on-gb10-e0451689ac6f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
