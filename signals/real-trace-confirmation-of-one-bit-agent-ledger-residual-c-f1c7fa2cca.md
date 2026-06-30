# Real-trace confirmation of one-bit agent ledger residual compression

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `real-trace-confirmation-of-one-bit-agent-ledger-residual-c-f1c7fa2cca`
Run ID: `real-trace-confirmation-of-one-bit-agent-ledger-residual-c-f1c7fa2cca-20260525T034820955392+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: 1-bit agent ledger with residual confidence: enoch://control-plane/projects/1-bit-agent-ledger-with-residual-confidence-091ea3c78b43/runs/1-bit-agent-ledger-with-residual-confidence-091ea3c78b43-20260525T031750991242+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/d6ad506a8a39

## What looked useful

A direct real-trace corpus test found 2,990.70 gzip-compressed residual bits per ledger event, far above the one-bit threshold even after excluding ids, statuses, exit codes, and outer schema fields.

## Boundaries and scale limits

The test covers local worker traces and gzip9 compression under a favorable residual definition; it does not test private traces, learned compressors, lossy summaries, or binary-only outcome ledgers.

## Claim scope

On 361 local real Enoch/Codex traces with 12,599 completed ledger events, favorable lossless residuals containing agent message text, shell commands, and command outputs do not compress to <=1 bit per event.

## Why it stopped

Controlled real-trace test directly falsified the <=1 bit/event lossless residual threshold for the operationalized claim; this is bounded evidence, not a universal compression impossibility proof.

## Recommended next action

Stop this line as a one-bit lossless residual compression claim; only revisit with a narrower lossy/binary ledger claim and a declared decoder.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-confirmation-of-one-bit-agent-ledger-residual-c-f1c7fa2cca`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
