# Medium realistic replay for layered home-task memory

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `medium-realistic-replay-for-layered-home-task-memory-dc639fff99`
Run ID: `medium-realistic-replay-for-layered-home-task-memory-dc639fff99-20260629T212413216073+0000`

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

- Parent run decision: Layered Agent Memory vs Flat Retrieval on Repeated Home Tasks: enoch://control-plane/projects/layered-agent-memory-vs-flat-retrieval-on-repeated-home-tasks-8203ddc814d8/runs/layered-agent-memory-vs-flat-retrieval-on-repeated-home-tasks-8203ddc814d8-20260629T204332141088+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/64cd9e1e824e

## What looked useful

Layered doctrine memory reached 96/96 accuracy in the main run and 1.0 accuracy in all five replicate seeds. Flat retrieval reached 64/96 in the main run and averaged 0.508 across replicates, with 214 stale-conflict matches across 480 replicate tasks.

## Boundaries and scale limits

96-task main run plus five 96-task replicate seeds; synthetic generated corpus; no human-authored traces, learned retrieval, natural-language extraction, adversarial paraphrase, or long-horizon live deployment.

## Claim scope

In a deterministic synthetic medium replay benchmark for repeated home-task memory, layered category/slot upsert memory outperformed no-memory, transcript-window search, and flat retrieval baselines by avoiding stale-conflict errors.

## Why it stopped

Synthetic benchmark supports the mechanism but is not publication-grade direct evidence for realistic deployed home-task memory.

## Recommended next action

Stop this run as no-paper useful signal; next concrete action is a bounded human-authored replay follow-up with independent extraction and a stronger flat/vector retrieval baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Human-authored replay validation for layered home-task memory
- Success threshold: Layered memory improves exact-answer accuracy by at least 10 percentage points over the best flat retrieval baseline and reduces stale-conflict errors by at least 50% with no more than 5% wrong-layer regressions.
- Stop condition: Stop if layered memory fails to beat the best flat/vector retrieval baseline by 5 percentage points or if wrong-layer regressions exceed the stale-conflict reduction.

## Evidence references

- Artifact root: `<local-path>/projects/medium-realistic-replay-for-layered-home-task-memory-dc639fff99`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
