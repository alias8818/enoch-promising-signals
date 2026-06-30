# Anchor-Exact KV Cache with Compressed Sliding Window

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-exact-kv-cache-with-compressed-sliding-window-33823cc91f27`
Run ID: `anchor-exact-kv-cache-with-compressed-sliding-window-33823cc91f27-20260629T130424694912+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5a05e6a496ea

## What looked useful

Anchor-exact cache used about 7.2% of full KV slots and reduced anchor-biased MSE by 30.3% versus compressed cache at beta 1.0 and by more than 99.99% at betas 2.0 and 3.0. It added little over compressed cache for random attention or recency-biased attention.

## Boundaries and scale limits

No real language-model traces, perplexity, generation quality, multi-layer/multi-head behavior, learned anchor policy, or optimized serving throughput were tested. Evidence is bounded to synthetic CUDA PyTorch probes.

## Claim scope

Synthetic single-head attention reconstruction at seq_len 8192 shows anchor-exact compressed sliding-window KV caching is useful when old anchor tokens receive concentrated attention, but not for random attention and only marginally for recency-dominated attention.

## Why it stopped

No-paper closure: this run is a synthetic mechanism probe, not direct model-level validation.

## Recommended next action

Run a bounded direct-evidence follow-up on real small-transformer KV traces with matched cache budgets and perplexity or next-token KL metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model trace validation for anchor-exact compressed KV cache
- Success threshold: At the same KV slot budget, anchor-exact must reduce next-token KL or perplexity degradation by at least 20% versus compressed-only on long-context prompts while preserving or improving decode throughput versus full-cache decoding.
- Stop condition: Stop if anchor-exact fails to beat compressed-only by at least 5% on real-trace next-token KL/perplexity at matched cache budgets or if added anchor bookkeeping removes throughput benefit.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-exact-kv-cache-with-compressed-sliding-window-33823cc91f27`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
