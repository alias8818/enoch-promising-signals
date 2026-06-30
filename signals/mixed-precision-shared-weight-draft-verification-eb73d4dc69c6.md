# Mixed-Precision Shared-Weight Draft Verification

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `mixed-precision-shared-weight-draft-verification-eb73d4dc69c6`
Run ID: `mixed-precision-shared-weight-draft-verification-eb73d4dc69c6-20260523T081505946157+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/e5e61da2f1e4

## What looked useful

8-bit and 6-bit same-weight quantized drafts preserved verifier distributions with high expected acceptance (average 0.9967 and 0.9865; worst case 0.9943 and 0.9768). 4-bit was weaker but still above 0.897 one-token acceptance, while 3-bit and 2-bit had poor multi-token block survival. The naive CPU quantized path did not deliver reliable speedup.

## Boundaries and scale limits

No pretrained LLM, real text corpus, transformer stack, GPU low-precision kernel, or end-to-end speculative decoding latency was tested. CPU quantized dot products are implementation-specific and not representative of optimized accelerator kernels.

## Claim scope

Synthetic shared-weight softmax probe with vocabulary 1024, hidden dimensions 64/128/256, 192 contexts per case, and row-wise symmetric 8/6/4/3/2-bit quantized drafts compared against a full-precision verifier.

## Why it stopped

Synthetic probability-level evidence supports only a bounded mechanism signal, not a full validation; practical speed remains unproven because the CPU quantized path was usually not faster than full precision.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should use a pretrained GPT-2-small-class verifier on a held-out text corpus with optimized low-precision draft kernels and an independent draft baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained GPT-2 Shared-Weight Quantized Draft Acceptance
- Success threshold: Mean one-token acceptance >= 0.95, mean block-4 acceptance >= 0.80, no measurable quality regression on sampled continuations, and optimized draft-path latency >= 1.3x faster than verifier-path latency.
- Stop condition: Stop if 8-bit acceptance falls below 0.95 on real text, block-4 acceptance falls below 0.80, or optimized low-precision draft execution fails to beat the verifier path by at least 1.3x.

## Evidence references

- Artifact root: `<local-path>/projects/mixed-precision-shared-weight-draft-verification-eb73d4dc69c6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
