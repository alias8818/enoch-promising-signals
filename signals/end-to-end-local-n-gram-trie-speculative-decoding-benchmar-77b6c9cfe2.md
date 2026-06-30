# End-to-end local n-gram trie speculative decoding benchmark

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `end-to-end-local-n-gram-trie-speculative-decoding-benchmar-77b6c9cfe2`
Run ID: `end-to-end-local-n-gram-trie-speculative-decoding-benchmar-77b6c9cfe2-20260608T012225687128+0000`

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

- Parent run decision: N-gram Trie Draft for Local Speculative Decoding: enoch://control-plane/projects/n-gram-trie-draft-for-local-speculative-decoding-623114e7e62f/runs/n-gram-trie-draft-for-local-speculative-decoding-623114e7e62f-20260607T211010775289+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/b929845421d7

## What looked useful

Primary distilgpt2 fp32 run matched greedy output on all prompts, reduced target forward calls by 43.88% on average, and achieved 2.26x mean wall-clock speedup; draft-length ablation showed forward-call reduction rising from 27.55% at draft length 2 to 51.53% at draft length 8. A tiny-gpt2 control accepted no proposals, showing the effect depends on target agreement with local repetition.

## Boundaries and scale limits

Only four prompts, small GPT-2-family models, greedy decoding, fp32 primary exactness, and a simple Python verifier with cache recomputation after mismatches. No production serving, large-model, batched, sampling, long-context, or broad-corpus validation.

## Claim scope

Tier 1 small direct benchmark: for distilgpt2 fp32 greedy decoding on four local prompts, a prompt/history-local n-gram trie proposer preserved exact greedy output and reduced target forward calls when the target model followed local repetition or code-like structure.

## Why it stopped

No-paper useful signal: Tier 1 direct evidence supports the mechanism but is too small and implementation-limited for publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up with a cache-preserving verifier on a larger prompt corpus and GPT-2-small-class or larger targets before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cache-preserving n-gram trie speculative decoding on a broader prompt corpus
- Success threshold: Exact greedy-token match on at least 99.5% of prompts under the chosen numeric policy, at least 25% target forward-call reduction on repetition/code-heavy subsets, and less than 5% latency regression on low-repetition prompts.
- Stop condition: Stop if exactness cannot be maintained under the numeric policy or if forward-call reduction is below 10% on repetition/code-heavy subsets after cache-preserving implementation.

## Evidence references

- Artifact root: `<local-path>/projects/end-to-end-local-n-gram-trie-speculative-decoding-benchmar-77b6c9cfe2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
