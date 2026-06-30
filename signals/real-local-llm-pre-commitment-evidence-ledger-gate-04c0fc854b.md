# Real Local LLM Pre-Commitment Evidence-Ledger Gate

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-local-llm-pre-commitment-evidence-ledger-gate-04c0fc854b`
Run ID: `real-local-llm-pre-commitment-evidence-ledger-gate-04c0fc854b-20260611T113251102775+0000`

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

- Parent run decision: Evidence-Ledger-Gated Action: Pre-Commitment Reduces Hallucinated Steps: enoch://control-plane/projects/evidence-ledger-gated-action-pre-commitment-reduces-hallucinated-steps-55ab28e2c1c6/runs/evidence-ledger-gated-action-pre-commitment-reduces-hallucinated-steps-55ab28e2c1c6-20260611T111701999760+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bfc61bad5e15

## What looked useful

A strict evidence-ledger gate eliminated unsupported acceptances in the strongest tested local model, reducing Qwen2.5-0.5B-Instruct unsupported accepts from 2/7 baseline to 0/7 gated, but it also rejected all 5/5 supported claims because the model failed to pre-commit exact evidence IDs.

## Boundaries and scale limits

Synthetic machine-checkable evidence, compact local models, small fixed dataset, simple prompt protocols, and a gold-ID verifier. This does not establish behavior on larger local LLMs, open-domain retrieval, production evidence, or learned entailment verification.

## Claim scope

Tier 1 controlled 12-case local-LLM test of a pre-commitment evidence-ID ledger gate using flan-t5-small, SmolLM2-135M-Instruct, and Qwen2.5-0.5B-Instruct on CPU.

## Why it stopped

Tier 1 direct test produced a useful but no-paper mixed result: the gate blocked unsupported acceptances, but failed the stated threshold by over-rejecting every supported claim.

## Recommended next action

Run a constrained evidence-ID selection follow-up that prevents value-only ledgers and tests whether the gate can keep zero unsupported accepts while retaining at least 4/5 supported accepts on this set plus a held-out controlled extension.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Constrained Evidence-ID Selection for Local LLM Ledger Gates
- Success threshold: Zero unsupported gated accepts and at least 4/5 supported gated accepts on the original set, plus at least 90% supported gated acceptance and zero unsupported gated acceptance on the held-out controlled extension.
- Stop condition: Stop if constrained ledgers still accept fewer than 4/5 supported original cases or produce any unsupported gated accept on the original set.

## Evidence references

- Artifact root: `<local-path>/projects/real-local-llm-pre-commitment-evidence-ledger-gate-04c0fc854b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
