# Prompt-Lookup Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `prompt-lookup-speculative-decoding-on-cpu-d6aa8f4c9306`
Run ID: `prompt-lookup-speculative-decoding-on-cpu-d6aa8f4c9306-20260527T045013088939+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/fb6b888c56d8

## What looked useful

Prompt lookup reduced median model forward calls from 64 to 6, 8, and 20 depending on prompt regime, producing median speedups of 4.41x, 2.72x, and 1.55x with exact requested-length prefixes on distilgpt2 CPU generation.

## Boundaries and scale limits

Small-model CPU-only benchmark; three handcrafted prompt regimes; no modern instruction model, quantized runtime, production batching, streaming, real user trace, or long-context corpus validation. Transformers 5.9.0 returned extra tokens beyond max_new_tokens, so full-output equality was not preserved without truncation.

## Claim scope

On this CPU worker, Transformers prompt-lookup speculative decoding with distilgpt2 improved greedy generation latency for 64 requested new tokens on three handcrafted prompts, while preserving the exact requested-length greedy prefix after truncation.

## Why it stopped

No-paper closure: bounded local evidence supports the CPU speedup mechanism, but the benchmark is too narrow and has a max_new_tokens overshoot caveat, so it is not publication-grade validation.

## Recommended next action

Run a bounded deepen study on a modern 0.5B-1.5B CPU-deployable instruction/code model with real repeated-context prompts, explicit truncation/length-control handling, and a prompt_lookup_num_tokens sweep.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Prompt-lookup CPU decoding on modern repeated-context workloads
- Success threshold: Median latency speedup >=1.5x on repeated-context workloads, no median slowdown worse than 5% on low-reuse controls, and 100% requested-prefix equality after truncation.
- Stop condition: Stop if modern-model repeated-context prompts fail exact prefix equality, show median speedup <1.2x after overhead/truncation, or overshoot/length-control behavior cannot be bounded safely.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-lookup-speculative-decoding-on-cpu-d6aa8f4c9306`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
