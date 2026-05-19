# Live-memory replay admission for real small local transformer cascades

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `live-memory-replay-admission-for-real-small-local-transfor-85eecba84d`
Run ID: `live-memory-replay-admission-for-real-small-local-transfor-85eecba84d-20260519T191844352029+0000`

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

- Parent run decision: Real-runtime VRAM-aware cascade replay with small local models: enoch://control-plane/projects/real-runtime-vram-aware-cascade-replay-with-small-local-mo-2f77d39ff5/runs/real-runtime-vram-aware-cascade-replay-with-small-local-mo-2f77d39ff5-20260519T191108433551+0000
- Parent run decision: Dynamic VRAM Router for Model Cascades: enoch://control-plane/projects/dynamic-vram-router-for-model-cascades-1ce88212c855/runs/dynamic-vram-router-for-model-cascades-1ce88212c855-20260519T190616995559+0000

## What looked useful

Live-memory replay at confidence 0.95 and similarity 0.90 matched the 0.91576 mean accuracy of the best eligible confidence cascade while reducing large-model call rate from 0.07520 to 0.02624; exact cache reached 0.04440, random-memory control failed the accuracy floor, and a no-repeat control removed nearly all replay benefit.

## Boundaries and scale limits

Validation used one task, one model pair, 5 fixed seeds, 2500 examples per seed, and constructed repeated/near-repeated traffic from SST-2; production recurrence, multi-task robustness, larger cascades, eviction overhead, and true online latency were not validated.

## Claim scope

On a GB10 local SST-2 sentiment cascade using DistilBERT as the small model and BERT-base as the larger fallback, live-memory replay admission reduced fallback calls on fixed-seed repeated/near-repeated streams while preserving the same mean accuracy as the best eligible confidence cascade.

## Why it stopped

Tier 2 local evidence supports the mechanism, but the central recurrence pattern is constructed and the result is too narrow for a paper.

## Recommended next action

Stop this run as no-paper useful evidence; the concrete next bounded test is a natural near-duplicate/paraphrase traffic benchmark across multiple classification or routing tasks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural near-duplicate replay admission across multiple local transformer routing tasks
- Success threshold: Across at least three streams, live-memory replay must reduce fallback-call rate by >=30% relative to exact cache while staying within 0.5 percentage points of the best eligible non-replay cascade accuracy and beating random-memory control by >=1.0 percentage point accuracy at matched replay rate.
- Stop condition: Stop as negative if live-memory replay fails the fallback-reduction threshold on two or more streams, loses more than 0.5 percentage points accuracy at matched cascade settings, or its online admission overhead eliminates measured latency savings.

## Evidence references

- Artifact root: `<local-path>/projects/live-memory-replay-admission-for-real-small-local-transfor-85eecba84d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
