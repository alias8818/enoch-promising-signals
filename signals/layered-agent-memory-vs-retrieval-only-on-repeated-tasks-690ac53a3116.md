# Layered agent memory vs retrieval-only on repeated tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layered-agent-memory-vs-retrieval-only-on-repeated-tasks-690ac53a3116`
Run ID: `layered-agent-memory-vs-retrieval-only-on-repeated-tasks-690ac53a3116-20260628T144412116905+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6038a796f7be

## What looked useful

Layering current entity state separately from stable operator doctrine removed both stale project fact recall and missing cross-project doctrine in this bounded replay. Transcript search reached 0.7833 accuracy with 12 stale/history errors; flat retrieval reached 0.7333 accuracy with 16 missing doctrine errors; layered memory reached 1.0000 accuracy with no errors.

## Boundaries and scale limits

Synthetic proxy only; no real LLM agent, embedding retrieval, noisy extractor, long-horizon transcript, or production-scale workload was tested.

## Claim scope

On a 12-episode deterministic synthetic repeated-task replay with structured facts, layered project-state plus doctrine memory achieved perfect exact fact recall and avoided stale-history errors seen in retrieval-only baselines.

## Why it stopped

No-paper useful signal: the local synthetic proxy supports the mechanism, but it is not direct or broad enough for publication-grade validation.

## Recommended next action

Run a bounded deepen evaluation on real or LLM-generated noisy repeated-agent transcripts with the same stale-recall metrics and a tuned vector retrieval baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Noisy transcript replay for layered memory versus tuned vector retrieval
- Success threshold: Layered memory improves exact fact accuracy by at least 10 percentage points over the best retrieval-only baseline and cuts stale/history errors by at least 50 percent without increasing missing doctrine errors.
- Stop condition: Stop if layered memory fails to beat the best retrieval-only baseline by 5 percentage points or if extraction noise dominates errors so strongly that memory strategy cannot be isolated.

## Evidence references

- Artifact root: `<local-path>/projects/layered-agent-memory-vs-retrieval-only-on-repeated-tasks-690ac53a3116`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
