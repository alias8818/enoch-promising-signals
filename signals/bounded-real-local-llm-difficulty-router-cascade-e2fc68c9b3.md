# Bounded Real Local LLM Difficulty-Router Cascade

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-real-local-llm-difficulty-router-cascade-e2fc68c9b3`
Run ID: `bounded-real-local-llm-difficulty-router-cascade-e2fc68c9b3-20260526T154121202735+0000`

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

- Parent run decision: Latency-Gated Local Model Cascade with Difficulty Router: enoch://control-plane/projects/latency-gated-local-model-cascade-with-difficulty-router-763ba2db21e7/runs/latency-gated-local-model-cascade-with-difficulty-router-763ba2db21e7-20260525T232631245457+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/74ed5f3bb060

## What looked useful

The Tier-1 direct local-LLM cascade met the predefined bounded threshold and showed a mechanism split: accepted Phi answers were 87.5% correct while escalated Phi answers were 55.6% correct. The signal is useful but mixed because two high-confidence Phi errors were accepted and threshold sweeps could not improve behavior due to coarse confidence outputs.

## Boundaries and scale limits

Small n=25 sample; one arithmetic benchmark; one local model pair; CPU-only llama.cpp process-per-call inference; prompt-level self-reported confidence router with coarse 1.0-or-missing confidence behavior; not validated across prompts, seeds, domains, persistent serving, or larger samples.

## Claim scope

On a fixed-seed 25-example GSM8K test sample using local GGUF Phi-4-mini as the cheap model and local GGUF Qwen2.5-7B as the strong model, a simple parseable-answer/self-confidence router achieved 84% cascade accuracy versus 88% Qwen-only accuracy while requiring Qwen on 36% of examples.

## Why it stopped

No-paper useful signal: the controlled small direct test supports the cascade mechanism at Tier 1, but the confidence router is too brittle and the sample too small for publication-grade evidence.

## Recommended next action

Run a bounded deepen follow-up with a calibrated router score, such as cheap-model self-consistency or logprob margin, on at least 200 GSM8K examples and require cascade accuracy within 3 percentage points of Qwen-only while using Qwen on no more than 50% of examples.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated Local LLM Difficulty Router for GSM8K Cascade
- Success threshold: Calibrated cascade accuracy within 3 percentage points of Qwen-only accuracy, Qwen call rate <= 50%, and wrong accepted Phi answers <= 5% of accepted examples on at least 200 GSM8K examples.
- Stop condition: Stop as negative if the calibrated score cannot reduce wrong accepts below the binary self-confidence router at comparable strong-call rate, or if cascade accuracy falls more than 5 percentage points below Qwen-only.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-real-local-llm-difficulty-router-cascade-e2fc68c9b3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
