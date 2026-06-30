# Residual-channel int2 quantization for KV cache under long-context CPU eval

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `residual-channel-int2-quantization-for-kv-cache-under-long-context-cpu-eval-04e1d38a9efb`
Run ID: `residual-channel-int2-quantization-for-kv-cache-under-long-context-cpu-eval-04e1d38a9efb-20260621T175135481477+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/408262a02f5a

## What looked useful

At seq_len 32768 and 12.5% residual channels, variance residual int2 used 3.75 bits/value and improved output relative L2 to 0.536 versus 1.476 for all-int2 and 1.471 for random residual, with output cosine 0.847 versus 0.162 and 0.175 respectively. Across tested lengths/fractions, variance residual reduced output relative L2 by 37.1-79.7% versus random residual at equal bits.

## Boundaries and scale limits

Synthetic KV distributions only; no real transformer KV traces, no packed int2 CPU kernel, no perplexity/generation/task metric evaluation, and no end-to-end serving throughput measurement.

## Claim scope

In a bounded NumPy CPU proxy using synthetic heavy-tailed KV tensors up to 32768 tokens, preserving top-variance residual K/V channels in fp16 substantially reduces attention-output error versus all-int2 and random residual-channel controls at equal bit budgets.

## Why it stopped

No-paper closure: the local result is a synthetic CPU proxy useful signal, not direct real-model or packed-kernel validation.

## Recommended next action

Run a bounded follow-up on captured real-model KV traces with packed or simulated packed int2 decode, comparing variance residual int2 against all-int2, random residual, int4, and fp16 on attention error plus perplexity or retrieval accuracy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual-channel int2 KV quantization on real long-context KV traces
- Success threshold: At 12.5% or lower residual channels, reduce output relative L2 by at least 50% versus random residual at equal bits, keep output cosine at or above 0.85 on 32768-token real KV traces, and avoid worse task-level quality than int4 by more than 5%.
- Stop condition: Stop if top-variance residual channels fail to beat random residual channels by at least 20% output-relative-L2 reduction on real KV traces at two residual budgets, or if CPU packed decode overhead eliminates the memory-bandwidth benefit versus int4.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-int2-quantization-for-kv-cache-under-long-context-cpu-eval-04e1d38a9efb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
