# Local speculative decoding INT4 draft + FP8 verifier on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `local-speculative-decoding-int4-draft-fp8-verifier-on-gb10-a83ad5bb71eb`
Run ID: `local-speculative-decoding-int4-draft-fp8-verifier-on-gb10-a83ad5bb71eb-20260628T122116525592+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1d6ea97e5fcf

## What looked useful

The local GB10 stack can execute the relevant native INT4 and FP8 primitives. The approach is shape-sensitive: INT4 draft overhead dominates at 1024 verifier width, while wider 4096 verifier proxy shapes can make FP8 verifier savings large enough for modeled speculative speedups.

## Boundaries and scale limits

This is not an end-to-end language-model serving result. The benchmark omits transformer attention, KV cache, token sampling, real logits, tokenizer overhead, and measured draft/verifier acceptance. Acceptance rates are swept assumptions, and FP8 quality is measured only as proxy-stack output drift versus BF16.

## Claim scope

On this GB10/PyTorch 2.12 stack, native TorchAO INT4 draft Linear and native PyTorch FP8 scaled verifier matmuls run successfully. A controlled shallow matmul-stack proxy shows no speedup for a 512-draft/1024-verifier shape, but shows modeled speculative speedups for a 512-draft/4096-verifier shape when assumed acceptance is at least moderate.

## Why it stopped

Proxy evidence is useful but not paper-ready: the smaller verifier proxy is negative, and the wide-verifier speedup depends on modeled acceptance rather than direct language-model acceptance and tokens/s.

## Recommended next action

Run a bounded deepen follow-up with a small real autoregressive transformer pair on GB10, measuring actual acceptance and end-to-end tokens/s for BF16 verifier-only versus INT4 draft plus FP8 verifier speculative decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Measure end-to-end INT4-draft FP8-verifier speculative decoding on a small transformer pair
- Success threshold: At least 1.25x end-to-end tokens/s improvement over BF16 verifier-only decoding on the same prompts with measured acceptance >= 0.7 and no severe output/logit drift attributable to FP8 verifier quantization.
- Stop condition: Stop if measured acceptance is below 0.5 across gamma 1-4, if end-to-end speculative throughput is below 1.0x after using native INT4/FP8 paths, or if FP8 verifier drift changes accepted-token decisions too often to support a fair comparison.

## Evidence references

- Artifact root: `<local-path>/projects/local-speculative-decoding-int4-draft-fp8-verifier-on-gb10-a83ad5bb71eb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
