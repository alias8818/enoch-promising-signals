# Noisy transcript replay for layered memory versus tuned vector retrieval

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `noisy-transcript-replay-for-layered-memory-versus-tuned-ve-29034cedee`
Run ID: `noisy-transcript-replay-for-layered-memory-versus-tuned-ve-29034cedee-20260628T150254299052+0000`

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

- Parent run decision: Layered agent memory vs retrieval-only on repeated tasks: enoch://control-plane/projects/layered-agent-memory-vs-retrieval-only-on-repeated-tasks-690ac53a3116/runs/layered-agent-memory-vs-retrieval-only-on-repeated-tasks-690ac53a3116-20260628T144412116905+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6038a796f7be

## What looked useful

Best tested vector recency weighting reached 0.8819 mean accuracy; layered doctrine memory reached 1.0000 mean accuracy, a +0.1181 absolute gain, by storing canonical latest facts instead of retrieving raw transcript chunks.

## Boundaries and scale limits

12 seeds, 8 projects, 24 sessions, 16 fact events per session, 0.55 noise rate; synthetic generated transcript text; layered memory used generator fact metadata rather than a real text-only extractor; no large embedding model, real transcript corpus, or long-horizon agent loop was tested.

## Claim scope

On a deterministic synthetic noisy transcript replay benchmark with schema-known fact updates, layered latest-fact memory outperformed a tuned TF-IDF vector retriever with alias normalization and recency weighting.

## Why it stopped

Closed as no-paper useful signal: the result is a synthetic proxy with oracle/schema extraction, not direct publication-grade validation.

## Recommended next action

Run a bounded text-only follow-up where both layered memory extraction and vector retrieval operate only on held-out noisy transcript text with manually checked labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Text-only noisy transcript extraction for layered memory versus tuned vector retrieval
- Success threshold: Layered memory beats the best tuned vector baseline by at least 8 absolute accuracy points while extractor-induced errors remain below 5 percent of queries.
- Stop condition: Stop if tuned vector retrieval is within 3 absolute accuracy points of layered memory after tuning, or if extraction errors exceed 10 percent and dominate the layered failures.

## Evidence references

- Artifact root: `<local-path>/projects/noisy-transcript-replay-for-layered-memory-versus-tuned-ve-29034cedee`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
