# Evidence-ledger rollback on existing natural-language local agent traces

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-rollback-on-existing-natural-language-loca-757ebbc5bb`
Run ID: `evidence-ledger-rollback-on-existing-natural-language-loca-757ebbc5bb-20260605T100313918889+0000`

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

- Parent run decision: Evidence-Ledger Rollback for Small Local Agents: enoch://control-plane/projects/evidence-ledger-rollback-for-small-local-agents-de053873248b/runs/evidence-ledger-rollback-for-small-local-agents-de053873248b-20260605T021944513018+0000
- Parent run decision: Evidence-ledger rollback on real small local tool-agent traces: enoch://control-plane/projects/evidence-ledger-rollback-on-real-small-local-tool-agent-tr-bc95ba8933/runs/evidence-ledger-rollback-on-real-small-local-tool-agent-tr-bc95ba8933-20260605T060340997659+0000

## What looked useful

Rollback-visible context can reduce stale-value leakage for a competent local model and for a latest-mention symbolic baseline, but the effect did not replicate across weaker/saturated/format-failing local models and missed the prior 20 percentage-point practical threshold.

## Boundaries and scale limits

Trace source was an existing structured local signed-tool corpus rendered into natural language, not originally model-authored natural-language agent transcripts; tasks were constrained multiple-choice final-state questions; models were small cached local checkpoints; no production agent loop or frontier model was tested.

## Claim scope

On 100 fixed-seed scenarios rendered into natural language from existing signed local tool traces, rollback-visible context significantly improved Qwen2.5-1.5B active-evidence accuracy and stale-leakage rate, while aggregate results across five local models were not significant.

## Why it stopped

Tier 2 fixed-seed validation produced a useful but mixed mechanism signal: one model improved by 18 pp with significant stale-leak reduction, but aggregate local-model evidence was not significant and the practical 20 pp threshold was not met.

## Recommended next action

Run a bounded depth-3 follow-up only if originally natural-language model-authored traces are available; otherwise stop because this rendered-trace Tier 2 result is mixed and no-paper.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Rollback-visible evidence ledgers on originally model-authored natural-language agent traces
- Success threshold: Rollback-visible improves active-evidence accuracy by >=20 percentage points over append-only and annotated controls and reduces stale leakage with paired or exact-test p<0.05 on at least two model classes.
- Stop condition: Stop if no originally natural-language trace corpus is available, if parse failures exceed 10% after a structured answer interface, or if rollback-visible fails to beat controls by >=10 pp on the first competent model.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-rollback-on-existing-natural-language-loca-757ebbc5bb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
