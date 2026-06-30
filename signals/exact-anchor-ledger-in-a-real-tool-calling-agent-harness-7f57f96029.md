# Exact-anchor ledger in a real tool-calling agent harness

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `exact-anchor-ledger-in-a-real-tool-calling-agent-harness-7f57f96029`
Run ID: `exact-anchor-ledger-in-a-real-tool-calling-agent-harness-7f57f96029-20260530T022513453926+0000`

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

- Parent run decision: Exact-Anchor Agent Ledger for Tool Safety: enoch://control-plane/projects/exact-anchor-agent-ledger-for-tool-safety-88a3dc2447be/runs/exact-anchor-agent-ledger-for-tool-safety-88a3dc2447be-20260529T221326602280+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9cb0c1dbbdea

## What looked useful

Exact ledger binding of entity, field, value, and anchor achieved 0.0000 unsupported claim rate and 1.0000 accuracy across 384 claim opportunities; loose context and anchor-only baselines had 0.5208 unsupported claim rate and 0.4792 accuracy.

## Boundaries and scale limits

96 synthetic controlled cases on a CPU worker; deterministic answer composer; no live LLM, no LangGraph/OpenAI/Anthropic runtime, no human-authored corpus.

## Claim scope

In a deterministic local tool-calling harness with adversarial stale records, exact value-anchor ledger validation eliminated unsupported cited claims while anchor-existence validation did not.

## Why it stopped

No-paper closure: controlled direct harness supports the mechanism, but live model/framework evidence is required for publication-grade validation.

## Recommended next action

Run the same invariant inside a live LLM tool-calling harness with repeated generations and adversarial retrieved records before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live LLM exact-anchor ledger replication
- Success threshold: Exact-ledger unsupported claim rate is at least 80% lower than baseline, exact-ledger accuracy is no worse than 5 percentage points below baseline, and abstention rate is at most 10%.
- Stop condition: Stop if live LLM integration cannot be run locally/API-backed, or if exact-ledger unsupported claim reduction is below 50% on the first 50 cases.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-ledger-in-a-real-tool-calling-agent-harness-7f57f96029`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
