# Signer-isolated append-only evidence ledger for real agent tool traces

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `signer-isolated-append-only-evidence-ledger-for-real-agent-b51c10fd31`
Run ID: `signer-isolated-append-only-evidence-ledger-for-real-agent-b51c10fd31-20260628T230215893085+0000`

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

- Parent run decision: Evidence-Ledger Attestation Chains for CPU Agent Tool Calls: enoch://control-plane/projects/evidence-ledger-attestation-chains-for-cpu-agent-tool-calls-e98be7807db5/runs/evidence-ledger-attestation-chains-for-cpu-agent-tool-calls-e98be7807db5-20260628T222049728668+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/edbe5c5bae6d

## What looked useful

Signer isolation plus signed hash chaining is viable for tamper-evident captured trace entries, but a ledger alone cannot prove all tool calls were captured and cannot detect truncation unless final roots or checkpoints are externally anchored.

## Boundaries and scale limits

Only three local subprocess tool traces were captured. No hostile multi-process agent, kernel-level isolation, long-running trace stream, remote transparency log, or tool-gateway interposition was evaluated. Completeness against omitted tool calls was not achieved.

## Claim scope

Local smoke-scale prototype: a separate signer process using OpenSSL Ed25519 signed three real local tool trace entries into a hash-chained JSONL ledger, and an offline public-key verifier detected content tamper, reordering, stale rollback append attempts, and truncation when an external anchor was supplied.

## Why it stopped

Local evidence supports the tamper-evidence mechanism but falsifies the stronger ledger-alone completeness claim; this is not full validation for real agent traces.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should put all tool execution behind a mandatory signer-backed gateway and measure whether intentional omission attempts are blocked.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Mandatory tool-gateway capture for signer-isolated trace ledgers
- Success threshold: Detect or block 100% of scripted content tamper, reordering, truncation with anchor, stale rollback append, and producer-level omission attempts in a local harness of at least 100 tool events, with zero verifier false accepts.
- Stop condition: Stop as negative if any scripted omission path can execute a tool without a corresponding signed ledger entry, or if anchored verification falsely accepts mutated, reordered, or truncated traces.

## Evidence references

- Artifact root: `<local-path>/projects/signer-isolated-append-only-evidence-ledger-for-real-agent-b51c10fd31`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
