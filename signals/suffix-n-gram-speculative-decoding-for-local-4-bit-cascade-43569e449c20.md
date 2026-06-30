# Suffix-n-gram speculative decoding for local 4-bit cascade

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-n-gram-speculative-decoding-for-local-4-bit-cascade-43569e449c20`
Run ID: `suffix-n-gram-speculative-decoding-for-local-4-bit-cascade-43569e449c20-20260604T163303122789+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/787b7ccf8e16

## What looked useful

Suffix n-gram drafting exactly matched greedy baseline output. With max_draft=8 it reduced target forwards by 33.2% on natural prompts and 74.2% on repetition-rich prompts; accepted/proposed draft-token ratios were 42.7% and 69.0% respectively. Draft-length ablation showed stronger forward reduction at longer drafts but lower acceptance ratio.

## Boundaries and scale limits

Small prompt sets only: 12 natural and 12 repetition-rich prompts, 64 generated tokens each, one 135M fp16 model, no real 4-bit quantized cascade, no KV-cache-optimized serving kernel, no broad corpus or multi-model robustness validation.

## Claim scope

On SmolLM2-135M fp16 exact greedy decoding with a full-context verifier, suffix n-gram drafting preserves target output and reduces target forward calls substantially on repetition-rich contexts and modestly on short natural prompts.

## Why it stopped

The mechanism is supported in favorable repeated-context probes, but the original 4-bit cascade serving claim was only proxied, not directly validated.

## Recommended next action

Stop this run as no-paper useful signal; next implement a true 4-bit/KV-cache local serving benchmark and require end-to-end latency gains on real chat/code/log corpora before reconsidering paper readiness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache 4-bit suffix n-gram speculative decoding benchmark
- Success threshold: At least 1.25x median end-to-end tokens/sec speedup on repetition-heavy real workloads, exact greedy equality, and no more than 5% slowdown on natural prompts.
- Stop condition: Stop if a working 4-bit/KV-cache backend cannot be made reproducible locally, if exact equality fails, or if median speedup is below 1.10x on repetition-heavy workloads.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-n-gram-speculative-decoding-for-local-4-bit-cascade-43569e449c20`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
