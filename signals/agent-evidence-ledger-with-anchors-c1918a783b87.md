# Agent Evidence Ledger with Anchors

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `agent-evidence-ledger-with-anchors-c1918a783b87`
Run ID: `agent-evidence-ledger-with-anchors-c1918a783b87-20260605T030110969055+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/a52a6c210eec

## What looked useful

Hash-chained evidence entries plus periodic Merkle anchors are a viable low-overhead tamper-evidence mechanism, but full-history rewrite detection requires an external pinned anchor tip. Internal consistency alone accepted a fully recomputed forged history.

## Boundaries and scale limits

Synthetic records only; no real agent workflow integration, no concurrent writers, no crash recovery, no signed agent identities, and no real external timestamp/transparency service. Tested only to 50k embedded-JSON records on one CPU process.

## Claim scope

A local single-process Python prototype of an agent evidence ledger can append and verify up to 50k synthetic records quickly, detect six common post-hoc tampering scenarios, and detect full-history rewrites when the latest anchor hash is pinned outside the mutable ledger.

## Why it stopped

The result is a bounded local prototype and synthetic/proxy validation, not direct publication-grade evidence; the critical external anchoring requirement was simulated rather than deployed.

## Recommended next action

Run a bounded real-agent integration follow-up with signed event identities, concurrent append behavior, and an actual external anchor publication path; stop this run as no-paper useful signal.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Agent Trace Ledger with External Anchor Publication
- Success threshold: For at least 10k real workflow events, p95 append latency below 25 ms, full verification throughput above 20k events/s, all predefined tampering attempts detected when checking the external anchor source, and documented behavior for crash recovery.
- Stop condition: Stop if external anchor verification cannot be integrated locally, if append p95 exceeds 100 ms on real traces without a clear batching fix, or if any predefined tampering scenario remains undetected despite external anchor checks.

## Evidence references

- Artifact root: `<local-path>/projects/agent-evidence-ledger-with-anchors-c1918a783b87`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
