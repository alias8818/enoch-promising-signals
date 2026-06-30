# 8-Bit KV Cache with Ring Eviction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `8-bit-kv-cache-with-ring-eviction-0b1fa66c7ce5`
Run ID: `8-bit-kv-cache-with-ring-eviction-0b1fa66c7ce5-20260527T025443165386+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/01d3df5daa94

## What looked useful

The mechanism split is clear: int8 KV storage is not the observed bottleneck in this probe, while naive ring eviction is the failure mode for long-range retrieval and even causes non-trivial drift when the top target is retained but older attention mass is discarded.

## Boundaries and scale limits

No real transformer weights, perplexity, downstream tasks, multi-layer interactions, GPU kernels, or serving throughput were tested. Ring eviction was represented by last-W-token retention, not an integrated production cache implementation.

## Claim scope

Synthetic single-head attention probe at seq_len=4096 and dim=64: per-row int8 KV quantization preserves retained-context attention outputs with about 0.006-0.009 mean relative L2 error, but fixed ring eviction causes large output drift when relevant older tokens or older attention mass are removed.

## Why it stopped

Synthetic evidence is sufficient to reject naive fixed ring eviction as generally viable, but it is not full validation of int8 KV caching or model-quality behavior.

## Recommended next action

Stop this run as no-paper useful signal; next run should test the same four-way comparison on a real small transformer with perplexity and needle/retrieval prompts before considering any broader claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model validation of int8 KV cache with fixed and adaptive retention
- Success threshold: Full int8 KV changes loss by less than 1% relative and preserves retrieval accuracy within 2 percentage points; any ring policy must retain at least 95% retrieval accuracy for targets outside the naive window while using less memory than full fp16.
- Stop condition: Stop if full int8 KV alone degrades loss by more than 3% or if every sub-full retention policy fails retrieval prompts by more than 10 percentage points at distances outside the window.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-kv-cache-with-ring-eviction-0b1fa66c7ce5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
