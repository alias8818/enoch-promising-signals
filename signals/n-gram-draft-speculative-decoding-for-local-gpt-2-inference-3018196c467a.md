# N-Gram Draft Speculative Decoding for Local GPT-2 Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-draft-speculative-decoding-for-local-gpt-2-inference-3018196c467a`
Run ID: `n-gram-draft-speculative-decoding-for-local-gpt-2-inference-3018196c467a-20260531T144250920510+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4d4231f33a1c

## What looked useful

N-gram drafting is a real mechanism for repeated-prefix workloads, but the simple implementation is not a reliable exact drop-in for common local fp16 GPT-2 inference. Float32 exact runs showed mean 1.18x speedup on natural prompts and 3.45x on repetitive prompts; fp16 diverged on natural prompts.

## Boundaries and scale limits

Small fixed prompt set only; no corpus-scale validation, no sampling validation, no quantized backend validation, and GPU fp16 exactness failed on 2 of 6 natural prompts.

## Claim scope

On local GPT-2 greedy decoding with 12 fixed prompts and 64 generated tokens, n-gram drafting reduced target forwards and sped up exact float32 decoding in repetition-heavy prompts and produced small mixed speedups on natural prompts.

## Why it stopped

Mixed bounded evidence: positive mechanism signal under float32 and repetition-heavy prompts, but natural-prompt gains are variable and the practical GPU fp16 path failed exactness in this proxy benchmark rather than a full validation.

## Recommended next action

Stop this run as no-paper useful signal; a bounded follow-up should test fp16-safe verification and corpus prompts before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: FP16-safe n-gram speculative decoding on corpus GPT-2 prompts
- Success threshold: Zero exactness failures and at least 1.10x median wall-clock speedup versus KV-cache greedy baseline on corpus prompts without more than 5% p10 slowdown.
- Stop condition: Stop if any intended-precision exactness failures remain after one conservative verification design, or if median corpus speedup is below 1.05x.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-draft-speculative-decoding-for-local-gpt-2-inference-3018196c467a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
