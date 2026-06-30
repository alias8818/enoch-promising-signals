# Real Small-LLM Evidence Ledger vs Unstructured Memory Reliability Probe

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-small-llm-evidence-ledger-vs-unstructured-memory-reli-52643fe13e`
Run ID: `real-small-llm-evidence-ledger-vs-unstructured-memory-reli-52643fe13e-20260525T193250975705+0000`

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

- Parent run decision: Evidence Ledger vs Unstructured Memory for Small Agent Reliability: enoch://control-plane/projects/evidence-ledger-vs-unstructured-memory-for-small-agent-reliability-9b5a7967bde2/runs/evidence-ledger-vs-unstructured-memory-for-small-agent-reliability-9b5a7967bde2-20260525T174110999471+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/12cd6f3c96f9

## What looked useful

Across three 48-case seeds, ledger accuracy was 26.39% versus 7.64% for unstructured memory, stale-error rate was 34.72% versus 92.36%, and paired correctness favored ledger-only correct over unstructured-only correct by 30 to 3 cases. Primary predefined threshold was narrowly missed, so this is mechanism support rather than success closure.

## Boundaries and scale limits

Single small LLM, synthetic short evidence, explicit answer options, and a structured-table versus prose format/length confound. The result is not paper-positive and does not validate real deployed agent memory systems.

## Claim scope

In a synthetic current-value retrieval task using google/flan-t5-small, a structured evidence ledger improved exact current-code accuracy over unstructured chronological memory and sharply reduced stale obsolete-value errors, but the primary 48-case run missed the predefined 20 percentage-point accuracy-lift threshold by 1.25 points.

## Why it stopped

Tier 1 controlled direct test completed; result is a useful no-paper signal because mechanism direction is stable but the predefined primary threshold was not met and important controls remain.

## Recommended next action

Run a bounded deepen test with 2-3 small LLMs and length-matched ledger/prose controls before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Length-Matched Multi-Model Evidence Ledger Reliability Check
- Success threshold: Mean ledger stale-error rate at least 20 percentage points lower than the best unstructured/prose control and exact-answer accuracy at least 20 percentage points higher, with the effect present in at least two models.
- Stop condition: Stop if length-matched controls reduce the ledger advantage below 10 percentage points on both accuracy and stale-error metrics for two models.

## Evidence references

- Artifact root: `<local-path>/projects/real-small-llm-evidence-ledger-vs-unstructured-memory-reli-52643fe13e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
