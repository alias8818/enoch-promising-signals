# Counterexample Mining on Realistic Agent Evidence Ledgers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `counterexample-mining-on-realistic-agent-evidence-ledgers-b4d46ca0c6`
Run ID: `counterexample-mining-on-realistic-agent-evidence-ledgers-b4d46ca0c6-20260517T133542774830+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/536f48d17d5a

## What looked useful

Invariant checks over evidence references, temporal order, command success, quote support, artifact existence, and summary scope are a practical mechanism for mining counterexamples in structured agent evidence ledgers; across 20 randomized 80-ledger trials the invariant miner achieved mean F1 1.0 versus baseline mean F1 0.5541.

## Boundaries and scale limits

The corpus is local and trace-derived rather than independently sourced; counterexamples are planted and taxonomy-aligned with the miner; no naturally occurring production ledger corpus, blinded human labels, semantic paraphrase stress test, or multi-framework validation was run.

## Claim scope

On a controlled Tier 1 corpus of 80 structured evidence ledgers derived from local Codex agent JSONL traces, with 40 clean ledgers and 40 planted counterexamples across seven ledger failure modes, explicit invariant-based counterexample mining detected all planted failures with zero false positives and substantially outperformed a simple error-signal baseline.

## Why it stopped

Tier 1 direct controlled test supports the mechanism but remains no-paper evidence because the ledgers and counterexamples were locally constructed and planted, not independently sourced or naturally occurring.

## Recommended next action

Run a bounded deepen follow-up on independently authored multi-agent evidence-ledger fixtures with blinded labels and a stronger graph or semantic consistency baseline before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Blinded Multi-Agent Evidence Ledger Counterexample Benchmark
- Success threshold: Invariant miner achieves precision >= 0.90, recall >= 0.85, and F1 at least 0.15 above the best non-invariant baseline on blinded independently authored ledgers.
- Stop condition: Stop if recall falls below 0.70 or precision falls below 0.80 after rule fixes are frozen, or if independent ledger fixtures cannot be collected without private/human evidence.

## Evidence references

- Artifact root: `<local-path>/projects/counterexample-mining-on-realistic-agent-evidence-ledgers-b4d46ca0c6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
