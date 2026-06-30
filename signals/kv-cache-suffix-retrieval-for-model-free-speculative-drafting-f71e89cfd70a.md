# KV-Cache Suffix Retrieval for Model-Free Speculative Drafting

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-suffix-retrieval-for-model-free-speculative-drafting-f71e89cfd70a`
Run ID: `kv-cache-suffix-retrieval-for-model-free-speculative-drafting-f71e89cfd70a-20260527T184043440878+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/1f0ab6a3dfc7

## What looked useful

Suffix retrieval produced 0.1738 accepted tokens/position on Shakespeare versus 0.1407 for online bigram, and 0.1492 on Austen versus 0.1632 for online bigram. Shuffled controls dropped suffix retrieval to about 0.0055 accepted tokens/position, showing the mechanism depends on real sequence order. Rare long suffix matches were high quality, but overall full-draft acceptance was low.

## Boundaries and scale limits

CPU-only proxy using exact text tokens, two valid corpora, no transformer KV vectors, no model acceptance probabilities, no latency measurement, no learned drafter comparison, and one invalid downloaded corpus excluded because it fell back to a 99-token synthetic text.

## Claim scope

On two valid public-domain word/punctuation token streams, exact prefix-visible suffix retrieval provides a real order-sensitive drafting signal and sometimes exceeds a simple online bigram next-token baseline, but it is corpus-dependent and not validated in a transformer serving loop.

## Why it stopped

Proxy evidence is useful but mixed: the method has a real repetition signal, yet it does not consistently beat a cheap online bigram baseline and lacks direct model-serving validation.

## Recommended next action

Run a bounded follow-up that gates suffix retrieval to long or high-confidence matches inside a small real transformer speculative decoding loop and compares accepted tokens per verification pass plus latency against no drafter and online n-gram baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Gated suffix retrieval in a small transformer speculative decoding loop
- Success threshold: Gated suffix retrieval improves accepted tokens per target verification pass by at least 20% over online n-gram drafting and reduces median decode latency by at least 10% versus no drafter on the tested local model without increasing memory by more than 10%.
- Stop condition: Stop if gated suffix retrieval fails to beat online n-gram drafting on accepted tokens per verification pass or if retrieval overhead erases measured latency gains on the small target model.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-suffix-retrieval-for-model-free-speculative-drafting-f71e89cfd70a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
