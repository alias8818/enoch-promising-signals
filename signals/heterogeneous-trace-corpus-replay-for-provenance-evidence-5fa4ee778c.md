# Heterogeneous Trace Corpus Replay for Provenance Evidence Ledgers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `heterogeneous-trace-corpus-replay-for-provenance-evidence-5fa4ee778c`
Run ID: `heterogeneous-trace-corpus-replay-for-provenance-evidence-5fa4ee778c-20260528T031313349541+0000`

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

- Parent run decision: Replay Realistic Agent Tool Traces Through a Provenance Evidence Ledger: enoch://control-plane/projects/replay-realistic-agent-tool-traces-through-a-provenance-ev-fa3579e0d8/runs/replay-realistic-agent-tool-traces-through-a-provenance-ev-fa3579e0d8-20260527T233341468950+0000
- Parent run decision: Tiny Agent Evidence Ledger for Tool Safety: enoch://control-plane/projects/tiny-agent-evidence-ledger-for-tool-safety-d6bc36179d7d/runs/tiny-agent-evidence-ledger-for-tool-safety-d6bc36179d7d-20260527T205101480337+0000

## What looked useful

Proposed canonical hash ledger reached mean edge F1 0.9893 and query F1 0.9563 with tamper detection 1.0. The W3C PROV-style source-local baseline reached edge F1 0.3058 and query F1 0.0. Removing alias resolution reduced edge F1 to 0.6804 and query F1 to 0.0; removing the hash chain kept graph F1 but reduced tamper detection to 0.0.

## Boundaries and scale limits

Synthetic generated corpus only: 10 seeds, 30,000 ground-truth events, about 33,600 collected trace records after duplicates/noise. No real operational trace corpus, production provenance database, legal audit process, or distributed multi-host clock-skew validation was tested.

## Claim scope

In a fixed-seed synthetic heterogeneous trace corpus with OpenTelemetry-like, Linux-audit-like, and CI-like records, canonical entity/activity replay with alias normalization and hash-chain commitments reconstructs provenance evidence substantially better than raw logs and source-local W3C PROV-style mapping, while preserving tamper evidence.

## Why it stopped

Tier 2 synthetic evidence supports the mechanism but is not direct enough for a paper-grade provenance ledger claim.

## Recommended next action

Run a bounded deepen validation on semi-real or public multi-source traces with independently labeled provenance ground truth and a production W3C PROV/provenance-store baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Semi-real multi-source trace replay against a production provenance baseline
- Success threshold: Mean edge F1 improvement >= 0.20 and query F1 improvement >= 0.20 over the real baseline across fixed seeds or fixed trace partitions, tamper detection >= 0.99, and storage/runtime overhead below 2x baseline.
- Stop condition: Stop if no shareable multi-source real or semi-real trace corpus with defensible ground truth can be assembled, or if edge/query F1 improvement is below 0.10 on two independent trace partitions.

## Evidence references

- Artifact root: `<local-path>/projects/heterogeneous-trace-corpus-replay-for-provenance-evidence-5fa4ee778c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
