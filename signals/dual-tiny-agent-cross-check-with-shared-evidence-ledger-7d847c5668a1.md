# Dual tiny agent cross-check with shared evidence ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `dual-tiny-agent-cross-check-with-shared-evidence-ledger-7d847c5668a1`
Run ID: `dual-tiny-agent-cross-check-with-shared-evidence-ledger-7d847c5668a1-20260607T121819331413+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ed5c7ff6fa8c

## What looked useful

Across 160,000 main-run synthetic tasks, the shared ledger reduced false accepts by 0.479812 absolute versus single-agent and 0.080731 absolute versus answer-only agreement, while improving utility by 1.571375 and 0.496806 respectively. A 9-variant robustness sweep preserved the mechanism signal.

## Boundaries and scale limits

Synthetic tasks only; no neural LLM agents, no real corpus, no real retrieval system, no token or latency budget comparison, and no human-labeled evidence beyond generated ground truth.

## Claim scope

In a synthetic conflicting-evidence fact-verification benchmark with two deterministic weak extractive agents, a shared cited-evidence ledger reduced false accepted answers and improved utility versus both a single weak agent and answer-only agreement.

## Why it stopped

No-paper closure: the evidence is a synthetic mechanism probe, not direct real-agent or publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up on a public fact-verification subset with two actual small local LLM/RAG agents and the same single-agent, answer-only, and shared-ledger baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real small-agent fact-check benchmark for shared evidence ledger
- Success threshold: At least 20% relative false-accept reduction versus answer-only agreement, no more than 15% relative coverage loss, and positive utility improvement under a predefined wrong-answer penalty.
- Stop condition: Stop if the shared ledger fails to beat answer-only agreement on false accepts in two independent dataset slices or requires substantially more token/latency budget than the baselines.

## Evidence references

- Artifact root: `<local-path>/projects/dual-tiny-agent-cross-check-with-shared-evidence-ledger-7d847c5668a1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
