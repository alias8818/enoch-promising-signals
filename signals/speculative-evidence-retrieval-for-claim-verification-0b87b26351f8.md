# Speculative Evidence Retrieval for Claim Verification

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `speculative-evidence-retrieval-for-claim-verification-0b87b26351f8`
Run ID: `speculative-evidence-retrieval-for-claim-verification-0b87b26351f8-20260525T201331016665+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/abf77b336ae1

## What looked useful

On SciFact, literal-claim BM25 outperformed deterministic speculative support/refute RRF on both dev and train consistency checks. Dev Recall@10 was 0.9091 for claim BM25 versus 0.9025 for speculative RRF; train Recall@10 was 0.9125 versus 0.9091. Generic support templates were consistently worse.

## Boundaries and scale limits

Real but small scientific claim-verification dataset; document-level retrieval only; no LLM-generated queries, neural retriever, sentence-level evidence selection, or end-to-end verifier.

## Claim scope

Deterministic speculative support/refute query expansion with BM25 on SciFact document-level evidence retrieval.

## Why it stopped

Direct small-scale evidence shows the tested speculative support/refute expansion is a proxy/early falsification, not a full validation of all speculative retrieval variants.

## Recommended next action

Stop this deterministic BM25 version as a no-paper negative signal; only revisit with a bounded learned or LLM-filtered speculative-query test requiring at least +2 pp Recall@20 with no AP@10 degradation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Filtered Generated Speculative Queries for SciFact Retrieval
- Success threshold: At least +0.02 absolute Recall@20 over literal-claim BM25 and no negative AP@10 delta on held-out claims.
- Stop condition: Stop if generated speculative queries fail the success threshold or show AP@10 degradation after entity-preserving filtering.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-evidence-retrieval-for-claim-verification-0b87b26351f8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
