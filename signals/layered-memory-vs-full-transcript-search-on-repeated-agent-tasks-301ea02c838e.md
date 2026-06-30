# Layered Memory vs Full-Transcript Search on Repeated Agent Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layered-memory-vs-full-transcript-search-on-repeated-agent-tasks-301ea02c838e`
Run ID: `layered-memory-vs-full-transcript-search-on-repeated-agent-tasks-301ea02c838e-20260628T064639174289+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b49dbf04196f

## What looked useful

Layered memory is promising as a context-reduction mechanism for repeated tasks, but its correctness depends on reliable consolidation. Simulated dropped updates reduced layered accuracy from 100% to 99.2% at 1% drops and 95.0% at 5% drops, while full transcript retained recoverability at much higher scan cost.

## Boundaries and scale limits

The benchmark isolates retrieval only. It does not test real agent task completion, LLM memory extraction, embedding search, human-authored transcripts, production token cost, or robustness on real repositories. The largest run used 6,000 synthetic episodes and 12,039,568 transcript characters.

## Claim scope

In a deterministic synthetic repeated-agent-task retrieval benchmark, layered current-state memory matched a strong full-transcript filtered-latest baseline at 100% accuracy while reducing per-query scanned context from megabytes to hundreds of characters when memory consolidation preserved relevant facts.

## Why it stopped

Synthetic retrieval evidence supports the mechanism but is not direct agent evidence and is not sufficient for a paper.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded deepen follow-up using real or replayed agent transcripts plus an actual memory writer and measure task success, token cost, latency, stale errors, and recovery behavior.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay Real Repeated Agent Tasks with Actual Layered Memory Extraction
- Success threshold: At least 98% layered answer accuracy, at least 10x reduction in retrieved context versus full-transcript filtered search, and stale-error rate no more than 1 percentage point worse than the full-transcript baseline on the replay corpus.
- Stop condition: Stop if the memory writer cannot reach 95% extraction recall on a validation subset or if layered retrieval fails to achieve a 5x context reduction at comparable accuracy.

## Evidence references

- Artifact root: `<local-path>/projects/layered-memory-vs-full-transcript-search-on-repeated-agent-tasks-301ea02c838e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
