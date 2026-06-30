# Hierarchical Sliding Window with Token Merge

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `hierarchical-sliding-window-with-token-merge-33405b63da40`
Run ID: `hierarchical-sliding-window-with-token-merge-33405b63da40-20260522T141244351815+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/04fb381aed47

## What looked useful

Across 9,000 corrected medium trials, recent merge improved accuracy over sliding window by +0.1998 mean on unique-key retrieval and +0.2093 mean on repeated-key retrieval; hash merge improved by +0.1767 and +0.1918 respectively. Query-aware summaries reached 1.0 accuracy, showing a mechanism upper bound, but query-agnostic merge stayed lossy.

## Boundaries and scale limits

No neural model was trained; no natural-language benchmark, parameter-matched Transformer baseline, gradient behavior, GPU throughput, or production serving behavior was tested. Results are limited to synthetic associative recall with deterministic summary policies.

## Claim scope

On a deterministic synthetic key-value retrieval proxy, hierarchical bounded summaries with recency or hash token-merge policies improved long-range retrieval accuracy over a fixed sliding window across all tested sequence lengths and capacities, with mean token-access cost about 23-25% of full scan.

## Why it stopped

Closed as no-paper useful signal: the evidence is a synthetic algorithmic proxy, not direct trained-model validation.

## Recommended next action

Run a bounded trained-model follow-up with a tiny parameter-matched local-attention baseline versus hierarchical token-merge attention on the same associative-recall task before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny Trained Benchmark for Hierarchical Sliding Window Token Merge
- Success threshold: At least +10 percentage-point validation accuracy over local sliding-window attention on held-out long-range recall at matched parameter count and no more than 60% of full-attention token-access cost.
- Stop condition: Stop if the hierarchical model fails to beat local attention by 5 percentage points after a calibrated small training budget, or if implementation requires unbounded scale beyond the local worker.

## Evidence references

- Artifact root: `<local-path>/projects/hierarchical-sliding-window-with-token-merge-33405b63da40`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
