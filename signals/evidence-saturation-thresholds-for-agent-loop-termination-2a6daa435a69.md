# Evidence Saturation Thresholds for Agent Loop Termination

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-saturation-thresholds-for-agent-loop-termination-2a6daa435a69`
Run ID: `evidence-saturation-thresholds-for-agent-loop-termination-2a6daa435a69-20260525T173101108804+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/12cd6f3c96f9

## What looked useful

Across 20k main tasks and two 10k controls, saturation_d0.030_c0.60 matched or exceeded fixed-24 accuracy while reducing mean steps from 24 to 12.51, 15.20, and 14.48 respectively. A conservative saturation setting had positive bootstrap step savings and non-negative accuracy deltas in all tested regimes. Confidence-only was cheaper in some regimes but failed in the low-redundancy control.

## Boundaries and scale limits

Proxy-only synthetic simulator: no real LLM agents, no browser/tool traces, no human-verified task labels, binary decisions only, calibrated evidence likelihoods assumed.

## Claim scope

In a controlled binary evidence-stream simulator with noisy, redundant, and distractor evidence, evidence-saturation loop termination can preserve fixed-budget decision accuracy while reducing mean loop iterations.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy-only; it supports a mechanism but not a publication-grade agent-loop termination claim.

## Recommended next action

Run a bounded real-trace replay study on labeled agent tasks comparing fixed budget, confidence-only, and evidence-saturation stopping on success rate, tool calls, tokens, and wall-clock cost.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace replay of evidence-saturation termination for labeled agent tasks
- Success threshold: Saturation reduces mean token or tool-call cost by >=20% versus fixed budget while preserving success within 1 percentage point, and beats confidence-only success by >=3 percentage points on low-redundancy traces.
- Stop condition: Stop if saturation fails to save at least 10% cost at matched success on the first 100 labeled traces or if confidence/posterior estimates cannot be reconstructed from traces.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-saturation-thresholds-for-agent-loop-termination-2a6daa435a69`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
