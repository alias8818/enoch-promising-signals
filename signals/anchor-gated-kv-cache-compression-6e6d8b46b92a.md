# Anchor-Gated KV Cache Compression

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchor-gated-kv-cache-compression-6e6d8b46b92a`
Run ID: `anchor-gated-kv-cache-compression-6e6d8b46b92a-20260530T060113392096+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/daf43b4f85d4

## What looked useful

Anchor-aware KV retention produced a reproducible mechanism signal: on distilgpt2, anchor_gated_proxy mean relative MSE was 0.01107 versus the best aggregate baseline 0.02542, and oracle_anchor mean relative MSE was 0.00376. Paired results were mixed but favorable in non-tie cases, indicating a useful next experiment rather than paper-ready closure.

## Boundaries and scale limits

No end-to-end generation, perplexity, latency, memory-bandwidth, long-context, or large-model validation was run. The deployable gate was hand-coded and the oracle policy used future/full attention, so this does not establish production KV cache compression quality.

## Claim scope

On a bounded distilgpt2 attention-output proxy over six local passages, an anchor-gated proxy retention policy reduced mean relative MSE versus recent, uniform, and magnitude retention baselines at 12.5%, 25%, and 50% KV budgets; an offline oracle anchor score provided a stronger upper bound.

## Why it stopped

This run produced a bounded attention-output proxy signal, but not direct generation-quality or systems evidence; it is useful no-paper evidence rather than a full validation.

## Recommended next action

Implement a causal deployable gate inside actual generation and measure logit drift, perplexity, latency, and memory at fixed KV budgets on longer contexts before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Causal generation test for anchor-gated KV compression
- Success threshold: At 25% KV budget, causal anchor-gated compression should reduce perplexity or logit-drift degradation by at least 20% versus the best simple retention baseline while preserving measured KV memory reduction and adding less than 10% latency overhead.
- Stop condition: Stop if the causal gate fails to beat the best simple baseline on perplexity/logit drift at 25% budget or if gate overhead erases the practical memory/latency benefit.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-gated-kv-cache-compression-6e6d8b46b92a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
