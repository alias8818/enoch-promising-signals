# N-Gram Draft Head Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-draft-head-speculative-decoding-on-cpu-28e56fbc376a`
Run ID: `n-gram-draft-head-speculative-decoding-on-cpu-28e56fbc376a-20260525T150850957435+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2348c1aa266a

## What looked useful

N-gram draft speculative decoding is mechanically viable on CPU and exact under greedy verification, but its usefulness appears workload-dependent: promising for repetitive/code/templated continuations, unsupported for broad natural prose without a stronger draft head or workload filter.

## Boundaries and scale limits

Tests used tiny-gpt2 and distilgpt2, short prompts, greedy decoding, and local CPU execution. The main timed model outputs were degenerate repetitive continuations, and the natural/code diversity check was a token trace rather than full verifier timing. No 7B+ model, production CPU runtime, batching study, or broad dataset was tested.

## Claim scope

On short CPU-only probes with small GPT-2-family models, an exact n-gram copy proposer plus verifier preserved greedy output and sped up highly repetitive greedy continuations by 1.9-2.3x. A fixed-token trace check showed the same proposer has very low natural-prose hit rate but strong hit rate on repetitive/code-like traces.

## Why it stopped

No-paper useful signal: local evidence supports a narrow repetitive/code mechanism but does not support a broad CPU speculative-decoding claim; model runs were short and degenerate, while natural-prose trace acceptance was only 1.0% per position.

## Recommended next action

Run a bounded deepen test on code/log/templated completions with GPT-2-small-class or larger CPU inference, comparing greedy KV-cache decoding against n-gram speculative decoding across gamma values and reporting exact-match, latency, acceptance, and overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: N-gram speculative decoding for code and templated CPU workloads
- Success threshold: Mean exact-decoding speedup of at least 1.3x on code/log/templated prompts with p10 speedup above 1.0x, exact output match for all prompts, and natural-prose controls reported separately.
- Stop condition: Stop if code/log/templated acceptance is below 35% or mean speedup is below 1.1x after overhead on the medium CPU benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-draft-head-speculative-decoding-on-cpu-28e56fbc376a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
