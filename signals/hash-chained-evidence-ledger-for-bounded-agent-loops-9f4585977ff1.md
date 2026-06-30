# Hash-Chained Evidence Ledger for Bounded Agent Loops

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `hash-chained-evidence-ledger-for-bounded-agent-loops-9f4585977ff1`
Run ID: `hash-chained-evidence-ledger-for-bounded-agent-loops-9f4585977ff1-20260620T231600345980+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/65f84ab55b3d

## What looked useful

The simple hash-chain ledger is operationally cheap enough for bounded agent loops and catches common trace tampering when a trusted head checkpoint is retained. The key failure mode is explicit: forged suffixes pass if verification has no trusted expected head.

## Boundaries and scale limits

Synthetic events only; no live LangGraph/Enoch integration, no concurrent writers, no crash/recovery persistence test, no external transparency service, and no evidence against adversaries who can modify both the ledger and all trusted checkpoints.

## Claim scope

In a local synthetic bounded-loop trace benchmark, canonical JSON hash-chained event records plus trusted final-head checkpoints detected and localized tested post-hoc mutation, deletion, adjacent reordering, forged-suffix, and truncation attacks while sustaining about 175k appends/second for 100k events in Python.

## Why it stopped

Synthetic local evidence supports the mechanism but is insufficient for a paper or broad production claim.

## Recommended next action

Stop this run as no-paper useful signal; next, test the same ledger on real worker/controller traces with persisted head checkpoints and crash/recovery replay.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Persisted Hash-Chain Checkpoints for Real Agent Trace Replay
- Success threshold: Detect 100 percent of injected tamper cases with persisted checkpoints and keep median end-to-end worker overhead below 5 percent versus plain trace logging.
- Stop condition: Stop if persisted checkpoints cannot survive restart/replay, if any injected tamper case is missed, or if median overhead exceeds 10 percent on representative real traces.

## Evidence references

- Artifact root: `<local-path>/projects/hash-chained-evidence-ledger-for-bounded-agent-loops-9f4585977ff1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
