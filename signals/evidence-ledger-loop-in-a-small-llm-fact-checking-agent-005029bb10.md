# Evidence ledger loop in a small LLM fact-checking agent

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `evidence-ledger-loop-in-a-small-llm-fact-checking-agent-005029bb10`
Run ID: `evidence-ledger-loop-in-a-small-llm-fact-checking-agent-005029bb10-20260531T142230835117+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Tiny agent evidence ledger loop: enoch://control-plane/projects/tiny-agent-evidence-ledger-loop-d32568392f5e/runs/tiny-agent-evidence-ledger-loop-d32568392f5e-20260530T082540923162+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/241613175b74

## What looked useful

The no-ledger baseline and evidence-ledger loop both scored 12/36 accuracy. Retrieval contained expected evidence for all cases, but the small model labeled all 216 ledger rows neutral and predicted true for all final decisions, showing a reproducible naive-ledger failure mode.

## Boundaries and scale limits

Single small instruction model, synthetic corpus, 36 claims, CPU-only inference, fixed-label scoring; not a real web/FEVER benchmark and not a sweep over prompt schemas or model families.

## Claim scope

In a 36-case controlled synthetic fact-checking task using google/flan-t5-small with fixed-label log-likelihood scoring and identical retrieved evidence, the tested evidence-ledger loop did not improve accuracy over a no-ledger baseline.

## Why it stopped

Tier 1 direct controlled test completed; result is no-paper useful signal because the tested ledger loop failed to beat baseline and does not support paper-positive claims.

## Recommended next action

Run a bounded deepen test that calibrates the relation-judgment prompt/schema before final aggregation, holding retrieval and the 36-case task fixed.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated relation ledger for small LLM fact-checking
- Success threshold: Calibrated ledger accuracy exceeds no-ledger baseline by at least 0.20 absolute accuracy with bootstrap 95% CI lower bound greater than 0.0 and no collapse to a single final label.
- Stop condition: Stop if relation judgments still collapse to one label or if calibrated-ledger accuracy is not above baseline on the 36-case controlled task.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-loop-in-a-small-llm-fact-checking-agent-005029bb10`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
