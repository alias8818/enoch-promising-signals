# Quantized KV anchors with residual corrections

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantized-kv-anchors-with-residual-corrections-b3ade2a62bbb`
Run ID: `quantized-kv-anchors-with-residual-corrections-b3ade2a62bbb-20260528T231140961364+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/862178abae9a

## What looked useful

On smooth traces at block size 16, anchor_int4_resid_int3 used 3.25 nominal bits/value and achieved attention output rel-MSE 0.000421 versus 0.005614 for direct_int3 and 0.000885 for direct_int4. Across smooth blocks 8/16/32, anchor+residual beat matching direct-int baselines in all 12/12 paired seeds. IID controls showed only small gains that shrink with block size, bounding the mechanism to locally correlated KV structure.

## Boundaries and scale limits

Proxy-only CPU experiment: 12 seeds, sequence length 512, 4 heads, dim 64, block sizes 8/16/32, smooth and IID synthetic regimes. No real transformer K/V activations, no perplexity, no serving latency, and nominal bit accounting excludes scale/metadata overhead.

## Claim scope

Synthetic NumPy attention traces show that int4 block anchors plus low-bit residual corrections substantially reduce attention-output error versus direct low-bit quantization when K/V vectors are locally correlated; the effect is weak to marginal on IID traces.

## Why it stopped

Closed as a proxy useful signal rather than a paper result: synthetic attention evidence supports the mechanism under local correlation but does not validate real-model KV cache quality or serving performance.

## Recommended next action

Run the same codec family on cached K/V activations from a GPT-2-small-class model on real text, including scale/metadata memory accounting and perplexity or next-token loss deltas.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real GPT-2 KV Activation Test for Anchor-Residual Quantization
- Success threshold: At an effective budget no greater than direct int4, an anchor-residual codec must reduce attention-output rel-MSE by at least 2x versus the best direct baseline and keep next-token loss delta within 5 percent of direct int4 on real text activations.
- Stop condition: Stop if real K/V activations do not show local block correlation or if anchor-residual codecs fail to beat direct baselines after full scale/metadata memory accounting.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-kv-anchors-with-residual-corrections-b3ade2a62bbb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
