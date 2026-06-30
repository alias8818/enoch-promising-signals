# Static pre-distilled n-gram draft table from public corpus

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `static-pre-distilled-n-gram-draft-table-from-public-corpus-d8f0fde9c250`
Run ID: `static-pre-distilled-n-gram-draft-table-from-public-corpus-d8f0fde9c250-20260619T050451364522+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6dad8e1c9970

## What looked useful

Longer n-gram contexts produced higher accepted tokens per proposal when they fired, but coverage collapsed; shorter contexts covered more positions but were too imprecise. The best in-domain table was n=1 at 0.06696 accepted tokens/position versus the unigram baseline at 0.07850.

## Boundaries and scale limits

This is a bounded teacher-forced proxy, not a direct target-model speculative decoding benchmark. It does not test BPE tokenization, GPU decode latency, target-model acceptance/rejection overhead, larger public corpora, or hybrid fallback policies.

## Claim scope

On a public Tiny Shakespeare train/held-out split with lowercase regex tokenization and 4-token drafts, naive static n-gram continuation tables for n=1..5 did not beat an always-propose unigram baseline on accepted tokens per evaluated position; cross-domain Alice in Wonderland performance was worse for every n.

## Why it stopped

Bounded public-corpus proxy provided an early falsification of the naive static n-gram draft table as a standalone useful draft source, not a full validation of all possible hybrid methods.

## Recommended next action

Stop the naive standalone static-table line; only revisit with a hybrid fallback policy and direct target-model speculative decoding wall-clock benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hybrid static n-gram fallback for target-model speculative decoding
- Success threshold: At least 5% net wall-clock decoding speedup over the fallback-only baseline on an in-domain public corpus, with no more than 2% slowdown cross-domain.
- Stop condition: Stop if accepted tokens per evaluated position remains below fallback-only or if lookup/verification overhead removes measured wall-clock speedup.

## Evidence references

- Artifact root: `<local-path>/projects/static-pre-distilled-n-gram-draft-table-from-public-corpus-d8f0fde9c250`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
