# Evidence Ledger Corruption Detection Under CPU Contention

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-corruption-detection-under-cpu-contention-d1b5ddac5fbe`
Run ID: `evidence-ledger-corruption-detection-under-cpu-contention-d1b5ddac5fbe-20260605T215325202683+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/d7ba9c7bd4a7

## What looked useful

Verifier scope mattered more than CPU contention in this bounded test: full scans detected 30/30 direct corruptions with median latency around 22-33 ms, while tail-only and append-only incremental verifiers detected 0/30 historical payload corruptions within the timeout.

## Boundaries and scale limits

Synthetic single-file ledger; 8,000 entries per trial; 5 trials per scenario; 3-second detection window for miss cases; synthetic CPU burners rather than production service load; no real filesystem fault injection, concurrent appenders, adversarial privilege model, distributed storage, or multi-hour persistence.

## Claim scope

On a local 8-CPU worker with a synthetic JSONL SHA-256 hash-chain ledger, full-ledger verification detected all injected old-record payload mutations and middle deletions under 0, 4, and 7 CPU burner processes, while append-only incremental and tail-window verifiers missed historical payload mutations after a prior clean verification.

## Why it stopped

Synthetic local evidence is sufficient to falsify unsafe verifier assumptions but not sufficient for a broad or paper-positive corruption-detection claim.

## Recommended next action

Stop this run as no-paper useful signal; next run should test the same verifier families with concurrent appenders plus crash/restart recovery and a production-like CPU load generator.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Concurrent Appender Evidence-Ledger Revalidation Under Crash Recovery
- Success threshold: At least 20 trials per verifier strategy with 100% detection for full/segment revalidation of injected historical corruptions after restart, and persistent 0% or clearly lower detection for append-only controls.
- Stop condition: Stop if crash/restart state cannot be reproduced locally, or if segment/full revalidation fails to detect any injected corruption in smoke tests.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-corruption-detection-under-cpu-contention-d1b5ddac5fbe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
