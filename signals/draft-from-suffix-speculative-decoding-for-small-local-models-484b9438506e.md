# Draft-from-Suffix Speculative Decoding for Small Local Models

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `draft-from-suffix-speculative-decoding-for-small-local-models-484b9438506e`
Run ID: `draft-from-suffix-speculative-decoding-for-small-local-models-484b9438506e-20260608T140525931192+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/92313955d92d

## What looked useful

On GPT-2 with 192 generated tokens across four prompts, suffix-speculative decoding matched greedy output exactly while reducing target forwards from 192 to 66 (65.625% reduction, 0.34375 forwards/token). A GPT-2 draft-length sweep preserved exact equality and improved forward reduction from 37.5% at max_draft=2 to 68.75% at max_draft=16.

## Boundaries and scale limits

Handcrafted short prompts only; no real trace corpus, no sampling, no batching, no production KV-cache serving integration, no latency percentiles, and no larger local model validation.

## Claim scope

Bounded local greedy-decoding mechanism test: suffix-copy drafts verified by the target model preserved exact greedy output and reduced target forward calls on four short prompts using tiny-gpt2 and GPT-2 small-class local inference.

## Why it stopped

Evidence supports the bounded mechanism but remains a short handcrafted-prompt local benchmark, not a full validation or paper-ready production serving result.

## Recommended next action

Stop this worker run as a no-paper useful signal; the next bounded direct test is a trace-based KV-cache serving benchmark on real local-model prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-Based KV-Cache Benchmark for Suffix-Draft Speculative Decoding
- Success threshold: Exact greedy output equality on all evaluated prompts plus at least 20% median latency reduction and no worse than 5% p95 latency regression on the full trace.
- Stop condition: Stop if exact equality fails, suffix matching overhead exceeds saved target work, or median latency improvement is below 10% on both models after KV-cache integration.

## Evidence references

- Artifact root: `<local-path>/projects/draft-from-suffix-speculative-decoding-for-small-local-models-484b9438506e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
