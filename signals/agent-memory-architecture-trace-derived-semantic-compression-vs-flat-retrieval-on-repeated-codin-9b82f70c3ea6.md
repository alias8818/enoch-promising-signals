# Agent memory architecture: trace-derived semantic compression vs flat retrieval on repeated coding tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `agent-memory-architecture-trace-derived-semantic-compression-vs-flat-retrieval-on-repeated-codin-9b82f70c3ea6`
Run ID: `agent-memory-architecture-trace-derived-semantic-compression-vs-flat-retrieval-on-repeated-codin-9b82f70c3ea6-20260628T031702169372+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a959f9b7cbe6

## What looked useful

Semantic compression appears useful when it joins distributed trace facts into compact retrievable units; compression that drops validation detail fails systematically.

## Boundaries and scale limits

Synthetic traces only; no real repositories, no LLM patch generation, no automatic noisy-trace summarizer, and no stronger flat baselines such as session-window, vector, or hybrid retrieval.

## Claim scope

In a deterministic synthetic repeated-coding-task retrieval benchmark, trace-derived semantic cards that preserve patch file, invariant, and validation command retrieve all required facts under 50-320 word budgets, while flat retrieval over raw trace chunks and a lossy compressed control do not.

## Why it stopped

Closed as no-paper useful signal because the evidence is a synthetic retrieval proxy, not direct coding-agent validation.

## Recommended next action

Run a bounded deepen follow-up on real or semi-real coding traces with end-to-end patch/test success and stronger flat retrieval baselines before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace coding-agent memory comparison with semantic cards versus flat session-window retrieval
- Success threshold: Semantic-card memory improves end-to-end test-pass rate by at least 10 percentage points over the best flat baseline at equal context budget, with no more than 5 percentage points lost to extraction omissions.
- Stop condition: Stop if semantic extraction omits required facts in more than 15% of tasks or if semantic cards fail to beat the best flat baseline on test-pass rate under equal budget.

## Evidence references

- Artifact root: `<local-path>/projects/agent-memory-architecture-trace-derived-semantic-compression-vs-flat-retrieval-on-repeated-codin`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
