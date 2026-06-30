# Corpus-scale GPT-2-small n-gram speculative decoding benchmark

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `corpus-scale-gpt-2-small-n-gram-speculative-decoding-bench-233ebdf484`
Run ID: `corpus-scale-gpt-2-small-n-gram-speculative-decoding-bench-233ebdf484-20260529T101813274835+0000`

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

- Parent run decision: N-gram speculative draft for GPT-2-small inference: enoch://control-plane/projects/n-gram-speculative-draft-for-gpt-2-small-inference-9ecc23bf69e6/runs/n-gram-speculative-draft-for-gpt-2-small-inference-9ecc23bf69e6-20260529T074535988040+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/ab3b49546753

## What looked useful

Exact n-gram speculative decoding is mechanically valid for GPT-2-small and can reduce target calls when the datastore contains the continuation or close repeated text, but a generic train-corpus n-gram table produced only about 6.15-6.25% call reduction in the best tested realistic condition.

## Boundaries and scale limits

Small direct benchmark only: 16-32 prompts, 512-1024 generated tokens per run, WikiText-2 raw text, full-context target forwards rather than optimized KV-cache serving, no larger corpus retrieval, no sampling, and no broad dataset robustness.

## Claim scope

Tier 1 GPT-2-small exact greedy decoding on WikiText-2 validation prompts with token-space n-gram drafting. A realistic train-corpus datastore did not reach the pre-registered 10% target-call reduction threshold; a leaky same-validation datastore did exceed it as an upper-bound diagnostic.

## Why it stopped

The controlled small direct test did not meet the realistic train-datastore success threshold; positive results were limited to a leaky upper-bound diagnostic and are not paper-positive.

## Recommended next action

Stop this run as no-paper useful evidence; next bounded test should add non-leaky retrieval-conditioned datastores and an optimized KV-cache verifier, with the same exactness and call-reduction metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Retrieval-conditioned n-gram speculative decoding for GPT-2-small
- Success threshold: At least 10% target-call reduction and positive wall-clock speedup versus a KV-cache greedy GPT-2-small baseline, with exact greedy equivalence on every generated token.
- Stop condition: Stop if retrieval-conditioned n-grams remain below 10% target-call reduction or if verifier overhead eliminates wall-clock speedup after KV-cache implementation.

## Evidence references

- Artifact root: `<local-path>/projects/corpus-scale-gpt-2-small-n-gram-speculative-decoding-bench-233ebdf484`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
