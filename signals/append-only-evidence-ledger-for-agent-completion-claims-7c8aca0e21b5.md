# Append-Only Evidence Ledger for Agent Completion Claims

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `append-only-evidence-ledger-for-agent-completion-claims-7c8aca0e21b5`
Run ID: `append-only-evidence-ledger-for-agent-completion-claims-7c8aca0e21b5-20260628T104055982775+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/92970d39d153

## What looked useful

The prototype verified the core mechanism and exposed the critical design requirement: hash chains are sufficient for local mutation/reorder/deletion evidence, but completion ledgers need an external head anchor to make append-only claims meaningful against tail truncation.

## Boundaries and scale limits

Synthetic evidence only; no real agent-runner integration, no external timestamping or signature service, no WORM storage, no concurrent writer stress, and no adversarial operating-system or storage-layer compromise. Tail truncation is not detectable without a separately preserved head anchor.

## Claim scope

A local standard-library JSONL hash-chain evidence ledger can bind synthetic agent completion claims to evidence file digests and detect claim mutation, evidence mutation, middle deletion, reorder, and anchored tail truncation in a bounded 100-5000 entry experiment.

## Why it stopped

No-paper useful-signal closure: bounded synthetic evidence supports the mechanism but does not validate real operational deployment or external append-only anchoring.

## Recommended next action

Integrate the ledger with one real agent completion pipeline and a signed or timestamped head-anchor sink, then replay benign and tampered traces to measure detection and overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Agent Completion Ledger With External Head Anchors
- Success threshold: All tamper classes including tail truncation are detected during replay, clean traces verify successfully, and median completion overhead stays below 10% for the tested local workload.
- Stop condition: Stop if clean real traces cannot be replay-verified, if any anchored tamper class is missed, or if median overhead exceeds 25% after one batching/fsync optimization pass.

## Evidence references

- Artifact root: `<local-path>/projects/append-only-evidence-ledger-for-agent-completion-claims-7c8aca0e21b5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
