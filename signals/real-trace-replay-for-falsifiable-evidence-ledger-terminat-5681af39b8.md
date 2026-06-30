# Real Trace Replay for Falsifiable Evidence Ledger Termination

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-trace-replay-for-falsifiable-evidence-ledger-terminat-5681af39b8`
Run ID: `real-trace-replay-for-falsifiable-evidence-ledger-terminat-5681af39b8-20260602T220011486212+0000`

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

- Parent run decision: Falsifiable Evidence Ledger for Agent Termination: enoch://control-plane/projects/falsifiable-evidence-ledger-for-agent-termination-bc59540c2c05/runs/falsifiable-evidence-ledger-for-agent-termination-bc59540c2c05-20260602T172039532720+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/77930d8ad634

## What looked useful

The replay ledger classified the real trace as bounded_nonterminal with 1 open turn, 0 pending items, and 0 malformed events; duplicate replay preserved classification; a missing-completion control remained nonterminal with one explicit pending item.

## Boundaries and scale limits

Validated on one real project trace with 45 events plus duplicate and missing-completion controls. The available real trace has one open turn and no turn.completed event, so the run does not validate fully terminal behavior on completed real multi-turn traces.

## Claim scope

A finite real Codex JSONL trace from this Enoch project can be replayed into a deterministic evidence ledger that halts computationally and returns a falsifiable terminal or bounded-nonterminal state with explicit pending/open evidence.

## Why it stopped

Stopped after Tier 1 controlled direct replay because the mechanism produced useful bounded evidence, but the only available real trace was open at the turn level and cannot support a paper-ready terminality claim.

## Recommended next action

Run a bounded deepen follow-up on a small corpus of completed real Enoch/Codex traces and require zero false-terminal classifications under duplicate and missing-completion perturbations.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Completed Real-Trace Corpus Replay for Evidence Ledger Terminality
- Success threshold: 100% of completed original traces classify terminal=true with 0 malformed events; 100% of duplicate controls preserve original classification; 100% of missing-completion/truncation controls classify bounded_nonterminal; false-terminal rate is 0/20 or better.
- Stop condition: Stop if any completed original trace fails to reach terminal=true for a schema reason not handled by the ledger, or if any missing-completion/truncation control is classified terminal.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-replay-for-falsifiable-evidence-ledger-terminat-5681af39b8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
