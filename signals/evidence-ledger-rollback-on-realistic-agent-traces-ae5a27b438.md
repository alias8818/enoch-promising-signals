# Evidence-ledger rollback on realistic agent traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-rollback-on-realistic-agent-traces-ae5a27b438`
Run ID: `evidence-ledger-rollback-on-realistic-agent-traces-ae5a27b438-20260527T171604050258+0000`

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

- Parent run decision: Evidence-Ledger Agent Rollback on CPU: enoch://control-plane/projects/evidence-ledger-agent-rollback-on-cpu-3e406a111087/runs/evidence-ledger-agent-rollback-on-cpu-3e406a111087-20260527T135143911097+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c397c3a251f1

## What looked useful

Rollback works cleanly when final claims have dependency edges to cited evidence, reaching 10/10 rescues with 0/10 false invalidations on realistic recorded traces. The prior no-edge boundary still applies: rollback alone cannot rescue unsupported answers that never cite evidence.

## Boundaries and scale limits

Small Tier 1 replay over recorded traces; invalidation events were controlled fault injections, not naturally occurring live failures. No live LLM regeneration, long-horizon LangGraph state, concurrency, human labels, adversarial traces, or no-evidence final-answer cases were tested.

## Claim scope

On five recorded realistic local-agent ledger traces with explicit claim-to-evidence dependencies, dependency-aware rollback invalidated all controlled active unsupported finals caused by cited evidence being audited invalid or missing, while preserving all supported finals including decoy-invalidation controls.

## Why it stopped

Tier 1 controlled direct replay passed the dependency-linked threshold but remains no-paper evidence because the corpus is small and faults were injected during replay rather than observed in a live agent run.

## Recommended next action

Run a bounded live LangGraph-style local-agent follow-up with mandatory evidence citations, injected realistic tool failures/corrections, and at least 50 tasks to measure rollback rescue and false invalidation rates under actual agent execution.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live local-agent rollback with mandatory evidence citations
- Success threshold: Rollback rescues at least 90% of active unsupported dependency-linked finals and causes 0% false invalidations of supported active finals; final-gate control should be reported separately.
- Stop condition: Stop as negative if rescue is below 90%, if any supported final is falsely invalidated, or if more than 20% of unsupported finals have no evidence dependency edges despite mandatory citation instrumentation.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-rollback-on-realistic-agent-traces-ae5a27b438`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
