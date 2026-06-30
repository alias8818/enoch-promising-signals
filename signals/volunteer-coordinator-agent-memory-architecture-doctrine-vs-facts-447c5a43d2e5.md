# Volunteer Coordinator Agent Memory Architecture: Doctrine vs Facts

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `volunteer-coordinator-agent-memory-architecture-doctrine-vs-facts-447c5a43d2e5`
Run ID: `volunteer-coordinator-agent-memory-architecture-doctrine-vs-facts-447c5a43d2e5-20260628T173602216223+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/68f1afa29ba0

## What looked useful

Layered doctrine memory reached 14/14 overall and 5/5 doctrine accuracy; transcript search reached 13/14 overall and 4/5 doctrine accuracy; flat retrieval reached 12/14 overall and 4/5 doctrine accuracy. The observed failures show privacy doctrine being overwritten by a contact fact and one flat-retrieval same-event fact confusion.

## Boundaries and scale limits

Small synthetic deterministic replay only; no live LLM, production data, tuned vector retrieval, human labels, or broad robustness testing.

## Claim scope

In a five-scenario, fourteen-query synthetic replay suite for volunteer coordination, explicit doctrine/fact memory layering outperformed no-memory, transcript-search, and undifferentiated flat retrieval baselines on doctrine/fact conflict questions.

## Why it stopped

Closed as no-paper useful signal because current evidence is synthetic and proxy-only, not direct deployment or publication-grade validation.

## Recommended next action

Run a bounded LLM-in-the-loop replay using the same doctrine/fact scenarios plus 50-100 noisy synthetic transcripts and a tuned vector-retrieval baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM replay validation for doctrine/fact memory separation in volunteer coordination
- Success threshold: Layered doctrine memory improves doctrine/fact conflict accuracy by >=25% relative over the best non-layered baseline while keeping event-fact accuracy within 5 percentage points of that baseline.
- Stop condition: Stop if the best non-layered baseline matches layered doctrine memory within 5 percentage points on doctrine/fact conflict accuracy or if event-fact accuracy drops by more than 5 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/volunteer-coordinator-agent-memory-architecture-doctrine-vs-facts-447c5a43d2e5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
