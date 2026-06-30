# Adaptive Anchor Spacing via Perplexity Monitoring

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `adaptive-anchor-spacing-via-perplexity-monitoring-3d4bfefa25d7`
Run ID: `adaptive-anchor-spacing-via-perplexity-monitoring-3d4bfefa25d7-20260602T221021095159+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2b9313274f67

## What looked useful

Adaptive spacing improved relevant-span coverage from roughly 0.506-0.530 for uniform anchors to 0.970-1.000 for adaptive anchors across clean, mixed, noisy-monitor, and irrelevant-noise synthetic settings. Capped adaptive spacing kept coverage at 0.966-1.000 in clean/noisy cases and 0.969 with irrelevant noise while reducing average max gaps to about 83-94 tokens.

## Boundaries and scale limits

Evidence is synthetic and proxy-only: local perplexity was online unigram surprisal, relevance was constructed, and the metric was nearest-anchor coverage rather than an end-to-end natural-text LM, retrieval, compression, or QA result.

## Claim scope

In synthetic 2048-token documents with fixed 64-anchor budgets, equal-cumulative-surprisal anchor spacing improves coverage of high-surprisal task-relevant spans versus uniform spacing; a max-gap repair preserves most of the gain while limiting low-surprisal blind spots.

## Why it stopped

No-paper useful signal: the local proxy experiment supports the mechanism but is not direct/full validation and cannot justify a publication-grade claim.

## Recommended next action

Run a bounded direct-evidence follow-up using token-level losses from a small pretrained LM on natural text and evaluate whether adaptive anchors improve an end-to-end retrieval or compression metric at equal anchor budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-LM Natural-Text Test of Perplexity-Adaptive Anchors
- Success threshold: Capped adaptive anchors improve the primary end-to-end metric by at least 5 percent relative over uniform anchors at the same anchor count, while keeping max-gap diagnostics within a predeclared cap.
- Stop condition: Stop if capped adaptive anchors fail to beat uniform anchors on the primary end-to-end metric in two natural-text datasets or if gains disappear after controlling for anchor count and max-gap cap.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-anchor-spacing-via-perplexity-monitoring-3d4bfefa25d7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
