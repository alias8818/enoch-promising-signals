# Small-LLM QA Validation of Dynamic Anchor Re-injection

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `small-llm-qa-validation-of-dynamic-anchor-re-injection-f22d73c7ac`
Run ID: `small-llm-qa-validation-of-dynamic-anchor-re-injection-f22d73c7ac-20260602T193808205513+0000`

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
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/a991488e6086

## What looked useful

The run supports the bounded mechanism that small QA models can recover answer accuracy when a query-matched anchor is compactly re-injected into the prompt budget, and that this is not explained by a generic highlighted sentence because wrong-anchor controls scored 0%. Earlier full-context and excerpt-retaining variants were weaker, constraining the claim to compact anchor re-injection.

## Boundaries and scale limits

Synthetic templated facts only; one small seq2seq model; no real QA dataset; successful intervention compressed the context to the matched anchor rather than retaining substantial distractor context; no learned retrieval, training, multi-model robustness, or adversarial paraphrase evaluation.

## Claim scope

In a deterministic synthetic QA task with google/flan-t5-small, 36 examples per seed, 55 distractor facts, and a 512-token input cap, compact re-injection of the query-matched anchor near the question improved exact-match accuracy from 8.33% raw long-context aggregate accuracy to 80.56% across three distractor seeds; a compact wrong-anchor control stayed at 0%.

## Why it stopped

Tier 1 controlled direct test passed its bounded threshold, but evidence remains synthetic and compact-anchor-only, so it is useful no-paper evidence rather than paper-positive validation.

## Recommended next action

Run a bounded deepen test on a real or semi-real QA dataset with anchors retrieved from source passages, comparing compact matched-anchor re-injection against BM25/top-k passage retrieval and wrong-anchor controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-QA Retrieval Control for Compact Anchor Re-injection
- Success threshold: Compact matched-anchor re-injection improves exact-match or token-F1 by at least 15 percentage points over the best non-anchor retrieval baseline, achieves at least 60% absolute exact-match or F1 on the scoped dataset, and wrong-anchor controls remain within 5 percentage points of the no-answer or irrelevant-retrieval baseline.
- Stop condition: Stop as negative if matched-anchor re-injection fails to beat the best non-anchor retrieval baseline by 15 percentage points or if wrong-anchor controls improve similarly, indicating the effect is not anchor specificity.

## Evidence references

- Artifact root: `<local-path>/projects/small-llm-qa-validation-of-dynamic-anchor-re-injection-f22d73c7ac`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
