# Spot-Check Volunteer Training: Deterministic Replay Audit

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `spot-check-volunteer-training-deterministic-replay-audit-0f8cb1b3f121`
Run ID: `spot-check-volunteer-training-deterministic-replay-audit-0f8cb1b3f121-20260613T124149387972+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f83ebaa4f43d

## What looked useful

The run produced a reproducible deterministic replay harness and showed that lexical transcript search can select plausible but wrong volunteer-training distractors, while tag/priority/doctrine-aware replay avoided those failures on this controlled corpus.

## Boundaries and scale limits

Synthetic small corpus only; no real volunteer data, no LLM-backed agent, no persistent memory store, no cross-host replay, and no human adjudication.

## Claim scope

On an 8-task synthetic volunteer-training replay spot-check with same-word distractors, a deterministic layered doctrine/tag/priority retrieval strategy produced stable replay hashes and higher exact-match accuracy than no-memory, transcript-search, and flat-retrieval baselines.

## Why it stopped

Synthetic proxy evidence is useful for future audit design but is not publication-grade direct validation.

## Recommended next action

Stop this run as a no-paper useful signal; next, apply the harness to a larger expert-authored or real volunteer-training replay set with an LLM-backed agent and persistent memory store.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Volunteer Training Replay Audit on Expert-Authored Traces
- Success threshold: Zero nondeterministic digest cases across three process restarts and at least a 15 percentage point exact-match improvement over the best non-layered baseline on 50 or more tasks.
- Stop condition: Stop if layered retrieval is nondeterministic across restarts or fails to beat the best non-layered baseline by 5 percentage points after the first 50 adjudicated tasks.

## Evidence references

- Artifact root: `<local-path>/projects/spot-check-volunteer-training-deterministic-replay-audit-0f8cb1b3f121`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
