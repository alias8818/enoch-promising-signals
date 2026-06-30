# Evidence ledger for 1B local agent safety

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-for-1b-local-agent-safety-1c8c2e268560`
Run ID: `evidence-ledger-for-1b-local-agent-safety-1c8c2e268560-20260528T223101013004+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/6b9b255ca769

## What looked useful

Mechanism-level evidence suggests an evidence ledger is cheap and catches edit/delete/reorder/truncate tampering when a trusted checkpoint is retained, but this is not enough to claim improved 1B local agent safety.

## Boundaries and scale limits

Synthetic traces only; no real 1B-parameter model, real sandbox, production key management, adversarial process isolation, concurrent writers, or end-to-end local-agent safety benchmark was tested.

## Claim scope

A stdlib Python hash-chain plus HMAC evidence ledger over 10,000 synthetic local-agent tool events verified cleanly, added about 3.221 microseconds mean overhead per event versus synthetic event generation, detected four common post-hoc tampering probes, and preserved structured fields for offline policy contradiction scans.

## Why it stopped

Proxy evidence supports the ledger mechanism but does not directly validate 1B local agent safety or production adversarial robustness.

## Recommended next action

Stop this run as a no-paper useful signal; the next concrete test is to integrate the ledger with a real local 1B-class agent harness and run bounded fault injection against omitted, forged, raced, truncated, and replayed tool records.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fault-injected evidence ledger around a real local 1B agent harness
- Success threshold: Less than 5% median end-to-end latency overhead, clean verification on untampered traces, at least 95% aggregate tamper detection across predeclared fault injections, and no more than 2% false-positive policy alerts on benign tasks.
- Stop condition: Stop early if untampered real-agent traces fail clean verification, median latency overhead exceeds 10%, or any core tamper class remains undetected after adding trusted checkpoint storage.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-1b-local-agent-safety-1c8c2e268560`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
