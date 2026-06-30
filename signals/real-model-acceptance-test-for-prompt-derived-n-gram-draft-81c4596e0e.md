# Real-model acceptance test for prompt-derived n-gram drafts on extractive QA

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-model-acceptance-test-for-prompt-derived-n-gram-draft-81c4596e0e`
Run ID: `real-model-acceptance-test-for-prompt-derived-n-gram-draft-81c4596e0e-20260528T154051587375+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Prompt-Derived N-Gram Speculative Decoding: enoch://control-plane/projects/prompt-derived-n-gram-speculative-decoding-07d6ffa9b4f1/runs/prompt-derived-n-gram-speculative-decoding-07d6ffa9b4f1-20260528T120627116702+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2f9ce934f070

## What looked useful

Top-1 draft acceptance was 2.4% versus 0.5% random control, below the preregistered 20% acceptance and 10-point lift threshold. Top-10 draft acceptance was 17.2% versus 2.4% random control, suggesting candidate-set signal but not practical single-shot acceptance.

## Boundaries and scale limits

Single dataset, single QA verifier model, first 1000 validation examples, hand-coded prompt-only drafter, answer-level exact-match acceptance rather than token-level speculative decoding or latency measurement.

## Claim scope

On SQuAD validation with distilbert-base-cased-distilled-squad as the verifier, a hand-coded prompt/context-derived n-gram drafter does not achieve useful top-1 answer acceptance, but its top-10 candidate set covers the verifier's preferred answer span substantially above random n-gram controls.

## Why it stopped

Direct 1000-example real-model test falsified the preregistered top-1 useful-signal threshold; result is an early direct negative for single-shot prompt-derived n-gram drafts, not a full validation across models or datasets.

## Recommended next action

Run a bounded reranking follow-up that tries to convert the observed top-10 candidate coverage into top-1 acceptance using only prompt-derived features or a cheap draft model, with held-out examples and the same verifier-acceptance metric.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Prompt-only reranking of n-gram QA drafts to recover top-10 verifier coverage
- Success threshold: Top-1 acceptance >= 12% and at least 8 percentage-point absolute lift over the current heuristic top-1 acceptance, while preserving top-10 acceptance >= 15%.
- Stop condition: Stop as negative if held-out top-1 acceptance remains below 8% or the lift over the current heuristic is less than 4 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/real-model-acceptance-test-for-prompt-derived-n-gram-draft-81c4596e0e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
