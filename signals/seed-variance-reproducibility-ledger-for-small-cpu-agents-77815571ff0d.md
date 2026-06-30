# Seed-Variance Reproducibility Ledger for Small CPU Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `seed-variance-reproducibility-ledger-for-small-cpu-agents-77815571ff0d`
Run ID: `seed-variance-reproducibility-ledger-for-small-cpu-agents-77815571ff0d-20260613T195831495361+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9bc227371e8f

## What looked useful

Accuracy varied by seed from 0.8333 to 1.0000 while complete ledgers replayed 40/40 trajectories exactly; incomplete ledgers omitting seed replayed 0/40.

## Boundaries and scale limits

Synthetic tasks only; no real LLM, hosted model API, external tools, nondeterministic kernels, cross-host replay, or long-horizon autonomous workflow was tested.

## Claim scope

In a 12-task synthetic deterministic CPU-agent harness over 40 seeds, a compact ledger containing seed, config, code hash, runtime metadata, RNG scheme, and decision trace made seed-variance outcomes exactly replayable and auditable.

## Why it stopped

Closed as no-paper useful signal because the evidence is a local synthetic/proxy validation rather than direct evidence on real LLM agents or nondeterministic serving stacks.

## Recommended next action

Run a bounded deepen follow-up against a small local LLM or real agent harness and require exact replay or localized mismatch diagnostics across at least two runtimes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay Ledger on a Small Local LLM Agent Harness
- Success threshold: At least 95% exact replay on deterministic local settings, or 100% first-mismatch localization when exact replay fails due to documented nondeterminism.
- Stop condition: Stop if exact replay falls below 80% and mismatch localization cannot identify a stable missing field or nondeterministic boundary.

## Evidence references

- Artifact root: `<local-path>/projects/seed-variance-reproducibility-ledger-for-small-cpu-agents-77815571ff0d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
