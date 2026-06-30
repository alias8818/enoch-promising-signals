# Suffix-array draft model vs learned draft model for speculative decoding on small LMs

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `suffix-array-draft-model-vs-learned-draft-model-for-speculative-decoding-on-small-lms-2355a5acc738`
Run ID: `suffix-array-draft-model-vs-learned-draft-model-for-speculative-decoding-on-small-lms-2355a5acc738-20260610T011641795124+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f699e45d6d8b

## What looked useful

The suffix-index draft had 6.47% token exact match and 0.148 accepted prefix tokens per 4-token block, versus 44.98% token exact match and 1.535 accepted prefix tokens for the learned DistilGPT-2 draft. The suffix draft accepted zero tokens on 223/256 prompts.

## Boundaries and scale limits

This is a bounded acceptance-proxy study, not an optimized end-to-end speculative decoding throughput benchmark. The suffix method used a 100k-token exact-match index and max suffix order 8; larger, domain-matched, approximate, or prompt-local suffix systems were not tested.

## Claim scope

On 256 held-out Wikitext-2 validation prompts with GPT-2 as target, DistilGPT-2 as learned draft, 4-token blocks, and greedy target verification, a simple longest-suffix continuation index is not competitive with the learned draft as a speculative proposal source.

## Why it stopped

Bounded direct acceptance evidence does not support the simple suffix-array-style draft model versus a learned draft model; this is a proxy/early falsification rather than a full production validation.

## Recommended next action

Stop this no-paper run; a bounded follow-up should test whether an optimized end-to-end suffix draft with prompt-local indexing changes wall-clock throughput enough to overcome the low acceptance proxy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end speculative decoding with optimized prompt-local suffix draft
- Success threshold: Suffix-draft speculative decoding achieves at least 1.15x wall-clock tokens/sec over target-only decoding and is within 15% of the learned-draft throughput on one tested small-LM/domain pair.
- Stop condition: Stop if optimized suffix acceptance remains below 0.5 accepted tokens per 4-token block or wall-clock throughput is not faster than target-only decoding on the first two small-LM/domain pairs.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-draft-model-vs-learned-draft-model-for-speculative-decoding-on-small-lms-2355a5acc7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
