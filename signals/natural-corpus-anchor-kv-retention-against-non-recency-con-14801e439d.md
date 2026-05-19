# Natural-Corpus Anchor KV Retention Against Non-Recency Controls

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `natural-corpus-anchor-kv-retention-against-non-recency-con-14801e439d`
Run ID: `natural-corpus-anchor-kv-retention-against-non-recency-con-14801e439d-20260515T155222756578+0000`

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

- Internal Enoch project: Natural-Corpus Anchor KV Retention Against Non-Recency Controls: internal_generated:natural-corpus-anchor-kv-retention-against-non-recency-con-14801e439d

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Tier 2 direct natural-corpus inference evidence supports the mechanism, but the run is limited to GPT-2, one corpus, chunk-level anchors, and a hand-written evaluator, so it is not publication-grade.

## Recommended next action

Do not write a paper from this run; run a bounded deepen follow-up across multiple models and corpora with true document-boundary anchors and paired statistics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-model true-document anchor KV retention validation
- Success threshold: Prefix/document-anchor retention must reduce recency excess NLL by at least 20% and beat every non-anchor old-token control by at least 5% excess-NLL share on each corpus/model pair, with paired confidence intervals excluding zero for the primary comparisons.
- Stop condition: Stop as negative if prefix/document anchors fail the threshold on either model family or if gains vanish after preserving true document boundaries and validated sparse-KV semantics.

## Evidence references

- Artifact root: `<local-path>/projects/natural-corpus-anchor-kv-retention-against-non-recency-con-14801e439d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
