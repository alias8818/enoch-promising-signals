# Budget-matched sparse FP8 residual ledger for fact retrieval

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `budget-matched-sparse-fp8-residual-ledger-for-fact-retriev-d0132312b4`
Run ID: `budget-matched-sparse-fp8-residual-ledger-for-fact-retriev-d0132312b4-20260523T030612819056+0000`

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

- Parent run decision: Ternary Agent Memory with FP8 Residual Ledger for Fact Retrieval: enoch://control-plane/projects/ternary-agent-memory-with-fp8-residual-ledger-for-fact-retrieval-507a3585af6b/runs/ternary-agent-memory-with-fp8-residual-ledger-for-fact-retrieval-507a3585af6b-20260523T025704940713+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8780efafda6d

## What looked useful

Top-k FP8 residual coordinates are informative: at 8192 facts/noise 0.20, sparse-salient top-1 was 0.7335 versus 0.1201 for random sparse; diffuse top-1 was 0.5972 versus 0.1171. But dense FP8 remained better at 0.7827 and 0.7813 top-1 respectively under the same 512-byte/fact budget.

## Boundaries and scale limits

Synthetic vectors only; no real language-model activations, corpus QA, learned memory, hybrid base-plus-residual design, or optimized sparse-serving kernel was tested. Largest run used 16384 facts, 512 dimensions, one query per fact, and one GPU process.

## Claim scope

In a controlled synthetic fact-key retrieval task with 8192-16384 facts and equal per-fact byte budgets, a standalone sparse FP8 residual ledger preserves meaningful retrieval signal versus random sparse storage but does not match or beat dense FP8 full-vector storage.

## Why it stopped

Tier 1 direct synthetic retrieval supports the mechanism over random sparse storage but falsifies the stronger standalone budget-matched claim against dense FP8; this is an early bounded result, not full validation on real model facts.

## Recommended next action

Stop this standalone sparse-ledger claim as no-paper; the next bounded test should evaluate a hybrid low-bit dense base plus sparse FP8 residual ledger under the same byte budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hybrid low-bit dense base plus sparse FP8 residual ledger for fact retrieval
- Success threshold: Hybrid must improve top-1 recall by at least 3 absolute percentage points over dense FP8 or match dense FP8 within 1 point while using at least 25% fewer bytes, with no regression larger than 3 points in diffuse residuals.
- Stop condition: Stop if hybrid fails to beat dense FP8 by at least 1 point in sparse-salient regimes and loses more than 5 points in diffuse regimes across 5 seeds.

## Evidence references

- Artifact root: `<local-path>/projects/budget-matched-sparse-fp8-residual-ledger-for-fact-retriev-d0132312b4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
