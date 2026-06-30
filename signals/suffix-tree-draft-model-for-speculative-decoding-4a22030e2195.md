# Suffix-Tree Draft Model for Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-draft-model-for-speculative-decoding-4a22030e2195`
Run ID: `suffix-tree-draft-model-for-speculative-decoding-4a22030e2195-20260620T224522247478+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/65f84ab55b3d

## What looked useful

Suffix-tree draft memory appears useful for repeated long-span domains but not as a general-purpose draft model. On Tiny Shakespeare, order-24 suffix memory matched trigram mean accepted tokens (0.1518 vs 0.1516) while using 4.87M arcs vs 262k; on synthetic repetitive code it improved mean accepted tokens from 2.46 to 5.82 and full 8-token acceptance from 3.18% to 53.62%.

## Boundaries and scale limits

No transformer target model, production tokenizer, GPU serving path, KV-cache behavior, or wall-clock speculative decoding speedup was tested. Corpora were small: Tiny Shakespeare plus one synthetic repetitive code-like generator.

## Claim scope

Bounded proxy evidence: a naive variable-order suffix draft improves contiguous accepted-token predictions on strongly repetitive synthetic code-like text, but does not improve over a fixed trigram on Tiny Shakespeare natural text despite much larger memory.

## Why it stopped

Proxy evidence is mixed and insufficient for a paper: it supports the mechanism only in repetitive code-like settings and early-falsifies the naive general-purpose suffix-tree draft claim on natural text.

## Recommended next action

Run a bounded direct small-model speculative decoding follow-up on a real code corpus with production tokenization and compare suffix draft, n-gram draft, and a small neural draft on accepted tokens per target pass and wall-clock decode speed.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct small-model code speculative decoding benchmark for suffix drafts
- Success threshold: Suffix draft achieves at least 20% higher wall-clock decode throughput than fixed n-gram at comparable output quality and memory below 2x the n-gram baseline on a held-out real code benchmark.
- Stop condition: Stop if suffix draft accepted tokens per target pass are within 5% of fixed n-gram or if memory required for a 20% throughput gain exceeds 2x the n-gram baseline.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-draft-model-for-speculative-decoding-4a22030e2195`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
