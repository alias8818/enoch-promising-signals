# Operator-Doctrine Memory vs Full-Transcript Search

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `operator-doctrine-memory-vs-full-transcript-search-66668792a2df`
Run ID: `operator-doctrine-memory-vs-full-transcript-search-66668792a2df-20260620T084231367351+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d42d75976a94

## What looked useful

Layered doctrine memory achieved 24/24 accuracy and 9.75 mean context tokens; transcript search and flat retrieval each achieved 12/24 accuracy and failed most updated-rule queries by retrieving stale high-overlap rules.

## Boundaries and scale limits

Synthetic hand-authored scenarios only; no private or real operator transcripts, no LLM answer generation, no automatic doctrine extraction/keying, and no embedding or hybrid retrieval baseline.

## Claim scope

In a small synthetic repeated-agent replay benchmark with stale operator-doctrine updates, keyed layered doctrine memory recovered current rules more accurately and with less context than lexical full-transcript search.

## Why it stopped

Bounded synthetic proxy evidence supports the mechanism but is not direct/full validation and is not publication-grade.

## Recommended next action

Stop this run as no-paper useful evidence; run a bounded deepen test on realistic multi-session transcripts with automatic doctrine extraction/keying and embedding or hybrid retrieval baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Realistic transcript doctrine-memory retrieval benchmark
- Success threshold: Layered doctrine memory improves updated-rule accuracy by at least 20 percentage points over the best transcript-search baseline while reducing mean context tokens by at least 30 percent on at least 100 replay queries.
- Stop condition: Stop as negative if layered memory does not beat the best transcript-search baseline on updated-rule accuracy or if automatic extraction/keying causes more than 10 percent doctrine-key errors.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-vs-full-transcript-search-66668792a2df`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
