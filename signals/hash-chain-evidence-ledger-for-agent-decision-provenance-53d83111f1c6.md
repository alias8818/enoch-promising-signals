# Hash-Chain Evidence Ledger for Agent Decision Provenance

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `hash-chain-evidence-ledger-for-agent-decision-provenance-53d83111f1c6`
Run ID: `hash-chain-evidence-ledger-for-agent-decision-provenance-53d83111f1c6-20260529T014550997657+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/91d47f7f6764

## What looked useful

At 100,000 events the ledger appended at 22,514.81 events/s, verified at 25,190.93 events/s, used 1.5286x baseline JSONL storage, detected payload mutation, middle deletion, adjacent reorder, and anchored suffix truncation, but did not detect suffix truncation without an external head/count anchor.

## Boundaries and scale limits

Validated on 100,000 synthetic records in one CPU-only Python process. Not validated on real agent traces, concurrent writers, crash recovery, log rotation, remote anchoring, signed identities, or adversarial key compromise.

## Claim scope

A single-writer canonical JSONL SHA-256 hash-chain ledger can provide practical local tamper evidence for synthetic agent decision provenance when the expected head hash and record count are anchored out of band.

## Why it stopped

No-paper closure: bounded synthetic evidence supports the mechanism but also confirms the structural anchor dependency, so this is useful engineering signal rather than publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up that instruments a real agent workflow with periodic out-of-band head/count anchors and tests crash, rotation, and concurrent-write failure modes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchored Hash-Chain Provenance on Real Agent Traces
- Success threshold: On at least 100,000 real/replayed agent events, detect every injected tamper case except explicitly out-of-scope compromised-writer attacks, recover cleanly from crash/partial-write scenarios, and keep storage overhead below 2x and append-time overhead below 3x versus baseline JSONL.
- Stop condition: Stop if anchored checkpointing fails to detect suffix truncation or checkpoint rollback, if crash recovery creates unverifiable ambiguous records, or if overhead exceeds 3x append time or 2x storage before 100,000 events.

## Evidence references

- Artifact root: `<local-path>/projects/hash-chain-evidence-ledger-for-agent-decision-provenance-53d83111f1c6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
