# Evidence Ledger for Tool-Use Agents with Small Models

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-for-tool-use-agents-with-small-models-67b98ca9e548`
Run ID: `evidence-ledger-for-tool-use-agents-with-small-models-67b98ca9e548-20260607T074315438315+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/c5f32c29a0f0

## What looked useful

Full ledger reached 1.000 answer+citation validity on 2,000 synthetic tasks, while raw status-aware transcript reached 0.126 and raw recency transcript reached 0.035. Removing freshness or status filters reduced ledger performance to 0.130 and 0.206, supporting the provenance/filtering mechanism.

## Boundaries and scale limits

No neural small model was run. The benchmark is synthetic and constructed so ledger fields are machine-readable; results should not be generalized to real LLM tool-use traces without a direct small-model evaluation.

## Claim scope

On a deterministic synthetic tool-trace QA benchmark with stale, failed, and irrelevant observations, an explicit evidence ledger with entity/attribute/status/freshness/trust fields outperformed limited-context raw transcript policies and ledger ablations on exact answer plus citation validity.

## Why it stopped

Bounded proxy experiment completed; it provides useful mechanism evidence but not direct neural small-model validation.

## Recommended next action

Run the same benchmark through one real local small instruction model and compare raw transcript prompting, ledger prompting, and ledger-enforced postprocessing before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Small-Model Evidence-Ledger Prompting Test
- Success threshold: Evidence ledger improves answer+citation by at least 15 percentage points over the best raw transcript prompt and beats both ledger ablations on 1,000 or more held-out synthetic tasks.
- Stop condition: Stop if no runnable small model can be obtained within the deployment budget or if ledger prompting fails to beat the strongest raw transcript baseline by 5 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-tool-use-agents-with-small-models-67b98ca9e548`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
