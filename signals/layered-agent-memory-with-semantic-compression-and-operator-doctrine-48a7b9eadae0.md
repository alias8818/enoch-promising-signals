# Layered Agent Memory with Semantic Compression and Operator Doctrine

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `layered-agent-memory-with-semantic-compression-and-operator-doctrine-48a7b9eadae0`
Run ID: `layered-agent-memory-with-semantic-compression-and-operator-doctrine-48a7b9eadae0-20260619T104602268948+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1bcea6a10f29

## What looked useful

Layered doctrine memory reached 1.000 accuracy with 0.000 stale/doctrine violation rate and 0.315 compression ratio versus raw transcript tokens; flat retrieval reached 0.889 accuracy and transcript search reached 0.444 with 0.444 violation rate.

## Boundaries and scale limits

Proxy-only synthetic evidence; no real agent traces, no LLM-in-the-loop responses, no learned semantic compression, no large corpus, and no long-run retrieval or persistence stress test.

## Claim scope

In a deterministic toy replay with 20 synthetic memory events and 9 queries, keyed layered doctrine memory preserved current facts and doctrine under revocations/noise better than raw transcript search and slightly better than flat retrieval while reducing stored-token footprint.

## Why it stopped

No-paper closure because this run is a deterministic synthetic proxy that supports the mechanism but does not provide direct publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up on a naturalistic repeated-agent trace set with at least 100 labeled queries and ablations separating compression from doctrine-aware revocation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Naturalistic trace benchmark for layered doctrine memory
- Success threshold: Layered doctrine memory improves stale/unsafe recall error rate by at least 25% relative to flat retrieval without reducing exact-answer accuracy by more than 2 percentage points.
- Stop condition: Stop if layered memory fails to improve stale/unsafe recall errors by at least 10% on the first 100 labeled queries or if labeling quality cannot distinguish current from revoked facts.

## Evidence references

- Artifact root: `<local-path>/projects/layered-agent-memory-with-semantic-compression-and-operator-doctrine-48a7b9eadae0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
