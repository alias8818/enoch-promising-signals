# Retrieval Suffix-Cache Speculation for Agentic Enoch Workloads

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `retrieval-suffix-cache-speculation-for-agentic-enoch-workloads-b59ec790bc95`
Run ID: `retrieval-suffix-cache-speculation-for-agentic-enoch-workloads-b59ec790bc95-20260519T230411717671+0000`

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

- ChatGPT Pro speculative decoding research map 2026-05-19: file://new-chatgpt-pro-ideas-05-19.md
- Spec-Decoding Oracle Trace Ranker: Instrumented DFlash Trace Analysis to Rank 12 Branch Proposals: file://new-chatgpt-pro-ideas-05-19.md

## What looked useful

Identical suffix text does not imply reusable deeper-layer suffix KV when retrieved prefix content changes; changed-prefix rows showed mean layer-2 to layer-4 suffix K rel-L2 of 0.651, 0.607, and 0.572 and suffix V rel-L2 of 0.644, 0.592, and 0.547. Synthetic overlap still suggests a possible latency opportunity only for designs that compute after the exact prefix is known or validate approximate reuse.

## Boundaries and scale limits

No production LLM, tokenizer, serving stack, or real agent traces were used. The latency result is a synthetic optimistic upper bound, not an end-to-end serving measurement.

## Claim scope

Mechanism-level local probe of exact context-independent suffix KV reuse for repeated suffix text under changed retrieved prefixes in a small deterministic causal transformer.

## Why it stopped

Proxy mechanism evidence rejects context-independent exact suffix KV reuse; this is not a full production validation.

## Recommended next action

Stop this run as an early proxy falsification of naive exact suffix-cache reuse; a follow-up should implement exact post-retrieval overlap in a real serving path and measure TTFT and quality on trace-derived agent prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end post-retrieval suffix prefill overlap for agent prompts
- Success threshold: At least 10% median TTFT reduction and no measurable output/quality regression on a bounded trace set, with scheduler overhead below 20% of saved prefill time.
- Stop condition: Stop if exact post-retrieval overlap saves less than 5% median TTFT or introduces output differences/quality regressions on the bounded trace set.

## Evidence references

- Artifact root: `<local-path>/projects/retrieval-suffix-cache-speculation-for-agentic-enoch-workloads-b59ec790bc95`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
