# Real-trace doctrine compression replay benchmark

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-trace-doctrine-compression-replay-benchmark-fa83a1d2e9`
Run ID: `real-trace-doctrine-compression-replay-benchmark-fa83a1d2e9-20260619T203001537660+0000`

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

- Parent run decision: Agent Memory Doctrine via Trace Semantic Compression: enoch://control-plane/projects/agent-memory-doctrine-via-trace-semantic-compression-b581408c1aab/runs/agent-memory-doctrine-via-trace-semantic-compression-b581408c1aab-20260619T200702666506+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ce09d176aa68

## What looked useful

Doctrine-compressed memory reached 1.000 accuracy and 0.000 forbidden-hit rate versus flat retrieval at 0.706 accuracy and 0.081 forbidden-hit rate. Mean paired bootstrap accuracy delta was +0.2950 with 95% interval [+0.2728, +0.3164]. Compressed memory selected 4.1 tokens on average versus flat retrieval's 117.8.

## Boundaries and scale limits

Small generated local replay corpus only: 1,536 cases, symbolic answerer, lexical retrieval baselines, no private live traces, no LLM agent, no human or executable task grading.

## Claim scope

In a deterministic Tier 1 replay benchmark with generated repo-shaped trace events, scoped key-preserving doctrine compression answered replay questions more accurately than lexical flat retrieval while using far fewer selected context tokens.

## Why it stopped

Tier 1 direct evidence supports the mechanism but is not publication-grade because traces and answers are deterministic/generated and baselines are limited.

## Recommended next action

Do not write a paper from this run; deepen with real held-out operator traces, a live or replayed LLM-agent harness, stronger retrieval baselines, and executable or human grading.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace LLM-agent replay for doctrine-compressed memory
- Success threshold: Compressed doctrine memory improves accuracy by >= 0.10 over the strongest retrieval baseline, has forbidden/stale/cross-scope error rate no worse than baseline, and uses <= 50% of the selected context tokens.
- Stop condition: Stop if compressed memory fails to beat the strongest retrieval baseline by 0.10 accuracy, increases forbidden/stale/cross-scope errors, or requires an unreliable extractor that cannot reproduce the structured memory.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-doctrine-compression-replay-benchmark-fa83a1d2e9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
