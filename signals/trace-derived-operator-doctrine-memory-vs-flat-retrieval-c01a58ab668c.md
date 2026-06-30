# Trace-derived operator-doctrine memory vs flat retrieval

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `trace-derived-operator-doctrine-memory-vs-flat-retrieval-c01a58ab668c`
Run ID: `trace-derived-operator-doctrine-memory-vs-flat-retrieval-c01a58ab668c-20260619T094637210729+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5bf2564d8304

## What looked useful

Across 30 seeds, trace-derived doctrine memory reached mean accuracy 0.8465 versus flat retrieval 0.1351 on adversarial full traces and 0.2697 in the no-label-token control; doctrine beat flat retrieval on 30/30 seeds in both settings.

## Boundaries and scale limits

Synthetic traces only; deterministic fact extraction; hand-coded latent doctrine; no real operator logs, no LLM-based extraction, no embedding/vector retrieval baseline, and no human-rated action-quality scoring.

## Claim scope

In a deterministic synthetic incident-response benchmark with compositional held-out cases and distractor trace text, compact rules mined from prior traces outperform flat bag-of-words kNN retrieval over prior traces.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy-only; it supports the mechanism but not a real-world or publication-grade claim.

## Recommended next action

Run a bounded deepen follow-up on semi-real or human-written incident traces with human-reviewed doctrine extraction, BM25/embedding retrieval baselines, and blinded action-quality scoring.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Human-reviewed trace-derived doctrine memory on semi-real incident traces
- Success threshold: Doctrine memory beats the best flat retrieval baseline by at least 10 percentage points on held-out action accuracy and at least 90% of reviewed doctrine rules are judged faithful to source traces.
- Stop condition: Stop if doctrine memory fails to beat the best retrieval baseline by 10 percentage points, if rule faithfulness falls below 90%, or if the corpus cannot produce compositional held-out cases.

## Evidence references

- Artifact root: `<local-path>/projects/trace-derived-operator-doctrine-memory-vs-flat-retrieval-c01a58ab668c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
