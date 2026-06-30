# Layered agent memory: doctrine vs facts on repeated tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layered-agent-memory-doctrine-vs-facts-on-repeated-tasks-81bf971a756a`
Run ID: `layered-agent-memory-doctrine-vs-facts-on-repeated-tasks-81bf971a756a-20260620T050521968308+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ae97c47b70d8

## What looked useful

Layered doctrine/fact memory reached 14/14 accuracy versus transcript_search 10/14, flat_retrieval 8/14, and no_memory 0/14. The largest gap was on newer wrong-layer records: layered 6/6, transcript 3/6, flat 0/6.

## Boundaries and scale limits

Synthetic structured events only; no LLM agent, embedding retrieval, noisy extraction, real operator traces, or persistence restart validation. CPU-only run completed in under 10 seconds.

## Claim scope

On a deterministic synthetic replay corpus with 14 repeated-task queries, typed layered doctrine/fact memory avoided wrong-layer and stale-slot retrieval errors better than no-memory, transcript-search, and untyped flat-retrieval baselines.

## Why it stopped

Closed as a useful synthetic proxy signal, not full validation; evidence is too narrow and structured for a paper-positive decision.

## Recommended next action

Run a bounded LLM-agent replay with noisy extracted memories and persistence checks before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-agent replay for layered doctrine/fact memory under noisy extraction
- Success threshold: Layered memory improves accuracy by at least 15 percentage points over the best baseline on wrong-layer conflict queries and does not regress same-layer update queries by more than 5 percentage points.
- Stop condition: Stop if layered memory fails to beat the best baseline on wrong-layer conflict queries or if most errors are caused by unrecoverable extraction ambiguity rather than memory layering.

## Evidence references

- Artifact root: `<local-path>/projects/layered-agent-memory-doctrine-vs-facts-on-repeated-tasks-81bf971a756a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
