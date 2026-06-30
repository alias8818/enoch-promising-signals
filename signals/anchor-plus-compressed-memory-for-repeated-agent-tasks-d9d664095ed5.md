# Anchor-Plus-Compressed Memory for Repeated Agent Tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-plus-compressed-memory-for-repeated-agent-tasks-d9d664095ed5`
Run ID: `anchor-plus-compressed-memory-for-repeated-agent-tasks-d9d664095ed5-20260628T015546658156+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/795ee7683651

## What looked useful

Anchor-plus-compressed memory achieved 1.000 stable-anchor accuracy at capacity 9 with mean 96.37 prompt-token units, while plain compressed summary at similar cost achieved 0.002 stable-anchor accuracy. The tradeoff is worse volatile dynamic recall when the anchor reserve leaves too few dynamic slots; updatable anchors are needed when anchors can be corrected.

## Boundaries and scale limits

Synthetic deterministic benchmark only; no LLM extraction, real traces, retrieval baseline, production serving, long-running model workload, or end-to-end agent task validation.

## Claim scope

In a deterministic synthetic repeated-task key-value retention benchmark, separating stable anchor facts from bounded compressed working memory preserved invariant anchors at near-identical compact prompt cost to plain compression.

## Why it stopped

Closed as no-paper useful signal because evidence supports the memory-retention mechanism only in a synthetic deterministic proxy, not a publication-grade agent memory result.

## Recommended next action

Run a bounded LLM-in-the-loop trace benchmark with labeled repeated-agent transcripts, retrieval and periodic-reanchor controls, and explicit stale-anchor correction tests.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-in-the-loop anchor-plus-compressed memory on repeated agent traces
- Success threshold: Anchor-plus must improve stable-anchor accuracy by at least 20 percentage points over the best compact-memory baseline at equal or lower prompt-token cost, while dynamic-fact accuracy drops by no more than 10 percentage points versus the best compact baseline.
- Stop condition: Stop if LLM extraction cannot reliably identify anchors above 80 percent F1 on the trace labels, or if anchor-plus fails to beat the best compact baseline on stable-anchor accuracy at matched token cost.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-plus-compressed-memory-for-repeated-agent-tasks-d9d664095ed5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
