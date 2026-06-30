# Confidence-Gated Model Cascade for Local VRAM-Constrained Serving

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `confidence-gated-model-cascade-for-local-vram-constrained-serving-1b7c58b70437`
Run ID: `confidence-gated-model-cascade-for-local-vram-constrained-serving-1b7c58b70437-20260524T033512857502+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/d46c994fc477

## What looked useful

At threshold 0.55, cascade accuracy was 0.7409 versus 0.7485 large-only accuracy while falling back to the large model for 47.63% of requests, reducing large calls by 52.37% and expected CPU latency by 50.12% in the proxy. Hard examples were escalated more often than easy examples.

## Boundaries and scale limits

Proxy-only evidence: tiny CPU PyTorch classifiers, synthetic classification data, no real LLM prompts, no GPU serving stack, no actual VRAM residency or KV-cache measurements, and no batching/concurrency validation.

## Claim scope

In a deterministic synthetic classification proxy, a temperature-calibrated small-model confidence gate preserved near-large-model accuracy while reducing large-model invocations by about half at the best efficiency threshold within 1 percentage point of large-only accuracy.

## Why it stopped

Proxy evidence supports the mechanism but is insufficient for a paper or broad serving claim because no real LLM, prompt-quality, VRAM, or serving-stack measurements were collected.

## Recommended next action

Run a bounded direct local-serving follow-up with two real quantized local models, a labeled prompt set, calibrated confidence scores, and measured VRAM/latency under the same threshold sweep.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Local LLM Confidence-Gated Cascade
- Success threshold: At least 30% fewer large-model calls than large-only while final answer quality remains within 1 percentage point of large-only and measured p50 latency or large-model active time improves by at least 20%.
- Stop condition: Stop as unsupported if no threshold achieves both the quality bound and at least 15% large-call reduction on the held-out prompt set.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-gated-model-cascade-for-local-vram-constrained-serving-1b7c58b70437`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
