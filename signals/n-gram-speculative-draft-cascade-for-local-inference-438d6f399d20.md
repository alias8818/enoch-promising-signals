# N-gram Speculative Draft Cascade for Local Inference

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-speculative-draft-cascade-for-local-inference-438d6f399d20`
Run ID: `n-gram-speculative-draft-cascade-for-local-inference-438d6f399d20-20260522T012822208311+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/097ee83fc7b8

## What looked useful

Cascade n-gram drafting reduced ideal verifier passes by 60.0% on Tiny Shakespeare open prompts and 83.1% on copy-heavy prompts. A less aggressive 6/4/3/2 cascade retained most of the pass reduction with higher acceptance quality than unigram fallback.

## Boundaries and scale limits

No integrated speculative decoder latency was measured; no batched verifier KV-cache implementation, neural-draft baseline, sampling, larger model, production trace, or broad workload validation was run. Results are small-model and small-prompt-count only.

## Claim scope

Offline verifier-pass simulation for prompt/history n-gram speculative draft cascades against distilgpt2 greedy continuations on 24-prompt small local workloads. The supported claim is that the cascade can reduce ideal target verifier passes versus one-pass-per-token greedy decoding in repetition-heavy and Tiny Shakespeare prompt workloads.

## Why it stopped

Closed as no-paper useful signal because current evidence is an offline verifier-pass simulation, not an integrated latency or robustness validation.

## Recommended next action

Implement an actual KV-cache speculative verifier for a 0.5B-3B local model and measure end-to-end tokens/s against greedy decoding plus a neural draft baseline before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end KV-cache latency test for n-gram draft cascades
- Success threshold: At least 20% end-to-end tokens/s improvement over greedy decoding on copy-heavy workloads with no regression greater than 5% on natural open prompts, measured over at least 100 prompts.
- Stop condition: Stop if optimized n-gram draft overhead or verifier batching reduces end-to-end throughput below greedy decoding on both copy-heavy and natural prompt sets.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-draft-cascade-for-local-inference-438d6f399d20`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
