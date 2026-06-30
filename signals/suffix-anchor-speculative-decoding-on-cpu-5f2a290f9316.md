# Suffix-Anchor Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-anchor-speculative-decoding-on-cpu-5f2a290f9316`
Run ID: `suffix-anchor-speculative-decoding-on-cpu-5f2a290f9316-20260620T072732099266+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/8326b63f3b9a

## What looked useful

Primary run exactly matched serial greedy decoding over 7,680 generated tokens, accepted 98.63% of suffix-anchor draft tokens, and reduced modeled target rounds by 86.76% (7.55x idealized target-call speedup). The unoptimized Python prototype was slower wall-clock than serial n-gram decoding, so this is not evidence of actual CPU speedup.

## Boundaries and scale limits

Not a neural transformer result; no KV-cache, tokenizer, SIMD, batched logits, or real CPU serving path was tested. Corpus is local repeated scaffold/controller text only.

## Claim scope

Local CPU proxy with an exact n-gram target over repeated project/controller text: suffix-anchor drafts can preserve greedy output while reducing modeled target verification rounds.

## Why it stopped

Proxy evidence supports the target-round reduction mechanism but does not validate real CPU transformer speed; measured Python prototype wall-clock was slower than baseline n-gram decoding.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is a direct CPU transformer implementation that reports exactness, tokens/s, acceptance, verifier batches, and memory against serial greedy decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU transformer suffix-anchor speculative decoding check
- Success threshold: At least 1.15x end-to-end tokens/s improvement on repeated-prompt cases with exact greedy output and no more than 5% slowdown on non-repeated controls.
- Stop condition: Stop if exactness fails, if acceptance is below 50% on repeated prompts, or if end-to-end CPU tokens/s is not improved after a simple optimized suffix-index implementation.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-anchor-speculative-decoding-on-cpu-5f2a290f9316`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
