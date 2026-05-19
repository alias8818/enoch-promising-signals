# KV-cache prompt suffix lookahead on natural long-context copy workloads

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `kv-cache-prompt-suffix-lookahead-on-natural-long-context-c-6364cf9a9c`
Run ID: `kv-cache-prompt-suffix-lookahead-on-natural-long-context-c-6364cf9a9c-20260516T161623480471+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/651118c6a43c

## What looked useful

Actual KV-cache decoding with cloned speculative verification supports the mechanism: verified prompt suffix blocks can accept long copied runs and cut greedy decode calls while preserving exact token output; ablations at lookahead 4, 8, 16, and 32 all exceeded 2x aggregate call speedup with 6/6 exact equality.

## Boundaries and scale limits

Small controlled local benchmark only; natural passages were embedded snippets, suffix positions were known by construction, contexts were under 600 tokens, model was distilgpt2, and no production serving, batching, automatic suffix localization, larger model, or benchmark-scale validation was run.

## Claim scope

Tier 1 controlled direct test: on six distilgpt2 natural-language copy prompts with 440-572 token contexts, prompt-suffix lookahead preserved exact greedy output and reduced aggregate decode forward calls by 5.13x at lookahead 16.

## Why it stopped

No-paper closure: Tier 1 mechanism evidence is positive and useful, but the run is too small and controlled for publication readiness.

## Recommended next action

Run a bounded deepen follow-up on a held-out natural long-context copy dataset with automatic suffix localization and require exact greedy equality plus at least 2x aggregate forward-call reduction on 100+ examples.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out natural copy suffix localization benchmark
- Success threshold: Exact greedy-output equality under the safe fallback policy, aggregate decode forward-call speedup >= 2.0x, mean accepted tokens per verification call >= 4, and no wall-time regression on 100+ held-out examples.
- Stop condition: Stop if automatic suffix localization acceptance falls below 2 tokens per verification call or aggregate forward-call speedup is below 1.5x after correctness-preserving fallback.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-prompt-suffix-lookahead-on-natural-long-context-c-6364cf9a9c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
