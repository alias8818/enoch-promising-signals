# Real-trace tamper-evident agent ledger with crash and concurrency controls

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-trace-tamper-evident-agent-ledger-with-crash-and-conc-6937599e73`
Run ID: `real-trace-tamper-evident-agent-ledger-with-crash-and-conc-6937599e73-20260608T115353080999+0000`

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

- Parent run decision: Tamper-Evident Agent Ledger on CPU: enoch://control-plane/projects/tamper-evident-agent-ledger-on-cpu-a63c53e60871/runs/tamper-evident-agent-ledger-on-cpu-a63c53e60871-20260608T055007783007+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/8b444109bef9

## What looked useful

The bounded mechanism worked: all 43 real trace events appended concurrently with a valid chain, crash left a valid committed prefix, replay restored completeness, and a payload mutation was detected as a hash mismatch.

## Boundaries and scale limits

Single host, small trace, Python prototype, SQLite only, no power-loss test, no multi-host writers, no live production agent integration, no adversarial key or anchoring model, and no sustained throughput benchmark.

## Claim scope

A SQLite WAL ledger with canonical payload hashes and a SHA-256 row hash chain preserved integrity for one 43-event real Codex controller trace under 4 local concurrent append workers, one SIGKILL before commit, replay of the missing event, and copied-database payload tamper detection.

## Why it stopped

Tier 1 direct test produced useful mechanism support, but it is not broad or durable enough for publication readiness.

## Recommended next action

Run a bounded deepen test on at least 10k real agent events from multiple runs with repeated SIGKILL injection and an append-only non-hashed baseline for overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium real-trace ledger stress test with repeated crash injection and overhead baseline
- Success threshold: Zero hash-chain, payload-hash, or duplicate-event verification failures; all missing events replayed after crashes; tamper mutation detected; median append latency less than 2x the non-hashed baseline.
- Stop condition: Stop if any verified committed ledger becomes unrecoverably invalid, if replay cannot restore completeness after a crash, or if median append latency is 2x or worse than baseline on the 10k-event workload.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-tamper-evident-agent-ledger-with-crash-and-conc-6937599e73`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
