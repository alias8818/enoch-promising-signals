# Prompt-Ngram Speculative Decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `prompt-ngram-speculative-decoding-4051ffe75d71`
Run ID: `prompt-ngram-speculative-decoding-4051ffe75d71-20260522T172405403764+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/79d3f7dbc52f

## What looked useful

Prompt n-gram speculative drafts are mechanically viable for copy-like generations: draft_len=8 gave 0.932 proposal acceptance, 0.958 accepted/generated tokens, and 5.818x estimated verifier-forward reduction on copy-continuation cases. Controls showed accepted drafts can also arise from prompt boilerplate without intended source-copy success, so acceptance must be paired with task-quality checks.

## Boundaries and scale limits

The run used short hand-authored prompts, one small base LM, greedy decoding, and an estimated forward-call metric rather than an optimized end-to-end serving latency measurement. It does not validate 7B+ models, batching, real RAG/summarization/code workloads, or production KV-cache implementations.

## Claim scope

On a local synthetic copy-continuation benchmark with distilgpt2 greedy decoding, prompt n-gram lookup produced verifier-accepted draft tokens for 95.8% of generated copy-case tokens and reduced estimated target forward calls by 3.4x to 9.6x across draft lengths 4, 8, and 16.

## Why it stopped

The result supports the mechanism but remains a synthetic small-model proxy rather than publication-grade direct serving evidence.

## Recommended next action

Stop this run as a useful no-paper local signal; next, integrate prompt lookup into an optimized speculative decoding runtime and measure real tokens/sec and quality equivalence on copy-heavy prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end prompt-lookup speculative decoding latency benchmark
- Success threshold: At least 1.3x real tokens/sec improvement on copy-heavy prompts with no quality regression and less than 5% slowdown on non-copy controls.
- Stop condition: Stop if integrated runtime speedup is below 1.1x on copy-heavy prompts or non-copy controls slow down by more than 10%.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-ngram-speculative-decoding-4051ffe75d71`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
