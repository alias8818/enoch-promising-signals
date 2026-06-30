# Signed Evidence Ledger for Small Agent Reliability

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `signed-evidence-ledger-for-small-agent-reliability-4e00a8950a3b`
Run ID: `signed-evidence-ledger-for-small-agent-reliability-4e00a8950a3b-20260621T172654741253+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/2852c88656c4

## What looked useful

The bounded run supports the mechanism that signed evidence commitments can catch ledger tampering classes that shape/reference-only validation misses, but it does not establish broad small-agent reliability.

## Boundaries and scale limits

Synthetic/proxy-only ledgers; no real small-agent tool traces, blinded drift traps, adversarial prompt runs, production key management, replay attacks, or human reviewer workflows were tested.

## Claim scope

In a deterministic synthetic JSON-ledger suite, HMAC-signed evidence records plus claim-to-evidence commitments reduced false acceptance of tampered, injected, and untrusted-resigned ledgers from 4000/5000 for an unsigned structural checker to 0/5000, with 0/1000 false rejects on valid signed ledgers.

## Why it stopped

Synthetic proxy mechanism test completed successfully, but publication-grade reliability claims require direct real-agent trace evidence.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next, test the same verifier on real or replayed small-agent tool traces with blinded drift traps and an unsigned/no-ledger baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Signed Ledger on Real Small-Agent Drift Traces
- Success threshold: At least 200 trace-level claims with signed-ledger false accept rate reduced by 50% or more versus baseline and valid-claim false reject rate no greater than 2%.
- Stop condition: Stop if signed-ledger false accepts are not lower than baseline, if valid-claim false rejects exceed 2%, or if trace instrumentation cannot preserve evidence commitments.

## Evidence references

- Artifact root: `<local-path>/projects/signed-evidence-ledger-for-small-agent-reliability-4e00a8950a3b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
