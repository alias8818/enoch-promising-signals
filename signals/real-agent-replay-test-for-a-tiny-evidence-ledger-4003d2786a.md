# Real-Agent Replay Test for a Tiny Evidence Ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-agent-replay-test-for-a-tiny-evidence-ledger-4003d2786a`
Run ID: `real-agent-replay-test-for-a-tiny-evidence-ledger-4003d2786a-20260528T123221801857+0000`

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

- Parent run decision: Tiny Evidence Ledger for Safer Local Tool-Calling Agents: enoch://control-plane/projects/tiny-evidence-ledger-for-safer-local-tool-calling-agents-fbfa21ee327a/runs/tiny-evidence-ledger-for-safer-local-tool-calling-agents-fbfa21ee327a-20260528T120113794662+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/69f4e9668cc9

## What looked useful

Tier 1 direct replay passed: valid replay succeeded; 4/4 injected mutations were detected; mean verification time was 0.2829 ms per full replay and 0.0141 ms per event for a 20-event ledger.

## Boundaries and scale limits

Single local project transcript, 20 ledger events, 200 replay timing rounds, four injected mutation classes, no semantic command re-execution, no multi-agent traces, no external manifest anchoring, and no measurement of downstream agent correctness or human audit time.

## Claim scope

A tiny append-only hash-chain ledger built from one real local Codex transcript and three project files can replay and verify observation integrity, detecting the tested removal, reorder, command-output-hash tamper, and file-hash tamper cases with very low local overhead.

## Why it stopped

Tier 1 mechanism threshold passed, but the evidence is too small and local for publication-grade claims.

## Recommended next action

Stop this run as no-paper useful signal; next bounded deepen test should run the same ledger on several longer real agent tasks with external manifest anchoring and semantic command re-execution checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-Task Anchored Replay for Tiny Evidence Ledgers
- Success threshold: Valid replay passes for all unmodified tasks; at least 95% of injected provenance faults are detected; mean verification overhead remains below 1 ms per event; deterministic command re-execution mismatches are reported separately from hash-chain failures.
- Stop condition: Stop if any unmodified anchored task fails replay for reasons other than documented nondeterminism, if mutation detection falls below 95%, or if mean verification overhead exceeds 1 ms per event.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-replay-test-for-a-tiny-evidence-ledger-4003d2786a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
