# Exact-Anchor N-Gram Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-n-gram-speculative-decoding-24b75c888634`
Run ID: `exact-anchor-n-gram-speculative-decoding-24b75c888634-20260525T041851285718+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/7a13d09d61dc

## What looked useful

General natural-language exact anchors were too sparse or inaccurate for meaningful speculative decoding speedup: best WikiText held-out speedup estimate was 1.0195x and best distilgpt2 greedy estimate was 1.0112x. Repetitive local Python-source continuations showed a niche proxy signal: 4-token majority anchors accepted 29.16% of target tokens with an optimistic 1.3043x target-call speedup estimate.

## Boundaries and scale limits

No overhead-inclusive decoder was implemented; direct model-greedy evidence used distilgpt2 on WikiText only; the positive code-domain signal is a held-out-continuation proxy rather than a code-LM serving benchmark.

## Claim scope

Exact-anchor n-gram proposals were evaluated on WikiText held-out continuations, WikiText distilgpt2 greedy continuations, and local Python-source held-out continuations using 250k-token anchor stores and short speculative chunks.

## Why it stopped

Early direct/proxy evidence falsifies the broad general-purpose exact-anchor claim, while preserving a bounded domain-specific follow-up signal for repetitive code/log text.

## Recommended next action

Stop this broad run as no-paper useful-signal evidence; if continuing, run an overhead-inclusive code/log workload benchmark with a code-capable target model and domain-gated anchors.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Domain-Gated Exact-Anchor Speculative Decoding for Code and Logs
- Success threshold: At least 1.15x measured wall-clock tokens/s improvement on structured code/log prompts with byte-for-byte identical greedy output and less than 5% regression on natural-language negative controls.
- Stop condition: Stop if overhead-inclusive speedup is below 1.05x or if exact-anchor proposals accept under 10% of generated tokens on the structured workload.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-n-gram-speculative-decoding-24b75c888634`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
