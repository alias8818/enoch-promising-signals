# Reader EM/F1 Validation for Compact Anchor Re-injection

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `reader-em-f1-validation-for-compact-anchor-re-injection-212aced851`
Run ID: `reader-em-f1-validation-for-compact-anchor-re-injection-212aced851-20260603T213310935585+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real-QA Retrieval Control for Compact Anchor Re-injection: enoch://control-plane/projects/real-qa-retrieval-control-for-compact-anchor-re-injection-75cbd267bf/runs/real-qa-retrieval-control-for-compact-anchor-re-injection-75cbd267bf-20260603T150658602807+0000
- Parent run decision: Small-LLM QA Validation of Dynamic Anchor Re-injection: enoch://control-plane/projects/small-llm-qa-validation-of-dynamic-anchor-re-injection-f22d73c7ac/runs/small-llm-qa-validation-of-dynamic-anchor-re-injection-f22d73c7ac-20260602T193808205513+0000

## What looked useful

Across 1,200 shuffled SQuAD question-seed pairs, lexical re-injection achieved 63.67 EM and 73.58 F1 versus 0.17 EM and 1.23 F1 for prefix compaction and 6.08 EM and 8.56 F1 for random re-injection. Oracle answer-sentence re-injection reached 71.00 EM and 82.03 F1, leaving a measurable but smaller anchor-selection gap.

## Boundaries and scale limits

Validation used synthetic long contexts made by concatenating distractor SQuAD paragraphs, one extractive reader, 1000-character compact contexts, and a lexical overlap anchor selector. It did not test naturally long QA corpora, learned anchors, dense retrieval baselines, end-to-end RAG, or multiple reader architectures.

## Claim scope

In a constructed SQuAD v1.1 compaction stress test using a fixed DistilBERT extractive reader, lexical compact anchor re-injection substantially improves reader EM/F1 over naive prefix compaction and random omitted-sentence re-injection when answer-bearing evidence is outside the compact prefix.

## Why it stopped

Useful direct EM/F1 mechanism evidence was produced, but the evidence is constructed-context validation rather than broad natural long-context QA and the simple lexical anchor selector is not enough for paper readiness.

## Recommended next action

Stop paper escalation for this run; run a bounded deepen validation on a naturally long QA dataset with BM25/dense sentence retrieval baselines before making any publication claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural Long-QA CAR Validation Against Retrieval Baselines
- Success threshold: CAR improves by >=5 absolute F1 over naive compaction and random re-injection, and is within 5 F1 of the strongest non-oracle retrieval baseline at the same compact context budget.
- Stop condition: Stop if CAR fails to beat random re-injection by at least 3 absolute F1 or trails BM25/dense retrieval by more than 10 F1 on the natural long-QA validation split.

## Evidence references

- Artifact root: `<local-path>/projects/reader-em-f1-validation-for-compact-anchor-re-injection-212aced851`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
