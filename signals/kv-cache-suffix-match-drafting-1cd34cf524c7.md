# KV-Cache Suffix-Match Drafting

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `kv-cache-suffix-match-drafting-1cd34cf524c7`
Run ID: `kv-cache-suffix-match-drafting-1cd34cf524c7-20260523T201612986530+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/71f733db03f9

## What looked useful

Naive exact suffix-match drafting gives measurable but too-weak acceptance: best setting K=3 over 7.1M train tokens hit 48.0% of prompts but GPT-2 accepted >=1 draft token on only 11.7%, >=2 on 2.2%, with mean accepted length 0.146 tokens/query.

## Boundaries and scale limits

No production KV-cache server, no real serving traces, no end-to-end latency benchmark, no stochastic decoding, and no larger-than-GPT-2 target models were tested.

## Claim scope

Bounded GPT-2/Wikitext-103 proxy test of exact token suffix-match drafting from a train-corpus index into held-out validation prompts, with greedy target-model acceptance measured on CUDA.

## Why it stopped

Proxy/early falsification rather than full validation: exact suffix matching alone produced far below one accepted draft token per query, making speculative speedup unlikely without additional mechanisms.

## Recommended next action

Stop the naive exact suffix-match-only approach; only revisit with a bounded reranking/locality follow-up that must exceed 0.75 mean accepted tokens/query or 25% acceptance of two or more draft tokens on the same GPT-2/Wikitext protocol.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Reranked suffix-match drafting on GPT-2/Wikitext
- Success threshold: Mean GPT-2 accepted draft length >= 0.75 tokens/query or acceptance of two or more draft tokens on >= 25% of queries, with overhead low enough to plausibly beat no-draft decoding.
- Stop condition: Stop if reranking remains below 0.5 mean accepted tokens/query and below 15% acceptance of two or more draft tokens on 2048 held-out queries.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-suffix-match-drafting-1cd34cf524c7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
