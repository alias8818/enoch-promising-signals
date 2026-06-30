# Anchored Long-Context Cache with Byte-Exact Retrieval

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchored-long-context-cache-with-byte-exact-retrieval-64c49be9e59e`
Run ID: `anchored-long-context-cache-with-byte-exact-retrieval-64c49be9e59e-20260620T200102665941+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/0e65086e62ef

## What looked useful

On 2,048 queries over 96 generated long contexts totaling 12,564,660 bytes, anchored_span_cache achieved 1.0000 exact match, 0 missing, and 0 byte mismatches. It was 8.38x faster by mean local latency than full_scan and had a 456.34x estimated bytes-touched reduction. Fixed chunk cache reached 0.3584 exact match with 1,314 missing results, and normalized text memory reached 0.0000 exact match with 2,048 byte mismatches.

## Boundaries and scale limits

Synthetic ASCII byte payloads only; no model-in-the-loop QA, semantic retrieval, realistic trace corpus, noisy anchor discovery, duplicate-anchor stress, persistence reload, or production retrieval baseline.

## Claim scope

In deterministic local synthetic contexts with explicit anchors, an anchor-to-byte-span cache retrieved payloads byte-exactly while touching far fewer bytes per query than full-context scanning and avoiding the byte-loss failures of chunked or normalized memory proxies.

## Why it stopped

Synthetic/proxy-only evidence supports the mechanism but is insufficient for publication-grade validation.

## Recommended next action

Stop this run as a no-paper useful signal; run a bounded model-in-the-loop replay follow-up with noisy and duplicate anchors before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Model-in-the-loop anchored byte retrieval replay with noisy anchors
- Success threshold: At least 0.98 byte-exact span recovery on 500 or more model-in-the-loop replay queries, with at least 5x lower estimated bytes touched than full transcript search and no digest-corruption false positives.
- Stop condition: Stop as negative if anchored cache exact-match falls below 0.95, if duplicate/noisy anchors cause unresolved ambiguity above 2 percent, or if persistence reload changes any stored byte digest.

## Evidence references

- Artifact root: `<local-path>/projects/anchored-long-context-cache-with-byte-exact-retrieval-64c49be9e59e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
