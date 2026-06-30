# Long-Context Memory with Exact Anchors and Compressed State for Home AI

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `long-context-memory-with-exact-anchors-and-compressed-state-for-home-ai-a495c261e634`
Run ID: `long-context-memory-with-exact-anchors-and-compressed-state-for-home-ai-a495c261e634-20260607T102309018504+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/7a69b6f68e37

## What looked useful

Exact anchors are a low-overhead addition to compressed latest-fact state in this controlled task: anchored compressed memory achieved 1.0 joint answer+anchor accuracy, 0.3996 us mean query latency, and 15,475 mean state bytes across 5 trials of 100,000 events, while compressed state without anchors had 0.0 joint accuracy and 0.7412 answer accuracy.

## Boundaries and scale limits

No real household transcripts, LLM-integrated generation, neural compression, embedding retrieval, privacy deletion, adversarial noise, or long-term multi-device persistence were tested. The benchmark has finite structured subjects and values, so it is a mechanism probe rather than a broad deployment validation.

## Claim scope

On deterministic synthetic household event logs with latest-value factual queries, a compact memory state that stores exact source message ids preserves 100% answer and anchor accuracy while using about 1/1210th of the retained state size of full-log scanning.

## Why it stopped

Bounded synthetic mechanism evidence supports the anchor-plus-compression design, but this is not full validation of home-AI long-context memory and is not publication-grade.

## Recommended next action

Stop this run as no-paper useful signal; next run should evaluate an LLM-integrated anchored memory layer on semi-real transcripts with human-labeled answers and citation correctness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-integrated exact-anchor memory on semi-real home transcripts
- Success threshold: Anchored compressed memory reaches at least 0.90 answer accuracy and 0.90 citation precision, beats summary-only memory by at least 20 percentage points in citation precision, and uses at most 25% of full-transcript context tokens.
- Stop condition: Stop if anchored compressed memory citation precision is below 0.75 or answer accuracy drops more than 10 percentage points below full transcript retrieval on the labeled transcript benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/long-context-memory-with-exact-anchors-and-compressed-state-for-home-ai-a495c261e634`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
