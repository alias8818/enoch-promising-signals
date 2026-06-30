# Out-of-process receipt authority for real agent tool-call traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `out-of-process-receipt-authority-for-real-agent-tool-call-4422f4519d`
Run ID: `out-of-process-receipt-authority-for-real-agent-tool-call-4422f4519d-20260520T125846376516+0000`

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

- Parent run decision: Hash-Chained Evidence Ledger for Small Agent Action Verification: enoch://control-plane/projects/hash-chained-evidence-ledger-for-small-agent-action-verification-807a3647150d/runs/hash-chained-evidence-ledger-for-small-agent-action-verification-807a3647150d-20260520T123721896821+0000
- Parent run decision: Real agent tool-call ledger with separated receipt authority: enoch://control-plane/projects/real-agent-tool-call-ledger-with-separated-receipt-authori-34e74801fd/runs/real-agent-tool-call-ledger-with-separated-receipt-authori-34e74801fd-20260520T124809584201+0000

## What looked useful

Tier 2 fixed-seed replay produced 40,500 trial rows. Out-of-process receipts achieved 100% detection and exact localization on ordinary attacks; no-close-manifest missed 100% of truncation; 16-event batch manifest localized exactly only 6.5%; compromised in-process signer missed 100% of recompute-suffix trials.

## Boundaries and scale limits

Saved local traces only; 3,094 command-execution events; HMAC standard-library prototype; no live streaming, public-key verifier, concurrent writers, key rotation, crash recovery, remote authority, sandbox, TEE, HSM, or production deployment.

## Claim scope

On 30 saved local Enoch/Codex command-execution traces, a subprocess receipt authority with a signed close manifest detected and exactly localized the tested ordinary trace tampering classes, and resisted recompute-suffix attempts when the attacker lacked the authority secret.

## Why it stopped

Tier 2 mechanism support was achieved, but key isolation and live deployment properties remain proxied, so this is no-paper useful signal rather than paper-positive evidence.

## Recommended next action

Run a live sidecar receipt-authority validation with public-key signatures, authority restart, and independent verification on real multi-turn agent sessions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live sidecar public-key receipt authority for real agent tool-call sessions
- Success threshold: >=99% detection for all tamper classes, >=95% exact localization for ordinary non-recompute edits, 100% truncation detection with close manifest, 0% recompute-suffix acceptance without authority access, and median receipt overhead below 25 ms per tool event.
- Stop condition: Stop if the live sidecar cannot reliably receipt active tool events, if restart/transfer verification fails on clean traces, or if recompute-suffix attacks are accepted after close.

## Evidence references

- Artifact root: `<local-path>/projects/out-of-process-receipt-authority-for-real-agent-tool-call-4422f4519d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
