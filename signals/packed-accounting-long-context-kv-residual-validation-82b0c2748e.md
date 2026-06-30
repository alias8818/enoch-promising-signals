# Packed-accounting long-context KV residual validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `packed-accounting-long-context-kv-residual-validation-82b0c2748e`
Run ID: `packed-accounting-long-context-kv-residual-validation-82b0c2748e-20260620T081753858000+0000`

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

- Parent run decision: 2-bit KV-cache with Recent/Anchor Residual Stream: enoch://control-plane/projects/2-bit-kv-cache-with-recent-anchor-residual-stream-2f9c77b515e0/runs/2-bit-kv-cache-with-recent-anchor-residual-stream-2f9c77b515e0-20260620T074752170669+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a258cba71a72

## What looked useful

The Tier 1 direct test supports the mechanism that incorrect packed long-context KV accounting can leak prior packed sequence KV into later sequences. At 4096 prior tokens, faulty neutral-random accounting produced mean absolute residuals of 0.1437 and 0.1445 across two seeds; sentinel KV produced 0.8039 and 0.8164, while correct accounting stayed at numerical noise.

## Boundaries and scale limits

No trained transformer stack, tokenizer, MLP layers, real serving KV cache, FlashAttention varlen kernel, natural-language benchmark, or production inference path was tested. This is mechanism evidence, not paper-ready full-system validation.

## Claim scope

Controlled PyTorch attention-level test of packed A|B long-context KV accounting up to 4096 prior tokens and 256 current tokens. Correct block-causal packed accounting matched unpacked per-sequence attention to <=2.38e-7 max absolute error across two seeds, while faulty global-causal accounting produced large residuals.

## Why it stopped

No-paper closure: the mechanism is supported by a controlled direct attention test, but publication readiness would require integration evidence in a real model or serving kernel.

## Recommended next action

Run a bounded integration follow-up in a small transformer or actual varlen attention backend, requiring unpacked-vs-packed logit equivalence under correct accounting and measurable logit degradation under intentionally faulty accounting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer packed KV accounting logit-equivalence validation
- Success threshold: Correct packed execution must match unpacked logits within <=1e-4 max absolute difference while the injected faulty accounting condition must produce >=0.01 mean absolute logit residual or a clear controlled-task accuracy drop at >=4096 prior packed tokens.
- Stop condition: Stop if correct packed execution cannot be made equivalent to unpacked due to implementation noise, or if the injected boundary fault fails to produce residual/logit degradation above threshold across two seeds.

## Evidence references

- Artifact root: `<local-path>/projects/packed-accounting-long-context-kv-residual-validation-82b0c2748e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
