# End-to-end CPU n-gram speculative decoding benchmark

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `end-to-end-cpu-n-gram-speculative-decoding-benchmark-883a9c8707`
Run ID: `end-to-end-cpu-n-gram-speculative-decoding-benchmark-883a9c8707-20260525T212441007865+0000`

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
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c88017cb2969

## What looked useful

Single-threaded confirmation over 5 repeats showed exact output in all scenarios, 1.646x mean speedup with 88.9% target-call reduction on periodic prompts, 1.646x mean speedup with 88.1% target-call reduction on mixed prompts, and 0.658x mean speed on a low-repetition control with zero accepted draft tokens.

## Boundaries and scale limits

The target verifier is controlled/synthetic rather than a real Transformer or GGUF CPU model; results do not measure tokenizer effects, natural-corpus acceptance, KV-cache behavior, real attention/MLP kernels, or production serving overheads.

## Claim scope

Controlled Tier 1 CPU benchmark with a deterministic CPU-bound target verifier: n-gram speculative greedy decoding preserved exact output and improved throughput when prompt continuations were highly draftable, while a low-repetition control showed slowdown with no target-call reduction.

## Why it stopped

Controlled CPU mechanism support is not publication-grade evidence; the run did not validate a real neural model stack.

## Recommended next action

Stop this run as no-paper useful signal; next run should repeat the exactness/throughput protocol on a small real CPU causal LM or GGUF runtime with prompt-lookup n-gram drafts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU LM prompt-lookup n-gram speculative decoding confirmation
- Success threshold: Exact output for all prompts, at least 1.2x mean speedup on repetitive real-text/code prompts, and a control result that links speedup or slowdown to measured target-call reduction and acceptance.
- Stop condition: Stop as negative if exactness fails, if repetitive real-model speedup is below 1.2x after implementation tuning, or if the low-repetition control speeds up without corresponding target-call reduction.

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-cpu-n-gram-speculative-decoding-benchmark-883a9c8707`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
