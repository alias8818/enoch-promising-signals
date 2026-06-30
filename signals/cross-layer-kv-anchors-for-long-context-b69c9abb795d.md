# Cross-Layer KV Anchors for Long Context

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cross-layer-kv-anchors-for-long-context-b69c9abb795d`
Run ID: `cross-layer-kv-anchors-for-long-context-b69c9abb795d-20260525T235652516548+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b4b0386b97fe

## What looked useful

Anchor injection produced consistent final accuracy around 7.7-7.8% versus chance 1.56%; local controls were 1.3-1.8% and dense controls were 1.6-2.4% under the same budget. This supports the mechanism as a learnable shortcut for far-prefix retrieval, not a paper-ready long-context LLM result.

## Boundaries and scale limits

The evidence is synthetic and small-scale: 1.0M-parameter transformer, 3 total seeds across 400-600 training steps, fixed prefix anchors from embedding states, no natural-language long-context tasks, no GPT-2-small-class baseline, no serving KV-cache implementation, and no equal-FLOP or long-run optimization study.

## Claim scope

In a toy synthetic associative-recall benchmark at sequence length 512 with 16 prefix key/value pairs, a small local-attention transformer augmented with fixed prefix cross-layer KV anchors learned far-prefix retrieval above chance under a short GPU training budget, while local-only and dense controls stayed near chance.

## Why it stopped

Synthetic proxy evidence supports the mechanism but is not direct/full validation of cross-layer KV anchors for real long-context LLMs.

## Recommended next action

Stop this run as no-paper useful signal; next run a bounded deepen experiment with a parameter-matched GPT-2-small-class or stronger toy transformer comparing dense, local, local+anchors, and anchor-selection ablations at equal parameter count and reported FLOP/memory budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Parameter-matched long-context retrieval validation for cross-layer KV anchors
- Success threshold: Local+anchor should exceed local-only by at least 10 absolute accuracy points and match or exceed dense attention at lower memory or faster convergence on at least two tasks across three seeds.
- Stop condition: Stop if anchor gains disappear under parameter-matched controls, if dense attention catches up at equal compute with no memory advantage, or if anchor memory/latency overhead eliminates the practical benefit.

## Evidence references

- Artifact root: `<local-path>/projects/cross-layer-kv-anchors-for-long-context-b69c9abb795d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
