# Adaptive Precision Residual Gates for 2-bit KV Cache

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adaptive-precision-residual-gates-for-2-bit-kv-cache-84a98257a7a3`
Run ID: `adaptive-precision-residual-gates-for-2-bit-kv-cache-84a98257a7a3-20260519T155136211159+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b8ef7195f471

## What looked useful

Adaptive residual gates select useful entries: proxy and oracle residual gates reduce attention-output MSE by about 43% versus a 2-bit base, while random residual allocation reduces MSE by about 7%. However, uniform 3-bit quantization reduces MSE by about 89% at the same 3.0 bits/scalar budget and beats both adaptive residual variants on 30/30 paired seeds.

## Boundaries and scale limits

No end-to-end language model, no real transformer KV activation traces, no perplexity/task evaluation, no GPU kernel or decode-latency measurement, and no metadata-overhead implementation. The result is an early mechanism/proxy falsification of this residual format rather than a full deployment validation.

## Claim scope

Synthetic Numpy attention-cache reconstruction probe over 30 seeds, length 1024, dimension 128, and 128 queries: adaptive sparse fp16 residual gates on top of a 2-bit KV cache improve over a plain 2-bit base and random residual allocation, but are consistently worse than simple uniform 3-bit quantization at the same 3.0 bits/scalar budget.

## Why it stopped

Proxy attention reconstruction found the adaptive gate mechanism useful but the proposed 2-bit plus sparse fp16 residual memory tradeoff non-competitive against a simpler equal-budget uniform quantizer; this is not a full LM validation.

## Recommended next action

Stop this fp16 sparse-residual variant as a proxy early falsification; the only worthwhile bounded next test is a low-bit or block-coded residual gate that must beat uniform 3-bit quantization at no more than 3.0 effective bits/scalar on real or recorded KV traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Low-bit block residual gates for 2-bit KV cache
- Success threshold: At <=3.0 effective bits/scalar including metadata, the gated low-bit/block residual cache must reduce attention-output MSE by at least 20% versus uniform 3-bit on real KV traces and avoid a top-1 attention match regression.
- Stop condition: Stop if the gated residual format fails to beat uniform 3-bit on paired real-trace metrics, or if metadata/decode overhead pushes effective budget above 3.0 bits/scalar.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-precision-residual-gates-for-2-bit-kv-cache-84a98257a7a3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
