# GPT-2-small calibrated residual-channel KV-cache quantization with packed-cache accounting

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gpt-2-small-calibrated-residual-channel-kv-cache-quantizat-1840760fab`
Run ID: `gpt-2-small-calibrated-residual-channel-kv-cache-quantizat-1840760fab-20260526T210641258028+0000`

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

- Parent run decision: Principled Residual Channels for KV-cache 2-bit: enoch://control-plane/projects/principled-residual-channels-for-kv-cache-2-bit-af6acae252ca/runs/principled-residual-channels-for-kv-cache-2-bit-af6acae252ca-20260526T070320984174+0000
- Parent run decision: End-to-end calibrated residual-channel KV-cache quantization: enoch://control-plane/projects/end-to-end-calibrated-residual-channel-kv-cache-quantizati-fe43b6a7d9/runs/end-to-end-calibrated-residual-channel-kv-cache-quantizati-fe43b6a7d9-20260526T144021283863+0000

## What looked useful

Calibrated 12.5% residual channels reduced mean PPL from 104.392 for plain int4 to 51.510 at the same three seeds, and beat a same-budget random residual control at 92.286 PPL, while retaining 2.901x packed-cache compression by accounting. The FP16 baseline was 35.274 PPL, so the best tested variant remained +16.236 PPL worse.

## Boundaries and scale limits

The run used GPT-2-small only, one dataset, three deterministic offsets, and dequantized caches into the unmodified attention path. Packed-cache memory was accounted by bit formula, not validated by an actual packed CUDA/Triton cache allocation or serving kernel. GPT-2-small limits the direct cache length to 1024 tokens.

## Claim scope

On GPT-2-small with WikiText-2 raw test split, 512-token calibration, three fixed evaluation offsets, and native 1024-token cached decoding, calibrated residual-channel selection improves 4-bit per-channel KV-cache quantization quality versus plain int4 and random same-budget residual channels, but does not preserve FP16-level perplexity.

## Why it stopped

Tier 2 evidence supports the calibration mechanism but not the stronger claim that aggressive packed residual-channel int4 KV-cache quantization is quality-preserving on GPT-2-small.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded action is to implement a real packed residual KV-cache path and require actual allocation reduction plus much smaller PPL degradation before reconsidering paper readiness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real packed residual KV-cache allocation for GPT-2-small
- Success threshold: Measured KV-cache allocation reduction >=2.8x versus FP16 and mean PPL delta <=5.0 versus FP16, while beating the random residual control at the same budget by at least 10 PPL.
- Stop condition: Stop if actual packed allocation cannot exceed 2.5x compression, packed-kernel logits diverge from the reference dequantized path beyond numerical tolerance, or all residual budgets with >=2.8x compression remain more than 5 PPL worse than FP16.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-calibrated-residual-channel-kv-cache-quantizat-1840760fab`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
