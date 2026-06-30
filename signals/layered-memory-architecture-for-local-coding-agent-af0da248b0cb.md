# Layered Memory Architecture for Local Coding Agent

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `layered-memory-architecture-for-local-coding-agent-af0da248b0cb`
Run ID: `layered-memory-architecture-for-local-coding-agent-af0da248b0cb-20260630T162504588929+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/98573a40af07

## What looked useful

Layered memory can act as effective context compression for extractable durable project facts: 6000/6000 correct at 12, 20, and 40 token budgets versus BM25 at 0/6000, 2270/6000, and 4166/6000 respectively. The advantage disappeared by 100 tokens when BM25 could include enough raw snippets.

## Boundaries and scale limits

Synthetic traces only; exact keyed facts; perfect regex fact extraction; no real LLM, no code-edit task harness, no natural agent logs, no imperfect extraction, and no user productivity measurement.

## Claim scope

In a deterministic synthetic local-coding-agent memory benchmark, a compact latest-fact layer recovered keyed project facts under 12-40 token context budgets where flat recency failed and flat BM25 was budget-limited; BM25 matched layered accuracy once the budget reached 100 tokens.

## Why it stopped

Proxy-only synthetic evidence supports a mechanism but does not validate an end-to-end local coding-agent architecture or paper-grade claim.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded real-trace follow-up comparing the same policies on labeled coding-agent logs with imperfect fact extraction.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Layered Memory on Real Coding-Agent Trace Facts
- Success threshold: Layered memory improves answer accuracy by at least 15 percentage points over BM25 at one or more tight budgets below 100 tokens, or matches BM25 accuracy while using at least 50% fewer context tokens, with extractor F1 reported.
- Stop condition: Stop if imperfect extraction F1 is below 0.70 or if layered memory fails to beat BM25 by accuracy or context-token efficiency on the labeled trace set.

## Evidence references

- Artifact root: `<local-path>/projects/layered-memory-architecture-for-local-coding-agent-af0da248b0cb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
