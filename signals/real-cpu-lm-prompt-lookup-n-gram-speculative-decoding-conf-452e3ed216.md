# Real CPU LM prompt-lookup n-gram speculative decoding confirmation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-cpu-lm-prompt-lookup-n-gram-speculative-decoding-conf-452e3ed216`
Run ID: `real-cpu-lm-prompt-lookup-n-gram-speculative-decoding-conf-452e3ed216-20260527T064703289031+0000`

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

- Parent run decision: N-Gram Speculative Draft for CPU Inference: enoch://control-plane/projects/n-gram-speculative-draft-for-cpu-inference-a3d22353b628/runs/n-gram-speculative-draft-for-cpu-inference-a3d22353b628-20260525T204401204774+0000
- Parent run decision: End-to-end CPU n-gram speculative decoding benchmark: enoch://control-plane/projects/end-to-end-cpu-n-gram-speculative-decoding-benchmark-883a9c8707/runs/end-to-end-cpu-n-gram-speculative-decoding-benchmark-883a9c8707-20260525T212441007865+0000

## What looked useful

The mechanism is real in repetitive prompt-local contexts: long accepted draft spans reduce target calls and can produce CPU speedups. Acceptance rate alone is insufficient because control prompts accepted many one-token repeats without reducing calls.

## Boundaries and scale limits

Small fixed prompt set with four repetition-positive prompts and four nominal controls; no larger natural corpus, 7B+ model, quantized CPU engine, batching, sampled decoding, or production latency distribution was tested.

## Claim scope

On a CPU worker with distilgpt2, deterministic cached greedy decoding, 48 generated tokens, and fixed repeated prompt-local spans, prompt-lookup n-gram speculative decoding exactly preserved greedy token IDs while reducing target decode calls by 72.9-80.2% and improving mean throughput by about 3.0-3.34x across n-gram sizes 2, 4, and 6.

## Why it stopped

Tier 2 bounded confirmation supports the mechanism but the evidence is too narrow for a general paper claim.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should evaluate repeat-density buckets on a larger natural prompt corpus with the same exact-output and call-reduction metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Prompt-lookup speculative decoding by natural-corpus repeat density
- Success threshold: In the high-repeat bucket, mean target-call reduction >=25% and mean throughput speedup >=1.2x versus cached greedy, with exact greedy token-ID preservation and no speedup claim for low-repeat buckets unless measured.
- Stop condition: Stop if high-repeat natural prompts do not achieve >=25% target-call reduction or if exact greedy token-ID preservation fails.

## Evidence references

- Artifact root: `<local-path>/projects/real-cpu-lm-prompt-lookup-n-gram-speculative-decoding-conf-452e3ed216`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
