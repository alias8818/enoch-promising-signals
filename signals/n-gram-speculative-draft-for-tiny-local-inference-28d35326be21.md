# N-gram speculative draft for tiny local inference

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-speculative-draft-for-tiny-local-inference-28d35326be21`
Run ID: `n-gram-speculative-draft-for-tiny-local-inference-28d35326be21-20260608T044637010741+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/b2be2b147e7d

## What looked useful

For repetitive and code-like local prompts, n-gram speculative drafting achieved high acceptance and exact greedy equivalence; gamma=4 averaged 4.240x fewer target forwards and 4.386x wall speedup overall, while gamma=8 averaged 6.635x fewer target forwards and 6.650x wall speedup.

## Boundaries and scale limits

Handcrafted small prompt suites, 64-token continuations, distilgpt2 only, greedy decoding only, simple PyTorch loop, no KV-cache-aware serving integration, no real user trace distribution, no modern 0.5B-3B local model.

## Claim scope

In a bounded distilgpt2 greedy-decoding benchmark on 24 short local prompts, an exact verifier-correct n-gram prompt/history lookup drafter reduced target forward calls and wall-clock time with zero output mismatches.

## Why it stopped

No-paper closure: the result is a useful bounded signal but depends on small handcrafted prompts and a distilgpt2 greedy proxy rather than direct production local-inference evidence.

## Recommended next action

Run a bounded KV-cache-aware follow-up on a modern 0.5B-3B local model with public or collected prompt traces before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache n-gram speculative drafting on modern tiny local models
- Success threshold: Zero greedy mismatches and at least 1.5x median tokens/sec improvement on repetitive/code-like subsets with no more than 10% regression on natural prompts.
- Stop condition: Stop if exactness fails, median tokens/sec improvement is below 1.2x on repetitive/code-like subsets, or natural prompts regress by more than 10%.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-draft-for-tiny-local-inference-28d35326be21`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
