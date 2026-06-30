# Transformer perplexity probe for 1-bit weights with binary residual adapters

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `transformer-perplexity-probe-for-1-bit-weights-with-binary-bc2aca93d6`
Run ID: `transformer-perplexity-probe-for-1-bit-weights-with-binary-bc2aca93d6-20260622T005858030139+0000`

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

- Parent run decision: 1-bit Weight Quantization with Binary Residual Adapters: enoch://control-plane/projects/1-bit-weight-quantization-with-binary-residual-adapters-63adb3dd6712/runs/1-bit-weight-quantization-with-binary-residual-adapters-63adb3dd6712-20260621T234458695374+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/78415dbfa451

## What looked useful

Plain 1-bit linear weights were 10.16% higher perplexity than dense. Rank-8 binary residual adapters improved only slightly over plain binary. Rank-16 adapters improved the binary result but still remained 7.43% higher perplexity than dense; rank-32 regressed.

## Boundaries and scale limits

Tested only a tiny character-level model for 80 optimizer steps on one corpus slice; embeddings, LayerNorms, and biases remained full precision; no GPT-2-small-class token-level training or packed 1-bit inference measurement was run.

## Claim scope

In a small 2-layer character-level Transformer on Tiny Shakespeare, binary residual adapters recovered part of the validation perplexity gap introduced by 1-bit linear weights, but did not match the dense baseline.

## Why it stopped

The Tier 1 direct test produced mechanism support but not enough quality recovery for publication readiness: the best tested binary-adapter setting remained 7.43% higher perplexity than dense.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next bounded action is a token-level GPT-2-small-class or parameter-matched small LM confirmation with dense, binary, and binary-adapter controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Token-level confirmation of binary residual adapters for 1-bit Transformer weights
- Success threshold: Best binary-adapter configuration closes at least 50% of the dense-vs-plain-binary validation perplexity gap while adding no more than 25% trainable adapter parameters relative to the binarized linear parameter count.
- Stop condition: Stop if binary adapters close less than 25% of the dense-vs-plain-binary perplexity gap in the first controlled token-level run or if adapter overhead removes the intended compression advantage.

## Evidence references

- Artifact root: `<local-path>/projects/transformer-perplexity-probe-for-1-bit-weights-with-binary-bc2aca93d6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
