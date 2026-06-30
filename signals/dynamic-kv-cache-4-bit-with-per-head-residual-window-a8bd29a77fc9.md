# Dynamic KV Cache 4-Bit with Per-Head Residual Window

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `dynamic-kv-cache-4-bit-with-per-head-residual-window-a8bd29a77fc9`
Run ID: `dynamic-kv-cache-4-bit-with-per-head-residual-window-a8bd29a77fc9-20260522T004704414853+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/71b83696c4f4

## What looked useful

On the corrected five-seed medium synthetic probe, all-int4 mean relative L2 error was 0.1644, uniform residual window 32 was 0.0961, and dynamic per-head residual at the same 512 residual-token budget was 0.0881. Dynamic also improved top-1 attention agreement from 0.9215 to 0.9355 at the same estimated 3.05x compression vs fp16 KV. Budget sweeps at average windows 16 and 64 showed the same direction.

## Boundaries and scale limits

No real pretrained LLM, no perplexity or generation-quality evaluation, no packed int4 production kernel, no multi-layer cache interactions, and no end-to-end serving latency measurement. Sequence length was 512 in the medium probe with 16 heads and 64-dimensional heads.

## Claim scope

Synthetic structured-attention KV-cache probe: per-token int4 K/V quantization plus fp16 recent-token residual windows, with dynamic per-head residual allocation calibrated on held-out synthetic queries, reduced attention-output error versus all-int4 and versus uniform residual windows at matched residual-token memory.

## Why it stopped

Proxy-only useful signal: the mechanism was directly tested on synthetic attention tensors, but paper-grade claims require real-model quality and serving measurements.

## Recommended next action

Run a bounded real-decoder follow-up on a GPT-2-small-class model or similarly local pretrained decoder, comparing all-int4, uniform residual, and dynamic per-head residual at matched KV memory on next-token loss/perplexity and decode throughput.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-decoder validation of dynamic per-head KV residual windows
- Success threshold: Dynamic per-head residual reduces held-out next-token loss or perplexity by at least 2% relative to uniform residual at matched KV memory, with decode throughput no worse than 5% below uniform residual.
- Stop condition: Stop if dynamic per-head residual fails to beat uniform residual on held-out real-model loss/perplexity at matched memory for two sequence lengths, or if the implementable packed path erases the memory/throughput advantage.

## Evidence references

- Artifact root: `<local-path>/projects/dynamic-kv-cache-4-bit-with-per-head-residual-window-a8bd29a77fc9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
