# Context-Aware N-gram Speculative Decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `context-aware-n-gram-speculative-decoding-f67fadf77951`
Run ID: `context-aware-n-gram-speculative-decoding-f67fadf77951-20260602T122843976143+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/7195814c2f2d

## What looked useful

Context-aware n-gram drafting strongly outperformed global n-gram drafting in direct greedy speculative verification: mean target calls fell from 979.0 to 503.0 for 1152 generated tokens. Against prompt lookup alone, the global fallback gave a smaller 4.55% target-call reduction while lowering draft acceptance precision.

## Boundaries and scale limits

Evidence is limited to distilgpt2, WikiText-2, 48-token greedy continuations, two 24-prompt confirmation seeds, and a Python benchmark. It does not validate larger models, non-greedy sampling, production serving latency, batching, long contexts, or optimized KV-cache behavior.

## Claim scope

On distilgpt2 greedy decoding over short WikiText-2 validation prompts, a prompt/history n-gram drafter with global n-gram fallback reduced target-model verification calls versus a global n-gram drafter and gave a small repeatable improvement over prompt lookup alone.

## Why it stopped

Closed as no-paper useful signal: the direct small-scale evidence supports the mechanism but is not broad or production-realistic enough for publication-grade validation.

## Recommended next action

Run a bounded deeper implementation using GPT-2-small-class targets and a real assisted-generation loop with KV-cache-aware latency measurements before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache-aware context n-gram speculative decoding on GPT-2-small-class targets
- Success threshold: At least 15% fewer target forward passes than prompt lookup alone, no more than 5% worse measured end-to-end latency, and exact greedy-output equivalence across all prompts.
- Stop condition: Stop if context-aware fallback fails to beat prompt lookup by 5% target-call reduction or increases measured latency by more than 10% after threshold tuning.

## Evidence references

- Artifact root: `<local-path>/projects/context-aware-n-gram-speculative-decoding-f67fadf77951`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
