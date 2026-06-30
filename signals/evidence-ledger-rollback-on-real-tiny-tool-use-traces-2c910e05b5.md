# Evidence-ledger rollback on real tiny tool-use traces

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-rollback-on-real-tiny-tool-use-traces-2c910e05b5`
Run ID: `evidence-ledger-rollback-on-real-tiny-tool-use-traces-2c910e05b5-20260525T084251489530+0000`

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

- Parent run decision: Evidence-Ledger Rollback for Tiny Tool-Use Agents: enoch://control-plane/projects/evidence-ledger-rollback-for-tiny-tool-use-agents-b710d357ba05/runs/evidence-ledger-rollback-for-tiny-tool-use-agents-b710d357ba05-20260525T083241001331+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8a852442b9b4

## What looked useful

Rollback alone is insufficient for real tiny traces where models answer without evidence dependencies; mandatory final-answer gating rescued 4/4 active unsupported finals in replay, while rollback rescued 2/4.

## Boundaries and scale limits

Tiny inherited trace replay only: two models, four tasks per model, deterministic support labels, no live regeneration, no human labels, and no production agent framework.

## Claim scope

On 16 recorded rows from two balanced Qwen tiny tool-use trace files, dependency-aware rollback removed only 2 of 4 active unsupported baseline final answers because two unsupported answers had no evidence dependency edges.

## Why it stopped

Tier 1 real trace replay falsified the rollback-alone 90% rescue threshold; this is an early direct falsification for the scoped trace set, not a full validation.

## Recommended next action

Run a bounded prospective tiny-model test that forces final-answer dependency IDs, injects audited tool corrections, and compares rollback, final-gate-only, and combined gate-plus-rollback on at least 50 held-out traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Prospective gate-plus-rollback test on real tiny tool-use traces
- Success threshold: Gate-plus-rollback removes at least 90% of stale or unsupported dependency-linked finals, has zero false invalidations of supported finals, and does not reduce exact-match accuracy by more than 5 percentage points versus final-gate-only.
- Stop condition: Stop if fewer than 10 traces contain dependency-linked audited corrections after 50 tasks, or if gate-plus-rollback fails to exceed 80% stale-final removal in an interim 25-trace checkpoint.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-rollback-on-real-tiny-tool-use-traces-2c910e05b5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
