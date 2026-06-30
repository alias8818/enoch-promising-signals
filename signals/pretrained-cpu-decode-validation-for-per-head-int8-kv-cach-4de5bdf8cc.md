# Pretrained CPU decode validation for per-head int8 KV cache

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `pretrained-cpu-decode-validation-for-per-head-int8-kv-cach-4de5bdf8cc`
Run ID: `pretrained-cpu-decode-validation-for-per-head-int8-kv-cach-4de5bdf8cc-20260605T175138712549+0000`

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

- Parent run decision: End-to-end CPU transformer validation for per-head int8 KV cache: enoch://control-plane/projects/end-to-end-cpu-transformer-validation-for-per-head-int8-kv-85f954bdc0/runs/end-to-end-cpu-transformer-validation-for-per-head-int8-kv-85f954bdc0-20260605T121913826621+0000
- Parent run decision: Per-Head Quantized KV-Cache on CPU for Long Context: enoch://control-plane/projects/per-head-quantized-kv-cache-on-cpu-for-long-context-a4e1700936dd/runs/per-head-quantized-kv-cache-on-cpu-for-long-context-a4e1700936dd-20260605T044814108706+0000

## What looked useful

Per-head int8 KV cache is locally viable for memory compression and fixed-stream decode fidelity, but this Tier 2 CPU validation does not support a latency or novelty win over a real fp32 baseline and per-tensor int8 control.

## Boundaries and scale limits

Single pretrained small GPT-2-class model, six prompts, 40 decode steps, Hugging Face DynamicCache replay harness, no fused int8 attention kernel, no 7B-class model, no long-context perplexity or downstream task suite.

## Claim scope

On a CPU worker using pretrained distilgpt2, six fixed prompts, and 40-token forced replay, per-head symmetric int8 KV cache reduced persistent KV storage by about 75% and preserved greedy top-1 replay decisions, but decode plus dequantization was slower than the fp32 DynamicCache baseline and slower than a per-tensor int8 ablation.

## Why it stopped

Moderate direct pretrained CPU evidence is mixed: memory and top-1 fidelity are supported, but the per-head target misses the CPU latency criterion and is not stronger than the per-tensor ablation.

## Recommended next action

Stop this paper path; if continuing, run a bounded implementation follow-up with incremental quantized-cache updates and a CPU attention path that avoids full-cache reconstruction, comparing per-head directly against per-tensor int8.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Incremental CPU attention validation for per-head versus per-tensor int8 KV cache
- Success threshold: Per-head int8 must reduce KV memory by at least 70%, achieve at least 99.5% top-1 replay agreement or less than 1% perplexity drift versus fp32, and be no slower than both fp32 and per-tensor int8 on mean decode latency.
- Stop condition: Stop if per-head int8 remains slower than fp32 or per-tensor int8 after incremental update overhead is removed, or if fidelity drops below the stated threshold on the expanded prompt set.

## Evidence references

- Artifact root: `<local-path>/projects/pretrained-cpu-decode-validation-for-per-head-int8-kv-cach-4de5bdf8cc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
