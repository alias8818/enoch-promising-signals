# Hash-Chained Evidence Ledger for Local Agent Reliability

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hash-chained-evidence-ledger-for-local-agent-reliability-222fad19092a`
Run ID: `hash-chained-evidence-ledger-for-local-agent-reliability-222fad19092a-20260629T025921944755+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a6fb9d2552e0

## What looked useful

Hash chaining is locally useful for tamper evidence only when the verifier has a trusted anchor or secret. A keyless local chain can be rewritten if the attacker also controls the anchor. The HMAC version detected all tested mutations and ran at about 127,766 events/sec with about 2.01x bytes/event versus plain JSONL.

## Boundaries and scale limits

Synthetic events only; no production agent integration, append-only storage, remote notarization, crash recovery, key-store hardening, or human audit workflow was tested. The benchmark was CPU-only Python with 50,000 events, not a long-running or multi-agent deployment.

## Claim scope

In a deterministic local simulation of 200 trials per mutation type, anchored SHA-256 and HMAC hash chains detected edit/delete/reorder/truncate/insert mutations in synthetic agent event logs; HMAC also detected a keyless recomputation attack that bypassed a rewritten keyless SHA-256 chain and rewritten anchor.

## Why it stopped

No-paper useful signal: evidence is synthetic and bounded. It supports a design mechanism and exposes the keyless-chain failure mode, but it is not real-agent reliability validation.

## Recommended next action

Stop paper path for this run; next concrete step is a bounded integration test in a real local agent runner with HMAC ledger records and crash/tamper fault injection.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: HMAC evidence ledger integration in a real local agent runner
- Success threshold: At least 99 percent detection across injected real-artifact tamper cases, no undetected content edits, and under 5 percent median runtime overhead on 30 short local tasks.
- Stop condition: Stop if integration requires privileged/private control-plane components, if median overhead exceeds 20 percent after straightforward batching, or if any content-edit mutation remains undetected with intact verifier key material.

## Evidence references

- Artifact root: `<local-path>/projects/hash-chained-evidence-ledger-for-local-agent-reliability-222fad19092a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
