# KV-cache eviction via learned salience for long-context on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-eviction-via-learned-salience-for-long-context-on-gb10-4c7f9022cc3f`
Run ID: `kv-cache-eviction-via-learned-salience-for-long-context-on-gb10-4c7f9022cc3f-20260605T131635212211+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/0ecc541d5ba8

## What looked useful

The learned salience predictor fit future-attention labels well (train label correlation 0.9006) and beat recency/random on retained attention mass, but it was essentially tied with a simple key-norm heuristic and often worse than recency on output MSE at tight budgets.

## Boundaries and scale limits

Not a real LLM decoding or serving test; no multi-layer transformer KV traces, no task-level perplexity/retrieval accuracy, no paged-attention implementation overhead, and no full long-context model validation.

## Claim scope

Synthetic GPU attention-trace benchmark at context length 2048 with fixed cache budgets from 64 to 512 entries; learned insertion-time salience is compared with recency, random, key-norm, and oracle retention.

## Why it stopped

Proxy/early falsification rather than full validation: learned salience did not show a meaningful advantage over the simple norm baseline, and downstream output MSE did not justify added learned-policy complexity.

## Recommended next action

Stop this run as a proxy early falsification; a bounded next test should use real GPT-2-small KV traces and require learned salience to beat recency plus norm on task-level loss at equal cache size.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Layer-aware learned salience on real GPT-2-small KV traces
- Success threshold: At two or more cache budgets, learned salience improves task-level loss or retrieval accuracy by at least 5% relative to the better of recency and key-norm without increasing cache size.
- Stop condition: Stop if learned salience fails to beat the better simple baseline by 5% on task-level metrics or if gains disappear when key-norm and recency features are ablated/controlled.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-eviction-via-learned-salience-for-long-context-on-gb10-4c7f9022cc3f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
