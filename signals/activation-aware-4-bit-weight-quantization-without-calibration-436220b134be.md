# Activation-Aware 4-Bit Weight Quantization without Calibration

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `activation-aware-4-bit-weight-quantization-without-calibration-436220b134be`
Run ID: `activation-aware-4-bit-weight-quantization-without-calibration-436220b134be-20260604T065950995516+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ede08e12091f

## What looked useful

When activation variance was independent of weights, oracle activation saliency improved expected output NMSE by 15.34% while the best weight-only proxy improved only 0.33%, falsifying the broad no-calibration claim in this proxy. When column scale was visible in weights, inverse column-norm saliency improved 21.77% to 81.08%, indicating a narrower no-calibration range-equalization effect.

## Boundaries and scale limits

No real pretrained transformer layers, LLM perplexity, downstream tasks, calibration datasets, or inference kernels were tested. Evidence is limited to 1024x1024 synthetic matrices over 64 seeds and analytic expected output NMSE.

## Claim scope

Controlled synthetic linear-layer proxy for AWQ-style 4-bit per-group weight quantization under known diagonal activation covariance. The result supports a narrow weight-range equalization heuristic but does not support general calibration-free activation awareness.

## Why it stopped

Proxy early falsification rather than full validation: synthetic evidence shows weight-only saliency cannot generally recover activation-aware gains when activation variance is not encoded in weights.

## Recommended next action

Stop this run as a proxy useful signal; the concrete next bounded test is to evaluate inverse-column-norm no-calibration scaling versus oracle activation-aware scaling on real pretrained transformer linear layers with held-out perplexity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-transformer test of no-calibration inverse-column-norm 4-bit scaling
- Success threshold: No-calibration inverse-column-norm scaling must reduce model-level quantization loss versus RTN by at least 10% on multiple layers while retaining at least half of the oracle activation-aware improvement; otherwise treat it as a narrow range-equalization trick.
- Stop condition: Stop if inverse-column-norm scaling fails to beat RTN by 5% relative model-level quantization loss on the first evaluated pretrained transformer or if layer diagnostics show no stable weight-activation correlation.

## Evidence references

- Artifact root: `<local-path>/projects/activation-aware-4-bit-weight-quantization-without-calibration-436220b134be`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
