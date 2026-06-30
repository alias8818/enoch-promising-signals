# Prompt-lookup speculative decoding for local inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `prompt-lookup-speculative-decoding-for-local-inference-4812746dbdb3`
Run ID: `prompt-lookup-speculative-decoding-for-local-inference-4812746dbdb3-20260531T153853448408+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/cb6a73846e0f

## What looked useful

PLD achieved 2.138x mean speedup on copy-instruction prompts and 1.698x on structured continuations with exact greedy equivalence, while natural continuations were neutral at 0.998x because only 1 of 5 proposed draft tokens was accepted.

## Boundaries and scale limits

Evidence is limited to 12 hand-built prompts, 64 generated tokens per prompt, one 0.5B-class model, greedy decoding, batch size 1, and a minimal Python/Hugging Face harness rather than a production inference engine or real workload trace.

## Claim scope

On a GB10 local GPU with Qwen/Qwen2.5-0.5B and a validation-correct cached decoder, prompt-lookup speculative decoding preserved exact greedy outputs and accelerated hand-built copy-heavy and repeated-structure prompts, but did not accelerate ordinary natural continuations.

## Why it stopped

No-paper closure because the result is a bounded synthetic/local useful signal, not direct production-trace or broad model-scale validation.

## Recommended next action

Run a bounded deepen benchmark on real copy-heavy local inference workloads such as RAG quote extraction, code edit application, or document QA, using the same exact-output validation and latency metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Prompt-lookup decoding on real copy-heavy local inference traces
- Success threshold: At least 1.3x p50 decode latency speedup on copy-heavy workloads with identical greedy outputs and no more than 3% slowdown on the non-copy control set.
- Stop condition: Stop if real copy-heavy traces show less than 1.1x p50 speedup or if maintaining exact greedy equivalence requires cache recomputation that removes the latency benefit.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-lookup-speculative-decoding-for-local-inference-4812746dbdb3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
