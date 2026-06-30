# Layered Memory with Semantic Compression for Home Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layered-memory-with-semantic-compression-for-home-agents-694b3fe84ea8`
Run ID: `layered-memory-with-semantic-compression-for-home-agents-694b3fe84ea8-20260614T022254631638+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/ab1c977a3cf5

## What looked useful

Across 9,600 synthetic queries per strategy, layered memory reached 1.0000 accuracy with 347.8 mean memory tokens and 8.7 mean retrieval tokens, versus flat retrieval at 0.5423 accuracy with 2193.6 mean memory tokens and transcript search at 0.3081 accuracy with 3280.0 mean memory tokens. Budget sweeps at 24, 48, 96, and 192 tokens preserved the layered advantage.

## Boundaries and scale limits

No real household traces, no noisy LLM extraction, no privacy redaction, no long-horizon deployment drift, and no live agent/tool loop were tested. Evidence is proxy-only and not publication-grade direct validation.

## Claim scope

On deterministic synthetic home-agent replay traces with oracle-grade structured compression, layered semantic memory preserved latest locations, resident preferences, routines, and exceptions under a 96-token retrieval budget better than transcript search and flat retrieval baselines.

## Why it stopped

No-paper closure: the mechanism is supported only by a synthetic proxy with an oracle-grade compressor, not by direct real-trace or LLM-in-the-loop evidence.

## Recommended next action

Run a bounded direct follow-up with noisy extractor-generated memory on realistic or released home-agent traces and require at least a 15 percentage point accuracy gain over flat retrieval while using at most 25% of memory tokens.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Noisy semantic compression on realistic home-agent replay traces
- Success threshold: At least +15 percentage points accuracy over flat retrieval at no more than 25% of flat memory tokens on a held-out realistic trace split.
- Stop condition: Stop if noisy layered compression loses to flat retrieval, uses more than 25% of flat memory tokens, or failure analysis shows schema misses dominate.

## Evidence references

- Artifact root: `<local-path>/projects/layered-memory-with-semantic-compression-for-home-agents-694b3fe84ea8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
