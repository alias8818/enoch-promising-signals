# Real-Agent Evidence-Ledger Memory on Repeated Local Repository Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-agent-evidence-ledger-memory-on-repeated-local-reposi-339b810c49`
Run ID: `real-agent-evidence-ledger-memory-on-repeated-local-reposi-339b810c49-20260613T051501992980+0000`

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

- Parent run decision: Evidence-Ledger Agent Memory on Repeated Local Tasks: enoch://control-plane/projects/evidence-ledger-agent-memory-on-repeated-local-tasks-52f9818bcc74/runs/evidence-ledger-agent-memory-on-repeated-local-tasks-52f9818bcc74-20260613T045442025019+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3b47ae733d08

## What looked useful

Final Codex sample: stateless n=4 accuracy 1.00, mean elapsed 16.321s, mean command events 5.0; ledger n=4 accuracy 1.00, mean elapsed 14.633s, mean command events 3.0. Ledger was faster on 3 of 4 tasks and preserved correctness on all tasks.

## Boundaries and scale limits

Small generated repositories, four repeated lookup tasks, prompt-controlled ledger use, and no edit-and-test tasks. The ledger was deterministic ground truth rather than naturally formed autonomous memory, and the run did not test stale, incomplete, or conflicting ledger entries.

## Claim scope

In a Tier 1 controlled direct test on two generated local Python repositories and four repeated lookup tasks, an explicit evidence ledger preserved exact-answer accuracy for a nested Codex local-file agent while reducing mean elapsed time and coarse command events compared with stateless repository inspection.

## Why it stopped

Tier 1 controlled direct test met its scoped useful-signal threshold, but the evidence is small, generated, prompt-controlled, and not publication-grade.

## Recommended next action

Run a bounded deepen follow-up on real local repositories where the ledger is produced by a prior autonomous pass and includes some stale or missing facts, then measure edit/test success plus tool-use savings.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Autonomous Evidence-Ledger Formation and Trust on Real Local Repository Tasks
- Success threshold: Ledger condition matches or exceeds stateless success/test-pass rate while reducing mean tool calls or wall-clock by at least 15%, and stale-ledger cases do not produce more wrong final answers than stateless.
- Stop condition: Stop if autonomous ledger formation has below 80% factual precision on initial-pass facts or if stale-ledger cases increase wrong final answers relative to stateless on the bounded sample.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-evidence-ledger-memory-on-repeated-local-reposi-339b810c49`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
