# Entropy-Gated Local Model Cascades

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `entropy-gated-local-model-cascades-6a4ea0e74d7a`
Run ID: `entropy-gated-local-model-cascades-6a4ea0e74d7a-20260520T161922331865+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/964fde533235

## What looked useful

Cheap-model normalized entropy averaged 0.1568 on correct predictions and 0.4473 on mistakes. A threshold of 0.25 routed 29.98% of test examples to the fallback and reached 0.9148 accuracy versus 0.9150 for fallback-only; the best cascade point routed 36.3% and reached 0.9151.

## Boundaries and scale limits

MNIST-only, single seed, simple MLPs, no real LLM/local serving stack, no direct latency or energy measurement, and fallback strength was modest. This should not be treated as broad validation of entropy-gated local language-model cascades.

## Claim scope

On a NumPy MNIST proxy with a 25k-parameter cheap MLP and 153k-parameter fallback MLP, cheap-model predictive entropy separated mistakes from correct predictions and allowed a cascade to match fallback accuracy while routing a minority of examples to the fallback.

## Why it stopped

This run produced a useful proxy mechanism signal but not direct or broad evidence for production local model cascades, so it is no-paper closure rather than full validation.

## Recommended next action

Run a bounded deepen experiment on a harder non-toy task with real local model pairs and compare entropy gating against margin, max-confidence, random routing, and a learned router.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Entropy-gated cascades on a harder local model pair
- Success threshold: At one operating point, cascade quality is within 0.5 percentage points or an equivalent task metric margin of fallback-only while reducing fallback calls by at least 50%, and entropy gating is not dominated by the baseline routers.
- Stop condition: Stop if entropy fails to separate cheap-model errors from correct predictions or if no threshold reaches within 0.5 percentage points of fallback quality while reducing fallback calls by at least 25%.

## Evidence references

- Artifact root: `<local-path>/projects/entropy-gated-local-model-cascades-6a4ea0e74d7a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
