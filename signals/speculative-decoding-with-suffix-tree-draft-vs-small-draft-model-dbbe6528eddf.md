# Speculative decoding with suffix-tree draft vs small draft model

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-decoding-with-suffix-tree-draft-vs-small-draft-model-dbbe6528eddf`
Run ID: `speculative-decoding-with-suffix-tree-draft-vs-small-draft-model-dbbe6528eddf-20260629T194241982444+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1df4e6c7b29e

## What looked useful

Suffix retrieval accepted only 0.344 of 4 proposed tokens on average versus 1.172 for distilgpt2, but its 0.027 ms draft overhead yielded an estimated 1.51x speedup over a naive serial GPT-2 greedy baseline; distilgpt2 had better acceptance but lost wall time in the uncached local implementation.

## Boundaries and scale limits

This is not exact stochastic speculative decoding, not KV-cache optimized serving, not batched production inference, and not validated on larger target models or instruction/chat distributions.

## Claim scope

On a local greedy speculative-decoding proxy with GPT-2 as target, Tiny Shakespeare prompts, 4-token proposals, and 128 held-out prompts, a suffix-index draft is much cheaper but substantially lower quality than a distilgpt2 draft; it can still beat a naive serial greedy target baseline because its draft overhead is near zero.

## Why it stopped

Bounded local proxy shows mixed evidence rather than a publishable result: suffix drafting is fast but has weak target agreement and median zero accepted tokens.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should implement a KV-cached speculative decoder and compare suffix retrieval, distilgpt2, and a hybrid suffix-plus-model draft on exact wall throughput.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cached suffix retrieval versus small-model speculative decoding
- Success threshold: Suffix or hybrid draft achieves at least 1.2x wall throughput over target-only greedy decoding and at least 90% of the optimized small-draft throughput while preserving exact output semantics.
- Stop condition: Stop if optimized suffix or hybrid draft still has median zero accepted tokens or fails to exceed target-only throughput by 10% on the 1000-prompt benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-with-suffix-tree-draft-vs-small-draft-model-dbbe6528eddf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
