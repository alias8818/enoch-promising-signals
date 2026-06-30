# Layered agent memory with operator-model updates

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layered-agent-memory-with-operator-model-updates-b26aa8c35c44`
Run ID: `layered-agent-memory-with-operator-model-updates-b26aa8c35c44-20260629T043042072733+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d7b7caee9d55

## What looked useful

Across 20 seeds and 12,000 scored queries, layered_doctrine_memory reached 1.0000 mean accuracy versus 0.5106 for flat_retrieval and 0.2789 for transcript_search. Failure cases show flat retrieval scope bleed and transcript stale-recall errors.

## Boundaries and scale limits

Synthetic oracle-scored replay only; no natural-language extraction, LLM generation, human grading, production persistence, adversarial update streams, or real operator logs were tested.

## Claim scope

In a deterministic synthetic replay benchmark with explicit operator preference updates, stale contradictions, project-scoped overrides, and noisy distractors, a layered global-plus-project memory retrieves the currently valid operator rule more accurately than no-memory, earliest-match transcript search, and scope-blind flat recency retrieval.

## Why it stopped

Closed as no-paper useful signal because the current result directly tests only synthetic memory update/retrieval mechanics, not real transcript extraction or LLM response behavior.

## Recommended next action

Run a bounded model-in-the-loop replay using realistic natural-language preference updates, extraction errors included, and compare layered memory against cost-matched flat/vector retrieval on generated response correctness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Model-in-the-loop replay for layered operator memory
- Success threshold: Layered memory improves generated-response correctness by at least 10 percentage points over the strongest retrieval baseline across at least 500 scored queries without increasing false recall.
- Stop condition: Stop if layered memory fails to beat the strongest baseline by 5 percentage points in a 100-query pilot or if extraction noise eliminates the synthetic advantage.

## Evidence references

- Artifact root: `<local-path>/projects/layered-agent-memory-with-operator-model-updates-b26aa8c35c44`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
