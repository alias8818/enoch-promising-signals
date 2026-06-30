# Per-head KV cache quantization for long local context

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `per-head-kv-cache-quantization-for-long-local-context-d59e147960fd`
Run ID: `per-head-kv-cache-quantization-for-long-local-context-d59e147960fd-20260604T162252048619+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/787b7ccf8e16

## What looked useful

Per-head sensitivity is large enough to exploit at longer local windows: DP per-head avg-3 reduced MSE by 18.26% at a 256-token window and 22.99% at a 512-token window, while a 64-token smoke was 5.72% worse than uniform 3-bit.

## Boundaries and scale limits

Evidence is attention-level only, uses one small decoder model, one prompt-derived text source, no downstream perplexity/task evaluation, no fused cache kernel, and no serving latency or memory-traffic measurement.

## Claim scope

On GPT-2-small attention activations from project-prompt text, per-layer/head 2/3/4-bit KV allocation at an average 3-bit scalar budget reduced local causal attention-output MSE versus uniform 3-bit for 256- and 512-token windows.

## Why it stopped

No-paper useful signal: local attention-output evidence supports the mechanism, but this run is proxy-level rather than a full downstream or serving validation.

## Recommended next action

Run a bounded deepen follow-up that patches a small decoder KV cache path and measures perplexity plus decode latency on a standard corpus at equal memory budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Per-head KV quantization with downstream perplexity and decode latency
- Success threshold: At equal average KV bit budget, per-head allocation improves perplexity degradation by at least 10% relative to uniform 3-bit and keeps decode throughput within 10% of the uniform quantized path.
- Stop condition: Stop if per-head allocation fails to improve perplexity degradation by 5% or more at equal memory budget, or if decode overhead is more than 25% slower than uniform quantization.

## Evidence references

- Artifact root: `<local-path>/projects/per-head-kv-cache-quantization-for-long-local-context-d59e147960fd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
