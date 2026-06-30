# Anchor-Based Attention-Gated KV Pruning

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-based-attention-gated-kv-pruning-e8ea68209ba0`
Run ID: `anchor-based-attention-gated-kv-pruning-e8ea68209ba0-20260525T223541023507+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/7d3443ced414

## What looked useful

Anchor attention is a better gate than naive recency for retaining attention mass and preserving attention outputs, but it is not sufficient as a standalone KV-pruning policy because random broad retention produced lower mean relative attention-output MSE on distilgpt2 and GPT-2-small at the tested budgets.

## Boundaries and scale limits

No true autoregressive pruned-cache generation, no direct perplexity or quality measurement under cache pruning, no long-context benchmark, no serving latency/memory benchmark, and no full Wikitext run because dataset loading attempted online Hub access. Evidence is bounded to internal attention-output reconstruction on small cached models.

## Claim scope

On post hoc teacher-forced attention-output preservation for cached tiny-gpt2, distilgpt2, and GPT-2-small using built-in technical English contexts of length 64-128, anchor-derived attention gating consistently beats pure recency but does not beat random broad KV retention on the stronger small-model controls.

## Why it stopped

Proxy/internal attention-output evidence is mixed: anchor gating clears recency but fails the stronger random-retention control, so the current idea is not paper-positive without a materially improved gate and direct cache-pruning metrics.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should implement real autoregressive pruned-cache decoding and compare value-aware or diversity-aware anchor gates against random and recency on next-token NLL.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Value-Aware Anchor KV Pruning Under Real Autoregressive Cache Decoding
- Success threshold: At equal KV retention, the improved anchor policy must reduce mean NLL or perplexity degradation versus both random and recency by at least 10% relative on two cached GPT-style models, without adding more than 20% decoding latency overhead versus the pruning baseline.
- Stop condition: Stop if anchor-derived variants fail to beat random retention on direct NLL/perplexity at either 25% or 50% retention, or if pruning overhead eliminates practical memory/latency benefit.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-based-attention-gated-kv-pruning-e8ea68209ba0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
