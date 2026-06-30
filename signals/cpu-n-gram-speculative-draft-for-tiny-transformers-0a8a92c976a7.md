# CPU N-Gram Speculative Draft for Tiny Transformers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-speculative-draft-for-tiny-transformers-0a8a92c976a7`
Run ID: `cpu-n-gram-speculative-draft-for-tiny-transformers-0a8a92c976a7-20260531T184553860368+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4e31330fce0a

## What looked useful

A simple CPU n-gram drafter is cheap after rolling-context implementation, but full-block verification cost makes acceptance rate decisive. Best estimated wall speedups were 3.77x on a repetitive control, 3.22x on near-duplicate prompt boilerplate, 1.20x on license text, 0.97x on Python stdlib code, and 0.76x on random control.

## Boundaries and scale limits

No real pretrained tiny transformer, tokenizer, KV cache, or production serving loop was integrated. Project prompt data contains near-duplicate initial/resume text and is treated only as a boilerplate/low-entropy signal. The main interpreted run used at most 30k held-out tokens per corpus and a local CPU verifier proxy.

## Claim scope

Bounded CPU proxy: n-gram drafting over held-out local token streams plus a NumPy tiny-transformer-shaped verifier cost model. The mechanism helps repetitive or near-duplicate streams, is marginal on license-like formal text, and does not improve code-like or random streams.

## Why it stopped

The result is mixed and proxy-bounded rather than paper-ready: it supports a narrow mechanism for repetitive text but does not support a general CPU tiny-transformer speculative decoding speedup claim.

## Recommended next action

Stop this run as no-paper useful signal; a bounded follow-up should test the same drafter inside a real tiny-transformer CPU inference loop with KV-cache verification on non-duplicated corpora.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Tiny-Transformer CPU KV-Cache N-Gram Draft Test
- Success threshold: At least 1.1x median latency speedup on two non-duplicated low-entropy/prose subsets, no more than 2% slowdown on code-like subsets after gating, and identical greedy outputs or validated speculative sampling equivalence.
- Stop condition: Stop if real-model verification cost or acceptance rates keep estimated or measured speedup below 1.05x on all non-duplicated subsets.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-speculative-draft-for-tiny-transformers-0a8a92c976a7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
