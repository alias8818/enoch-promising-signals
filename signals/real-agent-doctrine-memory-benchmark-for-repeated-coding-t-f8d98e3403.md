# Real-agent doctrine memory benchmark for repeated coding tasks

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-agent-doctrine-memory-benchmark-for-repeated-coding-t-f8d98e3403`
Run ID: `real-agent-doctrine-memory-benchmark-for-repeated-coding-t-f8d98e3403-20260620T083823680991+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Operator-Doctrine Memory for Repeat Agents: enoch://control-plane/projects/operator-doctrine-memory-for-repeat-agents-2916349578ac/runs/operator-doctrine-memory-for-repeat-agents-2916349578ac-20260620T082302653028+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a49c4c28f6c4

## What looked useful

All six agent runs passed visible tests, but hidden passes were 0/3 for the doctrine-memory condition versus 1/3 for no-memory; the doctrine file influenced edits but did not reliably transfer hidden invariants.

## Boundaries and scale limits

One benchmark run, three generated Python tasks, one Codex CLI/model configuration, no repeated seeds, no production repositories, no human-authored doctrine, and no long-lived agent session memory.

## Claim scope

In a Tier 1 three-task synthetic Python benchmark using nested Codex exec agents, a simple persistent doctrine memory file did not improve hidden repeated-invariant pass rate over cold no-memory prompts.

## Why it stopped

No-paper useful signal: this small direct benchmark early-falsifies the simple doctrine-file mechanism as implemented here, but it is not a full validation of doctrine memory in real repositories.

## Recommended next action

Run a bounded deepen follow-up with 10-20 randomized repeated coding tasks and pre-registered doctrine updates before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Randomized repeated-task doctrine-memory benchmark
- Success threshold: Memory condition hidden pass rate exceeds no-memory by at least 20 percentage points with equal or better visible pass rate and no more than 25 percent higher median agent time.
- Stop condition: Stop if hidden pass delta is less than or equal to zero after 10 tasks or if memory reduces visible pass rate by more than one task.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-doctrine-memory-benchmark-for-repeated-coding-t-f8d98e3403`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
