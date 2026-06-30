# Hierarchical Evidence Ledger for Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hierarchical-evidence-ledger-for-long-context-4e00d38ace31`
Run ID: `hierarchical-evidence-ledger-for-long-context-4e00d38ace31-20260608T152405228110+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/5bdd7ad33d59

## What looked useful

Hierarchy reduced mean scanned spans from 52,200 to 65.9 with 100% accuracy and proof completeness, but the flat exact evidence index achieved the same accuracy/proof completeness with 3.0 scanned spans and 13x faster query time.

## Boundaries and scale limits

Synthetic schema-controlled evidence only; 1,000 queries; no LLM extraction, embedding retrieval, update/delete stress test, real corpora, adversarial paraphrase, or million-token serving workload.

## Claim scope

On a deterministic synthetic 52,200-span long-context benchmark with explicit 3-hop evidence links, a hierarchical evidence ledger preserved complete proof chains and avoided full-context scans, but it was dominated by a simpler flat exact evidence index.

## Why it stopped

Bounded synthetic evidence supports the provenance mechanism but early-falsifies the stronger novelty claim versus a flat exact index; this is not full validation and not paper-ready.

## Recommended next action

Stop this run as no-paper useful evidence; next bounded test should compare hierarchical ledgers against flat indexes when evidence links must be extracted from free text and updated over time.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Free-text and update stress test for hierarchical evidence ledgers
- Success threshold: At equal or higher proof completeness, the hierarchical ledger should reduce update or query cost by at least 2x versus the strongest flat baseline on a corpus of at least 100k spans with nontrivial extraction noise.
- Stop condition: Stop if the flat baseline matches proof completeness and remains within 1.25x of hierarchy on both query and update cost, or if extraction noise dominates both systems so ledger structure cannot be evaluated.

## Evidence references

- Artifact root: `<local-path>/projects/hierarchical-evidence-ledger-for-long-context-4e00d38ace31`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
