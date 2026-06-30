# Adversarial Ledger Red-Team

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adversarial-ledger-red-team-5af2131a548f`
Run ID: `adversarial-ledger-red-team-5af2131a548f-20260605T020011069410+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/96acb1bd8a94

## What looked useful

The red-team harness cleanly separates local integrity checks from externally retained evidence. It shows that tamper-evidence claims require an explicit trusted anchor/witness boundary; if the attacker can rewrite the external evidence too, all modeled schemes fail.

## Boundaries and scale limits

Synthetic 1,000-entry ledgers, 300 deterministic trials, HMAC proxy signatures, modeled anchor/witness dictionaries, no production ledger implementation, no distributed service, no real timestamp authority, and no crash/restart persistence tests.

## Claim scope

In a deterministic synthetic simulator of append-only audit ledgers, local hash-chain-only and signed-only designs fail to detect suffix or full-history rewrites once the attacker can recompute local history or use the writer signing key; external anchors or witnesses detect those rewrites only while their external evidence store remains trusted.

## Why it stopped

Bounded synthetic evidence supports a threat-model clarification but is not direct or novel enough for a paper; it is a proxy/local simulator result rather than full validation against production ledger systems.

## Recommended next action

Stop this run as a no-paper useful signal; the concrete next step is to apply the same adversarial matrix to a real persisted ledger implementation with real signatures and an external verifier retaining pre-attack anchors.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Persisted Ledger Red-Team With External Verifier
- Success threshold: Across at least 100 deterministic attack trials, signed-only persisted ledgers miss at least 95% of writer-key suffix rewrites, while anchored ledgers with a retained external verifier detect at least 99% of the same attacks.
- Stop condition: Stop if the selected ledger cannot persist and reload independently verifiable entries, or if a smoke attack cannot reproduce either a signed-only miss or an anchored detection within 2 hours.

## Evidence references

- Artifact root: `<local-path>/projects/adversarial-ledger-red-team-5af2131a548f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
