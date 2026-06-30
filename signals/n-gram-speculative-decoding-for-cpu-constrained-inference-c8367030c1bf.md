# N-gram Speculative Decoding for CPU-Constrained Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-decoding-for-cpu-constrained-inference-c8367030c1bf`
Run ID: `n-gram-speculative-decoding-for-cpu-constrained-inference-c8367030c1bf-20260607T084409277177+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/240bf78d3f82

## What looked useful

Best pass reduction was 8.316% at n=2,gamma=12 but modeled CPU speed was 0.633x baseline; best modeled speed among configurations with at least 1% pass reduction was 0.974x at only 1.505% pass reduction. No tested meaningful-reduction configuration exceeded 1.0x estimated CPU speed.

## Boundaries and scale limits

Single corpus, regex tokenizer, trace-based target continuation, no real LLM logits/KV-cache/runtime integration, and CPU feed-forward proxy for verification cost. Does not cover repetition-heavy prompts, code editing, RAG copy tasks, or production model runtimes.

## Claim scope

On an 80,000-token Tiny Shakespeare regex-token trace with online prompt-local n-gram proposals and a local NumPy CPU verification-cost proxy, naive n-gram speculation modestly reduces target passes but does not produce an estimated CPU speedup for any configuration with meaningful pass reduction.

## Why it stopped

Proxy/early falsification of practical CPU speedup for naive prompt-local n-gram speculation on an ordinary natural-language trace; not a full validation or universal negative.

## Recommended next action

Stop this proxy run; the concrete next evidence step is a bounded direct CPU LLM integration test on repetition-heavy and ordinary prompts with wall-clock tokens/sec versus baseline decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU LLM n-gram speculative decoding on ordinary versus repetition-heavy prompts
- Success threshold: At least 1.15x wall-clock tokens/sec on a predeclared repetition-heavy workload without more than 2% slowdown on ordinary prompts, across at least 100 generated continuations per bucket.
- Stop condition: Stop if ordinary and repetition-heavy workloads both stay below 1.05x wall-clock speedup or if implementation overhead causes more than 5% slowdown in baseline-equivalent no-proposal cases.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-decoding-for-cpu-constrained-inference-c8367030c1bf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
