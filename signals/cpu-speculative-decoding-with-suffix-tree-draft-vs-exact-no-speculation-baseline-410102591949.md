# CPU speculative decoding with suffix-tree draft vs exact no-speculation baseline

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-speculative-decoding-with-suffix-tree-draft-vs-exact-no-speculation-baseline-410102591949`
Run ID: `cpu-speculative-decoding-with-suffix-tree-draft-vs-exact-no-speculation-baseline-410102591949-20260622T004840926972+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f2f77c424514

## What looked useful

Suffix drafting preserved exact output and produced 83.27% exact-call reduction with 1.91x wall speedup on highly periodic streams, but lost on copied-span and random controls because suffix lookup/update overhead dominated despite call reduction.

## Boundaries and scale limits

Not a real LLM serving benchmark; exact model cost is proxied by deterministic CPU work, verification is oracle-based, and the suffix index is a Python bounded suffix table rather than an optimized suffix tree or rolling-hash implementation.

## Claim scope

Bounded synthetic CPU benchmark of suffix-index speculative drafting versus an exact no-speculation oracle baseline over 30k-token periodic, copied-span, and random streams.

## Why it stopped

Proxy/local benchmark produced mixed evidence rather than a direct paper-ready validation: the mechanism works on highly repetitive streams but the naive CPU suffix-index implementation is slower than exact baseline on broader controls.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should implement low-overhead rolling-hash suffix lookup plus adaptive gating before testing on a small real CPU language-model harness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive rolling-hash suffix draft on a small real CPU LM
- Success threshold: At least 1.2x median wall-clock speedup on repetitive prompts with no more than 5% slowdown on low-repetition controls and exact output equality across all prompts.
- Stop condition: Stop if optimized suffix lookup plus adaptive gating still causes more than 5% slowdown on low-repetition controls or fails to reach 1.2x median speedup on repetitive prompts.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-speculative-decoding-with-suffix-tree-draft-vs-exact-no-speculation-baseline-410102591949`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
