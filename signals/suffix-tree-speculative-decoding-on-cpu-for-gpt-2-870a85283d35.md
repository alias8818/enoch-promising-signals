# Suffix-tree speculative decoding on CPU for GPT-2

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-speculative-decoding-on-cpu-for-gpt-2-870a85283d35`
Run ID: `suffix-tree-speculative-decoding-on-cpu-for-gpt-2-870a85283d35-20260531T221014942108+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/88b7da3728d1

## What looked useful

Exact suffix speculative decoding reduced GPT-2 calls from 49 to 30 on repetitive code and 49 to 10 on repetitive prose with 1.72x and 2.28x mean wall-time speedups, but the natural prompt only reduced calls from 49 to 41 and slowed to 0.55x in the main measurement.

## Boundaries and scale limits

Only 16-token smoke and 48-token bounded measurements were run; prompts were hand-written rather than corpus sampled; CPU timing was noisy; sampling mode, optimized suffix-tree lookup, batching, quantization, long contexts, and production serving traces were not tested.

## Claim scope

GPT-2 small greedy decoding on a CPU worker with three hand-written prompts: suffix-context speculative decoding preserves exact greedy output and can reduce model calls and improve wall time on highly repetitive prompts, but it is not reliable on a natural prompt.

## Why it stopped

Bounded local evidence is mixed: the mechanism works and helps repetitive prompts, but the main natural-prompt result is negative and the workload is too small and synthetic for a paper-ready claim.

## Recommended next action

Stop this run as no-paper useful signal; a bounded follow-up should test an optimized suffix index on a real code-completion trace with fixed CPU affinity and latency confidence intervals.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-based CPU benchmark for suffix-context speculative decoding on GPT-2 code completion
- Success threshold: At least 20% p50 latency improvement and no p95 regression over greedy KV-cache decoding on the code trace, with 100% exact greedy output match and no speedup claim on the negative-control set unless independently supported.
- Stop condition: Stop if optimized draft lookup plus verification fails to improve p50 latency by 10% on the first 30 code prompts or if exact greedy matching fails.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculative-decoding-on-cpu-for-gpt-2-870a85283d35`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
