# Quantized-Shadow Self-Speculation: INT8 Draft from FP16 Target

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantized-shadow-self-speculation-int8-draft-from-fp16-target-62c30119109f`
Run ID: `quantized-shadow-self-speculation-int8-draft-from-fp16-target-62c30119109f-20260525T040918278136+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/6964266ffb6c

## What looked useful

Across 96 synthetic scenarios, 8-bit proxy drafts had mean acceptance mass 0.9759, worst scenario mean 0.9207, and mean top-1 match 0.9651. With gamma 4 and target verify cost 1.25x, all INT8 scenarios modeled speedup above 1.0x for draft costs 0.20, 0.35, and 0.50 of a target step.

## Boundaries and scale limits

No real transformer weights, FP16 target kernels, INT8 kernels, KV cache behavior, batching effects, or end-to-end tokens/s were tested. Vocab was 2048, contexts were synthetic, and the worker had CPU only with no PyTorch/Transformers stack.

## Claim scope

A standard-library synthetic distribution probe shows that INT8-like quantized draft distributions can retain high speculative acceptance against FP16-like target distributions under output-logit quantization and added logit-noise proxies.

## Why it stopped

Proxy mechanism supported, but full viability depends on real model quantization and serving costs that were not directly measured here.

## Recommended next action

Stop this worker run as proxy-only useful signal; next run should implement a real tiny or GPT-2-small-class FP16/BF16 target plus INT8 shadow speculative decoder and measure acceptance, wall-clock tokens/s, cache overhead, and quality against non-speculative decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny-model end-to-end INT8-shadow speculative decoding benchmark
- Success threshold: At least 1.20x wall-clock tokens/s improvement over non-speculative decoding with acceptance mass or empirical acceptance at least 0.90 for gamma 4, without quality regression under target-correct speculative sampling.
- Stop condition: Stop as negative if empirical gamma-4 acceptance is below 0.85 or measured draft plus verification cost removes speedup on the small real model.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-shadow-self-speculation-int8-draft-from-fp16-target-62c30119109f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
