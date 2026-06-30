# Compressed State Memory for Repeated Agent Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `compressed-state-memory-for-repeated-agent-tasks-ec2fae3d8a4c`
Run ID: `compressed-state-memory-for-repeated-agent-tasks-ec2fae3d8a4c-20260614T025451767109+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/ab1c977a3cf5

## What looked useful

Compact state memory is a viable mechanism when repeated agent tasks depend on a small set of updateable operational facts and those facts can be reliably extracted. In this benchmark it matched ground truth while using 0.0206 of full-transcript token footprint on average; transcript search reached 0.8359 accuracy at 0.0895 footprint and recent-window memory reached 0.4539 accuracy.

## Boundaries and scale limits

Synthetic proxy only; no real LLM extraction, real task completion, human operator doctrine assessment, long-horizon production memory drift, or adversarial natural language was tested. The compressed-state condition assumes a correct extractor for active update events.

## Claim scope

In a deterministic synthetic repeated-agent workload with structured update events, compressed key/value state recovered latest operational facts with 1.0000 exact accuracy using a mean 25.23 context tokens, outperforming recent-window and transcript-search baselines under a 160-token budget.

## Why it stopped

No-paper useful signal: this was a synthetic proxy that supports the mechanism but does not validate real agent/LLM memory behavior.

## Recommended next action

Run a bounded deepen test on real unstructured repeated-agent transcripts with an extractor-backed compressed state memory and measure downstream task success against transcript retrieval.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Extractor-backed compressed state memory on real repeated-agent transcripts
- Success threshold: At least 95% exact final-state accuracy and no more than one third of transcript-search mean context tokens on 500 or more labeled queries, with extractor-induced failures under 5%.
- Stop condition: Stop if extractor final-state accuracy is below 90% or compressed-state token footprint exceeds one third of transcript-search footprint after prompt/schema tuning on a small development split.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-state-memory-for-repeated-agent-tasks-ec2fae3d8a4c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
