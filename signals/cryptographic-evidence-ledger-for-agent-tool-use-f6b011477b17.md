# Cryptographic Evidence Ledger for Agent Tool Use

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cryptographic-evidence-ledger-for-agent-tool-use-f6b011477b17`
Run ID: `cryptographic-evidence-ledger-for-agent-tool-use-f6b011477b17-20260523T214343114748+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b49cd735f64b

## What looked useful

The mechanism is practical for small local logs: median ledger append throughput was 28,803 events/s, verification throughput was 18,153 events/s, write slowdown versus plain JSONL was 11.88x, size overhead was 1.47x, and all five tamper modes were detected when a signed checkpoint was available. Ledger-only verification failed to detect suffix truncation, establishing that checkpoint anchoring is required.

## Boundaries and scale limits

Tested only on 10k deterministic synthetic events in a single-process local Python benchmark; no real agent framework integration, external timestamping, public transparency-log anchoring, distributed consistency checking, privacy redaction, key rotation, or compromise recovery was validated.

## Claim scope

A local Python prototype can make synthetic agent tool-use traces tamper-evident for mutation, middle deletion, reordering, forgery without the signing key, and suffix truncation when verification uses an anchored signed checkpoint.

## Why it stopped

Synthetic local evidence supports a practical mechanism but not a paper-ready novelty claim; established transparency-log and provenance systems already cover the main cryptographic primitives, and external checkpoint anchoring was not directly validated.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should integrate the ledger with real agent tool-call traces and anchor checkpoints in an independent transparency service or local Rekor instance.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Agent Trace Ledger With Independent Checkpoint Anchoring
- Success threshold: On at least 1,000 real tool-call events, detect all tested tamper modes including suffix truncation via independent checkpoint anchoring, with less than 20x append slowdown versus raw JSONL and less than 3x storage overhead.
- Stop condition: Stop as negative if independent checkpoint anchoring cannot be automated locally, if any tamper mode passes verification, or if overhead exceeds the threshold on ordinary real tool traces.

## Evidence references

- Artifact root: `<local-path>/projects/cryptographic-evidence-ledger-for-agent-tool-use-f6b011477b17`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
