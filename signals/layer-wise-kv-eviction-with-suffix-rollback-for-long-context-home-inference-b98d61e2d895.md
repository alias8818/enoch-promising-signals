# Layer-wise KV eviction with suffix rollback for long-context home inference

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layer-wise-kv-eviction-with-suffix-rollback-for-long-context-home-inference-b98d61e2d895`
Run ID: `layer-wise-kv-eviction-with-suffix-rollback-for-long-context-home-inference-b98d61e2d895-20260609T041837675583+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ed565345b183

## What looked useful

Across 24 trials, stale suffix caches retained ghost prefix dependence in 24/24 trials with mean next-token logit L2 0.1815 between different evicted prefixes sharing the same suffix. A layer-wise retained-prefix variant also retained ghost dependence in 24/24 trials with mean L2 0.4530. Recomputing the suffix after eviction reduced the identical-suffix ghost metric to 0.0 by making the cache state consistent with the retained context.

## Boundaries and scale limits

Evidence is synthetic and mechanism-level only: random weights, short 256-token prompts, no trained language quality metrics, no real long-context benchmark, and no serving-system latency or memory comparison beyond local process telemetry.

## Claim scope

In a fixed-seed random causal transformer cache probe, suffix rollback removes evicted-prefix dependence from retained suffix KV state after prefix eviction.

## Why it stopped

No-paper closure: this run produced a useful synthetic mechanism signal, but not trained-model or full long-context evidence.

## Recommended next action

Run a bounded trained-model follow-up on a small GPT-2-class or tiny pretrained causal LM, comparing suffix rollback against sliding-window and no-rollback eviction on logit drift/perplexity, memory, and latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trained-model suffix rollback evaluation against no-rollback KV eviction
- Success threshold: At matched retained KV memory, suffix rollback reduces mean logit drift or perplexity degradation by at least 20% versus no-rollback eviction while adding less than 15% amortized decode latency on the tested prompt set.
- Stop condition: Stop if suffix rollback fails to improve logit drift/perplexity over no-rollback in two independent prompt sets or if recompute latency exceeds 25% at the smallest useful rollback length.

## Evidence references

- Artifact root: `<local-path>/projects/layer-wise-kv-eviction-with-suffix-rollback-for-long-context-home-inference-b98d61e2d895`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
