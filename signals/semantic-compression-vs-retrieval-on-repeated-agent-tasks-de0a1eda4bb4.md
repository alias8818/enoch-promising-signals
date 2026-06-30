# Semantic compression vs retrieval on repeated agent tasks

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `semantic-compression-vs-retrieval-on-repeated-agent-tasks-de0a1eda4bb4`
Run ID: `semantic-compression-vs-retrieval-on-repeated-agent-tasks-de0a1eda4bb4-20260611T162157722996+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/f0ba224577ac

## What looked useful

Compression and retrieval fail on different memory shapes. Compression can represent current-state profiles efficiently when the full profile set fits the context budget, but lossy compression drops rare episodic facts. Retrieval is a strong baseline when queries expose entity/key handles and remains necessary for exact sparse memories.

## Boundaries and scale limits

Synthetic/proxy-only evidence: no live LLM reasoning, no embedding model, no real agent traces, and no human task quality evaluation. Main run used 50 seeds, 900 events per seed, 6 context budgets, and 8,750 queries per budget on one CPU process.

## Claim scope

Synthetic repeated-agent-task memory benchmark with deterministic answer recovery over current-state preferences and episodic exact facts. Semantic compression was not a drop-in replacement for retrieval; retrieval dominated query-addressable state facts and retained much higher episodic accuracy, while compression only matched state accuracy once the compressed profiles fit in context.

## Why it stopped

Proxy early falsification of the broad replacement claim: semantic compression alone failed episodic exact-fact recovery and required enough budget to carry all compressed profiles before matching retrieval on state facts.

## Recommended next action

Stop this run as a proxy no-paper result; next run should test a query-aware compressed-profile plus retrieval hybrid with LLM-in-the-loop repeated tasks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-in-the-loop query-aware compression plus retrieval on repeated agent tasks
- Success threshold: Hybrid improves mean task accuracy by at least 5 percentage points over pure retrieval or reduces mean context tokens by at least 30% at statistically indistinguishable accuracy, while preserving at least 95% of retrieval's episodic exact-fact recall.
- Stop condition: Stop if query-aware hybrid loses more than 5 percentage points of accuracy to retrieval at matched budgets or if episodic exact-fact recall falls below 90% of retrieval across two independent seeds/datasets.

## Evidence references

- Artifact root: `<local-path>/projects/semantic-compression-vs-retrieval-on-repeated-agent-tasks-de0a1eda4bb4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
