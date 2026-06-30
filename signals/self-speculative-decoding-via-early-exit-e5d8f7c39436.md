# Self-Speculative Decoding via Early Exit

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `self-speculative-decoding-via-early-exit-e5d8f7c39436`
Run ID: `self-speculative-decoding-via-early-exit-e5d8f7c39436-20260602T160931248780+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/e5c9324cda0f

## What looked useful

Early-exit self-speculation becomes useful only when the shallow head is highly aligned with the final head; an undertrained exact run with 62.1% early/final agreement had only 26.8% draft-token acceptance and slowed decoding to 0.735x, while a better-trained run with 91.5% agreement accepted 89.7% of draft tokens and reached 1.38x speedup.

## Boundaries and scale limits

The evidence is toy-scale only: synthetic data, no natural language corpus, no pretrained GPT-2-small-class baseline, no production KV-cache verifier, no learned absolute positional embeddings in the final exact harness, and only short local GB10 runs. The result should not be read as a broad LLM serving validation.

## Claim scope

A tiny decoder-only transformer on a synthetic modular affine sequence task can use a layer-2 early-exit head as a self-drafter for exact greedy-equivalent speculative decoding when TF32 is disabled and the verification context is not cropped; after 2500 training steps it achieved 91.5% early/final agreement, 89.7% draft-token acceptance, and 1.38x decode throughput over full greedy baseline on 16 prompts.

## Why it stopped

Closed as no-paper useful signal: local toy evidence supports the mechanism but does not provide direct publication-grade evidence for real LLM decoding.

## Recommended next action

Run a bounded GPT-2-small-class natural-language follow-up with auxiliary early-exit loss and a KV-cache verifier; stop if early/final draft-token agreement does not exceed 85% or exact greedy throughput fails to beat baseline by at least 1.2x.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small early-exit self-speculative decoding on natural language
- Success threshold: Exact greedy match on all evaluated prompts, early/final draft-token agreement >= 85%, accepted draft-token rate >= 75%, and throughput speedup >= 1.2x over full greedy baseline without worse final-head validation loss than the matched baseline.
- Stop condition: Stop as negative if exactness fails after verifier fixes, if early/final agreement remains below 75%, or if measured exact throughput is <= baseline after adequate auxiliary-head training.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-via-early-exit-e5d8f7c39436`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
