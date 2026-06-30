# N-Gram Draft Speculative Decoding on 10GB GPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-draft-speculative-decoding-on-10gb-gpu-8cbff99ffc56`
Run ID: `n-gram-draft-speculative-decoding-on-10gb-gpu-8cbff99ffc56-20260529T035843544246+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f91fc069d69e

## What looked useful

Prompt/n-gram lookup drafting is viable for copy-like continuations on GB10 only when the workload has strong prompt reuse and the lookup window is kept small enough to preserve exact output length. It is harmful on the varied control prompt and unsafe for strict length equivalence at k=8/16 in this Transformers harness.

## Boundaries and scale limits

Single model, single GPU host, two synthetic prompt classes, unbatched greedy decoding, 64 generated tokens, five timed repeats; no 7B-class model, production serving stack, real workload distribution, sampling, batching, or acceptance-counter instrumentation.

## Claim scope

On GPT-2 fp16 greedy decoding on a GB10 CUDA host using Transformers prompt_lookup_num_tokens, small n-gram windows accelerated a repeat-heavy prompt with exact outputs, while varied prompts slowed and larger windows over-generated relative to max_new_tokens.

## Why it stopped

Bounded local evidence is mixed: exact speedups appear only on repeat-heavy synthetic prompts with k=2/4, controls slow down, and larger lookup windows violate exact output-length equivalence.

## Recommended next action

Stop this run as no-paper useful signal; a bounded follow-up should test strict max_new_tokens enforcement and acceptance counters on real repeated code/document prompts in a serving backend or patched Transformers path.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Strict-Length Prompt-Lookup Decoding on Real Reuse-Heavy Prompts
- Success threshold: At least 1.25x median speedup with exact outputs on reuse-heavy real prompts, less than 5% median slowdown on low-reuse controls after gating, and no over-generation beyond requested max_new_tokens.
- Stop condition: Stop if strict length cannot be enforced, if exact output equivalence fails, or if reuse-heavy real prompts do not exceed 1.10x median speedup after gating.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-draft-speculative-decoding-on-10gb-gpu-8cbff99ffc56`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
