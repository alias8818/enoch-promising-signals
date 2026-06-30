# Evidence Ledger for Small Local Tool Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-for-small-local-tool-agents-76918e2b1151`
Run ID: `evidence-ledger-for-small-local-tool-agents-76918e2b1151-20260607T063205294852+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/2342148c1368

## What looked useful

The 50,000-event benchmark passed clean verification in all 5 trials, detected payload edits, interior deletions, predecessor rewrites, and suffix truncation in all trials, and achieved median 122,690 ledger writes/second and 183,309 verification checks/second. Median overhead was 3.38x runtime and 1.74x storage versus plain JSONL.

## Boundaries and scale limits

Synthetic event payloads only; single-process writes only; no real tool-agent integration, crash recovery, concurrent writers, fsync durability analysis, external checkpointing, or full adversary model.

## Claim scope

A dependency-free SQLite evidence ledger with per-run hash chains and committed manifests can make 50,000 synthetic local tool-agent events replay-verifiable and tamper-evident with sub-second write and verification times on this worker.

## Why it stopped

Synthetic/proxy evidence supports the mechanism but does not provide direct operational validation or publication-grade evidence.

## Recommended next action

Stop this worker run as no-paper useful-signal evidence; next run should integrate the manifest-backed ledger into a real local tool-agent runner and test replay plus tamper/crash injection on real transcripts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Agent Evidence Ledger With Crash and Tamper Injection
- Success threshold: At least 10 real agent runs and 10,000 total real events verify cleanly; all injected tamper/crash cases are detected or classified; median ledger overhead remains below 5x runtime and below 3x storage versus existing trace logging.
- Stop condition: Stop if real traces cannot be replayed deterministically, if suffix/manifest tampering can evade detection without an external checkpoint, or if median overhead exceeds 5x on 10,000 real events.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-small-local-tool-agents-76918e2b1151`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
