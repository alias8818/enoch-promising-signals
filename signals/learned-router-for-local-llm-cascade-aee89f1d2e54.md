# Learned Router for Local LLM Cascade

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `learned-router-for-local-llm-cascade-aee89f1d2e54`
Run ID: `learned-router-for-local-llm-cascade-aee89f1d2e54-20260522T011804423331+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/d176ef2f214d

## What looked useful

Learned routing features beyond max confidence produced consistent small gains over confidence thresholding in a reproducible local cascade proxy: router AUC for weak-model correctness averaged 0.826 versus 0.771 for max probability, and policy accuracy lift was positive at every tested escalation rate in the main run.

## Boundaries and scale limits

This run used classical text classifiers, three random seeds, 4000 held-out test examples per seed, and a simplified cost model. It did not run local LLM inference, generation scoring, real token latency measurements, batching, or multi-model serving.

## Claim scope

In a bounded 20 Newsgroups text-classification cascade proxy, a learned router trained on held-out calibration examples predicts weak-model correctness better than max probability and improves held-out cascade accuracy by 0.6 to 1.9 percentage points at matched 10 to 60 percent escalation rates.

## Why it stopped

Closed as no-paper useful signal because the evidence supports the routing mechanism only in a proxy text-classification setting, not in direct local LLM cascade serving.

## Recommended next action

Run a bounded direct local-LLM cascade follow-up on a small QA/instruction benchmark with two actual local models, correctness labels, measured latency/token cost, and the same learned-router versus confidence-threshold comparison.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Local-LLM Learned Router Cascade Benchmark
- Success threshold: Across at least three seeds or bootstrap splits, learned routing improves task accuracy by at least 1 percentage point at matched cost over the best confidence-threshold baseline without increasing normalized latency/token cost.
- Stop condition: Stop if learned routing fails to beat the confidence-threshold baseline at matched cost on two benchmark/model-pair configurations or if router overhead erases the measured cascade cost advantage.

## Evidence references

- Artifact root: `<local-path>/projects/learned-router-for-local-llm-cascade-aee89f1d2e54`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
