# End-to-end GPT-2-small perplexity test for residual-channel ternary quantization

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `end-to-end-gpt-2-small-perplexity-test-for-residual-channe-7a9183ad70`
Run ID: `end-to-end-gpt-2-small-perplexity-test-for-residual-channe-7a9183ad70-20260523T192102197622+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Extreme 1.5-bit Quant with Principled Residual Channels: enoch://control-plane/projects/extreme-1-5-bit-quant-with-principled-residual-channels-b41be30e8524/runs/extreme-1-5-bit-quant-with-principled-residual-channels-b41be30e8524-20260523T191343043839+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/00855c71463b

## What looked useful

Baseline GPT-2-small PPL was 32.899. Residual projection ternary quantization at the default threshold factor 0.7 produced PPL 4680.931 (+14128.24%). A threshold sweep from 0.0 to 1.0 remained far above threshold; the best tested residual result was PPL 1530.446 (+4551.97%) at threshold factor 1.0.

## Boundaries and scale limits

This was a Tier 1 controlled small direct test, not full-corpus evaluation, quantization-aware training, recovery finetuning, packed-kernel benchmarking, or larger-model validation.

## Claim scope

Naive post-training per-output-channel ternary quantization of GPT-2-small residual projection weights does not preserve perplexity on 128 WikiText-2 validation windows; all tested thresholds exceeded the pre-declared >10% early falsification threshold.

## Why it stopped

Tier 1 direct early falsification: the tested post-training residual-channel ternary quantization variants exceeded the >10% perplexity degradation threshold by orders of magnitude, though this is not a full validation against trained or calibrated ternary methods.

## Recommended next action

Stop this post-training ternary residual projection line; only pursue a bounded follow-up if it tests quantization-aware training or activation-aware calibration against the same GPT-2-small perplexity threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small QAT recovery test for residual-channel ternary projections
- Success threshold: Residual projection ternary GPT-2-small PPL degradation <=10% after bounded QAT/calibration on at least the same 128 WikiText-2 validation windows; stop early if degradation remains >25% after the planned recovery budget.
- Stop condition: Stop if recovery finetuning/calibration cannot bring PPL degradation below 25% within the bounded local budget, or if the method requires scale-only resources beyond this deployment.

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-gpt-2-small-perplexity-test-for-residual-channe-7a9183ad70`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
