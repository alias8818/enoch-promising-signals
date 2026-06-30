# Agent Reliability with Quantized Memory Residuals

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `agent-reliability-with-quantized-memory-residuals-48cffd7b5409`
Run ID: `agent-reliability-with-quantized-memory-residuals-48cffd7b5409-20260529T221611511495+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/731bd7b356aa

## What looked useful

Residual codes reduced quantized top-score collisions in outlier-heavy memory. Against q4, q3+r1 improved accuracy by +0.1346, +0.0675, and +0.0411 at query noise 0.04, 0.08, and 0.12 respectively; in clean memory, q4 matched or slightly beat residual variants.

## Boundaries and scale limits

Proxy-only synthetic retrieval; 8192 keys, 128 dimensions, 8192 queries per condition, 10 seeds. No full LLM-agent, learned memory controller, real embedding corpus, latency-matched ANN index, or long-horizon task validation was run.

## Claim scope

In a synthetic clustered nearest-neighbor episodic-memory benchmark, residual-coded quantized memory improved top-1 retrieval reliability over q4 when memory keys contained sparse large-coordinate outliers that caused quantized score ties; it did not meaningfully improve over q4 in clean clustered memory.

## Why it stopped

Closed as no-paper useful signal because the evidence is a synthetic retrieval proxy, not direct full agent reliability validation.

## Recommended next action

Run a bounded direct agent-memory follow-up on real LLM/RAG episodic-memory embeddings, measuring task accuracy and quantized retrieval collision rates for q4 versus q3+r1 under matched storage and retrieval latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Embedding Agent-Memory Residual Quantization Check
- Success threshold: Residual memory improves task-level correctness or retrieval top-1 accuracy by at least 3 percentage points over q4 in an outlier-heavy real-embedding regime without more than 10% retrieval latency overhead, and reduces top-score tie/collision rate by at least 50%.
- Stop condition: Stop if real embeddings do not exhibit quantized collision/tie failures under q4, or if residual variants fail to improve retrieval/task correctness by at least 1 percentage point in the identified collision-heavy subset.

## Evidence references

- Artifact root: `<local-path>/projects/agent-reliability-with-quantized-memory-residuals-48cffd7b5409`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
