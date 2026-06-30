# INT8 Activations + Error-Feedback Residual on GPT-2-small CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int8-activations-error-feedback-residual-on-gpt-2-small-cpu-e2f9797390b9`
Run ID: `int8-activations-error-feedback-residual-on-gpt-2-small-cpu-e2f9797390b9-20260614T032641938644+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/59cbdc3df83e

## What looked useful

Plain int8 block-boundary activations raised loss by 0.063988 versus fp32; int8 with full-precision error feedback raised loss by 0.045292, recovering 0.018696 loss and 3.22 perplexity versus plain int8. However, estimated activation-boundary storage was 70.85 MB for int8+EF versus 56.62 MB fp32 and 14.23 MB plain int8.

## Boundaries and scale limits

Small fixed local corpus; inference only; Python/PyTorch hooks rather than custom int8 kernels; no training, public benchmark perplexity, long-context serving, KV-cache path, peak RSS measurement, or compressed residual implementation.

## Claim scope

On GPT-2-small CPU inference with simulated block-boundary int8 activation quantize/dequantize hooks over a fixed 842-token local corpus, a full-precision error-feedback residual reduced the loss penalty versus plain int8 activations, but did not demonstrate a practical memory-saving or speed-positive method.

## Why it stopped

No-paper closure: this direct small GPT-2-small CPU probe supports the EF compensation mechanism but falsifies the tested full-precision-residual variant as a practical activation-memory-saving method.

## Recommended next action

Run a bounded compressed-residual follow-up that keeps total activation-boundary storage below fp32 while preserving most of the EF loss recovery; otherwise stop treating full-precision EF residuals as a practical memory-saving path.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Compressed error-feedback residuals for GPT-2-small int8 activations on CPU
- Success threshold: A compressed EF variant recovers at least 50% of the full-precision EF loss improvement over plain int8 while total activation-boundary storage remains below fp32 and throughput is no worse than 20% below plain int8 in the same harness.
- Stop condition: Stop if compressed residual variants recover less than 25% of the full-precision EF loss improvement or require storage at or above fp32.

## Evidence references

- Artifact root: `<local-path>/projects/int8-activations-error-feedback-residual-on-gpt-2-small-cpu-e2f9797390b9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
