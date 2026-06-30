# Human-authored replay validation for layered home-task memory

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `human-authored-replay-validation-for-layered-home-task-mem-9deab5203b`
Run ID: `human-authored-replay-validation-for-layered-home-task-mem-9deab5203b-20260629T214134815942+0000`

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

- Parent run decision: Medium realistic replay for layered home-task memory: enoch://control-plane/projects/medium-realistic-replay-for-layered-home-task-memory-dc639fff99/runs/medium-realistic-replay-for-layered-home-task-memory-dc639fff99-20260629T212413216073+0000
- Parent run decision: Layered Agent Memory vs Flat Retrieval on Repeated Home Tasks: enoch://control-plane/projects/layered-agent-memory-vs-flat-retrieval-on-repeated-home-tasks-8203ddc814d8/runs/layered-agent-memory-vs-flat-retrieval-on-repeated-home-tasks-8203ddc814d8-20260629T204332141088+0000

## What looked useful

Canonical current-state conflict resolution plus layer-balanced retrieval eliminated stale household instructions in this bounded replay, while transcript and flat retrieval frequently recalled superseded routines.

## Boundaries and scale limits

Small authored suite; no LLM answer generation; no noisy transcript-to-memory extraction; oracle-structured canonical facts and supersession links; no held-out corpus or adversarial paraphrase stress.

## Claim scope

On a 10-task human-authored deterministic home-task replay benchmark with explicit canonical supersession links, layered memory with current-fact conflict resolution achieved 100% exact action-readiness at top_k=4, compared with 50% for flat retrieval and 30% for transcript search.

## Why it stopped

No-paper useful signal: the mechanism is supported locally, but the evidence is too small and oracle-structured for publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up with 50 held-out human-authored replay tasks, noisy transcript-to-memory extraction, a conflict-aware non-layered baseline, and LLM answer grading.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out noisy replay validation for layered home-task memory
- Success threshold: Layered memory improves exact action-readiness by >=15 percentage points over the best conflict-aware non-layered baseline with 95% bootstrap CI lower bound above 0.
- Stop condition: Stop as non-viable if layered memory's exact action-readiness gain is below 5 percentage points or if extraction errors erase the stale-fact suppression advantage.

## Evidence references

- Artifact root: `<local-path>/projects/human-authored-replay-validation-for-layered-home-task-mem-9deab5203b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
