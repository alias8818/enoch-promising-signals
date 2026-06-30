# N-gram Context Cache for Draft-Free Speculative Decoding

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `n-gram-context-cache-for-draft-free-speculative-decoding-a9342d684a1e`
Run ID: `n-gram-context-cache-for-draft-free-speculative-decoding-a9342d684a1e-20260525T080315117310+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/31aa1832cda5

## What looked useful

The mechanism is viable in bounded local tests: repetitive text reached 3.0 tokens per target call and wikitext reached 1.38-1.44 tokens per target call for n=3-4. Longer n=6 keys accepted cleaner proposals but hit too rarely, showing the core tradeoff is exact-context hit rate versus proposal correctness.

## Boundaries and scale limits

Only GPT-2, greedy decoding, short prompts, small token counts, and a simple verification harness were tested. Production KV-cache verification, stochastic sampling, larger models, batch serving, long contexts, and learned draft-model baselines were not tested.

## Claim scope

Small direct GPT-2 greedy-decoding probe: exact n-gram context-cache proposals can reduce target-model calls when contexts repeat, including 27-31% target-call reduction on six short wikitext prompts for n=3-4 and block size 4.

## Why it stopped

Evidence supports the mechanism but is too narrow and partly implementation-proxy-based for a paper claim.

## Recommended next action

Stop this run as a no-paper useful signal; next run should implement KV-cache-aware verification and compare latency/tokens/sec against greedy decoding and a small draft-model speculative baseline on a standard generation benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache serving benchmark for n-gram draft-free speculative decoding
- Success threshold: At least 15% end-to-end tokens/sec improvement over greedy decoding on a non-repetitive benchmark split while preserving exact greedy outputs, plus a clear positive-control gain on repetitive prompts.
- Stop condition: Stop if KV-cache-aware implementation gives less than 5% end-to-end speedup on non-repetitive prompts or loses exact greedy equivalence.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-context-cache-for-draft-free-speculative-decoding-a9342d684a1e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
