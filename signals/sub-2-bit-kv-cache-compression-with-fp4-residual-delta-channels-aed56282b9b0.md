# Sub-2-bit KV cache compression with FP4 residual delta channels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sub-2-bit-kv-cache-compression-with-fp4-residual-delta-channels-aed56282b9b0`
Run ID: `sub-2-bit-kv-cache-compression-with-fp4-residual-delta-channels-aed56282b9b0-20260628T224725793076+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/43b45edd452f

## What looked useful

The method is promising when KV has strong temporal correlation: at 1.75 bits it had attention relative MSE 0.0002 on smooth AR and 0.0099 on mixed AR with jumps, versus Lloyd 2-bit absolute at 0.0474 and 0.0679. It was only slightly better than Lloyd 2-bit on rough AR and clearly worse on IID KV, where relative MSE was 0.4032 versus 0.1335.

## Boundaries and scale limits

Synthetic CUDA tensor probe only: batch=2, heads=16, seq=1024, dim=128, five seeds, no real language model KV traces, no perplexity/task evaluation, no serving kernels, no metadata/packing overhead validation.

## Claim scope

On synthetic KV tensors with temporal coherence, a 1-bit delta base plus FP4 residual channels at 1.5-1.75 nominal bits/element can reduce reconstruction and attention-output drift versus absolute 1-bit, simple 2-bit, and a strong per-block Lloyd 2-bit absolute baseline; the mechanism fails on IID KV.

## Why it stopped

Closed as no-paper useful signal because current evidence is a synthetic proxy with a clear failure boundary, not direct real-model validation.

## Recommended next action

Run a bounded real-model GPT-2-small-class KV trace and perplexity/logit-drift study using the same codec against fair 2-bit baselines; stop if any layer class shows IID-like drift requiring frequent fallback.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model KV trace validation for sub-2-bit delta FP4 residual channels
- Success threshold: At 1.75 nominal bits/element or lower, mean perplexity/logit drift is no worse than the best 2-bit absolute baseline, at least 80% of layers do not require fallback, and decode overhead is plausibly bounded by simple fused delta-dequant kernels.
- Stop condition: Stop as unsupported if real KV traces show IID-like or jump-heavy behavior in enough layers that delta FP4 has more than 1.25x the logit/perplexity drift of 2-bit absolute baselines or needs fallback for more than 20% of layers.

## Evidence references

- Artifact root: `<local-path>/projects/sub-2-bit-kv-cache-compression-with-fp4-residual-delta-channels-aed56282b9b0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
