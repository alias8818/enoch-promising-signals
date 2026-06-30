# Compressed-state long-context memory with exact-anchor decoding on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `compressed-state-long-context-memory-with-exact-anchor-decoding-on-cpu-a1aa11cadff6`
Run ID: `compressed-state-long-context-memory-with-exact-anchor-decoding-on-cpu-a1aa11cadff6-20260619T140832692770+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/88573e2fcf6e

## What looked useful

Exact anchors are necessary and sufficient for exact recall in this controlled compressed-state setting; lossy summaries alone cannot recover exact values, and anchor overflow creates predictable misses. The result is useful as a bounded mechanism check, not as publication-grade long-context memory evidence.

## Boundaries and scale limits

Synthetic key/value workload only; no LLM decoding, no real document corpus, no learned compression policy, no adversarial query distribution, and no validation above 50000 facts or 5000 queries. Anchor capacity was complete for the positive mechanism test, so the result does not solve anchor selection under tight budgets.

## Claim scope

In a deterministic synthetic CPU benchmark with 50000 generated key/value facts and 5000 exact recall queries, compressed state plus a complete exact-anchor table preserved 100% exact recall while using 2.87x fewer bytes than full transcript storage and reducing mean lookup latency from 1558.428 us to 2.238 us. Lossy compressed summaries without exact anchors had 0% exact recall, and an undersized anchor table fell to 19.5% recall.

## Why it stopped

Proxy synthetic benchmark supports the exact-anchor mechanism but is insufficient for full validation or a paper claim.

## Recommended next action

Stop this run as a no-paper useful signal; the next concrete step would be a bounded model-in-the-loop follow-up on real long-document QA with explicit anchor-selection budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Model-in-the-loop exact-anchor long-document QA under anchor budgets
- Success threshold: At a matched compressed-state budget, exact-anchor decoding improves exact-match accuracy by at least 20 percentage points over summary-only and reaches at least 90% of full-context exact-match accuracy while using at least 2x less context/state than full replay.
- Stop condition: Stop if exact-anchor decoding fails to beat summary-only by 10 percentage points, if gains disappear across two independent corpus slices, or if anchor storage exceeds 50% of full-context bytes without matching full-context accuracy.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-state-long-context-memory-with-exact-anchor-decoding-on-cpu-a1aa11cadff6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
