# KV-Cache Suffix Array Drafting

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-suffix-array-drafting-fb9e7f240c3b`
Run ID: `kv-cache-suffix-array-drafting-fb9e7f240c3b-20260524T171843711101+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/90ccc2e70cdf

## What looked useful

Exact suffix-copy drafting can accept long drafts on repeated text, but real-text BPE exact matches are sparse beyond short contexts; the suffix-array query found the same drafts as an online fixed-context hash while running slower in this implementation.

## Boundaries and scale limits

No real transformer KV-cache tensors, logits, verifier loop, production serving latency, broad corpus mix, or long-context model deployment were tested.

## Claim scope

CPU-only proxy benchmark of exact token-copy drafting from prior prefix matches on synthetic repeated text and a Tiny Shakespeare slice, using byte and GPT-2 BPE tokenizations.

## Why it stopped

Proxy evidence supports the mechanism in repetitive cases but does not support a suffix-array-specific advantage, and real-text BPE coverage is too sparse for a paper claim.

## Recommended next action

Stop this run as a no-paper useful signal; only continue if implementing an in-model speculative decoding comparison against an online n-gram/hash drafter on repetition-heavy prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: In-model exact-copy drafting versus online n-gram baseline
- Success threshold: At least 10% end-to-end decode speedup versus no drafter on repetition-heavy prompts, with no regression versus the online hash baseline and no material slowdown on ordinary prompts.
- Stop condition: Stop if exact-copy drafting gives under 5% speedup versus no drafter or if suffix-array indexing is slower than the online hash at matched accepted-token counts.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-suffix-array-drafting-fb9e7f240c3b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
