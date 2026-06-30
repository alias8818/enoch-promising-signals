# Live anchored evidence-ledger replay under adaptive bypass attempts

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `live-anchored-evidence-ledger-replay-under-adaptive-bypass-dd11860405`
Run ID: `live-anchored-evidence-ledger-replay-under-adaptive-bypass-dd11860405-20260529T050813190336+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real-agent trace validation for local evidence-ledger policy verification: enoch://control-plane/projects/real-agent-trace-validation-for-local-evidence-ledger-poli-b9a003676d/runs/real-agent-trace-validation-for-local-evidence-ledger-poli-b9a003676d-20260529T010331547459+0000
- Parent run decision: Corpus-scale real-agent evidence-ledger replay with adversarial bypass controls: enoch://control-plane/projects/corpus-scale-real-agent-evidence-ledger-replay-with-advers-2867063edf/runs/corpus-scale-real-agent-evidence-ledger-replay-with-advers-2867063edf-20260529T024651314689+0000

## What looked useful

Anchoring materially improves replay integrity over mutable logs and local-only hash chains for committed history, but the adaptive bypass boundary is sharp: unanchored suffixes and anchor blackouts remain fully bypassable in this model. Source-sequence replay is necessary for omitted-event detection when the ledger anchors an incomplete stream.

## Boundaries and scale limits

20,000 simulated episodes with 512 events, 16 sources, batch size 32, and 8 CPU workers; no real networked anchor, production key custody, live telemetry, adversarial scheduler, or deployed append-only transparency log was tested.

## Claim scope

In a fixed-seed local replay simulator, externally anchored batch hash-chain replay detects all tested committed-history mutations, and a source-sequence invariant detects pre-ledger source omissions; neither mechanism detects rewrites inside an unanchored live suffix or anchor blackout window.

## Why it stopped

Useful simulator evidence supports the mechanism for committed anchors but falsifies sufficiency under adaptive pre-anchor and blackout rewrites; this is not full live validation or publication-grade evidence.

## Recommended next action

Stop this branch as no-paper evidence; the next bounded depth-4 deepen test should implement a real append-only anchor and replay live generated traces with injected anchor delays, omissions, and forked reader views.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real append-only anchor replay under live delay and fork injection
- Success threshold: Across at least 100,000 live generated events, detect 100% of committed-history mutations and source-sequence omissions, reduce successful pre-anchor bypasses to the explicitly measured uncommitted latency window, and keep throughput overhead below 25% versus local hash-chain logging.
- Stop condition: Stop if the real anchor cannot make commitments durably visible to replay clients, if forked-reader views cannot be detected, or if pre-anchor bypass remains unconstrained beyond the configured commit cadence.

## Evidence references

- Artifact root: `<local-path>/projects/live-anchored-evidence-ledger-replay-under-adaptive-bypass-dd11860405`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
