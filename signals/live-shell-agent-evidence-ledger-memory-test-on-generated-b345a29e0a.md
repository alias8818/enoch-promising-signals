# Live shell-agent evidence-ledger memory test on generated diagnostic traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `live-shell-agent-evidence-ledger-memory-test-on-generated-b345a29e0a`
Run ID: `live-shell-agent-evidence-ledger-memory-test-on-generated-b345a29e0a-20260610T111430179620+0000`

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

- Parent run decision: Evidence-ledger vs flat-scratchpad shell agent: enoch://control-plane/projects/evidence-ledger-vs-flat-scratchpad-shell-agent-7a7f2f312eda/runs/evidence-ledger-vs-flat-scratchpad-shell-agent-7a7f2f312eda-20260610T060351799288+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/25cc1bb5a3c2

## What looked useful

The run supports the narrow memory mechanism that durable evidence ledgers can prevent early diagnostic facts from being lost under transcript-window eviction. A no-distractor control showed the rolling baseline succeeds when evidence remains in context.

## Boundaries and scale limits

Synthetic generated traces only; structured EVIDENCE markers; deterministic parsing agents; no live LLM shell-agent, real incident logs, noisy extraction, adversarial evidence, or remediation execution.

## Claim scope

In a deterministic Tier 1 generated shell-diagnostic trace harness, an explicit evidence ledger preserved early structured diagnostic facts across context eviction and achieved 100% exact root-cause+fix accuracy, while a four-observation rolling-window baseline achieved 0% when 18 distractors displaced the evidence.

## Why it stopped

Tier 1 generated-trace mechanism test is complete and positive within scope, but it is synthetic and not paper-positive direct evidence for real shell agents.

## Recommended next action

Run a bounded deepen follow-up with a live LLM shell-agent loop on noisy unmarked generated traces, comparing ledger extraction quality and final diagnostic accuracy against matched transcript-only baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live LLM evidence-ledger diagnostic memory test on noisy unmarked shell traces
- Success threshold: Ledger agent improves exact root-cause+fix accuracy by at least 20 percentage points over transcript-only baseline across at least 80 noisy cases, with evidence extraction precision and recall both at least 0.80.
- Stop condition: Stop if ledger accuracy is within 5 percentage points of transcript-only baseline or evidence extraction precision or recall falls below 0.60 on the first 40 cases.

## Evidence references

- Artifact root: `<local-path>/projects/live-shell-agent-evidence-ledger-memory-test-on-generated-b345a29e0a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
