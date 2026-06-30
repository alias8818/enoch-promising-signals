# LLM Agent Evidence Ledger Gate on Hidden-Ground-Truth Tool Tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `llm-agent-evidence-ledger-gate-on-hidden-ground-truth-tool-e1cdd0415c`
Run ID: `llm-agent-evidence-ledger-gate-on-hidden-ground-truth-tool-e1cdd0415c-20260605T192658463561+0000`

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

- Parent run decision: Real Agent Evidence Ledger Integration: enoch://control-plane/projects/real-agent-evidence-ledger-integration-b56158bc4f/runs/real-agent-evidence-ledger-integration-b56158bc4f-20260605T064255162146+0000
- Parent run decision: Tool Agent Evidence Ledger: enoch://control-plane/projects/tool-agent-evidence-ledger-386cc4fd1cc5/runs/tool-agent-evidence-ledger-386cc4fd1cc5-20260605T022444266171+0000

## What looked useful

Evidence-ledger gating is effective as a guardrail/repair mechanism for cheap-search-first agents, but the medium control run shows it is not a publishable improvement over directly querying the authoritative tool for every required fact.

## Boundaries and scale limits

The benchmark uses synthetic attributes and stochastic proxy agents rather than real LLM transcripts, real external tools, or natural ambiguous evidence. A trivial lookup-all control matched full-gate accuracy with about half the mean tool calls.

## Claim scope

In a synthetic hidden-ground-truth tool-task benchmark with stochastic proxy agents, an evidence-ledger final-answer gate eliminated unsupported final answers and, with enough repair budget, matched lookup-all accuracy across 108000 fixed-seed trials.

## Why it stopped

Medium synthetic evidence supports the mechanism but not publication readiness because the result is proxy-agent-only and a simple lookup-all control dominates tool-call efficiency.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should use an actual local or API LLM agent with transcript-level evidence ledgers and a lookup-all prompting baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real LLM Transcript Evidence-Ledger Gate on Hidden-Ground-Truth Tool Tasks
- Success threshold: Evidence gate reduces unsupported final-answer rate by at least 80% relative to ReAct and improves or matches exact accuracy versus ledger/no-gate, while using no more than 1.5x the authoritative tool calls of the always-query baseline.
- Stop condition: Stop if transcript parsing is unreliable above 5%, unsupported-rate reduction is below 50%, or the always-query baseline dominates both accuracy and tool-call efficiency.

## Evidence references

- Artifact root: `<local-path>/projects/llm-agent-evidence-ledger-gate-on-hidden-ground-truth-tool-e1cdd0415c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
