# Per-Request Quantization Routing in Local Cascades

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `per-request-quantization-routing-in-local-cascades-5b7e63315676`
Run ID: `per-request-quantization-routing-in-local-cascades-5b7e63315676-20260527T220523347327+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/3731a45b2210

## What looked useful

A small reproducible harness showed that confidence-threshold quantization routing can identify requests suitable for cheap low-bit inference and fallback on harder cases, producing near-high-tier held-out accuracy at much lower proxy cost across three synthetic difficulty levels.

## Boundaries and scale limits

Proxy-only evidence: synthetic MLP classification, fake quantized weights, dequantized float execution, normalized bit-width cost proxy, no real LLM task suite, no real int4/int8 kernels, no batching/tail-latency/KV-cache serving measurement.

## Claim scope

In a synthetic CUDA PyTorch classifier with fake weight quantization, validation-selected per-request margin routing between low-bit and 16-bit tiers preserved held-out accuracy within about 0.001 absolute of the 16-bit tier while reducing normalized bit-width cost by about 82% on average across 9 runs.

## Why it stopped

Proxy mechanism supported, but evidence is synthetic/fake-quantized and not a full validation of local LLM cascade serving.

## Recommended next action

Run a bounded direct follow-up on a small local LLM using real quantized kernels and a held-out task suite; this run should stop as no-paper proxy evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Small-LLM Quantization Routing Probe
- Success threshold: Routed cascade matches high-tier held-out quality within 1% relative or a task-appropriate predeclared tolerance while reducing measured p50 latency or memory-bandwidth proxy by at least 25% after routing overhead.
- Stop condition: Stop if real routing overhead erases the measured speed/memory benefit or if validation-selected routing misses the high-tier quality tolerance on held-out tasks.

## Evidence references

- Artifact root: `<local-path>/projects/per-request-quantization-routing-in-local-cascades-5b7e63315676`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
