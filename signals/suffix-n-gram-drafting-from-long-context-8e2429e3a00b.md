# Suffix N-gram Drafting from Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-n-gram-drafting-from-long-context-8e2429e3a00b`
Run ID: `suffix-n-gram-drafting-from-long-context-8e2429e3a00b-20260608T075542327635+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/98a3a9dfd9b2

## What looked useful

Suffix n-gram drafting is strong on repeated contexts and moderately useful on local Python code, but weak on plain prose. Backoff 8/4/2 accepted the first token at 38.3% of local-code positions with 1.816 mean accepted tokens per position, versus only 10.7-13.7% first-token acceptance and 0.153-0.242 mean accepted tokens on Gutenberg prose.

## Boundaries and scale limits

No LLM tokenizer, neural verifier, serving loop, or large-scale corpus evaluation was run; metrics are exact-token offline acceptance over at most 5000 sampled positions per corpus/setting.

## Claim scope

Offline regex-token benchmark of suffix n-gram continuation drafting from prior long context on synthetic repetition, local Python code, and Gutenberg prose.

## Why it stopped

No-paper useful signal: the mechanism works in offline exact-token tests for repeated/code-like contexts, but model-integrated speculative decoding speedup remains untested.

## Recommended next action

Run a bounded deepen follow-up with a real LLM tokenizer and small transformer verifier on code-completion traces to measure accepted tokens per model call and wall-clock speedup.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Model-Integrated Suffix N-gram Drafting on Code Traces
- Success threshold: At least 1.25x median wall-clock tokens/sec on code traces with identical accepted output and no worse than 5% slowdown on the prose/low-repetition control.
- Stop condition: Stop if accepted draft tokens per verifier call are below 0.5 on code traces or if indexing overhead eliminates speedup in the small-model loop.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-n-gram-drafting-from-long-context-8e2429e3a00b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
