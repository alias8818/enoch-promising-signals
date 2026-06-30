# KV-cache aware GPT-2 prompt-lookup speculative decoding benchmark

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-aware-gpt-2-prompt-lookup-speculative-decoding-be-7b3be23996`
Run ID: `kv-cache-aware-gpt-2-prompt-lookup-speculative-decoding-be-7b3be23996-20260528T131543262823+0000`

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

- Parent run decision: N-gram Suffix Draft for GPT-2 Speculative Decoding: enoch://control-plane/projects/n-gram-suffix-draft-for-gpt-2-speculative-decoding-f4e6bb279901/runs/n-gram-suffix-draft-for-gpt-2-speculative-decoding-f4e6bb279901-20260528T090713419826+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9f6fadd21e81

## What looked useful

Prompt lookup showed 3.20x mean speedup and 75.0% mean forward-call reduction on repetitive prompts, plus 2.32x speedup on controls, but exact output equality failed because prompt lookup emitted 65-70 new tokens for a 64-token request.

## Boundaries and scale limits

Small controlled prompt suite, 64 requested new tokens, GPT-2 small only, no production serving stack, no 7B model, and accepted-token internals inferred from forward-call reductions rather than direct acceptance tracing.

## Claim scope

On a four-prompt GPT-2-small greedy decoding benchmark on GB10, Transformers prompt-lookup speculative decoding reduced target forward calls and improved wall-clock latency while producing a prefix-consistent greedy continuation, but it returned more new tokens than requested.

## Why it stopped

Controlled direct test produced useful no-paper evidence: the KV-cache prompt-lookup speed mechanism is supported, but the strict exact-length/exact-output threshold failed without caller-side trimming.

## Recommended next action

Implement or wrap prompt-lookup generation with strict max_new_tokens trimming and direct accepted-token tracing, then rerun the same GPT-2 benchmark plus a modest real-text prompt set.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Strict-length KV-cache prompt-lookup decoding with acceptance tracing
- Success threshold: Across at least 20 prompts, exact greedy output equality for the requested generation length, mean speedup >= 1.5x on repetitive prompts, mean target forward-call reduction >= 40%, and control-prompt mean speedup >= 0.95x.
- Stop condition: Stop if strict-length exact output equality fails on any prompt or if repetitive-prompt mean speedup is below 1.10x after acceptance tracing confirms low draft acceptance.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-aware-gpt-2-prompt-lookup-speculative-decoding-be-7b3be23996`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
