# Evidence-Ledger Replay Auditing for Small Agents on Repeated Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-replay-auditing-for-small-agents-on-repeated-tasks-440f9d062ba0`
Run ID: `evidence-ledger-replay-auditing-for-small-agents-on-repeated-tasks-440f9d062ba0-20260628T154510157152+0000`

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

- Provider-backed Research Facility batch: z-ai/glm-5.2: enoch://research-facility/provider/z-ai/glm-5.2/9ea8f3f1be6b

## What looked useful

Across a 5,000-episode synthetic benchmark and a 10-seed 10,000-episode sweep, ledger replay achieved 1.0 recall/F1 for injected audit-worthy faults, while final-answer-only auditing averaged 0.593 recall and transcript heuristics averaged 0.762 recall in the sweep.

## Boundaries and scale limits

Toy simulator only; no real LLM agent traces, no non-deterministic external tools, no adversarial ledger-forging tests, and no production workload validation.

## Claim scope

On deterministic synthetic repeated tasks, replayable evidence ledgers can detect injected process faults that final-answer-only and shallow transcript-heuristic auditors miss.

## Why it stopped

No-paper closure: this run produced a useful synthetic mechanism signal, but the evidence is not direct or broad enough for publication-grade validation.

## Recommended next action

Run a bounded direct validation on snapshot-backed real small-agent traces with independent fault labels and a stronger model-based transcript auditor baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay-audit real small-agent traces on snapshot-backed repeated tasks
- Success threshold: Ledger replay improves labeled fault recall by >=20 percentage points over the strongest non-ledger baseline at >=0.95 precision.
- Stop condition: Stop if replay cannot be made deterministic for the selected tool environment or if ledger replay fails to beat the strongest baseline by at least 10 recall points in the first 100 labeled traces.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-replay-auditing-for-small-agents-on-repeated-tasks-440f9d062ba0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
