# Confidence-gated local cascade router

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `confidence-gated-local-cascade-router-51e17ed3c919`
Run ID: `confidence-gated-local-cascade-router-51e17ed3c919-20260525T113531514796+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/625d0a40f048
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ba2a2599325c

## What looked useful

Calibrated SGD confidence routed about 93% of in-distribution cases locally with mean 0.89 percentage-point expert accuracy drop and +2.13 points over random routing, but under noisy shift it missed the 1-point expert-drop target in 10/10 seeds despite still beating random routing.

## Boundaries and scale limits

Small CPU-only classifier proxy with 1797 digit samples; not an LLM router, not production latency/cost, and not semantic OOD traffic.

## Claim scope

On a sklearn digits proxy, calibrated local confidence can reduce expert calls and beat random same-budget routing in distribution, but does not reliably preserve expert accuracy under synthetic input shift.

## Why it stopped

Proxy/mid-level falsification: confidence routing has useful signal, but the broad quality-preservation claim fails under shifted inputs and is not direct LLM evidence.

## Recommended next action

Stop paper path for this proxy result; run a bounded deepen follow-up on a real local LLM cascade with OOD detection or conservative calibration before making broader claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Shift-aware confidence gating for a real local LLM cascade
- Success threshold: Across all tested task families, OOD/verifier-augmented routing is within 1 percentage point of expert accuracy, beats random same-budget routing by at least 2 points, and routes at least 50% of in-distribution traffic locally.
- Stop condition: Stop if confidence-only and OOD/verifier-augmented gates both miss the 1-point expert-drop target on any shifted suite or require more than 75% expert calls to pass.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-gated-local-cascade-router-51e17ed3c919`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
