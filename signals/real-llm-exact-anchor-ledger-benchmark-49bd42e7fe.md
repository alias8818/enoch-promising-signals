# Real-LLM Exact Anchor Ledger Benchmark

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-llm-exact-anchor-ledger-benchmark-49bd42e7fe`
Run ID: `real-llm-exact-anchor-ledger-benchmark-49bd42e7fe-20260528T224713331607+0000`

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

- Parent run decision: Exact Anchor Evidence Ledger for Tiny Agents: enoch://control-plane/projects/exact-anchor-evidence-ledger-for-tiny-agents-36d47913c507/runs/exact-anchor-evidence-ledger-for-tiny-agents-36d47913c507-20260527T154913869242+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/529125218837

## What looked useful

A real local LLM showed a large exact retrieval improvement from an explicit anchor ledger: +0.75 both-exact rate and +0.375 exact-value rate versus the no-ledger prompt, with no observed ledger hallucinated or distractor values in the main run.

## Boundaries and scale limits

Single small instruction model, one synthetic fixture family, one prompt template, CPU-only local inference, 8 paired cases; not validated on natural documents, larger context windows, multiple models, or adversarial prompt variants.

## Claim scope

In an 8-case synthetic exact-anchor extraction benchmark using Qwen/Qwen2.5-0.5B-Instruct, adding an explicit anchor ledger improved exact anchor-and-value JSON retrieval from 0.125 to 0.875.

## Why it stopped

Tier 1 direct test produced useful mechanism support, but the evidence remains too narrow for publication readiness.

## Recommended next action

Run a bounded multi-model replication with at least three open/local instruction models, 50+ paired cases, shuffled ledger order, and prompt-template ablations before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-Model Exact Anchor Ledger Replication
- Success threshold: Mean ledger-minus-plain both-exact improvement >= 0.20 across models, no model with negative both-exact delta worse than -0.05, and hallucinated/distractor value rates not higher for ledger than plain.
- Stop condition: Stop if two or more tested models show ledger-minus-plain both-exact delta <= 0.05 or if ledger increases hallucinated/distractor value rate by >= 0.10.

## Evidence references

- Artifact root: `<local-path>/projects/real-llm-exact-anchor-ledger-benchmark-49bd42e7fe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
