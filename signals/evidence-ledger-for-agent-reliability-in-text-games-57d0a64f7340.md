# Evidence Ledger for Agent Reliability in Text Games

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-for-agent-reliability-in-text-games-57d0a64f7340`
Run ID: `evidence-ledger-for-agent-reliability-in-text-games-57d0a64f7340-20260629T172748207033+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fa338371aaca

## What looked useful

Explicit evidence references can prevent acceptance of incorrect text-game state claims when the game engine emits reliable evidence, but strict gating needs a missing-evidence recovery policy to avoid rejecting correct unsupported claims.

## Boundaries and scale limits

Synthetic-only local probe; no real LLM agents, no natural-language parser, one toy game, one seed, 240 episodes, and no benchmark-scale text-game diversity.

## Claim scope

In a deterministic synthetic five-step text-game with engine-backed evidence and simulated unreliable agent self-reports, an evidence-ledger gate reduced false acceptance of incorrect claims from 521/3600 to 0/3600 while introducing 89/3600 false rejects for correct claims with missing evidence references.

## Why it stopped

Closed as no-paper useful signal because the current evidence is a controlled synthetic proxy, not direct validation on real LLM text-game agents.

## Recommended next action

Run a bounded deepen study on a real text-game benchmark with live LLM agents, claim extraction, and manual audit of parser and ledger decisions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real LLM Text-Game Evidence Ledger Gate
- Success threshold: Ledger false-accept rate at least 50% lower than baseline and ledger false-reject rate below 10% across repeated real-agent runs.
- Stop condition: Stop if claim extraction cannot reach at least 90% auditable predicate coverage or if ledger gating fails to reduce false accepts in the first repeated-seed batch.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-agent-reliability-in-text-games-57d0a64f7340`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
