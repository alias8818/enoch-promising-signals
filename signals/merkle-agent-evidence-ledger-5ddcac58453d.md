# Merkle Agent Evidence Ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `merkle-agent-evidence-ledger-5ddcac58453d`
Run ID: `merkle-agent-evidence-ledger-5ddcac58453d-20260607T073828825028+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/74310f1de90c

## What looked useful

MMR-style evidence ledgers appear practical for compact independently verifiable agent evidence proofs at local small-to-medium scale, with about 1.65x to 1.72x append slowdown versus a minimal hash-chain baseline and proof sizes around 1.6 KB to 2.2 KB across 1k to 100k events.

## Boundaries and scale limits

Synthetic in-memory benchmark only; no real agent framework integration, concurrent writers, persistent crash recovery, remote notarization, privacy redaction, external verifier process, or adversarial operator model was tested.

## Claim scope

A dependency-free Python Merkle Mountain Range prototype can append 100,000 synthetic agent evidence events at about 206,819 events/s, verify sampled compact inclusion proofs in about 10.69 us each, reject tampered proofs, and localize stored mid-ledger tampering by full audit.

## Why it stopped

Synthetic mechanism-only evidence supports viability but is not direct publication-grade validation of an agent evidence ledger system.

## Recommended next action

Stop this run as no-paper useful signal; next, run a bounded real-trace integration test with crash persistence and an external verifier before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Persistent Merkle evidence ledger on real agent traces
- Success threshold: All external proof checks pass, crash recovery preserves a verifiable prefix without silent corruption, and median append overhead is below 2.5x versus the practical baseline on real traces.
- Stop condition: Stop if external proof verification fails, crash recovery can silently accept corrupted evidence, or median append overhead exceeds 2.5x on real traces without a clear fix.

## Evidence references

- Artifact root: `<local-path>/projects/merkle-agent-evidence-ledger-5ddcac58453d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
