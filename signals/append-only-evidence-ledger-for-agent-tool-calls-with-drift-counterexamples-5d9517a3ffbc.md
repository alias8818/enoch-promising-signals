# Append-Only Evidence Ledger for Agent Tool Calls with Drift Counterexamples

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `append-only-evidence-ledger-for-agent-tool-calls-with-drift-counterexamples-5d9517a3ffbc`
Run ID: `append-only-evidence-ledger-for-agent-tool-calls-with-drift-counterexamples-5d9517a3ffbc-20260620T052547411639+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d5f543192b10

## What looked useful

In a 1000-entry synthetic run, the clean ledger verified with zero failures, injected modification/deletion/reordering were all detected, replay produced 209 semantic drift counterexamples, and semantic validators filtered 190 benign exact-hash-only metadata changes.

## Boundaries and scale limits

1000 synthetic deterministic calls only; no real agent runtime integration, no external API drift, no concurrent writers, no adversarial fork resistance, no privacy/redaction evaluation, and no human triage study.

## Claim scope

Synthetic local probe of a JSONL SHA-256 hash-chain ledger for deterministic tool calls, with replay against deterministic v2 tools and hand-written semantic validators.

## Why it stopped

Synthetic/proxy evidence supports the mechanism but is insufficient for publication-grade validation.

## Recommended next action

Run the bounded real-trace follow-up; this run should stop as no-paper useful signal because the current evidence is synthetic/proxy rather than direct production-agent validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Agent Trace Validation for Append-Only Tool Evidence Ledger
- Success threshold: Tamper detection rate 1.0 on injected attacks, semantic drift recall at least 0.9, and at least 30% fewer benign drift flags than exact output-hash replay on real traces.
- Stop condition: Stop if the real-trace semantic false-positive rate is not at least 30% lower than exact output-hash replay or if ledger capture breaks ordinary agent execution.

## Evidence references

- Artifact root: `<local-path>/projects/append-only-evidence-ledger-for-agent-tool-calls-with-drift-counterexamples-5d9517a3ffbc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
