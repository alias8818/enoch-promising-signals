# Efficient Hybrid Low-Rank AdamW Update for Small LM Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `efficient-hybrid-low-rank-adamw-update-for-small-lm-traini-c8a1d93ce9`
Run ID: `efficient-hybrid-low-rank-adamw-update-for-small-lm-traini-c8a1d93ce9-20260518T095607245440+0000`

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

- Internal Enoch project: Efficient Hybrid Low-Rank AdamW Update for Small LM Training: internal_generated:efficient-hybrid-low-rank-adamw-update-for-small-lm-traini-c8a1d93ce9

## What looked useful

Fixed-seed rank ablations show a monotonic rank-quality tradeoff: rank 64 used 5.84 MB estimated optimizer state versus AdamW's 14.77 MB, but had mean 600-step validation loss 2.2828 versus AdamW 2.1843. A 2,000-step seed-11 check preserved the gap: rank 64 reached 1.8077 validation loss versus AdamW 1.6733.

## Boundaries and scale limits

Validated only on a small byte-level transformer and WikiText-2. Optimizer memory is estimated from state element counts, not isolated peak CUDA allocation. Runtime uses an unfused Python optimizer with periodic SVD and should not be read as a custom-kernel upper bound. GPT-2-small-class BPE training and larger/longer corpus runs remain untested.

## Claim scope

On a 1.85M-parameter byte-level WikiText-2 causal LM, hybrid low-rank projected AdamW state trains stably and reduces estimated optimizer-state memory, but does not match AdamW validation loss or throughput at ranks 8-64.

## Why it stopped

Medium local evidence supports stable low-rank state compression but falsifies the stronger efficient-AdamW-replacement claim for this small LM setting: quality lags AdamW and the naive implementation is slower.

## Recommended next action

Stop this paper path; only pursue a bounded deepen follow-up that changes the optimizer mechanism with periodic dense correction or adaptive rank allocation and must beat rank-64 loss-memory tradeoff locally.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive or periodically corrected low-rank AdamW for small LM training
- Success threshold: At 2,000 steps, best variant must reduce the AdamW-vs-rank64 validation-loss gap by at least 50% while keeping estimated optimizer-state memory under 50% of AdamW and not losing more than 25% tokens/sec versus the current rank-64 implementation.
- Stop condition: Stop if the best corrected/adaptive variant remains within 10% of rank-64 validation loss or requires at least 50% AdamW state memory to improve.

## Evidence references

- Artifact root: `<local-path>/projects/efficient-hybrid-low-rank-adamw-update-for-small-lm-traini-c8a1d93ce9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
