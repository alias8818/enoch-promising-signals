# Real-model KV trace validation for 2-bit residual hot-token buffers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-model-kv-trace-validation-for-2-bit-residual-hot-toke-97e5cdc454`
Run ID: `real-model-kv-trace-validation-for-2-bit-residual-hot-toke-97e5cdc454-20260608T040140363517+0000`

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

- Parent run decision: 2-bit KV-Cache with Residual Hot-Token Buffers: enoch://control-plane/projects/2-bit-kv-cache-with-residual-hot-token-buffers-de4bdb4f177d/runs/2-bit-kv-cache-with-residual-hot-token-buffers-de4bdb4f177d-20260607T222356136710+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/291a0c948d7c

## What looked useful

Cumulative-attention hot residual tokens reduced relative attention-output MSE versus random residuals at budgets 8/16/32, but did not consistently beat a simple recency residual buffer. Hot beat recency at budget 8 by 12.8% aggregate relative MSE, then lost by 5.9% at budget 16 and 44.4% at budget 32; row-level hot-better-than-recency counts were 21/48, 19/48, and 16/48.

## Boundaries and scale limits

Not an online decode/perplexity test; not evaluated on 7B+ models, production traces, long contexts, latency, or memory allocator behavior. The 2-bit quantizer is a harsh symmetric trace proxy with scale metadata rather than a production kernel.

## Claim scope

Tier-1 real-model attention-output trace validation on distilgpt2, Wikitext-2 text, sequence length 128, first 6 layers, comparing 2-bit KV quantization with cumulative-attention hot residual tokens against recency and random residual controls.

## Why it stopped

Controlled small direct test produced a mixed mechanism signal but failed to validate pure cumulative-attention hot-token residual buffers against the recency control; this is trace-level early evidence, not full online KV-cache validation.

## Recommended next action

Stop this run as no-paper useful evidence; if continuing locally, test a hybrid recency-plus-hot residual policy in the same trace harness and require it to beat recency-only by at least 10% relative MSE at budgets 8/16/32.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hybrid recency-plus-hot residual policy for 2-bit KV caches
- Success threshold: At least one hybrid split beats recency-only by >=10% aggregate relative MSE at budgets 8, 16, and 32, and wins at least 30/48 prompt-layer rows for each budget.
- Stop condition: Stop as negative if no hybrid split beats recency-only by >=5% aggregate relative MSE at two or more budgets, or if row-level wins remain below 24/48 for all budgets.

## Evidence references

- Artifact root: `<local-path>/projects/real-model-kv-trace-validation-for-2-bit-residual-hot-toke-97e5cdc454`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
