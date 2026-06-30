# Real CPU-agent citation support test for evidence-ledger constraints

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-cpu-agent-citation-support-test-for-evidence-ledger-c-1ea4c738a6`
Run ID: `real-cpu-agent-citation-support-test-for-evidence-ledger-c-1ea4c738a6-20260608T151358728431+0000`

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

- Parent run decision: Evidence-ledger constraint for small CPU agent loops: enoch://control-plane/projects/evidence-ledger-constraint-for-small-cpu-agent-loops-e81200c07a6a/runs/evidence-ledger-constraint-for-small-cpu-agent-loops-e81200c07a6a-20260608T082610296465+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/97e96394eeb2

## What looked useful

The ledger constraint reduced unsupported claims from 12 to 0 and invalid citations from 12 to 0 while improving exact fact match from 0.8333 to 1.0000 in the controlled harness.

## Boundaries and scale limits

Synthetic small corpus; deterministic fact-key answers; no real LLM runtime or free-form generation; no large retrieval corpus; no human adjudication.

## Claim scope

In a deterministic CPU-only 12-document, 12-question citation-support harness, an evidence-ledger-constrained agent eliminated unsupported emitted claims and invalid citations compared with an unconstrained cited-draft agent.

## Why it stopped

Tier 1 controlled mechanism support was obtained, but this is no-paper evidence because it used a deterministic harness rather than a real LLM or production agent.

## Recommended next action

Run a bounded deepen follow-up using a real CPU-runnable LLM draft generator on the same evidence-ledger harness before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU LLM Drafts With Evidence-Ledger Citation Gate
- Success threshold: Ledger-gated outputs have at least 50% fewer unsupported emitted claims than ungated drafts and exact supported fact accuracy is no worse by more than 5 percentage points.
- Stop condition: Stop as negative if the ledger gate fails to reduce unsupported emitted claims by 25% or if it causes more than a 10 percentage point drop in exact supported fact accuracy.

## Evidence references

- Artifact root: `<local-path>/projects/real-cpu-agent-citation-support-test-for-evidence-ledger-c-1ea4c738a6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
