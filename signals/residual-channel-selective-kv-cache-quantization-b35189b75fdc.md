# Residual-Channel Selective KV Cache Quantization

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-channel-selective-kv-cache-quantization-b35189b75fdc`
Run ID: `residual-channel-selective-kv-cache-quantization-b35189b75fdc-20260528T050413420344+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/4a9b5300cb31

## What looked useful

Energy-selected residual channels consistently beat random residual channels by 9.1% to 35.0% relative MSE reduction across 2/3/4-bit settings, but effective-bit controls were unfavorable: all-channel 5-bit and 6-bit quantization gave lower error than 4-bit plus FP16 residual channels at similar or lower effective bits per value.

## Boundaries and scale limits

Only 16 prompts, sequence length 128, GPT-2 small, and offline attention-output reconstruction were tested. No end-to-end perplexity, long-context generation, throughput, memory-bandwidth, or packed-kernel serving validation was run.

## Claim scope

On GPT-2-small activations, high-energy residual KV channels reduce layerwise attention-output reconstruction error compared with random or low-energy residual channel choices at the same low-bit format and residual fraction.

## Why it stopped

Proxy/local reconstruction evidence supports selective-channel mechanism but not a broad efficiency claim; effective-bit controls undermine paper readiness.

## Recommended next action

Stop this run as no-paper useful signal; only reopen with an end-to-end same-memory or same-throughput KV-cache inference benchmark that includes all-channel 5-bit/6-bit controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end same-memory residual KV cache quantization benchmark
- Success threshold: Residual-channel selective cache must improve perplexity or task quality over the best same-memory/same-throughput baseline by at least 5% relative without worse decoding throughput.
- Stop condition: Stop if all-channel 5-bit/6-bit or groupwise baselines match or beat residual-channel selective cache at equal memory/throughput, or if residual side-buffer overhead removes the memory/latency advantage.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-selective-kv-cache-quantization-b35189b75fdc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
