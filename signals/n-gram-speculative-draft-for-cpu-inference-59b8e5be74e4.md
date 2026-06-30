# N-gram Speculative Draft for CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-draft-for-cpu-inference-59b8e5be74e4`
Run ID: `n-gram-speculative-draft-for-cpu-inference-59b8e5be74e4-20260528T203513459376+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2f06b4594a63

## What looked useful

Simple n-gram drafting has a real repeated-context mechanism: repeated text reached 4.64x modeled speedup at draft length 8 and rho=0.1. On natural/code traces, draft length 8 averaged 0.91x and was only marginally positive on Linux code; draft length 4 averaged about 1.12x under optimistic verification cost, while draft length 16 fell to about 0.65x. This supports short, telemetry-gated n-gram drafting for repetitive/code contexts and argues against ungated long n-gram drafts as a general CPU decoding accelerator.

## Boundaries and scale limits

No live LLM decoding loop, no measured transformer CPU wall-clock serving, no quality evaluation, and only small public text/code traces up to 180k BPE tokens. Results should not be read as full validation for 7B-class or production CPU inference.

## Claim scope

Trace-level BPE-token evaluation of suffix n-gram speculative drafting on three small natural/code corpora plus a repeated-text positive control, using online/static caches and an analytic CPU verification cost model.

## Why it stopped

Stopped after a bounded proxy/early mechanism test: evidence is useful but not full model-serving validation or paper-ready.

## Recommended next action

Run a bounded direct CPU decoding follow-up with a GPT-2-small-class or llama.cpp-compatible small model, comparing greedy baseline versus online n-gram drafting on repetitive, code, and prose prompts with wall-clock tokens/sec and acceptance telemetry.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU LLM decoding benchmark for telemetry-gated n-gram speculative drafting
- Success threshold: At least 1.15x wall-clock throughput on repetitive/code prompt categories with no exact-output regression for greedy decoding, and automatic backoff limiting prose slowdown to less than 3%.
- Stop condition: Stop if direct CPU wall-clock speedup is below 1.05x on repetitive/code prompts or if prose slowdown exceeds 5% after telemetry gating.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-draft-for-cpu-inference-59b8e5be74e4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
