# Implementation replay of multi-anchor trace ledger tamper detection

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `implementation-replay-of-multi-anchor-trace-ledger-tamper-00cd14379a`
Run ID: `implementation-replay-of-multi-anchor-trace-ledger-tamper-00cd14379a-20260603T141932005388+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real Trace Evidence Ledger with External Anchor Publication: enoch://control-plane/projects/real-trace-evidence-ledger-with-external-anchor-publicatio-79b9732127/runs/real-trace-evidence-ledger-with-external-anchor-publicatio-79b9732127-20260602T155313723073+0000
- Parent run decision: Multi-anchor durability and tamper-control test for trace evidence ledgers: enoch://control-plane/projects/multi-anchor-durability-and-tamper-control-test-for-trace-b85e9fbb76/runs/multi-anchor-durability-and-tamper-control-test-for-trace-b85e9fbb76-20260602T190413498663+0000

## What looked useful

Across 30000 seeded tamper trials over anchor intervals 25, 100, and 500, the hash-chain-only baseline detected 0.0000 of strong recompute rewrites. At interval 100, single-anchor and multi-anchor both detected 1.0000 with no anchor faults; with 25% unavailable and 25% compromised anchors, single-anchor detected 0.9942 while multi-anchor detected 0.9993; with 50% unavailable and 25% compromised anchors, single-anchor detected 0.9760 while multi-anchor detected 0.9955. Benign no-fault false positives were 0.0000 for all strategies over 10000 checks. Detection fails for both anchor strategies when all anchors are unavailable or compromised.

## Boundaries and scale limits

Synthetic payloads and local HMAC anchor stores only; no real distributed anchor service, production trace workload, network partition, timestamp authority, transparency log, blockchain anchor, operator workflow, or correlated provider compromise was tested.

## Claim scope

Bounded local implementation replay: for deterministic 10000-record synthetic trace ledgers, a strong contiguous rewrite attacker that recomputes the local SHA-256 hash chain is detected by external anchors when at least one honest available anchor remains; three independent anchors improve detection and localization over a single anchor under modeled independent anchor unavailability/compromise.

## Why it stopped

Mechanism supported in bounded synthetic implementation replay, but publication readiness is blocked by synthetic-only anchors/workloads and explicit independent-fault assumptions rather than by local compute scale.

## Recommended next action

Stop this run as no-paper useful evidence; next concrete action is to replay the same verifier against a real trace ledger backed by three independent anchor stores with correlated outage and compromise fault injection.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real anchor-store replay for multi-anchor trace ledger tamper detection
- Success threshold: At least 99% detection for strong recompute rewrites with benign false positives below 0.1%, and statistically clear localization improvement over single-anchor under correlated fault injection.
- Stop condition: Stop if multi-anchor detection drops below single-anchor by more than 0.5 percentage points in any realistic correlated-fault regime, or if benign false positives exceed 0.1% without a clear operational filter.

## Evidence references

- Artifact root: `<local-path>/projects/implementation-replay-of-multi-anchor-trace-ledger-tamper-00cd14379a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
