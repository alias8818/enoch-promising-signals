# Suffix-tree speculative decoder with exact no-spec and n-gram baselines on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-speculative-decoder-with-exact-no-spec-and-n-gram-baselines-on-gb10-bc6212cf8aa7`
Run ID: `suffix-tree-speculative-decoder-with-exact-no-spec-and-n-gram-baselines-on-gb10-bc6212cf8aa7-20260628T190811890395+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b7567edcb0a4

## What looked useful

Acceptance rate alone was misleading: the suffix-history drafter reached high acceptance but often generated short draft blocks, so target-forward reduction and wall-clock were worse than a fixed n-gram baseline. A future suffix-tree decoder must optimize continuation length and cache amortization, not only longest suffix match.

## Boundaries and scale limits

No production KV-cache implementation, no optimized suffix-tree construction benchmark, no 7B+ model, no batched serving, no long-corpus evaluation, and only small bounded prompt suites were tested.

## Claim scope

On GB10, an exact greedy suffix-history speculative decoder was compared against exact no-spec greedy decoding and a fixed 4-gram speculative baseline on small GPT-2-class models and bounded prompt suites. The suffix policy can reduce work versus no-spec on repetitive prompts but did not beat the n-gram baseline.

## Why it stopped

Bounded direct CUDA tests falsified the simple suffix-tree-style policy as superior to the n-gram baseline; this is not a full large-model validation, but it is sufficient early evidence against the tested mechanism.

## Recommended next action

Stop this run as no-paper useful signal; only pursue a follow-up if implementing a cache-aware suffix selector with an explicit requirement to beat the n-gram baseline on target forwards and wall-clock.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cache-aware suffix selector versus n-gram speculative decoding
- Success threshold: Suffix selector beats fixed n-gram by at least 15% in wall-clock tokens/s and target-forward count on both natural text and repeated/code-like prompt subsets without any exactness failures.
- Stop condition: Stop if suffix selection overhead or short draft blocks keep suffix within 15% of or below the n-gram baseline after cache-aware implementation on the bounded corpus.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculative-decoder-with-exact-no-spec-and-n-gram-baselines-on-gb10-bc6212cf8aa7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
