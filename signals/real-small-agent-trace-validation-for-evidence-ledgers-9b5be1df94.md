# Real Small-Agent Trace Validation for Evidence Ledgers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-small-agent-trace-validation-for-evidence-ledgers-9b5be1df94`
Run ID: `real-small-agent-trace-validation-for-evidence-ledgers-9b5be1df94-20260525T164011029534+0000`

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

- Parent run decision: Evidence Ledger for Small Agent Tool-Use Verification: enoch://control-plane/projects/evidence-ledger-for-small-agent-tool-use-verification-eb219bc87c40/runs/evidence-ledger-for-small-agent-tool-use-verification-eb219bc87c40-20260525T143821026652+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2348c1aa266a

## What looked useful

The Tier 1 direct harness supports the mechanism that evidence-span ledgers can cheaply validate honest small-agent traces and catch common trace tampering classes, but exact substring support is too narrow for publication-grade claims.

## Boundaries and scale limits

The run did not test LLM-generated traces, semantic entailment, adversarial spans that contain the answer string while failing to support the claim, concurrent/multi-agent ledger merges, distributed consensus, source corruption, large corpora, or long open-ended workflows.

## Claim scope

In a controlled deterministic small-agent lookup harness over a fixed local corpus, a hash-chained evidence ledger with source hashes, byte spans, observation events, and claim-to-evidence links accepted all 800 honest traces and rejected all 5,600 tested tampered or unsupported traces with p95 validation latency below 0.1 ms.

## Why it stopped

Stopped after a successful Tier 1 controlled direct test because the mechanism signal is useful but not paper-ready; the remaining gap is semantic and agent-realism validation, not more repetitions of the same deterministic harness.

## Recommended next action

Run a bounded deepen follow-up that replaces exact substring checking with semantic evidence sufficiency tests on small LLM/tool-agent traces and adversarial near-miss spans.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Semantic Evidence Sufficiency for Small-Agent Evidence Ledgers
- Success threshold: Semantic verifier detects at least 0.85 of adversarial non-entailing cited spans, keeps honest trace acceptance at or above 0.90, and keeps p95 validation latency under 500 ms per trace in the bounded harness.
- Stop condition: Stop if exact-substring and semantic validation both fail to distinguish non-entailing spans above 0.70 detection or if honest trace false rejects exceed 0.20 after prompt/threshold calibration.

## Evidence references

- Artifact root: `<local-path>/projects/real-small-agent-trace-validation-for-evidence-ledgers-9b5be1df94`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
