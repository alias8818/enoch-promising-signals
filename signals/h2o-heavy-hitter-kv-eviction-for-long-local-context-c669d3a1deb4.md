# H2O heavy-hitter KV eviction for long local context

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `h2o-heavy-hitter-kv-eviction-for-long-local-context-c669d3a1deb4`
Run ID: `h2o-heavy-hitter-kv-eviction-for-long-local-context-c669d3a1deb4-20260529T064021255382+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2ce92ee43bde

## What looked useful

H2O retained 1.46x-1.72x the attention mass of recency and reduced context reconstruction MSE to 1.9%-17.4% of recency across tested budgets, while selecting much older keys. This supports the mechanism but not a paper-ready claim.

## Boundaries and scale limits

Proxy-only attention-trace study on distilgpt2 with deterministic local-context passages; no generation-time KV cache, no perplexity/task-accuracy measurement, no latency/memory serving benchmark, and no 7B+ or production-length validation.

## Claim scope

On distilgpt2 attention traces at 512 and 1024 tokens, H2O-style cumulative-attention KV retention preserved substantially more full-attention mass and produced lower reconstructed per-head context error than recency or random at the same KV budgets.

## Why it stopped

Proxy mechanism evidence is positive but not full validation; the run stops as a no-paper useful signal rather than claiming production KV-cache viability.

## Recommended next action

Implement actual generation-time H2O KV-cache pruning for a small Hugging Face causal LM and compare perplexity plus long-context retrieval accuracy against recency at matched cache budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Generation-time H2O KV-cache perplexity and retrieval test
- Success threshold: At two or more cache budgets, H2O should reduce perplexity or retrieval error by at least 10% relative to recency while preserving a meaningful memory reduction versus full cache.
- Stop condition: Stop if H2O's trace-level advantage fails to improve perplexity/retrieval over recency at matched budgets or if pruning overhead erases the practical cache benefit.

## Evidence references

- Artifact root: `<local-path>/projects/h2o-heavy-hitter-kv-eviction-for-long-local-context-c669d3a1deb4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
