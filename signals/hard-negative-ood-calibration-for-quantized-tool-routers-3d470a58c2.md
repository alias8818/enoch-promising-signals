# Hard-Negative OOD Calibration for Quantized Tool Routers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `hard-negative-ood-calibration-for-quantized-tool-routers-3d470a58c2`
Run ID: `hard-negative-ood-calibration-for-quantized-tool-routers-3d470a58c2-20260522T072710255512+0000`

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

- Parent run decision: Quantized Tool Router for Safer Small Agents: enoch://control-plane/projects/quantized-tool-router-for-safer-small-agents-e12bce903e45/runs/quantized-tool-router-for-safer-small-agents-e12bce903e45-20260522T012314896937+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/097ee83fc7b8

## What looked useful

Mean hard-OOD false accepts fell from 0.1211 to 0.0506 for int8 and from 0.1272 to 0.0828 for int4, with calibrated ID acceptance above 0.95. The int4 effect was weaker and one seed missed the 30% relative-reduction threshold.

## Boundaries and scale limits

Synthetic templated requests; bag-of-words linear router; uniform post-training quantization of the router head only; no production trace, transformer encoder, full LLM quantization, or independently authored hard-negative dataset.

## Claim scope

In a five-seed controlled synthetic text-router benchmark with fp32/int8/int4 linear router heads, a hard-negative post-hoc accept/reject calibrator reduced held-out hard-OOD false tool accepts at about 95% ID acceptance versus an ID-only max-softmax threshold.

## Why it stopped

Tier 1 controlled direct test completed and supports the mechanism, but the evidence is synthetic/small and not sufficient for paper readiness.

## Recommended next action

Run a bounded deepen follow-up using a transformer or embedding-based router with full int8/int4 quantization and an independently authored hard-negative evaluation set.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer-router hard-negative calibration under full int8/int4 quantization
- Success threshold: At 95% ID acceptance, int8 and int4 calibrated routers each reduce hard-OOD false accepts by at least 30% relative to ID-only thresholding, with no per-tool ID acceptance below 90%.
- Stop condition: Stop if the calibrated quantized router fails to achieve at least 15% relative hard-OOD false-accept reduction in two independent seeds or if ID acceptance drops below 90%.

## Evidence references

- Artifact root: `<local-path>/projects/hard-negative-ood-calibration-for-quantized-tool-routers-3d470a58c2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
