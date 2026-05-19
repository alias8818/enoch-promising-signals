# Activation-Magnitude Residual Channel Preservation for Sub-2bit Transformer Quantization

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `activation-magnitude-residual-channel-preservation-for-sub-64eddc32c2`
Run ID: `activation-magnitude-residual-channel-preservation-for-sub-64eddc32c2-20260516T082932995773+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/86fcadeec75f

## What looked useful

Across residual fractions 0.02, 0.04, and 0.06, activation-selected residual channels recovered 30.5% to 41.1% of the FP-to-1bit NLL gap while random residual channels recovered about -4.3% to 5.2%; activation beat random by 0.297 to 0.444 recovery fraction at 1.314 to 1.958 average targeted-weight bits.

## Boundaries and scale limits

Only distilgpt2 was tested at valid sub-2bit scale; evaluation used 16,256 validation tokens, targeted transformer matrices only, no embeddings or LM head quantization, no production kernel, no complete model storage accounting, and a simple 1-bit sign quantizer rather than competitive GPTQ/AWQ baselines.

## Claim scope

Small direct distilgpt2/WikiText-2 evidence shows that activation-magnitude selected exact residual input-channel preservation improves 1-bit transformer matrix quantization under sub-2 average targeted-weight bits versus random channel preservation.

## Why it stopped

Closed as no-paper useful signal: the small direct test supports the mechanism under a sub-2bit targeted-weight budget, but absolute NLL remains far from FP and the evidence is too narrow for publication readiness.

## Recommended next action

Run a medium confirmation on GPT-2-small or OPT-125M with complete storage accounting and AWQ/GPTQ-style importance controls before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium Confirmation of Activation-Selected Residual Channels for Whole-Model Sub-2bit Quantization
- Success threshold: Activation-magnitude residual preservation must beat the strongest non-activation control by at least 0.10 of the FP-to-quantized NLL gap at a measured whole-model average below 2.0 bits, and reduce absolute NLL versus plain sub-2bit quantization on at least 100k validation tokens.
- Stop condition: Stop as negative if activation selection fails to beat the strongest control by 0.10 recovery fraction or if complete accounting pushes all effective configurations to 2.0 bits or higher.

## Evidence references

- Artifact root: `<local-path>/projects/activation-magnitude-residual-channel-preservation-for-sub-64eddc32c2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
