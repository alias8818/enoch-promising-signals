# Real-QA Retrieval Control for Compact Anchor Re-injection

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-qa-retrieval-control-for-compact-anchor-re-injection-75cbd267bf`
Run ID: `real-qa-retrieval-control-for-compact-anchor-re-injection-75cbd267bf-20260603T150658602807+0000`

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

- Parent run decision: Anchor Checkpoint Sliding Window with Dynamic Re-injection: enoch://control-plane/projects/anchor-checkpoint-sliding-window-with-dynamic-re-injection-af316dd198c3/runs/anchor-checkpoint-sliding-window-with-dynamic-re-injection-af316dd198c3-20260602T141046179758+0000
- Parent run decision: Small-LLM QA Validation of Dynamic Anchor Re-injection: enoch://control-plane/projects/small-llm-qa-validation-of-dynamic-anchor-re-injection-f22d73c7ac/runs/small-llm-qa-validation-of-dynamic-anchor-re-injection-f22d73c7ac-20260602T193808205513+0000

## What looked useful

Across 5 fixed seeds and 4,000 QA instances per budget, compact anchors improved answer coverage over plain BM25 by +4.13 percentage points at 80 words, +1.43 points at 120 words, and +0.45 points at 180 words. It also beat random and low-score anchor controls at all budgets.

## Boundaries and scale limits

This run did not test downstream reader EM/F1, generated answer faithfulness, dense retrieval, multi-hop QA, larger Wikipedia corpora, or neural long-context lost-in-the-middle behavior. The effect shrinks as the context budget approaches baseline saturation.

## Claim scope

On SQuAD v1.1 dev questions with BM25 over SQuAD paragraph contexts, compact question-overlap anchor re-injection improves answer-string coverage in the delivered retrieval context under tight word budgets, most clearly at 80 words.

## Why it stopped

Tier 2 retrieval-context evidence supports the mechanism in a bounded setting, but publication-grade QA evidence is missing and the effect is small near saturation.

## Recommended next action

Stop this run as no-paper useful evidence; next run should test whether the tight-budget coverage gains translate to reader EM/F1 with a fixed open-source QA reader and a dense-retrieval baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Reader EM/F1 Validation for Compact Anchor Re-injection
- Success threshold: At 80-120 word budgets, compact anchors improve reader F1 by at least 1.0 point over plain BM25 and at least 3.0 points over random anchors, with paired wins exceeding losses on fixed seeds.
- Stop condition: Stop if compact anchors fail to improve reader F1 over plain BM25 at both 80 and 120 word budgets, or if gains appear only in answer coverage but not in reader predictions.

## Evidence references

- Artifact root: `<local-path>/projects/real-qa-retrieval-control-for-compact-anchor-re-injection-75cbd267bf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
