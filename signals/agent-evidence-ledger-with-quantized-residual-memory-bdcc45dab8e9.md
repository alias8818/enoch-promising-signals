# Agent Evidence Ledger with Quantized Residual Memory

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `agent-evidence-ledger-with-quantized-residual-memory-bdcc45dab8e9`
Run ID: `agent-evidence-ledger-with-quantized-residual-memory-bdcc45dab8e9-20260605T035152724237+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/6bd3f315dc2e

## What looked useful

The mechanism is budget-dependent: size the evidence ledger to fact cardinality first, then allocate remaining memory to quantized residual retrieval. Naive hybrid splits fail under severe memory pressure, but moderate budgets produced higher balanced fact-plus-clue recall than raw recency, ledger-only, or residual-only controls.

## Boundaries and scale limits

No real agent traces, no imperfect natural-language extraction, no LLM downstream QA, no learned compression baselines, and no large-scale or long-horizon deployment evidence. CPU-only benchmark completed in seconds.

## Claim scope

Synthetic fixed-byte memory benchmark over deterministic agent-like observation streams: a hybrid evidence ledger plus quantized residual memory outperformed raw recency and single-component controls at 64 KiB and 128 KiB budgets, but not at 16 KiB or 32 KiB.

## Why it stopped

Closed as no-paper useful signal: synthetic evidence supports the storage mechanism in moderate-budget regimes but is not direct validation of an agent evidence-ledger system.

## Recommended next action

Run a bounded real-trace follow-up with noisy extraction, citation checks, fixed downstream LLM QA, and the same memory policies before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace evidence ledger and quantized residual memory evaluation
- Success threshold: Hybrid memory improves balanced QA accuracy by at least 10 percentage points over the best non-hybrid baseline at two or more practical byte budgets while preserving citation correctness within 2 percentage points of ledger-only on fact questions.
- Stop condition: Stop if hybrid fails to beat the best non-hybrid baseline by at least 5 percentage points at all tested budgets, or if extraction noise removes the fact-recall advantage.

## Evidence references

- Artifact root: `<local-path>/projects/agent-evidence-ledger-with-quantized-residual-memory-bdcc45dab8e9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
