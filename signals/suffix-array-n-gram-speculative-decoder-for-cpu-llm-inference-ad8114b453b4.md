# Suffix-Array N-gram Speculative Decoder for CPU LLM Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-array-n-gram-speculative-decoder-for-cpu-llm-inference-ad8114b453b4`
Run ID: `suffix-array-n-gram-speculative-decoder-for-cpu-llm-inference-ad8114b453b4-20260621T222732264428+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/2852c88656c4

## What looked useful

Suffix-array n-gram drafting accepted substantial tokens on copy-heavy and edit-noisy traces, but gave zero benefit on random/no-copy traces and only a small 4.0% estimated pass reduction on scaffold holdout text.

## Boundaries and scale limits

No real CPU LLM backend, tokenizer integration, KV-cache accounting, batching, or measured wall-clock inference speedup; small traces only, one single-threaded Python process.

## Claim scope

Trace-level evaluation of a suffix-array n-gram prompt lookup drafter on synthetic copy-heavy, edit-noisy, random/no-copy, and scaffold-holdout continuations.

## Why it stopped

Stopped after bounded trace evidence: useful specialized mechanism signal, but proxy-only evidence is not full validation or paper-ready.

## Recommended next action

Run a bounded direct CPU inference follow-up that integrates this drafter with a fixed tokenizer and backend, then require measured tokens/sec gains on prompt-copying workloads with no ordinary-prompt regression.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU LLM benchmark for suffix-array prompt-copy drafting
- Success threshold: At least 15% wall-clock tokens/sec improvement on copy-heavy prompts at equal output quality, with less than 3% slowdown on ordinary prompts.
- Stop condition: Stop if suffix-array lookup overhead or low acceptance yields less than 5% measured speedup on copy-heavy prompts, or more than 3% slowdown on ordinary prompts.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-n-gram-speculative-decoder-for-cpu-llm-inference-ad8114b453b4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
