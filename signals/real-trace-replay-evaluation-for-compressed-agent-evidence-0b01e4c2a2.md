# Real-trace replay evaluation for compressed agent evidence ledgers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-trace-replay-evaluation-for-compressed-agent-evidence-0b01e4c2a2`
Run ID: `real-trace-replay-evaluation-for-compressed-agent-evidence-0b01e4c2a2-20260529T191331016239+0000`

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

- Parent run decision: Compressed State Evidence Ledger for CPU Agent Safety: enoch://control-plane/projects/compressed-state-evidence-ledger-for-cpu-agent-safety-cddb89afe499/runs/compressed-state-evidence-ledger-for-cpu-agent-safety-cddb89afe499-20260529T143610646387+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/770071bce95e

## What looked useful

Compressed structured ledgers can preserve replay/audit decisions for a narrow but real numeric trace-claim class while dropping raw output text, provided the needed facts are extracted and hash-anchored.

## Boundaries and scale limits

Tier 1 local direct test only; claim extraction is limited to numeric metric and elapsed-time claims; counterfactuals are controlled; corpus is filename-selected local Enoch/Codex traces rather than a frozen public benchmark; non-numeric semantic evidence and broad scientific conclusions were not tested.

## Claim scope

On 60 local real Codex/Enoch JSONL traces, a compressed structured evidence ledger preserving hashes, command status, byte counts, and extracted numeric facts matched the full-ledger replay decisions for 24 real agent-written metric claims, rejected 22/22 same-output numeric counterfactuals, and reduced estimated ledger bytes by about 68%.

## Why it stopped

The Tier 1 direct replay threshold was met, but the evidence is narrow mechanism support rather than publication-grade validation of general compressed agent evidence ledgers.

## Recommended next action

Stop as no-paper useful signal; next bounded work should evaluate a frozen larger trace corpus with richer non-numeric claim classes and independent labels before any paper decision.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Frozen multi-class replay benchmark for compressed agent evidence ledgers
- Success threshold: At least 200 traces, at least 100 labeled/evaluable claims across at least four claim classes, compressed-vs-full decision agreement >= 0.98, compressed unsupported-claim rejection >= 0.95, and byte reduction >= 0.50.
- Stop condition: Stop negative if compressed-vs-full agreement falls below 0.95 on any major claim class or byte reduction is below 0.50 after preserving required replay evidence.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-replay-evaluation-for-compressed-agent-evidence-0b01e4c2a2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
