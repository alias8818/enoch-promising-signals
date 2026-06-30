# Tokenizer BPE-Merge Speculative Drafting

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `tokenizer-bpe-merge-speculative-drafting-4e590c7345e2`
Run ID: `tokenizer-bpe-merge-speculative-drafting-4e590c7345e2-20260529T120510868232+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ba560ee0641d

## What looked useful

Adjacent tokens in an already-BPE-tokenized stream were mergeable into a single GPT-2 vocab token only 2.398% of the time, matching the merge-rank drafter hit rate. The merge table mostly proposes continuations that tokenization would already have absorbed into the previous token.

## Boundaries and scale limits

Single corpus, GPT-2 tokenizer, CPU-only proxy next-token hit-rate evaluation. This did not measure full model-verifier speculative decoding throughput, other tokenizers, other corpora, or learned hybrid drafters.

## Claim scope

For GPT-2 BPE on Tiny Shakespeare, using tokenizer merge-rank continuations alone as next-token speculative draft candidates is not useful: it reached only 2.4% hit@64, far below unigram and bigram frequency baselines.

## Why it stopped

Proxy early falsification: the tested tokenizer-only merge-rank drafter underperformed trivial baselines by a wide margin, and the adjacent-token mergeability diagnostic explains the failure mechanism. This is not a full speculative-decoding validation.

## Recommended next action

Stop this tokenizer-only merge-rank drafting path; any future work should test a different BPE-derived signal or a learned drafter against unigram/bigram baselines in a real speculative decoder.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/tokenizer-bpe-merge-speculative-drafting-4e590c7345e2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
