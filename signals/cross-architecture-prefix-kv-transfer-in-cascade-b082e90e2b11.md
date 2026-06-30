# Cross-Architecture Prefix KV Transfer in Cascade

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cross-architecture-prefix-kv-transfer-in-cascade-b082e90e2b11`
Run ID: `cross-architecture-prefix-kv-transfer-in-cascade-b082e90e2b11-20260614T075831613833+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7e6034c628f0

## What looked useful

Across 4 seeds, transferred KV achieved mean continuation CE 0.1838 versus target-prefill CE 0.0317 and zero-prefix CE 5.2669; mean top-1 agreement with target-prefill logits was 0.9828 for transferred KV versus 0.0880 for zero-prefix KV.

## Boundaries and scale limits

Toy models trained from scratch, shared synthetic vocabulary, 16-token prefixes, short 34-token sequences, no pretrained language models, no natural-language corpus, no tokenizer mismatch, no quantized caches, and no end-to-end serving latency measurement.

## Claim scope

In a synthetic prefix-dependent causal-LM task, a learned linear adapter can map prefix KV caches from a smaller 2-layer/4-head/64-wide Transformer into usable target-shaped KV caches for a different 3-layer/6-head/96-wide Transformer, preserving most target continuation behavior without target prefix recomputation.

## Why it stopped

No-paper closure: the local evidence supports the mechanism only on a toy synthetic task and is not a full validation of cross-architecture KV transfer in real cascade serving.

## Recommended next action

Run a bounded pretrained-LM follow-up using two small compatible-tokenizer causal models, real text prefixes, and latency/KL/CE comparisons against target prefill and no-prefix baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained Small-LM Cross-Architecture KV Transfer on Real Text
- Success threshold: On held-out real text, transferred KV should recover at least 80% of the CE gap between no-prefix and target-prefill baselines, keep top-1 agreement with target-prefill logits above 90%, and show a plausible latency advantage after adapter overhead for prefixes of at least 128 tokens.
- Stop condition: Stop if transferred KV recovers less than 50% of the no-prefix-to-prefill CE gap or adapter overhead exceeds target prefill time for the tested prefix lengths.

## Evidence references

- Artifact root: `<local-path>/projects/cross-architecture-prefix-kv-transfer-in-cascade-b082e90e2b11`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
