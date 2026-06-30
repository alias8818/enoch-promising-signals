# 2-Bit KV Cache with FP8 Residual Summary for Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-kv-cache-with-fp8-residual-summary-for-long-context-08fee1860263`
Run ID: `2-bit-kv-cache-with-fp8-residual-summary-for-long-context-08fee1860263-20260523T024654422637+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8780efafda6d

## What looked useful

FP8 residual summaries consistently reduce plain 2-bit KV attention error and are especially effective on synthetic low-rank KV, but they fail to match 4-bit KV on attention KL and output RMSE at comparable or even higher estimated bytes/token for gaussian and outlier distributions.

## Boundaries and scale limits

No real transformer KV traces, no fused serving kernel, no downstream perplexity or generation benchmark, and no datacenter-scale validation. Evidence is bounded to synthetic gaussian, low-rank, and outlier KV distributions on one GB10 GPU.

## Claim scope

Synthetic 8192-token attention reconstruction with per-token 2-bit KV quantization plus block-wise FP8 low-rank residual summaries, compared against plain 2-bit and 4-bit KV baselines.

## Why it stopped

Early synthetic/proxy falsification of the competitive-cache claim: the mechanism improves 2-bit quantization but remains substantially worse than 4-bit KV on key reconstruction metrics at comparable memory.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should use real transformer KV traces and require the residual scheme to beat a tuned 4-bit KV baseline at equal or lower bytes/token.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Transformer KV Trace Test for 2-Bit Plus FP8 Residual Cache
- Success threshold: At equal or lower estimated bytes/token than 4-bit KV, 2-bit plus FP8 residual summaries must reduce attention-output RMSE and attention KL by at least 10% versus 4-bit on real KV traces without worse downstream proxy quality.
- Stop condition: Stop if real-trace residual summaries do not beat tuned 4-bit KV at matched bytes/token on both attention-output RMSE and KL, or if reconstruction latency/metadata overhead removes the memory advantage.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-kv-cache-with-fp8-residual-summary-for-long-context-08fee1860263`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
