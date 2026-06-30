# Evidence Ledger on Real Small Tool-Calling Traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-on-real-small-tool-calling-traces-7c40e260a3`
Run ID: `evidence-ledger-on-real-small-tool-calling-traces-7c40e260a3-20260525T213450637691+0000`

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

- Parent run decision: Evidence Ledger for Small Tool-Calling Agents: enoch://control-plane/projects/evidence-ledger-for-small-tool-calling-agents-ffe2a6c85e6f/runs/evidence-ledger-for-small-tool-calling-agents-ffe2a6c85e6f-20260525T205411106069+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c88017cb2969

## What looked useful

The ledger mechanism produced exact agreement with raw parsing for command counts, exit-code histogram, failed command list, and error-token counts; all 544 original ledger entries validated by source-line and output hashes; one copied-trace perturbation caused one source-line hash mismatch and one JSON reparse mismatch.

## Boundaries and scale limits

Small local corpus only; Codex JSONL command-execution schema only; deterministic command-level audit queries only; no human audit-time study, no semantic claim labels, no non-Codex trace portability test, and no large-scale deployment.

## Claim scope

On 24 real local Codex JSONL tool-calling traces containing 544 completed command-execution events, a hash-backed evidence ledger reproduced basic command-level audit answers from an independent raw parser and detected a controlled copied-trace perturbation.

## Why it stopped

Tier 1 controlled small direct test succeeded for the mechanism but is not paper-positive evidence for human auditability or agent reliability.

## Recommended next action

Run a bounded deepen follow-up with held-out real traces and labeled natural-language audit questions to test whether the ledger improves semantic audit accuracy or review time versus raw logs.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Labeled Semantic Audit Benchmark for Real Tool-Calling Evidence Ledgers
- Success threshold: Ledger condition reaches at least 95% exact-answer accuracy, has zero missed source-hash perturbations, and improves review effort by at least 2x or reduces unsupported answers by at least 50% relative to raw-log review.
- Stop condition: Stop if ledger answers disagree with raw ground truth on more than 5% of labeled questions, misses any source-hash perturbation, or shows no measurable review-effort or unsupported-answer improvement.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-on-real-small-tool-calling-traces-7c40e260a3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
