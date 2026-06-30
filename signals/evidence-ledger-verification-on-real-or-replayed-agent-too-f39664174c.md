# Evidence ledger verification on real or replayed agent-tool traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-verification-on-real-or-replayed-agent-too-f39664174c`
Run ID: `evidence-ledger-verification-on-real-or-replayed-agent-too-f39664174c-20260607T084909283285+0000`

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

- Parent run decision: Evidence ledger infrastructure for agent reliability: enoch://control-plane/projects/evidence-ledger-infrastructure-for-agent-reliability-250ad63a40d2/runs/evidence-ledger-infrastructure-for-agent-reliability-250ad63a40d2-20260607T052838375790+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/2b828dab0d6c

## What looked useful

Mechanism support: anchored ledger verification detected 4/4 controlled tamper cases with 0 false accepts on clean replay, but an adversarially reissued tampered trace passed when both ledger and manifest were regenerated.

## Boundaries and scale limits

Single small trace, one event schema family, no external root anchor or signature, no heterogeneous corpus, and no schema-aware benign-transformation policy.

## Claim scope

On one real Enoch/Codex worker JSONL trace, a canonical SHA-256 event hash chain with an anchored manifest accepted clean replay and rejected content mutation, event deletion, adjacent reordering, and duplication against the original root.

## Why it stopped

No-paper useful signal: the Tier 1 direct test supports anchored single-trace tamper detection, but the reissue control shows that provenance-grade verification requires an external root anchor or signature.

## Recommended next action

Run a bounded deepen test with signed or transparency-log anchored roots on at least 10 heterogeneous real/replayed traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchored evidence ledger verification across heterogeneous agent-tool traces
- Success threshold: Accept 100% of clean replays, reject 100% of controlled tamper and regenerated-manifest cases, and document any benign-transformation false positives with reproducible artifacts.
- Stop condition: Stop if any regenerated tampered manifest verifies under the claimed anchor model, or if clean replay false rejects exceed one trace without a schema-policy explanation.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-verification-on-real-or-replayed-agent-too-f39664174c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
