# Independent Ground-Truth Completeness Check for Local-Agent Evidence Ledgers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `independent-ground-truth-completeness-check-for-local-agen-75f49ee193`
Run ID: `independent-ground-truth-completeness-check-for-local-agen-75f49ee193-20260526T214721195812+0000`

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

- Parent run decision: Evidence Ledger and Rollback for Local Agents: enoch://control-plane/projects/evidence-ledger-and-rollback-for-local-agents-df9522eeec1b/runs/evidence-ledger-and-rollback-for-local-agents-df9522eeec1b-20260526T001711499660+0000
- Parent run decision: Intercepted Evidence Ledger on Real Local-Agent Tool Calls: enoch://control-plane/projects/intercepted-evidence-ledger-on-real-local-agent-tool-calls-3b9d879c0b/runs/intercepted-evidence-ledger-on-real-local-agent-tool-calls-3b9d879c0b-20260526T150041318082+0000

## What looked useful

Artifact ledger completeness recall was 0.9819 versus 0.3753 for command-history and 0.3133 for transcript baselines; tamper detection was 0.9773 with hashes and 0.0 without hashes; removing dependency/support links reduced claim-support recall from 1.0 to 0.0.

## Boundaries and scale limits

Validated on 200 generated local-task episodes across 5 fixed seeds and 6 ledger policies. Not validated on production local-agent traces, real user tasks, vendor-specific agent logs, or manifests generated independently of the harness.

## Claim scope

In a fixed-seed synthetic local-task harness with hidden ground-truth manifests, artifact-aware evidence ledgers with hashes and dependency/support links enable independent completeness and support checking substantially better than transcript-only and command-history baselines.

## Why it stopped

No-paper closure: fixed-seed direct metrics, baselines, and ablations support the mechanism, but the evidence is synthetic local-harness evidence rather than production-trace validation.

## Recommended next action

Run the same checker on real local-agent traces captured with sidecar filesystem/process instrumentation that produces independently generated ground-truth manifests.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Trace Ground-Truth Completeness Check for Local-Agent Evidence Ledgers
- Success threshold: Full artifact ledger achieves at least 0.85 completeness recall and at least +0.30 completeness-recall advantage over both baselines, with at least 0.90 claim-support recall and at least 0.80 tamper detection on injected stale-output cases.
- Stop condition: Stop if sidecar manifests cannot be generated independently, if fewer than 50 real traces are available, or if the artifact ledger fails to beat both baselines by 0.15 completeness recall after the first 25 traces.

## Evidence references

- Artifact root: `<local-path>/projects/independent-ground-truth-completeness-check-for-local-agen-75f49ee193`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
