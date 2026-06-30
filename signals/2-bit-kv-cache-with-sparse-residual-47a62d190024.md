# 2-Bit KV Cache with Sparse Residual

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-kv-cache-with-sparse-residual-47a62d190024`
Run ID: `2-bit-kv-cache-with-sparse-residual-47a62d190024-20260608T050911210631+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4244dd767c13

## What looked useful

Sparse residuals are a conditional mechanism, not a robust standalone fix: recent residual works well for recent-correlated attention, key-norm works well for heavy-tail traces, but simple feasible policies can be neutral or harmful when their retained tokens do not match attention salience. Oracle residual has large headroom, implying residual admission policy is the core research problem.

## Boundaries and scale limits

No trained transformer, perplexity, generation-quality, multi-layer KV trace, serving throughput, or CUDA implementation was tested. Evidence is limited to vectorized NumPy synthetic Q/K/V traces with seq_len up to 2048, dim 64, and 64 trials per condition.

## Claim scope

Synthetic single-step decode attention traces show that 2-bit KV cache with sparse full-precision residual tokens can substantially reduce attention-output error when the residual policy retains the tokens that dominate attention or value magnitude.

## Why it stopped

This is a proxy/mechanism result rather than full validation: synthetic attention-output evidence is mixed and policy-dependent, with no real-model quality or serving evidence.

## Recommended next action

Run a bounded real-transformer KV trace follow-up on a small GPT-style model, comparing feasible online residual admission policies against pure 2-bit KV at fixed memory.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Transformer KV Trace Test for 2-Bit Cache with Salience-Based Sparse Residual
- Success threshold: A feasible non-oracle residual policy reduces mean attention-output or logit relative error by at least 25% versus pure 2-bit KV at <=25% fp16 KV memory, without regressions larger than 5% on any tested layer family or prompt group.
- Stop condition: Stop if feasible policies fail to beat pure 2-bit KV by 10% mean error reduction or show repeated prompt/layer regressions above 10% at matched memory.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-kv-cache-with-sparse-residual-47a62d190024`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
