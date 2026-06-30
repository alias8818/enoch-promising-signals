# Semantic Compression Paired with Exact Anchor Spans

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `semantic-compression-paired-with-exact-anchor-spans-cfe68a6d019b`
Run ID: `semantic-compression-paired-with-exact-anchor-spans-cfe68a6d019b-20260628T232314787056+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/aa15f41a92c5

## What looked useful

Semantic text and exact anchors address complementary failure modes: semantic claims route queries to the intended fact, while anchor dereferencing restores exact quote-level evidence that lossy compression removes.

## Boundaries and scale limits

Synthetic documents, deterministic compression, lexical retrieval, no LLM-generated summaries, no real corpus, no mutation or anchor-drift testing, and no end-to-end answer generation.

## Claim scope

On a deterministic synthetic fact-retrieval benchmark with near-match distractors, lossy semantic claims paired with exact character spans preserved exact answer sentences at about 6.6% stored-character budget, while semantic-only compression at the same budget retrieved the right fact but lost exact answer text.

## Why it stopped

Synthetic/proxy evidence supports the mechanism but is not direct full validation of real semantic compression systems.

## Recommended next action

Stop this run as no-paper useful signal; next run should test real documents with LLM-generated compressed claims, exact byte/character anchors, and anchor-drift checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-document semantic compression with exact anchor drift checks
- Success threshold: At least 90% exact evidence-span recovery at 80% or greater stored-text reduction, with a statistically meaningful improvement over summary-only compression on exact-answer accuracy.
- Stop condition: Stop if generated summaries cannot retrieve the correct anchored fact above 75% or if anchor drift exceeds 5% after realistic document normalization.

## Evidence references

- Artifact root: `<local-path>/projects/semantic-compression-paired-with-exact-anchor-spans-cfe68a6d019b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
