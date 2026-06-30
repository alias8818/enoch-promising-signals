# Evidence-Ledged Agent Rollback on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledged-agent-rollback-on-cpu-c8483538a7e8`
Run ID: `evidence-ledged-agent-rollback-on-cpu-c8483538a7e8-20260527T184911041439+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/d13ad575a741

## What looked useful

Rollback can help when the rollback evidence signal is precise enough, but naively adding noisy test-drop triggers can cause excessive false rollbacks and lower task completion.

## Boundaries and scale limits

No real LLM agents, repositories, tool calls, wall-clock checkpoint cost, or held-out software tasks were tested. The benchmark used 24,000 synthetic episodes and fixed controller policies on one CPU process.

## Claim scope

Synthetic CPU mechanism probe of rollback controllers on noisy multi-requirement agent trajectories. Evidence-only rollback improved success and reduced harmful committed actions versus no rollback across low, medium, and high noise. A combined evidence-plus-noisy-test ledger was not robust and underperformed no rollback in the high-noise scenario.

## Why it stopped

Proxy mechanism test only; the combined ledger policy failed in high noise and real-agent evidence is required before any paper claim.

## Recommended next action

Run a bounded direct agent-harness follow-up on small repository-editing tasks comparing no rollback, test-only rollback, evidence-only rollback, and calibrated evidence-ledger rollback.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Agent-Harness Evidence-Ledger Rollback
- Success threshold: Evidence-ledger rollback improves task pass rate by at least 10 percentage points over no rollback and at least 5 percentage points over test-only rollback, while false rollbacks stay below 1.0 per task on average.
- Stop condition: Stop if evidence-ledger rollback fails to beat no rollback on pass rate or if false rollbacks exceed 2.0 per task on average after the first 30 tasks.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledged-agent-rollback-on-cpu-c8483538a7e8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
