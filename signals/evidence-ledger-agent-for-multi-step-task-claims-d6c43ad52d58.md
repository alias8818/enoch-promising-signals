# Evidence-ledger agent for multi-step task claims

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-for-multi-step-task-claims-d6c43ad52d58`
Run ID: `evidence-ledger-agent-for-multi-step-task-claims-d6c43ad52d58-20260628T051317747496+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fa3281111506

## What looked useful

The ledger verifier achieved 1.000 F1 and 100% tamper detection on the controlled synthetic harness, while final-state checking accepted all missing-evidence and wrong-order false claims and rejected history-sensitive true claims.

## Boundaries and scale limits

Synthetic generator only; no natural-language claim extraction, real LLM agent traces, human-labeled evidence, production storage, or stronger LLM transcript-judge baseline. CPU-only run completed in 43 seconds with 76 MB peak RSS.

## Claim scope

A structured append-only evidence ledger with event-level citations and hash-chain integrity checks distinguished supported from unsupported claims on 5,000 synthetic multi-step task traces and 40,000 structured claims.

## Why it stopped

No-paper closure: this is a synthetic structured mechanism signal, not direct publication-grade validation of an evidence-ledger agent in realistic multi-step tasks.

## Recommended next action

Run a bounded direct-evidence follow-up on real small-agent traces with human-labeled claim support and compare against transcript retrieval plus LLM judging.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger verification on real small-agent traces
- Success threshold: Ledger verifier improves unsupported-claim false-accept rate by at least 25% relative to the strongest baseline while maintaining supported-claim recall of at least 0.85 on human labels.
- Stop condition: Stop if ledger citation requirements reduce supported-claim recall below 0.75 or fail to improve false-accept rate by at least 10% against transcript-retrieval LLM judging.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-for-multi-step-task-claims-d6c43ad52d58`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
