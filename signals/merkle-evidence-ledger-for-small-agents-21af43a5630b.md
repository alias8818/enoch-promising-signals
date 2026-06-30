# Merkle Evidence Ledger for Small Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `merkle-evidence-ledger-for-small-agents-21af43a5630b`
Run ID: `merkle-evidence-ledger-for-small-agents-21af43a5630b-20260608T234540882146+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/48099f486882

## What looked useful

At 32,768 events, append hashing ran at about 109k events/s, Merkle build took 0.012 s, median inclusion verification was 0.009 ms with a 1,149-byte proof, and tampering was detected. A hash-chain baseline also detected tampering but required median replay of 4.7 MiB and 37.16 ms for random audits.

## Boundaries and scale limits

Synthetic payloads only; single process; in-memory proof generation; no disk-backed append log, checkpoint signatures, crash recovery, multi-agent merge protocol, network synchronization, adversarial workload, or production deployment test.

## Claim scope

A deterministic in-memory Python prototype shows that Merkle checkpointing over canonical small-agent evidence events provides compact random inclusion proofs, reproducible roots, and tamper detection with low local overhead up to 32,768 synthetic events.

## Why it stopped

Local mechanism evidence is useful but not paper-ready; production claims require durability, signing, synchronization, and adversarial tests.

## Recommended next action

Run a bounded durability and synchronization follow-up with a disk-backed append-only ledger, signed checkpoints, crash/restart replay, and two-agent merge/audit traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Disk-backed signed Merkle ledger durability and two-agent synchronization
- Success threshold: For at least 10,000 events per agent, restart root reproduction is exact, all injected tampering is detected, median random proof verification stays under 1 ms, and proof payload is at least 100x smaller than replaying the equivalent hash-chain suffix.
- Stop condition: Stop if restart cannot reproduce the signed checkpoint root, if any injected tamper is accepted, or if proof verification/proof size loses its asymptotic advantage over the hash-chain baseline.

## Evidence references

- Artifact root: `<local-path>/projects/merkle-evidence-ledger-for-small-agents-21af43a5630b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
