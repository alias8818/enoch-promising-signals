# Agent memory with trace-derived semantic compression vs flat retrieval on local LLMs

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `agent-memory-with-trace-derived-semantic-compression-vs-flat-retrieval-on-local-llms-2b7e9b4c8c90`
Run ID: `agent-memory-with-trace-derived-semantic-compression-vs-flat-retrieval-on-local-llms-2b7e9b4c8c90-20260621T083406533053+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/114ecde8251c

## What looked useful

Across 10 seeds and 216 queries per seed, semantic compression reduced average index tokens from about 31,865 to 2,263 and achieved 1.000 exact answer availability at all tested budgets. Flat retrieval achieved 0.7995 at 60-80 tokens, 0.9616 at 120, 0.9931 at 180, and 0.9995 at 260. Semantic retrieval was also faster, about 0.130 ms/query versus 0.554 ms/query for flat chunks.

## Boundaries and scale limits

Evidence is synthetic and retrieval-context-only. It did not run end-to-end local LLM generation, real agent traces, noisy learned compression, multi-model robustness, or long-horizon agent tasks.

## Claim scope

On synthetic noisy agent traces with perfectly parseable durable facts, trace-derived semantic compression produced a much smaller memory index and improved answer-bearing retrieval under tight context budgets compared with BM25 retrieval over raw trace chunks.

## Why it stopped

Bounded synthetic retrieval evidence supports the mechanism, but paper-positive closure requires direct local-LLM generation and real or messier traces.

## Recommended next action

Stop this run as a no-paper useful signal; deepen with an end-to-end local 1B-3B instruction-model benchmark using the same retrieved contexts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end local LLM evaluation of compressed versus flat agent memory contexts
- Success threshold: At 60-120 token budgets, compressed contexts improve model exact answer accuracy by at least 10 percentage points over flat retrieval without increasing hallucination rate, across at least 5 seeds.
- Stop condition: Stop if compressed contexts fail to improve exact model accuracy by 5 percentage points at 60-120 token budgets or if hallucination increases by more than 3 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/agent-memory-with-trace-derived-semantic-compression-vs-flat-retrieval-on-local-llms-2b7e9b4c8c9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
