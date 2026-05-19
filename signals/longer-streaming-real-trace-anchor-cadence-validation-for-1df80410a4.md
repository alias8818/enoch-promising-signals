# Longer streaming real-trace anchor-cadence validation for evidence-ledger auditing

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `100`
Project ID: `longer-streaming-real-trace-anchor-cadence-validation-for-1df80410a4`
Run ID: `longer-streaming-real-trace-anchor-cadence-validation-for-1df80410a4-20260518T133642897436+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `100`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 35, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- strong evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Longer streaming real-trace anchor-cadence validation for evidence-ledger auditing: internal_generated:longer-streaming-real-trace-anchor-cadence-validation-for-1df80410a4

## What looked useful

Across 17,600 auditor-trial rows, anchored hash chains detected 100% of attacks, exact-localized all ordinary modify/delete/insert/reorder/truncate attacks, detected all recompute-suffix attacks at the next anchor, beat batch manifests on exact localization, and beat unanchored chains on recompute/truncate resistance. Anchor p95 offset rose from 22 events at cadence 32 to 1550.7 events at cadence 2048 while anchor bytes/event fell from about 2.32 to 0.04.

## Boundaries and scale limits

Offline deterministic harness over local JSONL traces; largest stream 16,852 events; attacks are injected rather than observed live; external anchors are trusted in-memory/JSON records; no production timestamping, key custody, crash recovery, concurrent writers, retention workflow, privacy redaction, or million-event deployment was tested.

## Claim scope

Bounded local validation on 66,634 real Codex/Enoch JSONL agent-trace events shows that periodic externally anchored hash-chain ledgers detect all tested tamper attacks, including recompute-suffix and truncation attacks that unanchored chains miss, and that anchor cadence controls recompute-aware detection offset.

## Why it stopped

The bounded real-trace mechanism is supported, but the run is not paper-positive because production anchor custody, concurrency, recovery, and live deployment adversary behavior were not directly validated.

## Recommended next action

Run one depth-4 production-style deepen test that persists anchors through crash/restart, key rotation, and concurrent appenders on multi-session real agent traces; stop paper work until those deployment properties are directly measured.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Production-style persistent external-anchor ledger under crash and concurrent real-agent traces
- Success threshold: At least 50k real appended events with zero clean-control false positives, 100% detection of ordinary and recompute/truncate attacks under intact external anchors, exact localization for ordinary attacks, documented recovery after forced crashes, and measured append/audit overhead versus digest and batch-manifest baselines.
- Stop condition: Stop as negative if persistence/concurrency introduces false positives, anchor loss, unrecoverable ordering ambiguity, or missed recompute/truncate attacks under intact anchors.

## Evidence references

- Artifact root: `<local-path>/projects/longer-streaming-real-trace-anchor-cadence-validation-for-1df80410a4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
