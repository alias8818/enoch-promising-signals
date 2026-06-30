# Anchor-Indexed Compressed Memory Beats Flat Retrieval on Long-Horizon Agent Tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-indexed-compressed-memory-beats-flat-retrieval-on-long-horizon-agent-tasks-382040d9f6aa`
Run ID: `anchor-indexed-compressed-memory-beats-flat-retrieval-on-long-horizon-agent-tasks-382040d9f6aa-20260628T111807163741+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c6936620b079

## What looked useful

Anchor indexing plus compressed per-anchor state can turn multi-fact long-horizon recall into exact keyed lookup and avoid global flat retrieval dilution. However, generic vector retrieval over anchor summaries failed at 1000 anchors, and oracle metadata filtering made flat retrieval competitive once enough raw context was allowed.

## Boundaries and scale limits

The benchmark is synthetic and CPU-only. It does not validate real LLM agents, learned summarization, noisy online anchor creation, naturalistic observations, or production retrievers with reranking. An oracle anchor-filtered flat baseline reached 99.1% at top-16, so the broad claim is not established.

## Claim scope

In a synthetic context-budgeted long-horizon recall task with explicit anchor keys and 12-fact route-signature queries, exact anchor-indexed compressed state achieved 100% accuracy with about 15% of the raw text footprint, while global flat retrieval at top-32 achieved 0.2%. This supports the mechanism only for explicit-anchor structured recall under tight raw-context budgets.

## Why it stopped

No-paper useful signal: local synthetic evidence supports a narrow mechanism but does not provide direct publication-grade validation of the broad long-horizon agent-task claim.

## Recommended next action

Run a bounded direct LLM-agent trace benchmark with online/noisy anchor creation, generated summaries under a fixed token budget, and strong flat, metadata-filtered, and hierarchical retrieval baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Noisy Online Anchor Memory on LLM-Agent Trace Recall
- Success threshold: Anchor-indexed compressed memory improves answer accuracy by at least 10 percentage points over the strongest non-anchor baseline at the same context/token budget, without more than 2x query latency, across at least three trace/task families.
- Stop condition: Stop if metadata-filtered or hierarchical flat retrieval matches anchor memory within 3 percentage points at equal budget, or if anchor noise above 10% collapses anchor-memory accuracy below the strongest baseline.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-indexed-compressed-memory-beats-flat-retrieval-on-long-horizon-agent-tasks-382040d9f6aa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
