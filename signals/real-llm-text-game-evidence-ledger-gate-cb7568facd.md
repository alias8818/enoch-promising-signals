# Real LLM Text-Game Evidence Ledger Gate

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-llm-text-game-evidence-ledger-gate-cb7568facd`
Run ID: `real-llm-text-game-evidence-ledger-gate-cb7568facd-20260629T181142069652+0000`

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

- Parent run decision: Evidence Ledger for Agent Reliability in Text Games: enoch://control-plane/projects/evidence-ledger-for-agent-reliability-in-text-games-57d0a64f7340/runs/evidence-ledger-for-agent-reliability-in-text-games-57d0a64f7340-20260629T172748207033+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fa338371aaca

## What looked useful

The ledger gate had 0 false accepts and 0 false rejects on 8 labeled synthetic claims, while a naive accept-all baseline falsely accepted 4 of 8 claims.

## Boundaries and scale limits

Synthetic hand-built text-game ledgers only; no real LLM traces, no stochastic sampling, no human adjudication, and no large benchmark corpus.

## Claim scope

A standard-library evidence-ledger gate rejected unsupported, drifted, missing-reference, and stale-reference claims in 5 deterministic text-game ledger episodes with 8 labeled claims.

## Why it stopped

Closed as a no-paper useful signal because this run directly tested the gate mechanism but only proxied LLM errors; no local LLM runtime was available for direct real-model validation.

## Recommended next action

Run the same ledger gate on real LLM text-game outputs with at least 50 episodes and 200 labeled claims before considering a bounded paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real LLM Text-Game Ledger Gate Validation
- Success threshold: False accept rate at least 50% lower than baseline and false reject rate below 10% on 200 or more labeled real-LLM claims.
- Stop condition: Stop if no real LLM runtime/API is available, if fewer than 200 labeled claims can be produced, or if the gate fails to reduce false accepts by 50%.

## Evidence references

- Artifact root: `<local-path>/projects/real-llm-text-game-evidence-ledger-gate-cb7568facd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
