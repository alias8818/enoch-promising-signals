# Confidence-gated suffix drafting as an opportunistic hybrid drafter

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `confidence-gated-suffix-drafting-as-an-opportunistic-hybri-2be5f9e711`
Run ID: `confidence-gated-suffix-drafting-as-an-opportunistic-hybri-2be5f9e711-20260524T053343427987+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real-corpus suffix-index drafting with strong retrieval baselines: enoch://control-plane/projects/real-corpus-suffix-index-drafting-with-strong-retrieval-ba-7f40914aa9/runs/real-corpus-suffix-index-drafting-with-strong-retrieval-ba-7f40914aa9-20260524T050803717795+0000
- Parent run decision: LCP-accelerated suffix-index context drafting: enoch://control-plane/projects/lcp-accelerated-suffix-index-context-drafting-99edfb8d11/runs/lcp-accelerated-suffix-index-context-drafting-99edfb8d11-20260524T050011598399+0000

## What looked useful

Target confidence is a real selector for drafter suffix quality: versus matched random gates, accept-rate lift was 0.8-5.3 percentage points on gpt2 and 6.3-12.3 points on gpt2-medium; wall speedup lift was 0.7-4.8 and 7.4-10.3 points respectively. All gated/speculative modes exactly matched target greedy output. Ungated drafting remained fastest on gpt2-medium, so the result supports a conditional mechanism rather than a paper-ready serving win.

## Boundaries and scale limits

Validated on 40 handcrafted prompts with gpt2/distilgpt2 and 20 prompts with gpt2-medium/distilgpt2 on one GB10 GPU using non-KV-cached Hugging Face forward passes and greedy decoding only. No modern 7B+ target, production serving kernel, sampled decoding, batched traffic, or public benchmark prompt corpus was tested.

## Claim scope

In greedy GPT-2-class local inference with exact speculative verification, confidence-gated suffix drafting improves suffix acceptance and wall-clock latency versus matched-rate random opportunistic drafting, while preserving exact target-greedy outputs. It does not universally beat ungated speculative drafting.

## Why it stopped

Bounded direct validation supports the mechanism but not a publication-grade claim; limitations are model scale, prompt source, greedy-only decoding, and non-production inference implementation.

## Recommended next action

Stop this run as no-paper useful signal; deepen once with a KV-cache-aware implementation, a real prompt dataset, sampling-compatible verification, and a larger target/draft pair.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache confidence-gated suffix drafting on larger target models
- Success threshold: Confidence gating must preserve exact speculative correctness and improve end-to-end tokens/s or p95 latency by at least 10% over both ungated drafting and matched-rate random gating on the same prompt set, with no degradation in output distribution tests.
- Stop condition: Stop if confidence gating fails to beat matched random gating on acceptance quality or fails to beat ungated drafting on latency after calibrated KV-cache runs on at least 500 generated continuations.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-gated-suffix-drafting-as-an-opportunistic-hybri-2be5f9e711`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
