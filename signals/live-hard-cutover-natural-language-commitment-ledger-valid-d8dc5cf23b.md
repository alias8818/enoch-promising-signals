# Live hard-cutover natural-language commitment ledger validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `live-hard-cutover-natural-language-commitment-ledger-valid-d8dc5cf23b`
Run ID: `live-hard-cutover-natural-language-commitment-ledger-valid-d8dc5cf23b-20260619T045429538399+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Live-agent commitment-window context under controlled truncation: enoch://control-plane/projects/live-agent-commitment-window-context-under-controlled-trun-4aecf6f875/runs/live-agent-commitment-window-context-under-controlled-trun-4aecf6f875-20260619T030331507954+0000
- Parent run decision: Real multi-turn commitment ledger under hard-cutover compaction: enoch://control-plane/projects/real-multi-turn-commitment-ledger-under-hard-cutover-compa-c77ef9a806/runs/real-multi-turn-commitment-ledger-under-hard-cutover-compa-c77ef9a806-20260619T040832892966+0000

## What looked useful

Across three fixed seeds, the natural-language commitment ledger achieved 1.000 mean pooled cross-cutover recall, versus 0.000 for suffix-only and category-summary baselines and 0.904 for the recent-one ablation.

## Boundaries and scale limits

Labels are deterministic weak labels, not human-audited semantic labels; cutovers are simulated replay cutovers, not live LangGraph controller cutovers; metrics cover identity recovery, not end-to-end task or safety outcomes.

## Claim scope

On 80 real local Codex/Enoch traces per seed and 2,508 simulated hard cutovers, a deterministic natural-language commitment ledger preserved weak-labeled cross-cutover commitment identity better than suffix-only, category-summary, and recent-one baselines.

## Why it stopped

Useful scoped replay signal, but not paper-positive because the natural-language labels are weakly matched and the hard cutover is simulated rather than live.

## Recommended next action

Stop short of paper writing; run a bounded live-controller hard-cutover validation with manually audited commitment/action labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live-controller audited natural-language commitment ledger cutover test
- Success threshold: Audited cross-cutover commitment recall >= 0.95 and at least 25% relative reduction in missed commitments versus suffix-only resume on the same live task set.
- Stop condition: Stop if audited recall is below 0.90, if the ledger produces more false carried commitments than the suffix-only baseline, or if live cutover instrumentation cannot expose comparable ledger and baseline states.

## Evidence references

- Artifact root: `<local-path>/projects/live-hard-cutover-natural-language-commitment-ledger-valid-d8dc5cf23b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
