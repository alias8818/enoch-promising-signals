# CPU Bigram Trie Draft Decode

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-bigram-trie-draft-decode-e23e6bf5f141`
Run ID: `cpu-bigram-trie-draft-decode-e23e6bf5f141-20260607T205012832731+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/7efcb0693f7e

## What looked useful

Validation/test top-1 agreement was 19.40%/18.79% versus unigram 5.20%/4.89%, top-8 hit rate was 38.40%/38.00%, and dense batched lookup exceeded 461M tokens/s. However, greedy 4-token drafts averaged only 0.270/0.260 accepted tokens and matched all four tokens only 0.682%/0.647%. Confidence >=0.7 rows covered about 8% of positions with about 65% top-1 accuracy.

## Boundaries and scale limits

This run used WikiText-2 only, GPT-2 tokenization only, teacher-forced next-token agreement as a proxy for speculative acceptance, Python/Numpy lookup microbenchmarks, and no integrated target-model decode loop or GPU verifier timing.

## Claim scope

On GPT-2-tokenized WikiText-2 with a 1M-token training budget, a CPU-resident top-k bigram table is tiny and fast and provides a persistent held-out next-token candidate signal, but naive greedy 4-token drafting has too little multi-token exact-match yield to justify a practical speculative-decoding claim.

## Why it stopped

No-paper closure: this was a proxy/early mechanism probe, and the naive greedy draft path is too weak for a practical decode-speed claim without integrated verifier evidence.

## Recommended next action

Run one bounded deepen follow-up that integrates confidence-gated CPU bigram drafting into a real small target-model speculative decode loop and accepts the idea only if end-to-end tokens/s improves versus the same model without drafting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Confidence-gated CPU bigram draft in an actual small-model speculative decode loop
- Success threshold: At least 1.05x end-to-end tokens/s improvement over the no-draft baseline on 100 or more prompts with no degradation in the controlled decoding objective, and measured CPU draft overhead below 5% of wall time.
- Stop condition: Stop as negative if all confidence thresholds fail to exceed 1.0x end-to-end tokens/s or if verifier synchronization overhead dominates the saved target-model work.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-bigram-trie-draft-decode-e23e6bf5f141`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
