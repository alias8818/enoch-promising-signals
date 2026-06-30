# Memory Architecture for Volunteer Training Coordinator Agent

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `memory-architecture-for-volunteer-training-coordinator-agent-ad9922d2a455`
Run ID: `memory-architecture-for-volunteer-training-coordinator-agent-ad9922d2a455-20260620T213032781860+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/48917399b75b

## What looked useful

Layered doctrine memory reached 10/10 accuracy, flat retrieval 8/10, transcript search 7/10, and no memory 0/10. The observed advantage came from policy-source precedence and entity-scoped state under noisy late notes and same-name collisions.

## Boundaries and scale limits

Synthetic facts only; no real volunteer data; no LLM generation layer; no production persistence, privacy, or long-horizon degradation test; 10 cases is too small for publication-grade claims.

## Claim scope

On a 10-case synthetic deterministic volunteer training coordinator replay suite, layered doctrine memory with entity compartments and source-aware policy precedence improved exact fact retrieval over no-memory, transcript-search, and flat-retrieval baselines.

## Why it stopped

No-paper useful signal: this was a small synthetic proxy evaluation, not direct/full validation of a deployed volunteer training coordinator agent.

## Recommended next action

Run a medium sanitized-transcript replay with an LLM answer layer and the same baseline strategies before considering a bounded paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium realistic replay for layered volunteer coordinator memory
- Success threshold: Layered memory improves exact/grounded answer accuracy by at least 30% relative error reduction over flat retrieval and has no policy-safety regressions on the medium replay.
- Stop condition: Stop if layered memory fails to beat flat retrieval by at least 10% relative error reduction or introduces any high-severity policy-source regression.

## Evidence references

- Artifact root: `<local-path>/projects/memory-architecture-for-volunteer-training-coordinator-agent-ad9922d2a455`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
