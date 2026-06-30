# Evidence-Ledger Agent Reliability via Cryptographic Decision Hashing

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-agent-reliability-via-cryptographic-decision-hashing-07c17bdb051a`
Run ID: `evidence-ledger-agent-reliability-via-cryptographic-decision-hashing-07c17bdb051a-20260529T124550995496+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/e0091f7136cf

## What looked useful

Decision hashing is useful only when final roots are externally anchored and entries include immutable identity. Unanchored SHA chains failed against a ledger-aware attacker that recomputed hashes; anchored SHA with stable event ids and anchored HMAC detected all tested synthetic tampering.

## Boundaries and scale limits

2,000 synthetic episodes with 8 steps each, controlled attacks, no real LLM agent traces, no distributed storage, no production key management, and no adversarial system integration.

## Claim scope

Synthetic CPU-only tamper-detection study of agent decision ledgers showed that anchored SHA-256 or HMAC hash chains detect controlled post-hoc edits that plain schema logs miss. The result supports audit integrity only, not decision correctness or broad agent reliability.

## Why it stopped

Closed as no-paper useful signal because evidence is synthetic and validates only audit-integrity mechanics, not full agent reliability.

## Recommended next action

Run a bounded real-agent trace replay study with persisted root checkpoints and injected tampering across process restarts before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchored Decision Ledger Replay on Real Agent Traces
- Success threshold: Anchored ledger detects at least 99% of injected tampering in replayed real-agent traces with less than 5% overhead and no unexplained false accepts.
- Stop condition: Stop as negative if unanchored or anchored implementations miss more than 1% of injected tampering after excluding attacks outside the declared threat model, or if overhead exceeds 5% without a clear optimization path.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-reliability-via-cryptographic-decision-hashing-07c17bdb051a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
