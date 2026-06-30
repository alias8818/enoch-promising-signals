# Blinded multi-trace audit benchmark for an agent evidence ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `blinded-multi-trace-audit-benchmark-for-an-agent-evidence-da89e39e19`
Run ID: `blinded-multi-trace-audit-benchmark-for-an-agent-evidence-da89e39e19-20260531T150311180651+0000`

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

- Parent run decision: Agent Evidence Ledger: enoch://control-plane/projects/agent-evidence-ledger-de8437d4cb37/runs/agent-evidence-ledger-de8437d4cb37-20260530T085611021728+0000
- Parent run decision: Real-trace audit study for an agent evidence ledger: enoch://control-plane/projects/real-trace-audit-study-for-an-agent-evidence-ledger-3bec48a1f9/runs/real-trace-audit-study-for-an-agent-evidence-ledger-3bec48a1f9-20260531T114810950760+0000

## What looked useful

Medium validation showed blinded_multi_trace AUROC 0.9864 and best-F1 0.9862 versus single_trace_baseline AUROC 0.8859 and best-F1 0.8711. Mean deltas were +0.1005 AUROC and +0.1151 best-F1; adverse 2/6 and 3/6 corruption-rate controls preserved about +0.10 AUROC and +0.11 F1 gains.

## Boundaries and scale limits

Evidence is synthetic only; no real agent traces, no human labels, no collusive same-wrong-value corruptions, and no strong retrieval/provenance audit baseline beyond ledger-internal checks. The unblinded oracle did not separate from the blinded method, so the result supports multi-trace consensus more than a distinct blinding advantage.

## Claim scope

In a deterministic synthetic benchmark with 5 fixed seeds, 24,000 medium-run traces, blinded trace IDs, hashed evidence keys, and heterogeneous injected ledger faults, a multi-trace evidence-ledger auditor materially improves trace-corruption detection over a single-trace ledger consistency baseline.

## Why it stopped

Tier 2 synthetic mechanism support is useful but not paper-positive direct evidence.

## Recommended next action

Run a bounded deepen test with collusive same-wrong-value corruptions and a stronger retrieval/provenance audit baseline; stop paper escalation until that harder setting and at least one realistic trace replay are tested.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Collusive-corruption and stronger-baseline audit benchmark for blinded multi-trace evidence ledgers
- Success threshold: Across at least 5 fixed seeds, blinded multi-trace audit improves AUROC and best-F1 by at least 0.05 over the strongest baseline at 1/6 and 2/6 collusive corruption rates, and reports a clear failure boundary at 3/6 if no clean majority/source-diversity signal exists.
- Stop condition: Stop as negative if collusive corruption reduces AUROC delta below 0.02 or best-F1 delta below 0.02 against the strongest baseline at 1/6 and 2/6 corrupt trace rates.

## Evidence references

- Artifact root: `<local-path>/projects/blinded-multi-trace-audit-benchmark-for-an-agent-evidence-da89e39e19`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
