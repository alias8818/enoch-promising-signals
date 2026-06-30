# Replay Ledger on a Small Local LLM Agent Harness

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `replay-ledger-on-a-small-local-llm-agent-harness-86d418ea88`
Run ID: `replay-ledger-on-a-small-local-llm-agent-harness-86d418ea88-20260613T205242215506+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Seed-Variance Reproducibility Ledger for Small CPU Agents: enoch://control-plane/projects/seed-variance-reproducibility-ledger-for-small-cpu-agents-77815571ff0d/runs/seed-variance-reproducibility-ledger-for-small-cpu-agents-77815571ff0d-20260613T195831495361+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9bc227371e8f

## What looked useful

Replay-ledger memory eliminated stale/decoy conflict failures in the local harness, but the transcript-search baseline remained strong enough that the predeclared +0.30 improvement threshold was not met.

## Boundaries and scale limits

This was a small controlled direct memory-policy test, not a stochastic small-LLM inference test or publication-grade validation. The corpus had 10 scored queries and one deterministic seed.

## Claim scope

In a 24-event deterministic local replay harness, layered replay-ledger memory answered 10/10 queries correctly and produced 0 conflict errors, outperforming no-memory and flat retrieval, but improving over raw transcript search by only +0.20.

## Why it stopped

Early direct Tier 1 threshold falsification: ledger accuracy was 1.00 with 0 conflicts, but improvement over transcript search was +0.20 rather than the required +0.30.

## Recommended next action

Stop as no-paper useful signal; run a bounded deepen follow-up through an actual local small LLM runtime using the same replay contract and thresholds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay ledger with an actual local small LLM runner
- Success threshold: layered replay ledger accuracy >= 0.80, conflict_errors <= 1, and accuracy delta over transcript_search >= +0.30 on the held-out small-LLM replay suite.
- Stop condition: Stop negative if the local LLM run again shows delta < +0.30 or ledger conflict_errors > 1 after prompt/harness sanity checks.

## Evidence references

- Artifact root: `<local-path>/projects/replay-ledger-on-a-small-local-llm-agent-harness-86d418ea88`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
