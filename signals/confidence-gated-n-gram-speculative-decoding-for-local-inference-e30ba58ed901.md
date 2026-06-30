# Confidence-Gated N-gram Speculative Decoding for Local Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `confidence-gated-n-gram-speculative-decoding-for-local-inference-e30ba58ed901`
Run ID: `confidence-gated-n-gram-speculative-decoding-for-local-inference-e30ba58ed901-20260601T003222297995+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/3e2a40b3a776

## What looked useful

Confidence is a useful rejection filter for n-gram drafts, but the tested static n-gram source was too weak: ungated speculation accepted 5 of 376 proposed tokens and needed 478 verifier calls for 384 generated tokens; the best high-confidence gate at 0.99 accepted 1 of 20 proposed tokens and still needed 389 verifier calls for 384 generated tokens.

## Boundaries and scale limits

Tested 12 prompts and 384 generated tokens with distilgpt2, not 7B+ models, production KV-cache serving, prompt-lookup repetition, code/chat workloads, batched inference, or wall-clock tokens/sec in llama.cpp/vLLM-style runtimes.

## Claim scope

On a bounded local CUDA trace using distilgpt2, held-out WikiText-2 prompts, and a static WikiText frequency 2-gram drafter with 4-token drafts, target-confidence gating reduced wasted draft attempts but did not beat greedy decoding under a verifier-call cost model.

## Why it stopped

Bounded direct/proxy evidence showed confidence gating improves filtering but does not reach greedy break-even for the tested static WikiText n-gram drafter; this is an early scoped falsification, not a full production validation.

## Recommended next action

Stop this static-corpus n-gram variant as no-paper evidence; if continuing, run a bounded prompt-lookup or domain-specific n-gram follow-up with direct wall-clock local-serving measurements.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Prompt-lookup confidence-gated n-gram speculative decoding on repetitive/code prompts
- Success threshold: At least 5% wall-clock tokens/sec improvement over greedy baseline and positive verifier-call reduction on two held-out prompt families, with no output mismatch for greedy decoding.
- Stop condition: Stop if prompt-lookup/domain-specific drafting still has less than 1.05 generated tokens per verifier call or less than 5% tokens/sec improvement at the best threshold.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-gated-n-gram-speculative-decoding-for-local-inference-e30ba58ed901`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
