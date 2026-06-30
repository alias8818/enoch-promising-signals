# End-to-End Residual-Aware Speculative Decoding with a Quantized Draft Model

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `end-to-end-residual-aware-speculative-decoding-with-a-quan-bc4132a403`
Run ID: `end-to-end-residual-aware-speculative-decoding-with-a-quan-bc4132a403-20260524T032443023833+0000`

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

- Parent run decision: Residual-Aware Speculative Decoding: Using Quantization Residuals to Improve Draft Acceptance: enoch://control-plane/projects/residual-aware-speculative-decoding-using-quantization-residuals-to-improve-draft-acceptance-156f8494ee2c/runs/residual-aware-speculative-decoding-using-quantization-residuals-to-improve-draft-acceptance-156f8494ee2c-20260524T031345599389+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/156899663d7c

## What looked useful

Residual correction consistently improved draft-target fit and exact speculative decoding efficiency. For 8-bit quantization, mean acceptance increased from 0.6263 to 0.6821 and generated tokens per target call increased from 3.2396 to 3.4609 across three seeds. For 4-bit quantization, residual correction improved metrics but absolute acceptance remained poor, rising only from 0.0022 to 0.0292.

## Boundaries and scale limits

Small prompt set, small calibration text, distilgpt2 only, quantized copy of the target rather than a distinct small draft, simple per-tensor uniform weight quantization, no production KV-cache serving benchmark, and no large-corpus robustness test.

## Claim scope

In a Tier 1 controlled direct test on distilgpt2 with exact speculative decoding, a calibrated mean logit residual improved a weight-only quantized draft proposal versus the same quantized draft without correction across three seeds. The supported claim is limited to acceptance-rate and target-call efficiency improvement in this small local setup.

## Why it stopped

No-paper closure: this is reproducible Tier 1 mechanism support, but the evidence is too small and the draft/quantization stack is too synthetic for publication readiness.

## Recommended next action

Run a bounded deepen test with a genuine smaller draft model, a production-relevant quantizer, separated calibration/evaluation text, and KV-cache decoding; stop if residual correction fails to improve generated tokens per target call by at least 5% over the quantized-draft baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual-Aware Speculative Decoding with a Real Smaller Quantized Draft
- Success threshold: Residual-corrected quantized draft improves generated tokens per target call by at least 5% and wall-clock tokens/sec by at least 3% over the uncorrected quantized draft without reducing exactness, with acceptance improvement on every seed or shard.
- Stop condition: Stop as negative if the residual correction gives under 2% generated-per-target-call improvement or any wall-clock regression after KV-cache overhead is included.

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-residual-aware-speculative-decoding-with-a-quan-bc4132a403`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
