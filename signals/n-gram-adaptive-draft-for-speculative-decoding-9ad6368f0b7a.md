# N-gram Adaptive Draft for Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-adaptive-draft-for-speculative-decoding-9ad6368f0b7a`
Run ID: `n-gram-adaptive-draft-for-speculative-decoding-9ad6368f0b7a-20260523T080938969691+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/e5e61da2f1e4

## What looked useful

Highest-order backoff reduced target verification calls by about 13-14% across prompt lengths when draft tokens were nearly free. Adaptive_stop reduced calls by about 8% but won the cost-adjusted proxy when one draft token cost 0.05 target calls, suggesting adaptivity is mainly useful when draft overhead is material.

## Boundaries and scale limits

Not a real LLM speculative decoding benchmark; no target probability-ratio acceptance, tokenizer/runtime effects, GPU/KV-cache latency, or production serving measurements. Corpus is public-domain prose with 24 random segments per prompt length.

## Claim scope

On a CPU-only corpus-continuation exact-match proxy over 120k Gutenberg-derived tokens, adaptive confidence-gated n-gram drafting did not beat simple highest-order backoff on target-call reduction, but did outperform aggressive drafting under nontrivial draft-token cost sensitivity.

## Why it stopped

Proxy evidence is useful but not paper-ready: it is an early mixed result, not a full validation of LLM speculative decoding performance.

## Recommended next action

Run a bounded real-model speculative decoding follow-up comparing highest_order, adaptive_stop, and fixed n-gram policies on GPT-2-small-class or larger targets with accepted-token, target-forward, draft-overhead, and wall-clock latency metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model latency test for adaptive n-gram speculative drafts
- Success threshold: Adaptive_stop achieves at least 5% lower median end-to-end latency than highest_order at equal output quality on two or more workloads, with no increase in target forward calls large enough to erase the latency gain.
- Stop condition: Stop if adaptive_stop fails to beat highest_order on median latency or if draft overhead is below 1% of target verification cost, making adaptivity irrelevant.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-adaptive-draft-for-speculative-decoding-9ad6368f0b7a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
