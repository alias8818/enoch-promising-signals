# Mandatory evidence ledger for small CPU agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `mandatory-evidence-ledger-for-small-cpu-agents-ed3a1af71024`
Run ID: `mandatory-evidence-ledger-for-small-cpu-agents-ed3a1af71024-20260609T052523891451+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/9e27228b3cd6

## What looked useful

Across 50 seeds with 120 entities per seed, ledger gating reduced unsupported claim rate from 13.73% to 0.00% and improved claim accuracy from 87.38% to 100.00%, with coverage falling from 92.82% to 80.29%. Sensitivity sweeps at hallucination-prior rates 0.25, 0.50, and 0.75 showed the same zero-unsupported ledger result with increasing coverage cost.

## Boundaries and scale limits

Synthetic corpora and deterministic proxy agents only; no live LLM agent, no real repository task suite, no human trace audit, and no long-running production workload validation.

## Claim scope

In a deterministic synthetic repository-QA benchmark, mandatory exact-span evidence ledgers eliminated unsupported emitted claims from a constrained retrieval/extraction agent, while reducing coverage through additional abstention.

## Why it stopped

Synthetic proxy evidence supports the ledger mechanism but is not direct publication-grade validation for real small CPU agents.

## Recommended next action

Stop this run as no-paper useful proxy evidence; the next concrete step is a bounded real-agent benchmark using small local models or CPU-only agent frameworks on repository QA/debugging traces with the same ledger metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real small-agent evidence-ledger benchmark on repository QA traces
- Success threshold: Unsupported claim rate reduced by at least 50% relative to permissive mode, task success drop no greater than 10 percentage points, and median wall-clock overhead no greater than 25%.
- Stop condition: Stop if ledger mode cannot reduce unsupported claims by at least 25% in an initial 20-task smoke run or if overhead exceeds 50% before accuracy gains appear.

## Evidence references

- Artifact root: `<local-path>/projects/mandatory-evidence-ledger-for-small-cpu-agents-ed3a1af71024`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
