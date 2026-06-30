# Real multi-turn commitment ledger under hard-cutover compaction

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-multi-turn-commitment-ledger-under-hard-cutover-compa-c77ef9a806`
Run ID: `real-multi-turn-commitment-ledger-under-hard-cutover-compa-c77ef9a806-20260619T040832892966+0000`

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

- Parent run decision: Live-agent commitment-window context under controlled truncation: enoch://control-plane/projects/live-agent-commitment-window-context-under-controlled-trun-4aecf6f875/runs/live-agent-commitment-window-context-under-controlled-trun-4aecf6f875-20260619T030331507954+0000
- Parent run decision: Commitment-Window Agent Context: enoch://control-plane/projects/commitment-window-agent-context-1cf940282a36/runs/commitment-window-agent-context-1cf940282a36-20260619T021652117396+0000

## What looked useful

Stable-ID commitment ledgers preserve real command commitments across simulated hard-cutover compaction; baselines that drop prefix state or stable IDs fail exact cross-cutover recovery.

## Boundaries and scale limits

The test covers structured command_execution events in local JSONL traces only. It does not validate natural-language commitments, live LangGraph compaction behavior, non-command tools, adversarial event-envelope mutation, public corpora, or high-concurrency traces beyond the sampled local corpus.

## Claim scope

On 30 real local Enoch/Codex command-execution traces with 720 fixed-seed hard-cutover samples, a structured commitment ledger keyed by stable item IDs exactly recovered command commitments that started before cutover and completed after cutover, outperforming suffix-only, FIFO-summary, and text-keyed baselines.

## Why it stopped

Medium local evidence supports the mechanism, but the scoped result is command-event reconstruction rather than publication-grade evidence for real user-facing commitment memory.

## Recommended next action

Run a bounded live hard-cutover follow-up that maps natural-language assistant commitments to tool/action outcomes with manual audit labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live hard-cutover natural-language commitment ledger validation
- Success threshold: Structured ledger improves commitment recall by at least 20 percentage points over transcript-summary baseline while keeping false active commitments at or below 5%.
- Stop condition: Stop as no-paper negative if the ledger fails to beat transcript summary by 10 percentage points on commitment recall or exceeds 10% false active commitments on audited labels.

## Evidence references

- Artifact root: `<local-path>/projects/real-multi-turn-commitment-ledger-under-hard-cutover-compa-c77ef9a806`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
