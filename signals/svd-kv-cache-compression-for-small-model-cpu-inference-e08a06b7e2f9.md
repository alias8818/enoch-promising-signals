# SVD KV-cache compression for small-model CPU inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `svd-kv-cache-compression-for-small-model-cpu-inference-e08a06b7e2f9`
Run ID: `svd-kv-cache-compression-for-small-model-cpu-inference-e08a06b7e2f9-20260604T032724890659+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/91e01e9fca96

## What looked useful

At seq 1024 on a favorable correlated trace, rank 16 used 26.6% of exact KV memory, had 0.0109 relative attention-output L2 error, and reduced isolated attention latency to 0.655x exact latency excluding factorization. The same approach was inaccurate on iid KV, with best iid error still 0.6385 at rank 32, and one-shot factorization cost was 29.9-116.0 ms versus sub-millisecond exact attention.

## Boundaries and scale limits

No real transformer KV traces, no perplexity/logit quality measurement, no autoregressive generation loop, no quantized kernels, and no online or incremental SVD maintenance. One-shot SVD factorization cost was measured separately and is too high for naive per-token use.

## Claim scope

Isolated NumPy CPU single-token attention over synthetic 8-head KV caches with head dimension 64 and sequence lengths 128, 512, and 1024. SVD-factor attention can reduce memory and speed the attention kernel only on favorable correlated low-rank traces at longer context; it fails on iid/high-rank traces and is not validated end-to-end.

## Why it stopped

Bounded synthetic probe produced a mixed mechanism result but not direct model evidence; it is insufficient for paper-positive closure.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should use real small-transformer KV traces and include end-to-end decode latency plus logit/perplexity drift with compression cost amortized.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real small-transformer SVD KV-cache decode probe
- Success threshold: At context length 1024, at least one rank uses <=50% exact KV memory, has <=1% relative logit or perplexity degradation, and has end-to-end decode latency no worse than exact KV after including amortized compression cost.
- Stop condition: Stop if real KV traces require rank above half the head dimension to keep quality drift within threshold, or if compression/update cost causes any memory-saving configuration to be slower than exact KV end-to-end.

## Evidence references

- Artifact root: `<local-path>/projects/svd-kv-cache-compression-for-small-model-cpu-inference-e08a06b7e2f9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
