# Extractor-backed compressed state memory on real repeated-agent transcripts

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `extractor-backed-compressed-state-memory-on-real-repeated-dbeb15ff30`
Run ID: `extractor-backed-compressed-state-memory-on-real-repeated-dbeb15ff30-20260614T044802065894+0000`

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

- Parent run decision: Compressed State Memory for Repeated Agent Tasks: enoch://control-plane/projects/compressed-state-memory-for-repeated-agent-tasks-ec2fae3d8a4c/runs/compressed-state-memory-for-repeated-agent-tasks-ec2fae3d8a4c-20260614T025451767109+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/ab1c977a3cf5

## What looked useful

Small direct mechanism support: structured extraction can preserve replay-critical transcript facts more efficiently than recent-window or keyword transcript search under a tight local budget.

## Boundaries and scale limits

Single thin worker transcript, deterministic generated tasks, exact-answer scoring, handcrafted extraction, no held-out corpus, no model-in-the-loop answer generation, and no privacy/noise robustness test.

## Claim scope

On one local Codex repeated-agent JSONL transcript snapshot, deterministic extractor-backed compressed state answered 8 generated replay-fact questions at 100% accuracy while fitting within a 220-token-proxy budget; raw transcript search answered 37.5% under the same budget.

## Why it stopped

Evidence supports a bounded mechanism but is not publication-grade because the corpus is a single local transcript and the replay questions are generated from the same deterministic extractor facts.

## Recommended next action

Stop this run as no-paper useful signal; run a deepen follow-up only with a held-out real transcript set and independently authored replay questions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out real transcript replay benchmark for extractor-backed compressed state memory
- Success threshold: Extractor-backed compressed state accuracy >= best raw transcript/retrieval baseline accuracy and compressed context <= 60% of baseline context on at least 50 held-out questions.
- Stop condition: Stop as negative if extractor-backed compressed state is below the best baseline by more than 5 percentage points, exceeds 60% of the baseline context budget, or fails privacy-sensitive redaction checks.

## Evidence references

- Artifact root: `<local-path>/projects/extractor-backed-compressed-state-memory-on-real-repeated-dbeb15ff30`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
