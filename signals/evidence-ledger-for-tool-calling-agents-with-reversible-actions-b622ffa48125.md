# Evidence Ledger for Tool-Calling Agents with Reversible Actions

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-for-tool-calling-agents-with-reversible-actions-b622ffa48125`
Run ID: `evidence-ledger-for-tool-calling-agents-with-reversible-actions-b622ffa48125-20260522T122511041162+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/60fbf69a39be

## What looked useful

Evidence validation plus rollback made reversible actions fail closed: primary-run protected corruption dropped from 0.4168 to 0.0, stale overwrites from 0.6370 to 0.0, and mean net side effects from 0.9958 to 0.0. Immediate task success also dropped from 0.1713 to 0.0472 because rejected actions were not repaired.

## Boundaries and scale limits

The run used synthetic injected faults rather than live LLM tool traces, represented real tools as key/value state transitions, did not test crash-persistent undo logs, and did not include ledger-aware replanning after rejection.

## Claim scope

In a deterministic synthetic key/value tool-action benchmark, an evidence ledger with pre-execution evidence validation and inverse-action rollback prevented stale overwrites, protected-key corruption, and net side effects across 10,000 primary episodes plus a five-point fault-rate sweep.

## Why it stopped

No-paper useful signal: the mechanism is supported in a synthetic benchmark, but publication-grade evidence would require live agent traces and a replanning policy to resolve the observed success regression.

## Recommended next action

Run a bounded deepen test with ledger-aware repair/replanning on recorded or live LLM tool-call traces, and require near-zero corruption while recovering task success versus the naive runner.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Ledger-aware replanning after rejected reversible tool actions
- Success threshold: Ledger-with-replanning keeps protected corruption and stale overwrites at or below 1% while achieving at least 90% of naive task success on the same trace set.
- Stop condition: Stop if replanning either raises persistent corruption above 1% or fails to recover at least half of the success-rate gap between naive and ledger-without-replanning.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-tool-calling-agents-with-reversible-actions-b622ffa48125`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
