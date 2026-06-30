# Suffix-Trie Compressed Context with Exact Anchors

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-trie-compressed-context-with-exact-anchors-eff0d81a38da`
Run ID: `suffix-trie-compressed-context-with-exact-anchors-eff0d81a38da-20260621T115704820505+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/55f35adcd078

## What looked useful

Across 15 bounded cases, exact reconstruction passed in all cases. Mean cost-5 compression ratio was 0.0538 for repeat-heavy corpora, 0.5393 for near-duplicate corpora, and 1.0000 for low-repeat corpora.

## Boundaries and scale limits

Synthetic corpora only; no real repeated-agent traces, no end-to-end LLM quality test, no production prompt serialization, and no full compressed suffix-trie implementation. Low-repeat data produced no compression.

## Claim scope

Bounded synthetic CPU benchmark shows exact-anchor compression can reconstruct token streams exactly and substantially reduce repeated exact-span contexts under a simple 3-token/5-token anchor-cost proxy.

## Why it stopped

Proxy/synthetic evidence supports the mechanism but is not a full validation or paper-ready result.

## Recommended next action

Stop this run as no-paper useful signal; next bounded step is a real-trace deepen test with answer-quality controls against raw context and retrieval baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace exact-anchor context compression with answer-quality controls
- Success threshold: At least 30% serialized-token reduction versus raw context with no statistically meaningful drop in exact quote/fact accuracy and lower drift than lossy deduplication.
- Stop condition: Stop if exact reconstruction fails, quote/fact accuracy drops by more than 2 percentage points versus raw context, or serialized-token reduction stays below 15% on real traces.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-trie-compressed-context-with-exact-anchors-eff0d81a38da`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
