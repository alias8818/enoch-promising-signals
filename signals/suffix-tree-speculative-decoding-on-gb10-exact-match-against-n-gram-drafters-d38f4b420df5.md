# Suffix-Tree Speculative Decoding on GB10: Exact Match Against N-Gram Drafters

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-speculative-decoding-on-gb10-exact-match-against-n-gram-drafters-d38f4b420df5`
Run ID: `suffix-tree-speculative-decoding-on-gb10-exact-match-against-n-gram-drafters-d38f4b420df5-20260629T040021936794+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1af9aa073b79

## What looked useful

Longest-suffix drafting improved speedup proxy over the best fixed n-gram by only 0.5% on periodic motifs and 1.8% on ambiguous short-context motifs, tied on low-reuse Markov data, and produced near-zero accepted proposals on the low-reuse control.

## Boundaries and scale limits

No neural target model, no real LLM-tokenized corpus, no GPU serving path, no lookup-overhead-adjusted latency, and no production suffix-tree implementation were tested.

## Claim scope

Bounded offline exact-match simulation on three deterministic synthetic token streams with 80k train tokens, 30k held-out tokens, draft length 8, and fixed n-gram versus longest-suffix frequency drafters.

## Why it stopped

Proxy/local evidence is mixed: suffix matching helps controlled repetition but does not materially beat the best simple n-gram baseline and is likely inefficient on low-reuse streams.

## Recommended next action

Stop this run as no-paper useful signal; next bounded step is a real-token trace benchmark with acceptance gating before any GB10/GPU integration.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-token suffix drafting with confidence gating against tuned n-gram baselines
- Success threshold: At least 10% improvement over the best tuned n-gram baseline on verifier calls or end-to-end latency across multiple real corpora, with rejected proposal rate low enough to preserve the win after lookup overhead.
- Stop condition: Stop if gated suffix drafting fails to beat the best tuned n-gram baseline by 5% on two real-token corpora or if lookup overhead erases the verifier-call savings.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculative-decoding-on-gb10-exact-match-against-n-gram-drafters-d38f4b420df5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
