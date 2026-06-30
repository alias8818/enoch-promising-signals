# N-Gram Draft Model from Pretraining Data for Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-draft-model-from-pretraining-data-for-speculative-decoding-b5a9304ecb0b`
Run ID: `n-gram-draft-model-from-pretraining-data-for-speculative-decoding-b5a9304ecb0b-20260607T160509522694+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/74bd16827ba8

## What looked useful

Bigram drafts improved target-greedy match from 7.96-8.60% for unigram to 14.47-18.37% over all held-out positions, but online 4-token draft simulation accepted zero tokens in most contexts and accepted full drafts only 0-1.04% of the time.

## Boundaries and scale limits

Completed evidence is limited to 20k/50k train-token n-gram tables, 1,023/2,047 held-out target positions, and 32/96 online 4-token draft simulations. It does not measure production speculative decoding throughput, 7B+ targets, pretraining-scale corpora, KV-cache behavior, or compressed table lookup overhead. Larger local runs were terminated before metrics were written.

## Claim scope

On Wikitext-2 with distilgpt2, exact corpus-trained n-gram draft tables partially predict the target model's greedy next token, with bigrams outperforming a unigram baseline, but naive exact n-gram drafting has low multi-token speculative acceptance.

## Why it stopped

Completed smoke and confirmation runs provide a proxy/early falsification of the naive exact corpus n-gram draft model as a practical speculative decoder, not a full validation of all n-gram variants.

## Recommended next action

Stop this naive exact n-gram run as no-paper useful evidence; next, run a bounded backoff/interpolated corpus n-gram plus prompt-local baseline and require materially higher accepted tokens per cycle before considering scale-out.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Backoff and Prompt-Local N-Gram Drafts for Speculative Decoding
- Success threshold: Mean accepted tokens per 4-token draft cycle is at least 0.75 and at least-one-token acceptance is at least 45% on held-out contexts, with no worse than 95% coverage after backoff.
- Stop condition: Stop as negative if the best backoff or prompt-local variant remains below 0.5 mean accepted tokens per 4-token draft cycle or below 30% at-least-one-token acceptance on the completed held-out run.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-draft-model-from-pretraining-data-for-speculative-decoding-b5a9304ecb0b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
