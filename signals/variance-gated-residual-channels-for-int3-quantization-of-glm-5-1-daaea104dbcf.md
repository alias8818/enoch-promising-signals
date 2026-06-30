# Variance-Gated Residual Channels for INT3 Quantization of GLM-5.1

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `variance-gated-residual-channels-for-int3-quantization-of-glm-5-1-daaea104dbcf`
Run ID: `variance-gated-residual-channels-for-int3-quantization-of-glm-5-1-daaea104dbcf-20260529T143613765064+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/0f7118403712

## What looked useful

Residual correction mechanically reduced INT3 error in proportion to kept channels. On independent synthetic projections, variance selection did not beat random at 4% residual budget. On 12 real distilgpt2 projections, variance selection reduced mean NMSE by 21.18% at 1% residual channels and 30.77% at 4%, versus random at 0.78% and 3.62%.

## Boundaries and scale limits

Synthetic 4096x4096 projections and 12 distilgpt2 projection modules only; no GLM-5.1 weights, no packed INT3 kernel, no perplexity/task benchmark, no latency or memory-system validation.

## Claim scope

Bounded layer-reconstruction evidence: a variance-selected high-precision residual channel path can substantially reduce INT3 groupwise weight quantization output NMSE on small GPT-2-family projection layers, but this run does not validate GLM-5.1 or end-to-end model quality.

## Why it stopped

Closed as no-paper useful signal because evidence is proxy/small-model only and mixed; it supports a mechanism but does not validate the original GLM-5.1 INT3 quantization claim.

## Recommended next action

Run a bounded direct-evidence follow-up on a GLM-family or similarly sized public checkpoint with real calibration text, packed INT3 or faithful memory accounting, and perplexity plus latency metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GLM-family INT3 residual-channel validation with end-to-end metrics
- Success threshold: At 1-4% residual channels, variance selection beats random by at least 10% relative output-NMSE reduction and improves perplexity or task degradation versus INT3-only without exceeding the matched residual memory budget.
- Stop condition: Stop if variance selection fails to beat random on layer NMSE or fails to improve end-to-end quality at matched memory on the GLM-family checkpoint.

## Evidence references

- Artifact root: `<local-path>/projects/variance-gated-residual-channels-for-int3-quantization-of-glm-5-1-daaea104dbcf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
