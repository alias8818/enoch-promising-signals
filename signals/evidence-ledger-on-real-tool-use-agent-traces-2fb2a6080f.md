# Evidence Ledger on Real Tool-Use Agent Traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-on-real-tool-use-agent-traces-2fb2a6080f`
Run ID: `evidence-ledger-on-real-tool-use-agent-traces-2fb2a6080f-20260609T214333532634+0000`

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

- Parent run decision: Evidence Ledger for Tool-Use Agent Reliability: enoch://control-plane/projects/evidence-ledger-for-tool-use-agent-reliability-1d8b149bc7bf/runs/evidence-ledger-for-tool-use-agent-reliability-1d8b149bc7bf-20260609T171317283126+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3e789731a7f3

## What looked useful

The Tier 1 direct test produced a verifiable ledger for a real agent trace; clean verification passed, ledger mutation was rejected with entry_3_mismatch, and trace output mutation was rejected with root_hash_mismatch plus entry_4_mismatch.

## Boundaries and scale limits

Validated on 1 trace file with 26 events, 16 command_execution events, 8 completed command events, and 2 controlled corruption modes. Not validated across multiple agents, trace schemas, redaction policies, concurrent trace streams, or adaptive adversarial rewrites.

## Claim scope

A dependency-free SHA-256 evidence ledger can be built from one real Codex/Enoch tool-use trace snapshot and can detect controlled ledger and source-trace mutations in command evidence.

## Why it stopped

No-paper useful signal: mechanism supported by a small direct real-trace test, but the corpus and corruption coverage are too narrow for publication readiness.

## Recommended next action

Run a bounded deepen test over at least 50 real traces from multiple projects or agent surfaces with a fixed corruption suite and a raw-checksum baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-trace Evidence Ledger Robustness Suite
- Success threshold: Clean verification succeeds on 100% of unchanged traces and detects 100% of the fixed corruption suite, with more specific failure localization than a raw file checksum baseline.
- Stop condition: Stop if any unchanged real trace cannot be parsed without an explicit schema adapter, or if any fixed corruption is not detected by ledger verification.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-on-real-tool-use-agent-traces-2fb2a6080f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
