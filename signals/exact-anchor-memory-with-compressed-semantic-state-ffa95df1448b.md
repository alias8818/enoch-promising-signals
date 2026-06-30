# Exact-Anchor Memory with Compressed Semantic State

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `exact-anchor-memory-with-compressed-semantic-state-ffa95df1448b`
Run ID: `exact-anchor-memory-with-compressed-semantic-state-ffa95df1448b-20260614T062232538353+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9d7f0382a986

## What looked useful

At 60,000 facts with 8-bit sketches, semantic-only exact recovery was 7.7% with 100% sketch ambiguity, while exact-anchor memory matched the router/full-text control at 97.5% exact accuracy using 4.76% of full text storage. At 24-32 sketch bits, semantic-only matched anchors because sketches became effectively unique under the synthetic value vocabulary.

## Boundaries and scale limits

Proxy-only CPU benchmark; no learned compression, no transformer/GPT-2 integration, no real corpus, no training dynamics, and no long-context serving evaluation. Semantic routing quality was synthetic and hash/index based.

## Claim scope

In a deterministic synthetic exact-recall benchmark with 15,000 to 60,000 facts, exact anchors preserve arbitrary identifier values after compressed semantic routing and use about 4.76% of full-text storage.

## Why it stopped

Proxy synthetic mechanism supported, but evidence is not direct/full validation and is insufficient for paper-positive closure.

## Recommended next action

Stop this run as no-paper useful-signal evidence; the next bounded step is a learned-memory integration against a parameter-matched small transformer baseline on real exact-recall tasks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned Exact-Anchor Memory on Realistic Exact-Recall Tasks
- Success threshold: At equal or lower retained storage than the strongest compressed-memory baseline, improve exact-match recall by at least 10 percentage points on arbitrary identifiers while matching non-exact semantic retrieval within 2 percentage points.
- Stop condition: Stop if anchors fail to beat the parameter-matched compressed baseline by at least 3 percentage points on exact-match recall in a small learned-model pilot, or if gains require retaining full text.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-memory-with-compressed-semantic-state-ffa95df1448b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
