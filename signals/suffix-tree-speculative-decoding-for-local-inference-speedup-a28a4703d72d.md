# Suffix-Tree Speculative Decoding for Local Inference Speedup

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-speculative-decoding-for-local-inference-speedup-a28a4703d72d`
Run ID: `suffix-tree-speculative-decoding-for-local-inference-speedup-a28a4703d72d-20260619T205754491974+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3b455a7205b0

## What looked useful

Suffix/prompt lookup speculation is useful when continuation text repeats prompt/history patterns, but it is workload-sensitive and can slow open-ended text. Exactness also depends on robust cache rollback/slicing; bfloat16 plus full-context rebuild produced an open-ended divergence in this harness.

## Boundaries and scale limits

Small prompt set, 0.5B model, greedy decoding only, single request, simple Python/Hugging Face harness, list-scan lookup rather than production suffix tree, naive full-context cache rebuild after rejected drafts, no batching or long agentic traces.

## Claim scope

On three 64-token local greedy-decoding probes with Qwen/Qwen2.5-0.5B-Instruct on GB10, exact float32 suffix/prompt-lookup speculation sped up repetitive code and structured JSON prompts by 1.54x-1.69x wall-clock while slowing an open-ended prompt to 0.93x.

## Why it stopped

Broad suffix-tree speculative decoding is already public, and this run only provides a small local workload-sensitivity probe rather than publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should use a production cache rollback/slicing implementation and longer agentic/code traces to confirm exact bfloat16 speedups.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Production-cache suffix speculation on longer local agentic traces
- Success threshold: Median wall-clock speedup of at least 1.3x on structured/code/agentic traces with exact output match and no more than 5% slowdown on prompts where speculation is disabled by an acceptance gate.
- Stop condition: Stop if exact bfloat16 output cannot be preserved with cache rollback/slicing, or if median speedup on structured/code traces is below 1.15x after acceptance gating.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculative-decoding-for-local-inference-speedup-a28a4703d72d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
