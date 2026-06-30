# Evidence-ledger auditability on replayed tool-agent traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-auditability-on-replayed-tool-agent-traces-9cd0d6bf0c`
Run ID: `evidence-ledger-auditability-on-replayed-tool-agent-traces-9cd0d6bf0c-20260613T000631606074+0000`

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

- Parent run decision: Evidence-Ledger Auditability for Multi-Step Agent Tasks: enoch://control-plane/projects/evidence-ledger-auditability-for-multi-step-agent-tasks-d49ff8030a67/runs/evidence-ledger-auditability-for-multi-step-agent-tasks-d49ff8030a67-20260612T233921925346+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ce43259ae602

## What looked useful

Strict evidence-ledger verification achieved 10/10 accuracy with 0 false accepts and 0 false rejects; a naive reference-only baseline achieved 6/10 accuracy and falsely accepted 4 of 5 invalid claims.

## Boundaries and scale limits

Synthetic hand-authored fixture only; no natural LLM traces, no large corpus, no independent human labeling, no adversarial paraphrase testing, and no multi-hop semantic entailment beyond explicit JSON predicates.

## Claim scope

In a controlled Tier 1 replay fixture with 8 tool evidence records and 10 planted claims, a strict evidence-ledger verifier using evidence existence, predicate, freshness, and observation-hash checks rejected all planted unsupported claims and accepted all planted supported claims.

## Why it stopped

The Tier 1 controlled direct test supports the mechanism but remains synthetic and small, so it is no-paper useful signal rather than paper-positive evidence.

## Recommended next action

Run a bounded deepen follow-up on real replayed tool-agent traces with independent claim/evidence labels and the same strict-vs-naive metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger verifier on real replayed tool-agent traces
- Success threshold: Strict verifier false-accept rate at least 50% lower than citation-presence baseline and strict false-reject rate no greater than 10% on independently labeled real trace claims.
- Stop condition: Stop if independent labels cannot be produced, if strict false accepts are not reduced by at least 50%, or if strict false rejects exceed 10%.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-auditability-on-replayed-tool-agent-traces-9cd0d6bf0c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
