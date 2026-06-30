# Compressed State Ledger for Small Agent Tool Verification

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `compressed-state-ledger-for-small-agent-tool-verification-36d639504452`
Run ID: `compressed-state-ledger-for-small-agent-tool-verification-36d639504452-20260603T183845227647+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/810c7576d010

## What looked useful

The mechanism is viable for compact commitment and replay verification of small deterministic tool traces: 10000/10000 injected mutations detected, mean compressed ledger 7191.987 bytes versus mean raw trace 48809.714 bytes, mean verification 0.7312 ms per valid 32-step trace.

## Boundaries and scale limits

Synthetic only: 1000 traces, 32 steps per trace, three deterministic tools, 10000 injected local mutations. No real LLM agent traces, no production framework integration, no privacy-preserving verification without full trace reveal, and no comparison to existing audit-log or Merkle-log baselines.

## Claim scope

On deterministic synthetic small-agent workflows with explicit full traces available at verification time, a compressed digest ledger detected all injected local tool/trace/ledger mutations while reducing retained verification bytes by about 6.79x versus raw JSON traces.

## Why it stopped

No-paper useful signal: synthetic evidence supports the compact-ledger mechanism for local deterministic trace tampering, but it is not direct publication-grade evidence for real small-agent tool verification.

## Recommended next action

Run the verifier on real traces from two small agent frameworks and compare storage, replay cost, and detection coverage against a Merkle-log or audit-log baseline under replay, reorder, substitution, and tool-output tampering attacks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Agent Trace Test for Compressed Tool Verification Ledgers
- Success threshold: At least 99.9% detection of injected non-colliding attacks, at least 3x byte reduction versus raw logs, and p95 verification latency below 5 ms per 50-step trace on CPU.
- Stop condition: Stop if real traces require semantic context absent from the compressed commitments, if detection falls below 99.9% for non-colliding attacks, or if byte reduction drops below 3x versus raw audit logs.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-state-ledger-for-small-agent-tool-verification-36d639504452`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
