# 1.5-bit weights with per-block FP8 residual channel

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `1-5-bit-weights-with-per-block-fp8-residual-channel-51b38c13db9a`
Run ID: `1-5-bit-weights-with-per-block-fp8-residual-channel-51b38c13db9a-20260619T235044122377+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b77064485f94

## What looked useful

The residual channel is a real mechanism: default 16x64 geometry improved output RMSE versus ternary by about 16% on synthetic tensors and 11% on selected distilgpt2 tensors. The same format still had 1.36x the output RMSE of a 2-bit Lloyd baseline on distilgpt2 and 1.55x on synthetic tensors, so the scoped idea is no-paper but informative.

## Boundaries and scale limits

No end-to-end model perplexity, training, serving throughput, packing metadata, or custom-kernel measurements were run. Model evidence is limited to 12 selected distilgpt2 2D tensors and random-activation output-error proxies.

## Claim scope

A ternary per-row-block base plus one FP8 residual column per 16x64 matrix block improves tensor reconstruction and random-activation matmul output error over ternary alone, but is not competitive with a fitted 2-bit per-block Lloyd quantizer on synthetic tensors or selected distilgpt2 weight tensors.

## Why it stopped

Proxy and real-weight matrix evidence show early falsification of competitiveness: the residual channel improves ternary but remains substantially worse than a strong 2-bit block quantizer, so this is not a full validation and not paper-ready.

## Recommended next action

Stop this scoped variant as no-paper evidence; only continue with a bounded direct test if changing the mechanism to activation-aware or learned residual-channel selection against the same 2-bit baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-aware FP8 residual-channel selection for sub-2-bit weights
- Success threshold: At block geometry with payload <= 1.75 bits/weight, calibrated residual-channel output RMSE is within 10% of 2-bit Lloyd on selected distilgpt2 matrices and still improves ternary by at least 15%.
- Stop condition: Stop if activation-aware selection remains more than 20% worse than 2-bit Lloyd output RMSE on distilgpt2 matrices or loses the ternary improvement on synthetic outlier tensors.

## Evidence references

- Artifact root: `<local-path>/projects/1-5-bit-weights-with-per-block-fp8-residual-channel-51b38c13db9a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
