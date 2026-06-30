# Anchor-Gated Eviction for Long-Context Small Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchor-gated-eviction-for-long-context-small-agents-dbb1e0867935`
Run ID: `anchor-gated-eviction-for-long-context-small-agents-dbb1e0867935-20260524T222130936983+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/500874881783

## What looked useful

Across the main sweep, anchor-gated recall on anchor-linked queries had minimum 0.992 and mean 0.999 across sparse, dense, and drift scenarios, with mean +0.959 recall gain over the best non-anchor baseline. A seed-17 repeat preserved the pattern with mean +0.970 gain. The unanchored negative control showed consistent harm, so the policy should be conditional on reliable anchors.

## Boundaries and scale limits

No real LLM agent loop, no natural-language anchor extraction, no model attention measurement, and no full-scale long-context task validation. The result is a mechanism probe over synthetic streams only.

## Claim scope

In a synthetic online bounded-memory benchmark with symbolic declared anchors, anchor-gated eviction greatly improves retention of anchor-linked answer facts versus FIFO, random, and recency/salience baselines under 512-2048 token budgets.

## Why it stopped

Closed as no-paper useful signal: synthetic evidence supports the anchor-linked retention mechanism but does not directly validate real small-agent performance.

## Recommended next action

Run a bounded real-trace replay using natural-language anchor extraction and measure downstream task answer accuracy against FIFO, recency/salience, retrieval, and anchor-gated eviction.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-Language Agent Trace Replay for Anchor-Gated Eviction
- Success threshold: At least +10 percentage points answer accuracy over the best non-anchor eviction baseline on anchor-dependent tasks, with no more than -3 points degradation on unanchored control tasks across at least 100 traces.
- Stop condition: Stop if anchor-gated eviction fails to beat the best baseline by 5 percentage points on anchor-dependent traces or causes more than 5 points degradation on unanchored controls.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-gated-eviction-for-long-context-small-agents-dbb1e0867935`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
