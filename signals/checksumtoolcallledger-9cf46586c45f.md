# ChecksumToolCallLedger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `checksumtoolcallledger-9cf46586c45f`
Run ID: `checksumtoolcallledger-9cf46586c45f-20260523T154208525078+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/d1f0bf117fed

## What looked useful

The mechanism is practical for local trace-integrity checking: all five tested tamper classes were detected across 5 trials at 1k, 10k, and 50k entries, median build throughput ranged from 33.7k to 48.3k entries/sec, median verify throughput ranged from 43.6k to 48.9k entries/sec, and serialized storage overhead was about 2.01x raw canonical event JSON.

## Boundaries and scale limits

Synthetic traces only; single-process local verification; no real production agent logs; no crash/concurrency persistence; no adversarial runtime compromise; no append-only storage enforcement; no comparison against signed transparency-log systems.

## Claim scope

In a standalone Python prototype over synthetic JSON-like agent tool-call traces up to 50,000 entries, canonical JSON plus a SHA-256 hash chain detected edits, deletions, insertions, adjacent reordering, and session metadata mismatches with tens-of-thousands-of-entries-per-second local throughput.

## Why it stopped

Prototype evidence supports the bounded mechanism but is synthetic and not novel enough by itself for a paper; this is not a full security validation.

## Recommended next action

Stop as a no-paper useful signal; only reopen if the next run tests a real agent trace pipeline with append-only persistence and a signed/transparency-log baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Agent Trace Checksum Ledger On Real Tool-Call Logs
- Success threshold: Detect 100% of injected tamper cases while adding less than 5% median logging wall-clock overhead and less than 2.5x storage overhead versus plain trace logging on the selected real workload.
- Stop condition: Stop if real workload overhead exceeds 10%, any injected tamper class is not detected, or append-only persistence cannot recover cleanly after a forced crash.

## Evidence references

- Artifact root: `<local-path>/projects/checksumtoolcallledger-9cf46586c45f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
