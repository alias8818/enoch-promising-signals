# Evidence-ledger verification on real small-agent traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-verification-on-real-small-agent-traces-c4beb603f7`
Run ID: `evidence-ledger-verification-on-real-small-agent-traces-c4beb603f7-20260628T052635154269+0000`

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

- Parent run decision: Evidence-ledger agent for multi-step task claims: enoch://control-plane/projects/evidence-ledger-agent-for-multi-step-task-claims-d6c43ad52d58/runs/evidence-ledger-agent-for-multi-step-task-claims-d6c43ad52d58-20260628T051317747496+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fa3281111506

## What looked useful

Tier 1 controlled direct test met its threshold: clean real trace passed and deletion, exit-code edit, agent-message edit, event reorder, and event-type edit were all detected by ledger or semantic verification.

## Boundaries and scale limits

Single trace, one runtime, five basic tamper classes; no multi-trace corpus, no adversarial ledger replacement test, no remote timestamping or signature anchoring, and no cross-agent schema validation.

## Claim scope

A SHA-256 append-only evidence ledger accepted one real local Codex JSONL small-agent trace snapshot with 26 events and rejected 5/5 preregistered deterministic tamper variants.

## Why it stopped

No-paper useful signal: the Tier 1 direct small test supports the mechanism but is only a single-trace controlled validation, not publication-grade evidence.

## Recommended next action

Run a deepen follow-up on at least 20 independent real agent traces from multiple task types with a preregistered tamper taxonomy and report false-positive and false-negative rates.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Corpus validation of evidence-ledger verification across independent small-agent traces
- Success threshold: Clean verification passes for 20/20 traces and tamper detection is at least 95% across all generated tamper cases with explainable errors.
- Stop condition: Stop if any clean trace is falsely rejected without a schema-specific explanation, or if tamper detection falls below 90% on the preregistered taxonomy.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-verification-on-real-small-agent-traces-c4beb603f7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
