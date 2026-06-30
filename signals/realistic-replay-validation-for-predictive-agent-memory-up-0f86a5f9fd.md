# Realistic replay validation for predictive agent memory updates

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `realistic-replay-validation-for-predictive-agent-memory-up-0f86a5f9fd`
Run ID: `realistic-replay-validation-for-predictive-agent-memory-up-0f86a5f9fd-20260614T065032314542+0000`

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

- Parent run decision: Agent Memory Architecture: Retrieval vs Semantic Compression vs Predictive Updates: enoch://control-plane/projects/agent-memory-architecture-retrieval-vs-semantic-compression-vs-predictive-updates-fc364250b1f9/runs/agent-memory-architecture-retrieval-vs-semantic-compression-vs-predictive-updates-fc364250b1f9-20260614T055232785707+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/498077bb1909

## What looked useful

Predictive memory update reached 6/6 task success with 1.000 fact recall, 1.000 action recall, and 0.000 distractor rate. Best baseline reached 1/6 task success and leaked distractors.

## Boundaries and scale limits

Small scripted corpus; deterministic extraction policy; no LLM memory-update generation, human production traces, long-horizon persistence, or held-out transcript templates.

## Claim scope

In a six-task controlled replay harness, deterministic predictive memory updates that store canonical current facts, likely next-action affordances, and stale-cue suppression outperform no-memory, transcript-search, and flat-retrieval baselines on direct replay-task success.

## Why it stopped

Tier 1 controlled direct test passed, but evidence is mechanism support only and not publication readiness.

## Recommended next action

Run a bounded deepen follow-up with model-generated memory updates on held-out replay templates and the same distractor-suppression success threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out model-generated replay validation for predictive memory updates
- Success threshold: LLM predictive memory update task success >= 0.80, absolute gain over best baseline >= 0.30, and mean distractor recall <= 0.05 on held-out tasks.
- Stop condition: Stop as no-paper negative if predictive memory task success is below 0.65 or distractor recall exceeds 0.15 after the held-out run and failure inspection.

## Evidence references

- Artifact root: `<local-path>/projects/realistic-replay-validation-for-predictive-agent-memory-up-0f86a5f9fd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
