# Prompt-feature learned router for CPU cascade

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `prompt-feature-learned-router-for-cpu-cascade-323fb9981183`
Run ID: `prompt-feature-learned-router-for-cpu-cascade-323fb9981183-20260611T094811831027+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7c9d6f5d0952

## What looked useful

Across six confirmation-scale seeds, the learned router averaged 95.09% held-out accuracy at cost 5.8125 versus 8.0 for always-expert and 6.264 for length-threshold routing; on shifted prompts it averaged 95.03% accuracy at cost 6.5771 versus 8.0 always-expert and 7.1231 length-threshold.

## Boundaries and scale limits

Synthetic prompts only; simulated cheap/expert behavior; fixed unit cost model instead of measured CPU model latency; no real LLM, real prompt corpus, or production distribution shift validation.

## Claim scope

On a synthetic prompt-task CPU cascade where the cheap-stage failure label is generated from prompt complexity and the expert stage has fixed higher cost, a pure prompt-feature logistic router reduced average cascade cost while meeting a 95% target accuracy on held-out and shifted generated prompts.

## Why it stopped

Closed as no-paper useful signal because the local evidence supports the routing mechanism only in a synthetic/proxy cascade, not a real CPU model cascade.

## Recommended next action

Run the same router protocol with real CPU-served small and expert models on a real prompt benchmark, measuring quality and wall-clock/token latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU model cascade validation for prompt-feature routing
- Success threshold: At a predeclared quality target within 1 percentage point of always-expert, learned routing reduces measured average CPU cost or latency by at least 15% and beats the best heuristic baseline by at least 5% on held-out prompts.
- Stop condition: Stop if the learned router cannot beat the best heuristic baseline at the target quality on two independent held-out prompt sets, or if threshold calibration fails under a shifted prompt distribution.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-feature-learned-router-for-cpu-cascade-323fb9981183`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
