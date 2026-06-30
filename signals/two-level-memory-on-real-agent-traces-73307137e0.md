# Two-Level Memory on Real Agent Traces

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `two-level-memory-on-real-agent-traces-73307137e0`
Run ID: `two-level-memory-on-real-agent-traces-73307137e0-20260610T111436506501+0000`

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

- Parent run decision: Two-Level Agent Memory: Anchors Plus Operator Doctrine: enoch://control-plane/projects/two-level-agent-memory-anchors-plus-operator-doctrine-4fb7f3f91592/runs/two-level-agent-memory-anchors-plus-operator-doctrine-4fb7f3f91592-20260610T065228504416+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/40ad4bcae45f

## What looked useful

Two-level memory reached 50.7% accuracy at 160 tokens versus 34.6% for flat lexical and 16.2% for recency-only, but missed the 75% success threshold. At 640 tokens it reached 94.1%, only 2.2 points above flat lexical, suggesting the cold tier helps most when context is very tight and ranking quality is the main bottleneck.

## Boundaries and scale limits

Retrieval-only benchmark; no LLM-in-the-loop agent replay; opportunistic local traces; deterministic regex fact extraction; only 136 valid repeated-fact tasks found across 3505 trace files.

## Claim scope

On 136 masked-repeat retrieval questions mined from 3495 local real Codex/Enoch traces, a simple two-level hot recency plus structured cold fact memory improved over recency-only and flat lexical retrieval at tight 80-160 token budgets, but failed the predefined 75% absolute accuracy threshold at 160 tokens.

## Why it stopped

Direct Tier 1 real-trace retrieval test failed the stated absolute accuracy threshold; this is no-paper useful-signal evidence, not publication readiness.

## Recommended next action

Run a bounded deepen test that replaces the cold-tier lexical ranker with a semantic or learned reranker on the same masked-repeat benchmark and requires at least 75% accuracy plus at least a 15 point margin over flat lexical at 160 tokens before any LLM-agent replay.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Semantic cold-tier ranking for two-level memory on real agent traces
- Success threshold: At 160 tokens, semantic two-level memory reaches at least 75% retrieval accuracy and beats the best non-two-level baseline by at least 15 percentage points on at least 100 real-trace tasks.
- Stop condition: Stop if semantic reranking remains below 65% accuracy at 160 tokens or does not beat flat lexical retrieval by at least 5 points, because the mechanism would not justify LLM-in-the-loop replay.

## Evidence references

- Artifact root: `<local-path>/projects/two-level-memory-on-real-agent-traces-73307137e0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
