# Real-trace AgentMemQuant retrieval validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-trace-agentmemquant-retrieval-validation-47c8be6334`
Run ID: `real-trace-agentmemquant-retrieval-validation-47c8be6334-20260526T185431354120+0000`

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

- Parent run decision: AgentMemQuant: enoch://control-plane/projects/agentmemquant-fec115a9a6d2/runs/agentmemquant-fec115a9a6d2-20260525T161951437822+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/27448e2fdc40

## What looked useful

Top-16 sketches averaged 0.803 Recall@5, 0.967 relative Recall@5 versus full BM25, and 15.5x compression across three real-trace resamples. Top-8 sketches averaged only 0.844 relative Recall@5 despite 30.5x compression, giving a clear lower-bound failure mode.

## Boundaries and scale limits

Small local Tier 1 retrieval-only test: 1200 chunks, 300 deterministic queries per seed, three seeds. No human-labeled semantic questions, no downstream answer generation, no production memory serving, and no external benchmark comparison.

## Claim scope

On local real Codex/Enoch trace chunks with deterministic held-out retrieval labels, AgentMemQuant-style hashed top-token sketches at top-16/top-64 retained more than 95% of full BM25 Recall@5 while reducing storage by more than 4x.

## Why it stopped

Tier 1 direct retrieval evidence supports the compression/retrieval mechanism but is not full validation or publication-grade evidence because query labels are deterministic token-derived labels and downstream memory utilization was not tested.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded deepen follow-up with natural-language real-trace QA labels and BM25/dense/hybrid retrieval baselines before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-language real-trace AgentMemQuant QA retrieval validation
- Success threshold: Across at least 500 labeled natural-language queries, AgentMemQuant must achieve >=90% of the best non-quantized baseline Recall@5, >=4x storage reduction, and no worse than 5 percentage points absolute answer-support loss.
- Stop condition: Stop early if AgentMemQuant falls below 85% relative Recall@5 on the first 150 labeled natural-language queries or if label ambiguity prevents reliable source-memory scoring.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-agentmemquant-retrieval-validation-47c8be6334`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
