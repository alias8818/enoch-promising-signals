# Quantized Anchor KV for Long Context Memory

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantized-anchor-kv-for-long-context-memory-bea5c7434523`
Run ID: `quantized-anchor-kv-for-long-context-memory-bea5c7434523-20260608T202235410994+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/43da9b60f994

## What looked useful

The cache representation is viable only if anchor selection reliably includes important retrieved items. At seq=16384 and 2-bit KV, 0.5% oracle target anchors improved cosine-to-target from 0.8169 to 0.9999 at 12.94% of fp16 KV memory, while 5% periodic anchors improved only to 0.8274 because target-anchor rate was 5.56%.

## Boundaries and scale limits

No learned language model, no real long-context dataset, no online anchor selector, no packed low-bit serving kernel, and no throughput validation. Memory numbers are analytical estimates for KV storage, while quality computation used dequantized tensors.

## Claim scope

Synthetic CUDA attention-retrieval probe up to sequence length 16384, fp16 baseline KV, symmetric dequantized 2/3/4/8-bit KV, and sparse fp16 anchors. Oracle target anchors preserve value fidelity at very low anchor fractions; periodic non-oracle anchors do not meaningfully improve arbitrary retrieval.

## Why it stopped

Closed as no-paper useful signal because evidence is synthetic/proxy-only and shows the key bottleneck is anchor selection, not the mixed-precision KV representation alone.

## Recommended next action

Run a bounded follow-up that tests an actual online anchor-selection rule against uniform 3-bit and 4-bit KV quantization on a small transformer long-context recall task.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Online Anchor Selection for Quantized KV Recall
- Success threshold: <=1% anchors, >=50% target-anchor coverage on the recall events, and statistically clear task-quality improvement over uniform quantized KV at matched memory across at least three seeds.
- Stop condition: Stop if non-oracle anchor coverage remains within 2x the raw anchor fraction or if matched-memory uniform 4-bit KV is equal or better on task quality and runtime.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-anchor-kv-for-long-context-memory-bea5c7434523`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
