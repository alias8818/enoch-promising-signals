# Exact-Anchor Agent Memory Ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `exact-anchor-agent-memory-ledger-679f7a7192fc`
Run ID: `exact-anchor-agent-memory-ledger-679f7a7192fc-20260523T222931438247+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/032903e20ec6

## What looked useful

Exact-anchor memory achieved 1.000 precision and 0 stale/error rate among answered queries in the default benchmark while coverage fell to 0.7144; naive entity memory kept 1.000 coverage but had 0.7144 precision and 0.2350 stale-rate answered. Low- and high-drift sweeps preserved the same precision/coverage tradeoff.

## Boundaries and scale limits

Tested on structured synthetic line facts only: 40 default trials with 5000 facts and 2000 queries per trial, plus 20-trial low-drift, high-drift, and no-block-shuffle sweeps. No LLM agent, natural-language documents, persistent database, semantic paraphrase relocation, or production retrieval stack was tested.

## Claim scope

In a deterministic synthetic mutable-document benchmark, exact text+hash anchors with digest-index relocation prevent stale and misattributed memory answers by invalidating changed or deleted source spans, at the expected cost of lower coverage.

## Why it stopped

This run produced a reproducible synthetic useful signal, but it is not paper-ready because the core agent behavior and natural-document retrieval setting were only proxied.

## Recommended next action

Run a bounded direct LLM-agent benchmark over mutable real-ish task notes or issue/code files, comparing exact-anchor invalidation against unanchored and line-anchor memory on answer accuracy, abstention, and downstream task success.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct LLM Agent Test for Exact-Anchor Memory Invalidation
- Success threshold: Exact-anchor enforcement reduces stale answers by at least 50% relative to unanchored memory with no more than 25 percentage-point task-success loss from abstention on unchanged-source queries.
- Stop condition: Stop if exact-anchor enforcement fails to reduce stale answers by at least 25% in a smoke set of 100 drifted queries, or if abstention prevents measuring downstream task success.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-agent-memory-ledger-679f7a7192fc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
