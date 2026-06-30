# Residual-Protected Sparse Memory on Noisy Tool Traces

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `residual-protected-sparse-memory-on-noisy-tool-traces-0d62b39643`
Run ID: `residual-protected-sparse-memory-on-noisy-tool-traces-0d62b39643-20260522T102834634684+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real Tool-Loop Task Test for Sparse Residual Agent Memory: enoch://control-plane/projects/real-tool-loop-task-test-for-sparse-residual-agent-memory-6eca7c53d4/runs/real-tool-loop-task-test-for-sparse-residual-agent-memory-6eca7c53d4-20260522T080904558414+0000
- Parent run decision: LLM-Driven Sparse Residual Memory on Noisy Tool-Loop Tasks: enoch://control-plane/projects/llm-driven-sparse-residual-memory-on-noisy-tool-loop-tasks-ec6be77e46/runs/llm-driven-sparse-residual-memory-on-noisy-tool-loop-tasks-ec6be77e46-20260522T092514426449+0000

## What looked useful

Across 480 limited-capacity conditions, residual protection reduced RMSE versus sparse EMA by 9.8%, 15.3%, and 18.6% at 5%, 15%, and 30% outlier rates, respectively, and beat sparse EMA on every outlier-positive seed. No-outlier conditions were neutral to slightly negative, and recency won some high-outlier low-drift limited-capacity conditions. With full key capacity, residual protection reduced RMSE versus sparse EMA by 30.7% overall and 36.7%-44.3% on outlier-positive groups.

## Boundaries and scale limits

Synthetic traces only; no real LLM agent traces, learned embeddings, downstream task success, end-to-end model training, or production retrieval stack. Limited-capacity sparse memory with 96 slots for 256 keys remains mixed against a recency baseline in high-outlier low-drift conditions.

## Claim scope

In a deterministic synthetic noisy tool-trace benchmark, residual-protected keyed sparse-memory updates reduce latent-state reconstruction RMSE versus unprotected sparse EMA when outlier tool observations are present, especially when the queried key remains resident.

## Why it stopped

Bounded validation supports the anti-corruption update mechanism but falsifies a broad paper-positive claim because limited sparse capacity creates mixed results against a real recency baseline.

## Recommended next action

Stop as no-paper useful signal; run a bounded deepen follow-up that adds eviction-aware sparse memory and requires residual protection to beat both sparse EMA and recency under limited capacity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Eviction-Aware Residual-Protected Sparse Memory Under Limited Capacity
- Success threshold: At limited capacity, the eviction-aware residual variant must reduce RMSE by at least 15% versus sparse_ema on every outlier-positive condition group and must not have negative mean RMSE reduction versus recency in any outlier-positive condition group.
- Stop condition: Stop negative if improvements over sparse_ema come only from full-capacity/resident-key settings or if any high-outlier limited-capacity group remains worse than recency.

## Evidence references

- Artifact root: `<local-path>/projects/residual-protected-sparse-memory-on-noisy-tool-traces-0d62b39643`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
