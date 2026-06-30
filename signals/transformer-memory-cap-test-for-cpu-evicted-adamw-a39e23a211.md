# Transformer Memory-Cap Test for CPU-Evicted AdamW

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `transformer-memory-cap-test-for-cpu-evicted-adamw-a39e23a211`
Run ID: `transformer-memory-cap-test-for-cpu-evicted-adamw-a39e23a211-20260603T180813988443+0000`

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

- Parent run decision: Dynamic Optimizer State Eviction for Tiny-VRAM Training: enoch://control-plane/projects/dynamic-optimizer-state-eviction-for-tiny-vram-training-31fe34674533/runs/dynamic-optimizer-state-eviction-for-tiny-vram-training-31fe34674533-20260602T211743804112+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/13108353904e

## What looked useful

CPU-evicted AdamW completed capped transformer update steps at 170 MiB and 260 MiB CUDA allocator caps where GPU AdamW failed, and reduced uncapped CUDA peak allocation from 367.3 MiB to 198.5 MiB on the 31.60M parameter case with about a 10.5% short-run throughput drop.

## Boundaries and scale limits

One-to-three-step synthetic-token runs only; small models; simple unoptimized CPU update; no convergence, stability, real-corpus, GPT-2-small-class, production offload, multi-GPU, or datacenter-scale validation.

## Claim scope

On GB10, for 14.77M and 31.60M parameter synthetic transformer language-model training steps, CPU-evicting AdamW moment state reduced CUDA peak allocation and passed allocator caps where normal GPU AdamW OOMed.

## Why it stopped

Tier-1 direct cap threshold was met, but the result is no-paper useful signal rather than publication-grade evidence because it used small synthetic one-to-three-step runs and an unoptimized custom optimizer.

## Recommended next action

Run a bounded medium deepen test with a more efficient CPU/offloaded AdamW implementation on a GPT-2-small-class model, sweeping memory caps and reporting memory, throughput, and loss movement against GPU AdamW and a standard offload baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small-class memory-cap sweep for CPU-evicted AdamW
- Success threshold: CPU/offloaded AdamW should complete at least 100 steps at a CUDA allocator cap where GPU AdamW OOMs, reduce peak CUDA allocation by at least 30%, show monotonic or comparable loss movement, and keep throughput penalty at or below 50% versus GPU AdamW at an uncapped setting.
- Stop condition: Stop if CPU/offloaded AdamW cannot complete 100 steps under any cap lower than GPU AdamW's required cap, if loss is unstable versus baseline, or if the throughput penalty exceeds 50% without a larger than 30% CUDA memory reduction.

## Evidence references

- Artifact root: `<local-path>/projects/transformer-memory-cap-test-for-cpu-evicted-adamw-a39e23a211`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
