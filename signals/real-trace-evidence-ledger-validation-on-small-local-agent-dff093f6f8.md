# Real-trace evidence-ledger validation on small local agent tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-trace-evidence-ledger-validation-on-small-local-agent-dff093f6f8`
Run ID: `real-trace-evidence-ledger-validation-on-small-local-agent-dff093f6f8-20260614T024930460999+0000`

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

- Parent run decision: Evidence-Ledger Agent Reliability on GB10: enoch://control-plane/projects/evidence-ledger-agent-reliability-on-gb10-77cf92bec001/runs/evidence-ledger-agent-reliability-on-gb10-77cf92bec001-20260614T023551977993+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/34cc0b7659b0

## What looked useful

The mechanism worked on direct small local traces: 14 claims, TP=6, TN=8, FP=0, FN=0, precision=1.0, recall=1.0, valid six-entry hash chain, and tamper control detected an altered trace hash.

## Boundaries and scale limits

Only small deterministic local tasks were tested. The run did not validate natural-language claim extraction, full LLM/Codex agent trajectories, concurrent or networked evidence, long repository tasks, or malicious trace producers.

## Claim scope

In a controlled Tier 1 local test with six subprocess-backed file/command tasks, a hash-chained evidence ledger over exit codes, task-bound paths, and file SHA-256 hashes accepted all true structured claims and rejected all deliberately false structured claims.

## Why it stopped

Tier 1 controlled direct validation produced a useful mechanism signal, but the evidence is not publication-grade because it uses small deterministic tasks and structured claims.

## Recommended next action

Run a bounded deepen follow-up on real small-agent or Codex traces with natural-language completion reports mapped to audited structured claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-language evidence-ledger validation on real small-agent traces
- Success threshold: On at least 20 audited real traces, false accept rate <= 5 percent, false reject rate <= 10 percent, and all detected ledger tampering controls fail closed.
- Stop condition: Stop if false accepts exceed 5 percent on audited claims, if claim extraction cannot be made reproducible, or if required real traces are unavailable.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-evidence-ledger-validation-on-small-local-agent-dff093f6f8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
