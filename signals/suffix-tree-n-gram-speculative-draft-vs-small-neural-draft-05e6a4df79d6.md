# Suffix-Tree N-Gram Speculative Draft vs Small Neural Draft

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-n-gram-speculative-draft-vs-small-neural-draft-05e6a4df79d6`
Run ID: `suffix-tree-n-gram-speculative-draft-vs-small-neural-draft-05e6a4df79d6-20260611T104941873004+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e59f60beba17

## What looked useful

Suffix/n-gram acceptance was 0.2517 versus 0.5761 for DistilGPT-2, but draft throughput was 22479 tokens/s versus 542 tokens/s and simple-loop emitted throughput was 579 tokens/s versus 304 tokens/s for neural draft and 315 tokens/s for target-only greedy.

## Boundaries and scale limits

GPT-2-class models only; Wikitext-2 only; greedy decoding only; Python/PyTorch unbatched verifier; no production serving, sampling, long-context, batching, or large-target validation.

## Claim scope

On 48 Wikitext-2 prompts with GPT-2 as target, DistilGPT-2 as neural drafter, gamma=4, and greedy verification, a live-context-plus-corpus suffix/n-gram drafter had much lower target-token acceptance than the neural drafter but higher end-to-end throughput in the simple unbatched verifier loop because draft cost was near zero.

## Why it stopped

No-paper useful signal: the broad replacement hypothesis is mixed and not paper-positive because suffix/n-gram acceptance is far below the neural drafter, though low draft overhead produced a bounded throughput win in this proxy implementation.

## Recommended next action

Run a bounded deepen follow-up with an optimized batched verifier plus gamma/order/corpus ablations; stop if suffix/n-gram no longer beats target-only and neural draft under the optimized verifier.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Batched verifier ablation for suffix n-gram speculative drafting
- Success threshold: Suffix/n-gram emitted tokens per second is at least 1.2x target-only and at least 1.1x neural draft on both corpora while preserving the same target greedy outputs.
- Stop condition: Stop if optimized verifier results show suffix/n-gram throughput at or below target-only on either corpus or if acceptance falls below 0.15 across tested gamma/order settings.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-n-gram-speculative-draft-vs-small-neural-draft-05e6a4df79d6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
