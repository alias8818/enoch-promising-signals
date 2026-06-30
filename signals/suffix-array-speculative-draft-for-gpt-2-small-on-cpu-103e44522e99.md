# Suffix-Array Speculative Draft for GPT-2-Small on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-array-speculative-draft-for-gpt-2-small-on-cpu-103e44522e99`
Run ID: `suffix-array-speculative-draft-for-gpt-2-small-on-cpu-103e44522e99-20260608T052412918659+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/bb579c688b03

## What looked useful

The suffix-array draft is very cheap on CPU and reaches about 18% exact single-token agreement with GPT-2-small greedy tokens, but most drafts use 1-token or 2-token contexts, so the evidence supports only a weak lexical/backoff mechanism rather than a strong long-context suffix-array drafting method.

## Boundaries and scale limits

No integrated speculative decoder, no KV-cache end-to-end timing, no multi-token verify loop, Wikitext-2 only, 69k-token suffix array, 256 generated target steps.

## Claim scope

Bounded CPU proxy benchmark for a GPT-2-tokenized suffix-array lexical draft against GPT-2-small greedy next-token argmax on Wikitext-2 text and 8 short generated-prefix probes.

## Why it stopped

Proxy evidence is useful but not full validation: it measures draft agreement and overhead, not end-to-end speculative decoding speedup.

## Recommended next action

Stop this run as no-paper useful signal; next implement a bounded integrated GPT-2-small CPU speculative decoder with multi-token suffix-array drafts and compare wall-clock latency against greedy generation plus unigram/bigram controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Integrated CPU Speculative Decoder for Suffix-Array GPT-2 Drafts
- Success threshold: At least 1.10x median wall-clock tokens/s over greedy GPT-2-small CPU generation across at least 512 generated tokens, with suffix-array draft outperforming unigram and bigram controls.
- Stop condition: Stop if integrated speculative decoding is slower than greedy generation or if acceptance remains below the measured overhead break-even after controls.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-speculative-draft-for-gpt-2-small-on-cpu-103e44522e99`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
