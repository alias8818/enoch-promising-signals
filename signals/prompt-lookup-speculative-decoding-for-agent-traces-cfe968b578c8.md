# Prompt-Lookup Speculative Decoding for Agent Traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `prompt-lookup-speculative-decoding-for-agent-traces-cfe968b578c8`
Run ID: `prompt-lookup-speculative-decoding-for-agent-traces-cfe968b578c8-20260530T075511024160+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/6747810389ed

## What looked useful

Agent traces contain substantial repeated exact token spans. Prompt lookup beat random-context copying by a large margin: best n4_k16 acceptance was 0.436 versus random_k16 acceptance 0.00273, with median per-file upper-bound speedup 2.509x.

## Boundaries and scale limits

Files were local traces capped at 300000 characters and 20000 GPT-2 tokens each. No target model was run, no GPU latency was measured, and the speedup is an upper bound on verification-pass reduction rather than end-to-end serving throughput.

## Claim scope

Offline exact-token replay over 200 local Codex/Enoch agent trace JSONL files shows prompt-lookup candidates from prior context can reduce target verification calls in simulation, with best config n4_k16 reaching 2.480x pooled target-call upper-bound speedup and 0.436 drafted-token acceptance.

## Why it stopped

Closed as no-paper useful signal because the mechanism is supported by offline trace replay, but model-serving latency and correctness were proxied rather than directly validated.

## Recommended next action

Run a bounded end-to-end inference-loop follow-up that integrates prompt lookup with a small cached local model and reports wall-clock tokens/sec, target forward calls, lookup overhead, memory use, and output equivalence on held-out agent traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-End Prompt-Lookup Speculative Decoding on Held-Out Agent Traces
- Success threshold: At least 20% wall-clock tokens/sec improvement on a small local model with identical generated tokens and prompt-lookup overhead below 10% of decode time.
- Stop condition: Stop if exact-token output equivalence fails, lookup overhead erases speedup, or measured wall-clock improvement is below 10% on the held-out benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-lookup-speculative-decoding-for-agent-traces-cfe968b578c8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
