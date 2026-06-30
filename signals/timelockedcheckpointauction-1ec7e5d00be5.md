# TimeLockedCheckpointAuction

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `timelockedcheckpointauction-1ec7e5d00be5`
Run ID: `timelockedcheckpointauction-1ec7e5d00be5-20260619T154050219476+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.7-code: enoch://research-facility/provider/moonshotai/kimi-k2.7-code/8a8b14f4b5cd

## What looked useful

TimeLockedCheckpointAuction reduced checkpoint writes at capacity 96 (481.9 mean writes versus 519.4 layered, 660.8 flat, and 768.0 transcript), but it produced no final accuracy improvement over the best baseline at any tested capacity; deltas were 0.0000 for capacities 48, 96, 192, and 384.

## Boundaries and scale limits

No real agent transcripts, no language-model memory extractor, no production storage latency, and no irreversible checkpoint side effects were tested. This is a toy mechanism probe, not publication-grade validation.

## Claim scope

Deterministic synthetic delayed-evidence replay tasks with 20 seeds, 24 sessions per seed, 192 final facts per seed, five memory policies, and checkpoint capacities 48, 96, 192, and 384.

## Why it stopped

Proxy simulation failed the predeclared success threshold of at least +0.05 auction accuracy over the best non-auction baseline with no stale-rate increase; this is not a full real-world validation.

## Recommended next action

Stop this run as an early synthetic falsification; only revisit with a bounded adversarial-ordering follow-up where irreversible checkpoint costs or retrieval-time hazards make time-locking materially different from simple overwrite baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adversarial irreversible-checkpoint test for time-locked memory auctions
- Success threshold: Auction improves answer accuracy or cost-adjusted accuracy by at least 0.05 over the best baseline while keeping stale-rate no worse than the best baseline.
- Stop condition: Stop if the auction again ties the best baseline within 0.02 accuracy across the capacity sweep or if gains occur only from extra retained memory rather than the time-lock auction mechanism.

## Evidence references

- Artifact root: `<local-path>/projects/timelockedcheckpointauction-1ec7e5d00be5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
