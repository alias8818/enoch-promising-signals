# Realistic transcript doctrine-memory retrieval benchmark

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `realistic-transcript-doctrine-memory-retrieval-benchmark-da0f8152d0`
Run ID: `realistic-transcript-doctrine-memory-retrieval-benchmark-da0f8152d0-20260620T090252151751+0000`

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

- Parent run decision: Operator-Doctrine Memory vs Full-Transcript Search: enoch://control-plane/projects/operator-doctrine-memory-vs-full-transcript-search-66668792a2df/runs/operator-doctrine-memory-vs-full-transcript-search-66668792a2df-20260620T084231367351+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d42d75976a94

## What looked useful

Layering doctrine and episodic memories with freshness/staleness cues achieved recall@3 1.000, hit@1 1.000, MRR 1.000, term coverage 1.000, and contradiction rate 0.000 versus flat retrieval recall@3 0.917 and contradiction rate 0.500.

## Boundaries and scale limits

Small synthetic/direct controlled corpus only; no real private operator transcripts, no embedding retrieval, no LLM answer-generation evaluation, and no large-corpus persistence or latency validation.

## Claim scope

On a 12-task controlled replay benchmark with noisy transcripts, stale doctrine/fact conflicts, and deterministic lexical retrieval, layered doctrine-memory retrieval beat no-memory, transcript-search, and flat-retrieval baselines on the predeclared Tier 1 threshold.

## Why it stopped

Tier 1 controlled direct test completed and produced a useful mechanism signal, but the evidence is too small and synthetic for publication readiness.

## Recommended next action

Run a bounded deepen follow-up on at least 50 human-authored or replay-derived transcript tasks with held-out fixture generation and an embedding or LLM-rerank retrieval baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Human-authored replay confirmation for layered doctrine-memory retrieval
- Success threshold: Layered doctrine-memory retrieval improves hit@1 by at least 10 percentage points over flat retrieval, reduces contradiction rate by at least 25 percent relative, and has no statistically obvious regression in recall@3 on the held-out task set.
- Stop condition: Stop if layered retrieval fails to beat flat retrieval on hit@1 or contradiction rate, or if gains disappear after adding the embedding/LLM-rerank baseline.

## Evidence references

- Artifact root: `<local-path>/projects/realistic-transcript-doctrine-memory-retrieval-benchmark-da0f8152d0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
