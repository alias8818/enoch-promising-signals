# End-to-end Pythia-1B activation-aware int4 perplexity and GB10 packed-kernel validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `end-to-end-pythia-1b-activation-aware-int4-perplexity-and-6e5302189a`
Run ID: `end-to-end-pythia-1b-activation-aware-int4-perplexity-and-6e5302189a-20260611T021851806317+0000`

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

- Parent run decision: Activation-aware 4-bit weight quantization for 1-3B models on GB10: enoch://control-plane/projects/activation-aware-4-bit-weight-quantization-for-1-3b-models-on-gb10-e58ca6a3faf3/runs/activation-aware-4-bit-weight-quantization-for-1-3b-models-on-gb10-e58ca6a3faf3-20260611T015139381568+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d5a821022275

## What looked useful

Activation-aware clipping reduced Pythia-1B int4 loss degradation from 0.128977 to 0.082898 versus fp16 on the same small WikiText-2 slice, and the GB10 packed int4 kernel showed correct standalone execution with 2.19x speedup over a dequantized PyTorch reference at the tested shape.

## Boundaries and scale limits

Only 1,024 calibration tokens and 1,016 evaluated next-token predictions were used. Only one model, one dataset slice, one group size, and one kernel shape were tested. The Pythia quality path dequantizes weights in Python/PyTorch and does not integrate the packed kernel into model inference.

## Claim scope

On a Tier 1 small direct test, EleutherAI/pythia-1b with all 65 linear layers replaced by activation-aware group-size-128 int4 weight-only modules increased WikiText-2 small-slice perplexity from 17.949 to 19.500 on 1,016 next-token predictions, improving over a matched naive int4 control at 20.420 perplexity. A standalone packed signed-int4 Triton matmul on GB10 matched a dequantized PyTorch reference within fp16 tolerance and ran 2.19x faster at M=128,N=512,K=1024.

## Why it stopped

Tier 1 direct validation produced useful mechanism support, but the run remains too small and the packed kernel is not integrated into model inference, so it is no-paper evidence rather than paper-positive validation.

## Recommended next action

Run a bounded medium confirmation that evaluates at least 50k WikiText-2 or WikiText-103 validation tokens and integrates the packed int4 kernel into the Pythia linear forward path for end-to-end correctness and latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium Pythia-1B activation-aware int4 validation with packed-kernel model integration
- Success threshold: Activation-aware int4 loss delta <= 0.15 versus fp16 and at least 0.03 loss better than naive int4 on >=50k tokens, with packed-kernel model logits close to the dequantized int4 path and >=1.3x linear-layer throughput improvement.
- Stop condition: Stop if activation-aware int4 loss delta exceeds 0.25 on the first 10k-token checkpoint, if it does not beat naive int4 by at least 0.01 loss, or if packed-kernel integration fails correctness tolerance on representative Pythia linear shapes.

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-pythia-1b-activation-aware-int4-perplexity-and-6e5302189a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
