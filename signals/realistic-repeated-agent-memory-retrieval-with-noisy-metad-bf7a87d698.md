# Realistic repeated-agent memory retrieval with noisy metadata and non-oracle extraction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `realistic-repeated-agent-memory-retrieval-with-noisy-metad-bf7a87d698`
Run ID: `realistic-repeated-agent-memory-retrieval-with-noisy-metad-bf7a87d698-20260612T090718626031+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Noisy metadata extraction for repeated-agent memory baselines: enoch://control-plane/projects/noisy-metadata-extraction-for-repeated-agent-memory-baseli-9ef84479b2/runs/noisy-metadata-extraction-for-repeated-agent-memory-baseli-9ef84479b2-20260612T085703667200+0000
- Parent run decision: Natural-language repeated-agent memory benchmark with metadata-aware flat baselines: enoch://control-plane/projects/natural-language-repeated-agent-memory-benchmark-with-meta-e3e8cc7b25/runs/natural-language-repeated-agent-memory-benchmark-with-meta-e3e8cc7b25-20260612T085159531192+0000

## What looked useful

Repeated memory traces are useful (+11.7 percentage points over no-repeat control overall; +22.2 points at 8 repeats), hard metadata filters are brittle (0.8797 accuracy at clean metadata to 0.3230 at 60% metadata noise), and soft metadata needs reliability gating because it loses to simple top-k voting at 60% metadata noise.

## Boundaries and scale limits

512 facts per condition, 5 seeds, synthetic generated memory traces, lexical sparse retrieval, rule-based non-oracle extraction, no real LLM memory-writing/extraction traces, no human-authored corpus, no production embedding retriever, and no multi-day live agent deployment.

## Claim scope

In a deterministic synthetic benchmark of repeated agent memory notes with noisy metadata, content corruption, distractors, and non-oracle surface extraction, repeated independent traces substantially improve exact-answer retrieval over a one-note control, while hard metadata filtering fails under noisy metadata. The tested soft metadata voting method only slightly improves over a simple lexical top-k voting baseline and becomes worse at high metadata noise.

## Why it stopped

Direct synthetic validation supports repetition and rejects hard metadata filtering, but the proposed soft metadata method has only a small average gain over a real lexical top-k voting baseline and fails at high metadata noise, so it is not paper-positive.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should replace fixed soft metadata weighting with an adaptive metadata-reliability gate and evaluate on LLM-generated memory traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive metadata reliability gating for repeated-agent memory retrieval
- Success threshold: At least +3.0 percentage points paired exact-answer accuracy over lexical top-k voting at metadata_noise >= 0.4, no more than -0.5 points at metadata_noise <= 0.2, and at least +10 points over no-repeat control across repeat levels >= 2.
- Stop condition: Stop if adaptive gating cannot beat lexical top-k voting by +1 point at metadata_noise >= 0.4 on the synthetic grid or if LLM-generated extraction noise removes the repeated-trace gain below +5 points over no-repeat.

## Evidence references

- Artifact root: `<local-path>/projects/realistic-repeated-agent-memory-retrieval-with-noisy-metad-bf7a87d698`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
