# Sliding-window KV cache with sink tokens for 32K context on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sliding-window-kv-cache-with-sink-tokens-for-32k-context-on-gb10-2102eb8be67b`
Run ID: `sliding-window-kv-cache-with-sink-tokens-for-32k-context-on-gb10-2102eb8be67b-20260630T171253157509+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3a52a3160c0f

## What looked useful

For a llama-8b-like FP16 GQA cache, full 32K KV is 4.00 GiB versus 0.50 GiB for sink4+window4096 and 1.00 GiB for sink4+window8192. Compact sink4+window4096 attention ran 0.0491 ms median versus 0.6484 ms for full 32K, while naive concatenate-each-step at window8192 slowed to 0.5048 ms. Synthetic error was near zero when attention was recent-biased but large for uniform or forgotten-middle attention.

## Boundaries and scale limits

No trained model, tokenizer, dataset, serving backend, or end-to-end 32K generation quality was tested. The benchmark covers one-query synthetic attention with kv_heads=8 and head_dim=128, not full transformer inference.

## Claim scope

On a GB10 using PyTorch synthetic decode-attention tensors at 32K context, a compact sink-token plus sliding-window KV layout substantially reduces analytic KV memory and isolated attention latency, but it only approximates full attention when attention mass lies in the retained sink/recent tokens.

## Why it stopped

No-paper closure: this run produced a bounded synthetic/analytic useful signal, but not direct real-model evidence for preserving 32K-context quality.

## Recommended next action

Run a bounded real-model 32K evaluation with a compact or segmented sink-window KV backend, comparing full KV versus sink+window on needle retrieval and perplexity at matched decode settings.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model 32K sink-window KV quality probe
- Success threshold: At window4096 or window8192, retained-region retrieval accuracy is within 5 percentage points of full KV and end-to-end decode throughput is at least 1.5x full-KV baseline, while evicted-middle failures are explicitly characterized.
- Stop condition: Stop if compact/segmented KV cannot be implemented locally, if retained-region accuracy drops by more than 10 percentage points, or if end-to-end throughput is not faster than full KV.

## Evidence references

- Artifact root: `<local-path>/projects/sliding-window-kv-cache-with-sink-tokens-for-32k-context-on-gb10-2102eb8be67b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
