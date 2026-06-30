# Sliding-window KV cache with periodic exact-anchor flush on CPU Proxmox

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sliding-window-kv-cache-with-periodic-exact-anchor-flush-on-cpu-proxmox-e1d291672af0`
Run ID: `sliding-window-kv-cache-with-periodic-exact-anchor-flush-on-cpu-proxmox-e1d291672af0-20260619T190612223979+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/88573e2fcf6e

## What looked useful

Default sweep over 8 seeds found anchored old-fact accuracy of 0.3799 for anchor_flush versus 0.0000 for sliding_window and 1.0000 for full_context. Anchor_flush used 153.7 mean candidate slots versus 460.5 for full_context on the anchored workload. On deliberately unanchored old facts, anchor_flush and sliding_window both scored 0.0000 old-fact accuracy.

## Boundaries and scale limits

No real transformer implementation, no natural-language quality measurement, no latency/kernel benchmark, no multi-head or positional-encoding effects, and no long-context production serving workload.

## Claim scope

Synthetic CPU retrieval simulation over exact K/V facts: periodic exact anchor flushes recover a useful fraction of old facts only when those facts are selected as anchors, using fewer candidate K/V slots than full context.

## Why it stopped

Proxy simulation supports anchor-selected retrieval but is not direct transformer evidence and falsifies any broad claim that exact periodic anchors recover unselected long-range facts.

## Recommended next action

Stop this run as no-paper useful signal; next bounded action is to implement the policy in a small transformer inference path and measure perplexity/task accuracy, decode latency, and memory against full-context and sliding-window controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Implement exact anchor flush in a small transformer decode cache
- Success threshold: Anchor_flush should improve anchored long-range task accuracy by at least 20 percentage points over sliding_window while using at most 50% of full_context peak K/V memory and losing no more than 5% absolute accuracy versus full_context on anchor-targeted cases.
- Stop condition: Stop if anchor_flush fails to beat sliding_window by at least 10 percentage points on anchored long-range cases or if latency/memory overhead exceeds full_context benefits in the small transformer implementation.

## Evidence references

- Artifact root: `<local-path>/projects/sliding-window-kv-cache-with-periodic-exact-anchor-flush-on-cpu-proxmox-e1d291672af0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
