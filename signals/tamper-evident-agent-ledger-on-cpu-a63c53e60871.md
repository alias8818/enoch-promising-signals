# Tamper-Evident Agent Ledger on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tamper-evident-agent-ledger-on-cpu-a63c53e60871`
Run ID: `tamper-evident-agent-ledger-on-cpu-a63c53e60871-20260608T055007783007+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/8b444109bef9

## What looked useful

The prototype achieved median ledger construction throughput of 48499 events/s, median verification throughput of 50269 events/s, 2.35x JSONL size overhead, and 9/9 detection for each tested tamper class.

## Boundaries and scale limits

Synthetic events only; no real agent traces, concurrent writers, external anchoring, key rotation, crash recovery, storage backend comparison, compromised-key adversary, or comparison against established transparency-log systems.

## Claim scope

A single-process Python hash-chain plus HMAC ledger detected synthetic payload modification, deletion, adjacent reordering, suffix truncation with retained expected head hash, and public rehash attempts without the key across 183000 synthetic agent events on CPU.

## Why it stopped

This is useful synthetic mechanism evidence but not a broad or novel paper-grade validation.

## Recommended next action

Run a bounded follow-up on real agent traces with concurrent writers, crash/restart recovery, external head anchoring, and a transparency-log baseline before considering paper readiness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace tamper-evident agent ledger with crash and concurrency controls
- Success threshold: Detect 100% of predefined tamper cases after replay, crash/restart, and concurrent append tests while sustaining at least 10000 append events/s and 10000 verify events/s on CPU.
- Stop condition: Stop if real-trace replay or crash/concurrency tests miss any predefined tamper class, require trusted mutable local state for truncation detection, or fall below 1000 append events/s in a straightforward implementation.

## Evidence references

- Artifact root: `<local-path>/projects/tamper-evident-agent-ledger-on-cpu-a63c53e60871`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
