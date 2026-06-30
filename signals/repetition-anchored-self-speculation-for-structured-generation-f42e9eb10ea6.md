# Repetition-Anchored Self-Speculation for Structured Generation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `repetition-anchored-self-speculation-for-structured-generation-f42e9eb10ea6`
Run ID: `repetition-anchored-self-speculation-for-structured-generation-f42e9eb10ea6-20260621T134922097317+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/eb7eeb8e14a3

## What looked useful

Float32 confirmation showed structured prompts had 28.75% fewer target calls and 31.31% lower wall-clock with all outputs exact to greedy; prose controls had only 1.63% fewer calls and 1.54% lower wall-clock. A bf16 run reproduced the structured speed signal but exposed an exactness caveat on one prose control, indicating dtype/kernel consistency matters.

## Boundaries and scale limits

Tested only 6 structured prompts and 6 prose controls, one model, greedy decoding, full-context forwards, and synthetic prompts. Not validated on optimized KV-cache serving, larger models, constrained JSON decoders, real structured-output benchmarks, or multiple dtype/kernel configurations.

## Claim scope

On one cached small causal LM (Qwen/Qwen2.5-0.5B-Instruct) with synthetic repeated JSON-like prompts, a simple repetition-anchored self-drafter plus exact target verification reduced greedy target-model forward calls while preserving float32 greedy outputs exactly.

## Why it stopped

Bounded local evidence supports the mechanism, but the experiment is too small and synthetic for a paper-positive claim.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded work should implement KV-cache verification and test exactness/speed on a real structured-output benchmark across at least two model families.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache repetition-anchor speculation on real structured-output benchmarks
- Success threshold: All speculative outputs exactly match greedy outputs; structured tasks show at least 20% lower mean target calls or latency with no schema-validity loss; prose controls show less than 5% mean improvement or a clearly smaller effect.
- Stop condition: Stop if exactness cannot be maintained under deterministic verification, or if structured-task improvement is below 10% after anchor/block ablation on two model families.

## Evidence references

- Artifact root: `<local-path>/projects/repetition-anchored-self-speculation-for-structured-generation-f42e9eb10ea6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
