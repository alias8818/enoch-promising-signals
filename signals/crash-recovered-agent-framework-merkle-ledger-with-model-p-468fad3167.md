# Crash-Recovered Agent-Framework Merkle Ledger with Model-Parsed Tool Calls

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `crash-recovered-agent-framework-merkle-ledger-with-model-p-468fad3167`
Run ID: `crash-recovered-agent-framework-merkle-ledger-with-model-p-468fad3167-20260528T094943363419+0000`

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

- Parent run decision: Merkle Evidence Ledger for Local 1B Agents: enoch://control-plane/projects/merkle-evidence-ledger-for-local-1b-agents-3412c8832984/runs/merkle-evidence-ledger-for-local-1b-agents-3412c8832984-20260528T002253326962+0000
- Parent run decision: Real 1B-Agent Trace Integration for Merkle Evidence Ledger: enoch://control-plane/projects/real-1b-agent-trace-integration-for-merkle-evidence-ledger-1fa21c996d/runs/real-1b-agent-trace-integration-for-merkle-evidence-ledger-1fa21c996d-20260528T054643294794+0000

## What looked useful

Merkle chaining outperformed append-only JSONL, checkpoint+WAL, and a hash-only ablation on direct recovery and tamper-detection metrics; the ablation shows the previous-hash chain is needed for dropped-record and forked-tail detection. Overhead was 3.95x write time, 2.95x read time, and 2.62x storage versus plain JSONL in this prototype.

## Boundaries and scale limits

Synthetic model outputs, Python prototype storage, single-process execution, injected byte/record faults, no live LLM calls, no production agent framework, no concurrent tools, and no real power-loss or filesystem crash testing.

## Claim scope

In a deterministic local benchmark with model-parsed synthetic tool-call outputs, a Merkle-chained JSONL ledger achieved exact clean replay, strict prefix recovery after partial writes, and 100% detection of valid payload corruption, dropped records, and forked tails across 30 fixed seeds and 200 steps per seed.

## Why it stopped

Tier 2 evidence supports the mechanism but remains synthetic/local and is not publication-grade direct evidence for a real agent framework.

## Recommended next action

Stop paper escalation for this run; deepen with the same fault matrix inside a real agent runtime using live model/tool traces and explicit fsync/crash-boundary instrumentation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live Agent Runtime Merkle Ledger Crash Harness
- Success threshold: Across at least 20 live-agent traces and the same fault classes, Merkle ledger detection when needed is at least 0.95, clean false-positive rate is 0, acceptable recovery exceeds the best baseline by at least 0.30 absolute, and write/storage overhead remains below 5x plain JSONL.
- Stop condition: Stop if live-runtime integration cannot reproduce clean replay, if Merkle detection falls below 0.90 on dropped/forked records, or if overhead exceeds 5x before adding durability semantics.

## Evidence references

- Artifact root: `<local-path>/projects/crash-recovered-agent-framework-merkle-ledger-with-model-p-468fad3167`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
