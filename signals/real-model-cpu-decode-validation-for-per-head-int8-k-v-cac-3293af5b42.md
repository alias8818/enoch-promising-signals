# Real-model CPU decode validation for per-head INT8 K/V cache

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-model-cpu-decode-validation-for-per-head-int8-k-v-cac-3293af5b42`
Run ID: `real-model-cpu-decode-validation-for-per-head-int8-k-v-cac-3293af5b42-20260530T045803587088+0000`

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

- Parent run decision: Int8 per-head KV cache for CPU inference: enoch://control-plane/projects/int8-per-head-kv-cache-for-cpu-inference-e4a33fa97a79/runs/int8-per-head-kv-cache-for-cpu-inference-e4a33fa97a79-20260530T004503528887+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/6d56167698b4

## What looked useful

Per-head INT8 K/V cache is mechanically viable in a direct CPU decode harness and can preserve greedy token choices in small bounded tests, but pretrained GPT-2 showed nontrivial logit perturbation, so the result supports a follow-up quality/robustness benchmark rather than a paper claim.

## Boundaries and scale limits

Short contexts only; one pretrained GPT-2 prompt; no perplexity or task-quality benchmark; no long-context stress; no sampling robustness; unoptimized NumPy implementation, so timing is not a serving-throughput claim.

## Claim scope

Bounded CPU token-by-token GPT-2 decode validation: per-head symmetric INT8 K/V cache preserved greedy top-1 outputs against FP32 cache on five tiny GPT-2-format trials with 32 generated tokens and one short pretrained GPT-2 trial with 4 generated tokens, while reducing measured cache bytes to about 14-21% of FP32 in this implementation.

## Why it stopped

Tier-1 controlled direct test completed; evidence supports the mechanism but is too narrow and shows enough pretrained logit shift to stop as no-paper useful signal.

## Recommended next action

Run a bounded pretrained GPT-2 benchmark over at least 100 natural prompts with 64-256 decode tokens, reporting perplexity/logit deltas, greedy and sampling divergence rates, and long-context sensitivity before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained GPT-2 robustness benchmark for per-head INT8 K/V cache
- Success threshold: Mean perplexity increase <=1%, greedy first-divergence rate <=5% before 128 generated tokens, no catastrophic prompt class failures, and measured K/V cache bytes <=25% of FP32 for the tested cache layout.
- Stop condition: Stop negative if perplexity increases >5%, greedy divergence occurs before 64 generated tokens on >20% of prompts, or long-context tests show systematic top-1 instability attributable to INT8 K/V quantization.

## Evidence references

- Artifact root: `<local-path>/projects/real-model-cpu-decode-validation-for-per-head-int8-k-v-cac-3293af5b42`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
