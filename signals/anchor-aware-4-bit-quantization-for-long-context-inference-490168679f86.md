# Anchor-Aware 4-bit Quantization for Long-Context Inference

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchor-aware-4-bit-quantization-for-long-context-inference-490168679f86`
Run ID: `anchor-aware-4-bit-quantization-for-long-context-inference-490168679f86-20260619T161332203264+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3b455a7205b0

## What looked useful

Anchor preservation produced large attention-error reductions while random anchors at the same budgets produced almost no improvement, indicating that token choice matters. Attention-mass oracle anchors slightly outperformed first-token anchors, especially at larger budgets, suggesting useful anchors can extend beyond initial sink positions.

## Boundaries and scale limits

Proxy-only mechanism test on distilgpt2 within its 1024-token window; no end-to-end quantized decoding, perplexity/task evaluation, long-context model, packed int4 kernel, throughput measurement, or online non-oracle anchor predictor was validated.

## Claim scope

On real distilgpt2 attention tensors at 512 and 1024 tokens, preserving 0.5-1% anchor tokens in fp16 while 4-bit quantizing the remaining K/V vectors reduces attention-output relative L2 error by roughly 68-76% versus plain per-token 4-bit K/V quantization at about 3.9x estimated KV payload compression.

## Why it stopped

The run produced only proxy attention-error evidence, not direct long-context inference quality or serving evidence, so it cannot support a paper-positive decision.

## Recommended next action

Stop this worker as a no-paper useful signal; the next bounded test should implement end-to-end quantized-KV decoding with an online anchor selector and compare perplexity/retrieval accuracy against plain 4-bit and first-token-preserved baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end online anchor-aware 4-bit KV decoding on small long-context benchmarks
- Success threshold: At 0.5-1% anchors, online anchor-aware 4-bit KV improves quality degradation by at least 25% versus plain 4-bit and beats first-token-only preservation on at least one direct quality metric without reducing estimated KV payload compression below 3.8x.
- Stop condition: Stop if online anchors fail to outperform first-token-only preservation or random anchors on direct quality metrics at matched compression, or if selector overhead dominates any practical memory benefit.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-aware-4-bit-quantization-for-long-context-inference-490168679f86`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
