# Direct Small-LM Speculative Decoding With Suffix Retrieval Drafts

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `direct-small-lm-speculative-decoding-with-suffix-retrieval-32ba99342c`
Run ID: `direct-small-lm-speculative-decoding-with-suffix-retrieval-32ba99342c-20260601T091000918895+0000`

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

- Parent run decision: Suffix-Array Speculative Decoding for Zero-VRAM Drafting: enoch://control-plane/projects/suffix-array-speculative-decoding-for-zero-vram-drafting-ecdf3e2731f0/runs/suffix-array-speculative-decoding-for-zero-vram-drafting-ecdf3e2731f0-20260531T204900866624+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/435fc4b4d6a3

## What looked useful

On 500 held-out local-doc prompts, hybrid suffix+small drafts improved accepted-token rate from 0.2448 to 0.4295 (+75.5% relative) and idealized speedup from 2.956x to 4.228x (+43.0% relative). Suffix-only drafts reached 0.7800 acceptance and 6.604x idealized speedup. Synthetic repeated-pattern data showed the same direction but smaller hybrid lift because the bigram baseline was already strong.

## Boundaries and scale limits

The test used n-gram LMs, local documentation and synthetic corpora, greedy continuations, and idealized target-call counts. It did not measure transformer logits, KV-cache behavior, retrieval overhead in a serving system, wall-clock tokens/sec, or standard benchmark robustness.

## Claim scope

In a controlled word-level n-gram speculative-decoding test on held-out local documentation text, suffix retrieval drafts improved target-model draft acceptance and idealized target-call efficiency over a small bigram draft LM.

## Why it stopped

No-paper closure: the Tier 1 direct mechanism test supports the idea, but evidence is n-gram and idealized rather than publication-grade neural serving validation.

## Recommended next action

Run a bounded transformer follow-up with a tiny pretrained target/draft pair or GPT-2-small-class target, measuring exact speculative acceptance and wall-clock tokens/sec after retrieval overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer Speculative Decoding With Suffix Retrieval Drafts
- Success threshold: Hybrid suffix+small drafts improve accepted-token rate by >=20% relative and wall-clock tokens/sec by >=10% over small-LM-only speculative decoding on the bounded neural setup.
- Stop condition: Stop if retrieval overhead erases wall-clock gain or accepted-token lift is <10% relative on two prompt subsets.

## Evidence references

- Artifact root: `<local-path>/projects/direct-small-lm-speculative-decoding-with-suffix-retrieval-32ba99342c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
