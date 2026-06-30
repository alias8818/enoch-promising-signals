# AgentMemQuant

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `agentmemquant-fec115a9a6d2`
Run ID: `agentmemquant-fec115a9a6d2-20260525T161951437822+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/27448e2fdc40

## What looked useful

Across five medium seeds, int8 matched fp32 Recall@1/Recall@5 within noise at 3.96x compression and retained 0.978 mean top-10 Jaccard. Int4 achieved 7.84x compression with small Recall@1 loss but only 0.717 top-10 Jaccard. Binary achieved 32x compression but large recall loss.

## Boundaries and scale limits

Tested only synthetic normalized vectors up to 10,000 memories, 2,000 queries, and 384 dimensions on CPU NumPy. Did not test real LLM/agent embeddings, ANN indexes, write/update/delete dynamics, reranking, or end-to-end agent task success.

## Claim scope

Synthetic clustered vector-memory benchmark shows per-vector symmetric int8 memory-key quantization preserves nearest-neighbor recall while reducing key storage by about 4x; int4 is recall-usable but rank-drifting; binary sign keys are not viable in this setup.

## Why it stopped

Closed as no-paper useful signal because the positive mechanism evidence is synthetic/proxy-only rather than direct agent-memory validation.

## Recommended next action

Run a bounded deepen follow-up on real agent-memory embedding traces with fp32, int8, int4, and binary key stores, equal retrieval budgets, and downstream task or answer-quality metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace AgentMemQuant retrieval validation
- Success threshold: int8 within 1 percentage point of fp32 retrieval/task success at >=3.5x key-storage reduction; int4 only accepted if reranked downstream success is within 2 percentage points at >=7x key-storage reduction; binary rejected unless recall loss is under 5 percentage points.
- Stop condition: Stop if int8 loses more than 1 percentage point task/retrieval success versus fp32 on real traces or if real-trace metrics show synthetic rank preservation does not transfer.

## Evidence references

- Artifact root: `<local-path>/projects/agentmemquant-fec115a9a6d2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
