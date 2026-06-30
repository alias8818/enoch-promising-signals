# Exact anchor chain with compressed semantic summary for context reconstruction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-chain-with-compressed-semantic-summary-for-context-reconstruction-75414857ca9e`
Run ID: `exact-anchor-chain-with-compressed-semantic-summary-for-context-reconstruction-75414857ca9e-20260614T070041985869+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/c69875551c26

## What looked useful

Exact anchors supplied disambiguating information that compressed semantic summaries omitted. In the hierarchical collision profile, semantic summaries left all 8 variants tied, two anchors reduced ties to 2 variants, and three anchors achieved 100% exact top-1 re-identification across 640 documents. However, anchor_chain and exact_bag were identical, so the independent value of chain order was not supported.

## Boundaries and scale limits

Synthetic corpus only; deterministic substring scoring only; candidate re-identification from a known pool only; no LLM free-form reconstruction; no real conversation, codebase, or document corpus validation; ordered anchor chains were not better than unordered exact-anchor bags.

## Claim scope

In a deterministic synthetic candidate re-identification benchmark with 80 semantic groups and 8 near-duplicate variants per group, compressed semantic summaries alone did not recover exact variants, while enough exact anchors did.

## Why it stopped

Bounded local evidence supports exact anchors as useful for candidate re-identification, but the stronger ordered-chain context reconstruction claim remains unvalidated and is not paper-ready.

## Recommended next action

Stop this run as no-paper useful signal; next run should test real or realistic multi-turn contexts with unordered-anchor controls, ordered-chain distractors, and LLM-assisted exact reconstruction scoring.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Ordered anchor chains versus unordered exact anchors on realistic context reconstruction
- Success threshold: At the same payload budget, ordered anchor chains reduce exact reconstruction error or ambiguity by at least 25% relative to unordered exact-anchor bags on a held-out realistic corpus.
- Stop condition: Stop if ordered chains fail to outperform unordered exact anchors on the primary metric or if gains appear only on synthetic collision patterns.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-chain-with-compressed-semantic-summary-for-context-reconstruction-75414857ca9e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
