# Early-Exit Self-Speculative Decoding for VRAM-Constrained Models

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `early-exit-self-speculative-decoding-for-vram-constrained-models-8b9902529bab`
Run ID: `early-exit-self-speculative-decoding-for-vram-constrained-models-8b9902529bab-20260601T085952898408+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f880ef6e3b04

## What looked useful

Exit layers 2/4/6 reached 0.9545/0.9801/0.9908 agreement with final predictions. At gamma=4 they accepted 3.56/3.81/3.91 tokens on average. No-KV timing showed 1.46x-2.24x speedups for representative gamma=4 settings, but conservative serial layer-cost accounting was slower than baseline for every setting.

## Boundaries and scale limits

Synthetic data, tiny model, no real KV-cache implementation, no real text benchmark, no 7B+ model, no quantization or production serving stack, and simplified analytical compute accounting.

## Claim scope

In a tiny synthetic 8-layer causal transformer, trained intermediate exits matched final greedy predictions often enough for high speculative acceptance, reduced draft-time layer/KV footprint by construction, and improved a no-KV wall-clock decode proxy when verification was amortized across drafted tokens.

## Why it stopped

No-paper closure: this is a toy/proxy useful signal, not direct full validation of VRAM-constrained LLM serving.

## Recommended next action

Run a bounded cached-decoder follow-up on GPT-2-small-class weights with real text prompts, exact greedy equivalence checks, tokens/s, acceptance distributions, GPU utilization, and peak memory versus full greedy decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cached GPT-2-small early-exit self-speculative decoding benchmark
- Success threshold: At least one exit/gamma setting preserves exact greedy output for evaluated prompts while improving tokens/s by >=15% or reducing peak memory by >=20% without increasing end-to-end latency.
- Stop condition: Stop if exit/final agreement is below 0.90 after exit-head training, if exact greedy preservation fails systematically, or if all measured cached settings are slower and use no less peak memory than baseline.

## Evidence references

- Artifact root: `<local-path>/projects/early-exit-self-speculative-decoding-for-vram-constrained-models-8b9902529bab`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
