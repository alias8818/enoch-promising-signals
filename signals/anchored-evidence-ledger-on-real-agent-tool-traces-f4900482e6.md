# Anchored Evidence Ledger on Real Agent Tool Traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchored-evidence-ledger-on-real-agent-tool-traces-f4900482e6`
Run ID: `anchored-evidence-ledger-on-real-agent-tool-traces-f4900482e6-20260628T194732510180+0000`

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

- Parent run decision: Hash-Chained Evidence Ledger for Agent Reliability: enoch://control-plane/projects/hash-chained-evidence-ledger-for-agent-reliability-7460ad11295e/runs/hash-chained-evidence-ledger-for-agent-reliability-7460ad11295e-20260628T164251261647+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/98942fa828f9
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/deb7aa3d971c

## What looked useful

Implemented and verified a stdlib evidence-ledger builder over a real Codex trace: 54 JSONL events, 19 completed command executions, 8 agent messages, 28 evidence records, 3 claims, 0 parse errors, and 0 false accepts across 3 structural negative controls.

## Boundaries and scale limits

Only one local worker trace was tested; controls were deterministic structural corruptions rather than a labeled multi-project drift/trap benchmark; semantic truth of arbitrary natural-language claims was not evaluated.

## Claim scope

A single local Codex JSONL trace can be converted into a machine-checkable evidence ledger whose evidence records are anchored to source path, line number, and line SHA-256; simple broken references and anchor tampering are rejected.

## Why it stopped

Closed as no-paper useful signal: the mechanism works on one real local trace, but the evidence is too narrow for publication-grade validation.

## Recommended next action

Run the bounded multi-trace false-accept evaluation before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-trace anchored evidence ledger false-accept evaluation
- Success threshold: Zero false accepts on injected broken anchors/references and audited false-reject rate below 5% across at least 20 independent traces.
- Stop condition: Stop if any injected broken anchor/reference is accepted, or if labeled ungrounded claims cannot be represented without adding semantic assumptions outside the trace.

## Evidence references

- Artifact root: `<local-path>/projects/anchored-evidence-ledger-on-real-agent-tool-traces-f4900482e6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
