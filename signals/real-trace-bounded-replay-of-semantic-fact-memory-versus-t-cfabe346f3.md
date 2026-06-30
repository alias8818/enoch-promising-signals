# Real-trace bounded replay of semantic fact memory versus transcript retrieval

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-trace-bounded-replay-of-semantic-fact-memory-versus-t-cfabe346f3`
Run ID: `real-trace-bounded-replay-of-semantic-fact-memory-versus-t-cfabe346f3-20260622T002724389905+0000`

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

- Parent run decision: Trace-Derived Semantic Compression vs Full-Transcript Retrieval for Agent Memory: enoch://control-plane/projects/trace-derived-semantic-compression-vs-full-transcript-retrieval-for-agent-memory-b5d0092eee0f/runs/trace-derived-semantic-compression-vs-full-transcript-retrieval-for-agent-memory-b5d0092eee0f-20260621T232822240696+0000
- Provider-backed Research Facility batch: z-ai/glm-5.2: enoch://research-facility/provider/z-ai/glm-5.2/25a0052b910a

## What looked useful

Compressed semantic fact memory is useful under tight context budgets, but a lexical transcript retrieval baseline is competitive when the small traces fit within budget.

## Boundaries and scale limits

Local trace-derived tasks only; facts were manually structured; no raw real-user trace replay, no learned extractor, no LLM answer generation, and no broad corpus.

## Claim scope

On 3 local trace-derived replay tasks / 16 exact-answer queries, semantic fact memory matched transcript retrieval at a 72-token equal budget and exceeded it only under tighter equal budgets.

## Why it stopped

No paper-ready result: the primary 72-token direct test did not beat transcript retrieval, while the positive effect is limited to tight-budget trace-derived replay.

## Recommended next action

Run the same deterministic harness on a privacy-sanitized real repeated-agent trace set with at least 100 queries and pre-registered 24/48/72-token budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Sanitized real-trace tight-budget replay for semantic fact memory
- Success threshold: semantic_fact_memory accuracy minus transcript_search accuracy >= 0.20 at both 24-token and 48-token equal budgets, and >= -0.05 at 72 tokens
- Stop condition: Stop if transcript_search is within 0.05 accuracy of semantic_fact_memory at 24 and 48 tokens or if fact extraction errors account for more than 25% of semantic failures.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-bounded-replay-of-semantic-fact-memory-versus-t-cfabe346f3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
