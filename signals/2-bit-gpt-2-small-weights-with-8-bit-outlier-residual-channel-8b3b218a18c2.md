# 2-bit GPT-2-small weights with 8-bit outlier residual channel

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `2-bit-gpt-2-small-weights-with-8-bit-outlier-residual-channel-8b3b218a18c2`
Run ID: `2-bit-gpt-2-small-weights-with-8-bit-outlier-residual-channel-8b3b218a18c2-20260620T112757092789+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a257891428a7

## What looked useful

Residual corrections reduced weight reconstruction MSE by up to 41.46%, but the best candidate still had loss 17.345589 versus baseline 5.880731, perplexity ratio 95306.91, and 0.0 top-1 logit agreement. Simple 2-bit GPT-2-small weights with this 8-bit residual channel are not behaviorally viable in the bounded probe.

## Boundaries and scale limits

Evaluated on 8 fixed short text samples at 64-token cap on CPU; no standard LM benchmark, quantization-aware fine-tuning, GPTQ/AWQ-style rounding, packed kernel throughput test, or large-corpus validation.

## Claim scope

Bounded post-training probe of GPT-2-small with 2-bit affine quantization on non-embedding 2D weights plus sparse-entry or outlier-column 8-bit residual corrections up to 10% residual weights.

## Why it stopped

Proxy/early falsification: direct small-batch GPT-2-small behavior failed by a large margin despite residual reconstruction gains; this is not full validation and could be overturned only by stronger residual-aware or layer-sensitive quantization on standard benchmarks.

## Recommended next action

Stop this run as a no-paper bounded negative; if continuing, run a layer-sensitivity follow-up that keeps only the most damaging GPT-2-small tensors above 2 bits and measures whether residual-aware quantization can recover within 10% perplexity on a standard validation slice.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Layer sensitivity for 2-bit GPT-2-small with residual-aware recovery
- Success threshold: Recover to perplexity ratio <= 1.10 and top-1 logit agreement >= 0.90 on the selected validation slice while keeping effective non-embedding weight storage below 4 bits per weight.
- Stop condition: Stop if restoring or residual-quantizing the top 20% most sensitive non-embedding weights still leaves perplexity ratio > 1.25 or top-1 agreement < 0.80.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-gpt-2-small-weights-with-8-bit-outlier-residual-channel-8b3b218a18c2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
