# Evidence-ledger agent with rollback on contradiction

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-with-rollback-on-contradiction-b6f89c47dc66`
Run ID: `evidence-ledger-agent-with-rollback-on-contradiction-b6f89c47dc66-20260521T220804590367+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/1d33469bb5d9

## What looked useful

Rollback maintained 1.0 mean final accuracy with 0 stale active derived claims and 0 active contradiction rate, while append-only retained 1017.9 stale active derived claims and 0.5283 active contradiction rate on the main benchmark. A latest-fact recompute control also achieved perfect consistency and was much faster, so the result supports the mechanism but not a paper-ready advantage.

## Boundaries and scale limits

Tested only on CPU synthetic workloads up to 100 cases, 500 entities per case, and 6 updates per entity; no natural-language extraction, LLM agent traces, LangGraph persistence, source-reliability uncertainty, or large-scale long-running memory workloads were tested.

## Claim scope

In a structured synthetic event stream with exact contradiction keys and derived eligibility claims, dependency-linked rollback removes stale active derived claims and active contradictions while preserving final-answer accuracy.

## Why it stopped

No-paper useful signal: the synthetic mechanism worked, but the strongest structured-data baseline was faster and the run did not test realistic agent evidence ingestion.

## Recommended next action

Run a bounded LangGraph/LLM trace benchmark where evidence is extracted from natural-language observations and compare rollback, append-only, and recompute controls on consistency, auditability, and task success.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LangGraph evidence-ledger rollback on noisy natural-language contradiction traces
- Success threshold: Rollback reduces active contradiction rate and stale derived claims by at least 80% versus append-only while staying within 2x runtime or token overhead of the recompute/control path and without lowering final task accuracy.
- Stop condition: Stop if rollback does not materially reduce contradictions versus append-only, if recompute dominates both accuracy and cost on all realistic traces, or if natural-language contradiction extraction is too unreliable to evaluate rollback independently.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-with-rollback-on-contradiction-b6f89c47dc66`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
