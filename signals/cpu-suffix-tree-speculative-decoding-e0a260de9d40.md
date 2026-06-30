# CPU Suffix-Tree Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-suffix-tree-speculative-decoding-e0a260de9d40`
Run ID: `cpu-suffix-tree-speculative-decoding-e0a260de9d40-20260607T085303567958+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/14562d0f635d

## What looked useful

Online suffix order 4 improved Tiny Shakespeare estimated tokens per verify from 1.09 frozen to 1.17 online and Alice online suffix reached 1.38, but median accepted tokens stayed 0 on real text; synthetic repetition reached 5.89 but was beaten by online n-gram at 6.39.

## Boundaries and scale limits

Tested regex-tokenized synthetic repetition, Tiny Shakespeare, and Alice with 5,000 held-out positions each, 8-token drafts, and no actual LLM verifier, tokenizer, GPU overlap, batching, or serving integration.

## Claim scope

A bounded CPU-token-stream benchmark shows suffix-index drafting can exploit repeated spans, especially with an online cache, but natural-text exact-token acceptance remains low and high suffix orders increase memory/latency sharply.

## Why it stopped

Proxy benchmark supports the repeated-span mechanism but not a paper-ready CPU suffix-tree speculative decoding claim; real-text acceptance is too low after expected verifier overhead and high-order indexes are memory-expensive.

## Recommended next action

Stop this run as no-paper useful signal; a bounded follow-up should test the suffix-cache drafter inside an actual small LLM speculative decoding loop against n-gram and target-only baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-LLM Online Suffix-Cache Speculative Decoding
- Success threshold: At least 10% end-to-end tokens/s improvement over target-only and at least 5% over the n-gram drafter on repetition-heavy prompts, with no regression larger than 5% on ordinary prompts and less than 1 GB incremental CPU memory.
- Stop condition: Stop if suffix-cache end-to-end throughput does not beat the n-gram drafter by 5% on repetition-heavy prompts or if CPU memory exceeds 1 GB incremental RSS at the tested context sizes.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-suffix-tree-speculative-decoding-e0a260de9d40`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
