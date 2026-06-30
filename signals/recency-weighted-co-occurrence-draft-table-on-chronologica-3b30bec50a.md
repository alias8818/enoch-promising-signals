# Recency-weighted co-occurrence draft table on chronological real text

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `recency-weighted-co-occurrence-draft-table-on-chronologica-3b30bec50a`
Run ID: `recency-weighted-co-occurrence-draft-table-on-chronologica-3b30bec50a-20260522T184042825828+0000`

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

- Parent run decision: Recency-Weighted Co-occurrence Draft Table: enoch://control-plane/projects/recency-weighted-co-occurrence-draft-table-7a05b2129535/runs/recency-weighted-co-occurrence-draft-table-7a05b2129535-20260522T175004441374+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/77a8ea6ac213

## What looked useful

Best recency half-life was 4 documents. It improved over unweighted co-occurrence by +0.00531 hit@5, +0.01374 hit@10, and +0.00453 MRR; document-bootstrap CIs for hit@5 and MRR deltas were above zero.

## Boundaries and scale limits

Single real chronological corpus, 120147 held-out word tokens, bounded window/top-candidate draft table, no neural speculative-decoding acceptance test, no second-domain replication.

## Claim scope

In a Tier 1 past-only chronological evaluation on 60 U.S. inaugural addresses, a bounded word-level recency-weighted co-occurrence draft table improved next-token draft hit rates over an unweighted co-occurrence table.

## Why it stopped

No-paper closure: this run produced a useful direct small-corpus signal, but evidence is too narrow for publication readiness.

## Recommended next action

Run a bounded deepen follow-up on an additional timestamped real-text corpus with BPE-token tables and a shuffled-order control before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replicate recency-weighted draft tables on a second timestamped corpus with BPE tokens
- Success threshold: Best recency setting beats unweighted co-occurrence by at least +0.005 absolute hit@5 and has a paired time-block bootstrap 95% CI lower bound above zero on both the original and second corpus.
- Stop condition: Stop as no-paper negative if the second corpus shows <=0 hit@5 delta versus unweighted co-occurrence or the shuffled-order control matches/exceeds the chronological recency gain.

## Evidence references

- Artifact root: `<local-path>/projects/recency-weighted-co-occurrence-draft-table-on-chronologica-3b30bec50a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
