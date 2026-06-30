# Suffix N-Gram Speculative Decoding for Tiny Local LLMs

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-n-gram-speculative-decoding-for-tiny-local-llms-94add5c41be6`
Run ID: `suffix-n-gram-speculative-decoding-for-tiny-local-llms-94add5c41be6-20260609T015353409995+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/6efc1435e55d

## What looked useful

SmolLM2-135M with suffix_n=2 and draft_k=8 reduced estimated target iterations by 43.3% overall, but the effect was highly workload-dependent: 82.8% on repeat prompts, 53.1% on structured prompts, 28.9% on code prompts, and only 6.3% on prose prompts.

## Boundaries and scale limits

Tested only 16 handcrafted prompts per main model, up to 64 generated tokens, with trace replay rather than an optimized KV-cached speculative decoder. distilgpt2 results are confounded by degenerate repeated whitespace/newline outputs; SmolLM2-135M is the main non-degenerate evidence.

## Claim scope

On short greedy traces from tiny local decoder models, suffix n-gram drafting can reduce estimated target verification iterations when outputs are repetitive or template-like; it is weak on open prose in the SmolLM2-135M prompt set.

## Why it stopped

Trace-level evidence supports the mechanism in narrow cases but does not provide direct wall-clock decoding speed or broad workload robustness; this is a bounded proxy result, not full validation.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded action is to implement a KV-cached verifier and route suffix n-gram drafting only on repetition/template indicators.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cached suffix n-gram speculative decoder for SmolLM2-135M
- Success threshold: At least 20% median wall-clock latency reduction on structured/repetitive prompts, no more than 5% median slowdown on prose prompts, and stable output equality with greedy baseline under deterministic decoding.
- Stop condition: Stop if verifier batching or n-gram bookkeeping causes more than 5% slowdown on two consecutive prompt groups, or if structured/repetitive groups fail to exceed 10% median speedup.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-n-gram-speculative-decoding-for-tiny-local-llms-94add5c41be6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
