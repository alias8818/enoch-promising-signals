# Real-int4 GPT-2 small residual adapter versus matched adapter baselines

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-int4-gpt-2-small-residual-adapter-versus-matched-adap-dbf14811b5`
Run ID: `real-int4-gpt-2-small-residual-adapter-versus-matched-adap-dbf14811b5-20260605T074014319953+0000`

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

- Parent run decision: GPT-2-small-class 4-bit proxy residual adapter validation: enoch://control-plane/projects/gpt-2-small-class-4-bit-proxy-residual-adapter-validation-6695d7121b/runs/gpt-2-small-class-4-bit-proxy-residual-adapter-validation-6695d7121b-20260605T035001305558+0000
- Parent run decision: 4-bit Proxy Residual Training: enoch://control-plane/projects/4-bit-proxy-residual-training-67024687d419/runs/4-bit-proxy-residual-training-67024687d419-20260604T223601041484+0000

## What looked useful

SVD residual adapters achieved mean test nll 5.6809 +/- 0.0039 across seeds 0/1/2, versus 6.1362 +/- 0.0128 for the matched trainable random adapter and 8.8115 for int4 no-adapter/zero-zero controls. Full-precision GPT-2 reference on the same bounded test tokens was much better at nll 4.1576, so this supports a compensation mechanism but not full recovery.

## Boundaries and scale limits

Only GPT-2 small and WikiText-2 were tested; bounded grid evaluated the first 8192 validation/test tokens and trained adapters for 75 steps. The int4 path uses real signed int4 values stored in int8 tensors with dequantized matmul, not packed int4 kernels. No convergence run, rank sweep, group-size sweep, full-corpus eval, or cross-dataset robustness was completed.

## Claim scope

On GPT-2 small with frozen signed-int4 transformer projections, WikiText-2 bounded evaluation, rank-8 low-rank adapters, and 75 adapter-only training steps, SVD initialization from the quantization residual beats matched trainable random-A/zero-B adapters and no-adapter controls on next-token nll.

## Why it stopped

No-paper closure: bounded fixed-seed evidence supports the residual-initialization mechanism versus matched baselines, but the run is short, single-model/single-dataset, and still far from the full-precision GPT-2 reference.

## Recommended next action

Run a bounded deepen study with full WikiText-2 validation/test evaluation, 500-1000 adapter steps, and rank/group-size ablations before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Full WikiText-2 GPT-2 small int4 residual adapter rank and training-depth confirmation
- Success threshold: SVD residual adapter improves full-test nll by at least 0.15 over the matched random adapter in at least two ranks, with non-overlapping or clearly separated seed distributions, while closing at least 25% of the int4-to-fp32 nll gap.
- Stop condition: Stop if the SVD advantage falls below 0.05 nll after 500 steps on full validation, if matched random catches up within seed noise, or if the residual adapter fails to close at least 10% of the int4-to-fp32 gap.

## Evidence references

- Artifact root: `<local-path>/projects/real-int4-gpt-2-small-residual-adapter-versus-matched-adap-dbf14811b5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
