# Suffix-Tree Drafter Accelerates Long-Context Decoding Without Quality Loss

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `suffix-tree-drafter-accelerates-long-context-decoding-without-quality-loss-2b2da2e3076b`
Run ID: `suffix-tree-drafter-accelerates-long-context-decoding-without-quality-loss-2b2da2e3076b-20260619T075142194008+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7e33b636a484

## What looked useful

Across 72 repeat-structured medium configurations, exact output identity held and verifier-call proxy speedup ranged from 2.36x to 10.19x; 12 pure-random controls stayed at 1.0x with zero accepted draft tokens.

## Boundaries and scale limits

No real transformer verifier, tokenizer, stochastic sampling, GPU kernel timing, KV-cache measurement, production suffix tree, or real long-context benchmark was tested.

## Claim scope

In a synthetic exact-verification benchmark over 80k-token prefixes and 20k-token continuations, a suffix-history copy drafter preserved exact baseline output and reduced verifier calls on repeat-structured token streams.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy and does not validate real long-context LLM serving throughput.

## Recommended next action

Run a bounded direct verifier test with a small transformer using greedy decoding, byte/token identity checks against baseline, repeated-context and pure-random controls, and wall-clock tokens/sec including drafter overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer exact-verification test for suffix-history drafting
- Success threshold: At least 1.5x wall-clock tokens/sec improvement on repeated-context prompts with exact greedy output identity and no more than 5% slowdown on pure-random controls.
- Stop condition: Stop if exact output identity fails, if repeated-context wall-clock speedup is below 1.2x after overhead, or if pure-random controls slow down by more than 10%.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-drafter-accelerates-long-context-decoding-without-quality-loss-2b2da2e3076b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
