# Real-model trace validation for context-suffix speculative decoding on structured text

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-model-trace-validation-for-context-suffix-speculative-b7fbae9f1c`
Run ID: `real-model-trace-validation-for-context-suffix-speculative-b7fbae9f1c-20260523T174434462587+0000`

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

- Parent run decision: Context-Suffix Matching Speculative Decoding for Structured Text: enoch://control-plane/projects/context-suffix-matching-speculative-decoding-for-structured-text-c0e4c0ba9a39/runs/context-suffix-matching-speculative-decoding-for-structured-text-c0e4c0ba9a39-20260523T171226663359+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/7d1a8c055254

## What looked useful

Structured prompts reached 67.48% accepted target tokens and 2.62x simulated target-call reduction versus 15.53% accepted tokens and 1.17x for random-copy control; suffix/random acceptance ratio was 4.35x.

## Boundaries and scale limits

One 410M causal LM, hand-authored structured prompts, 8 unique structured templates repeated twice, 2048 structured generated tokens, offline trace simulation rather than a production speculative-decoding runtime, and prose controls also became repetitive at 128 tokens.

## Claim scope

Tier 1 direct trace validation with EleutherAI/pythia-410m shows that a context-suffix copy drafter can exactly match a large fraction of greedy target-model tokens on repetitive structured-text continuations, producing simulated target-call reductions above the predeclared mechanism threshold.

## Why it stopped

Tier 1 mechanism support was obtained, but the evidence remains no-paper because it is single-model, prompt-small, and uses offline simulated verification rather than measured serving speedup.

## Recommended next action

Run a bounded multi-model, de-duplicated trace validation with external structured corpora and a real KV-cache speculative verifier before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-model corpus validation of context-suffix speculative decoding on structured text
- Success threshold: On at least 100 de-duplicated structured prompts per model, context-suffix drafting accepts >=30% of target tokens, improves measured target verification throughput by >=1.3x, and beats random/no-suffix copy acceptance by >=2x without changing greedy target output.
- Stop condition: Stop as negative if either model has <20% structured token acceptance or <1.1x measured verifier throughput improvement after implementation overheads, or if gains are not better than a standard n-gram/prompt-lookup baseline.

## Evidence references

- Artifact root: `<local-path>/projects/real-model-trace-validation-for-context-suffix-speculative-b7fbae9f1c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
