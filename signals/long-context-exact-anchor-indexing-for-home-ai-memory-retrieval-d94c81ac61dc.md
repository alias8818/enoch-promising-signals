# Long-context exact anchor indexing for home AI memory retrieval

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `long-context-exact-anchor-indexing-for-home-ai-memory-retrieval-d94c81ac61dc`
Run ID: `long-context-exact-anchor-indexing-for-home-ai-memory-retrieval-d94c81ac61dc-20260613T160800453036+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/32895b5f366b

## What looked useful

Exact anchor dictionary lookup recovered the correct span for 100% of 500 anchored queries per corpus size with 0.00414 ms mean latency at 50k records, versus 0.61447 ms for full-context scan. Anchorless lexical hit@5 fell to 0.002 at 50k records, showing exact anchors are useful as a rehydration layer but not a standalone natural-language retrieval solution.

## Boundaries and scale limits

No real household traces, no human-written query set, no LLM anchor-selection component, no persistent database integration, and no stress test for anchor corruption/versioning/multi-record answers. Largest context was 8.69 MB and 50k records.

## Claim scope

Synthetic, dependency-free benchmark of exact-anchor rehydration over 1k, 10k, and 50k generated home-memory records. Exact anchors support deterministic exact-span lookup when the query already contains the anchor.

## Why it stopped

No-paper useful signal: the mechanism is supported in synthetic direct tests, but end-to-end home AI memory retrieval remains unvalidated.

## Recommended next action

Run a bounded two-stage evaluation on realistic home-memory notes where semantic retrieval or an LLM must select the anchor before exact rehydration; stop treating this synthetic mechanism result as paper-ready.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Two-stage home-memory anchor selection plus exact rehydration
- Success threshold: At least 90% exact span/citation accuracy on 300 or more held-out realistic queries, with statistically meaningful improvement over the no-anchor baseline and median added rehydration latency below 5 ms.
- Stop condition: Stop if anchor selection accuracy is below 70% or if exact rehydration adds operational complexity without improving exact evidence recovery over the baseline.

## Evidence references

- Artifact root: `<local-path>/projects/long-context-exact-anchor-indexing-for-home-ai-memory-retrieval-d94c81ac61dc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
