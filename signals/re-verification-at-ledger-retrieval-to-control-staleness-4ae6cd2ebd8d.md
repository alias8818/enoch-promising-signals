# Re-verification at ledger retrieval to control staleness

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `re-verification-at-ledger-retrieval-to-control-staleness-4ae6cd2ebd8d`
Run ID: `re-verification-at-ledger-retrieval-to-control-staleness-4ae6cd2ebd8d-20260628T020552352339+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d7fccdab20de

## What looked useful

Across 20 synthetic trials of 10,000 queries each, re-verification plus retry reduced stale-answer rate from 0.42558 to 0.0 and lifted accuracy from 0.52483 to 0.97988, at +1.43493 abstract latency units. Verification without retry also removed stale answers but abstained on 0.47517 of queries, showing fallback/current lookup is necessary for utility.

## Boundaries and scale limits

Synthetic-only local simulation; no LLM agent, real operator memory, production retrieval index, ambiguous entity resolution, partial ledger metadata, or wall-clock service latency was tested.

## Claim scope

In a deterministic synthetic ledger with explicit supersession metadata and authoritative current-state lookup, re-verifying retrieved records before answering eliminates stale answers and improves accuracy when the retrieval index is stale-biased.

## Why it stopped

Current run is a synthetic mechanism probe only; it provides useful signal but not direct evidence strong enough for a paper.

## Recommended next action

Run one bounded direct replay evaluation on a real or realistic repeated-agent ledger with supersession labels, ambiguous entity cases, and measured retrieval/verification latency; stop if stale-answer reduction is below 50% or abstention/latency makes utility worse than naive retrieval.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct replay validation of ledger retrieval re-verification
- Success threshold: At least 50% stale-answer-rate reduction versus naive retrieval, no more than +10 percentage-point abstention increase, and less than 2x measured median query latency on the replay corpus.
- Stop condition: Stop as negative if re-verification cannot access reliable current-state metadata, stale-answer reduction is below 50%, or latency/abstention regressions erase the accuracy gain.

## Evidence references

- Artifact root: `<local-path>/projects/re-verification-at-ledger-retrieval-to-control-staleness-4ae6cd2ebd8d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
