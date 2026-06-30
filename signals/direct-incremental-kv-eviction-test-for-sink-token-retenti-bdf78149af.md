# Direct Incremental KV Eviction Test for Sink-Token Retention

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `direct-incremental-kv-eviction-test-for-sink-token-retenti-bdf78149af`
Run ID: `direct-incremental-kv-eviction-test-for-sink-token-retenti-bdf78149af-20260526T133921491031+0000`

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

- Parent run decision: KV-Cache Compression via Cross-Layer Attention Sinks: enoch://control-plane/projects/kv-cache-compression-via-cross-layer-attention-sinks-5313eef5075b/runs/kv-cache-compression-via-cross-layer-attention-sinks-5313eef5075b-20260526T035032162235+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/db0fa7a5e0de

## What looked useful

A direct incremental KV-cache intervention showed that sink_recent eviction met the preregistered Tier 1 threshold at all tested budgets: median KL ratios versus recent-only were below 0.001 and top-1 match to the full-cache baseline improved to 1.0. A 1-token sink ablation produced the same qualitative effect.

## Boundaries and scale limits

Single small GPT-style model, synthetic prompts, next-token endpoint only, no multi-step generation quality, no real serving traces, and no validation on RoPE/ALiBi/sliding-window/GQA architectures.

## Claim scope

On distilgpt2 with 8 synthetic 384-token prompts and cache budgets of 64, 96, and 128 tokens, retaining the first 1-4 cached sink tokens plus a recent window preserves full-cache next-token distributions far better than a same-budget recent-only eviction policy.

## Why it stopped

Tier 1 direct mechanism support was achieved, but the evidence is too narrow for publication readiness.

## Recommended next action

Run a bounded deepen follow-up across at least three causal LM families and one real prompt corpus, measuring next-token KL plus multi-token generation divergence against the same full-cache baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-Model Direct KV Eviction Test for Sink-Token Retention
- Success threshold: For at least two of three model families and two cache budgets per model, sink_recent median KL must be <= 0.90 of recent-only without reducing top-1 match or downstream generation/task metric.
- Stop condition: Stop if sink_recent fails the KL threshold on two model families or if the effect only appears on synthetic prompts and disappears on the real prompt corpus.

## Evidence references

- Artifact root: `<local-path>/projects/direct-incremental-kv-eviction-test-for-sink-token-retenti-bdf78149af`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
