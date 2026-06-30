# N-Gram Suffix Drafting for CPU Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-suffix-drafting-for-cpu-speculative-decoding-f433b36be308`
Run ID: `n-gram-suffix-drafting-for-cpu-speculative-decoding-f433b36be308-20260604T070814803184+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/8ecf6cd3b5fd

## What looked useful

Byte-token traces showed meaningful simulated target-call reduction, with a best result of 39.69% and a byte-token median of 26.36%. Word/punctuation traces were much weaker, with a 3.25% median and 14.32% best reduction, so the mechanism appears sensitive to token granularity and repetition.

## Boundaries and scale limits

No real LLM tokenizer, logits verification, KV-cache behavior, sampling, or serving latency was measured. The largest completed grid used 40k-token prefixes and two small public corpora on a single CPU worker.

## Claim scope

Online suffix n-gram drafting was tested by trace replay on two public text corpora using byte and word/punctuation tokenization, measuring simulated target verification call reduction against a one-call-per-token baseline.

## Why it stopped

Trace-only evidence is mixed and useful but not sufficient for a paper-ready CPU speculative decoding claim.

## Recommended next action

Run a bounded CPU LLM integration using a real model tokenizer and logits verifier, comparing frequency suffix drafting at n=3 and k=4/8 against no drafting and prompt-lookup drafting on tokens/sec and p95 latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CPU LLM Runtime Test for Frequency Suffix Drafting
- Success threshold: At least 10% tokens/sec improvement with no p95 latency regression over no drafting on a representative repetitive-prompt subset, and performance no worse than prompt-lookup by more than 3%.
- Stop condition: Stop if target-call reduction is below 5%, drafter overhead erases throughput gain, or p95 latency regresses by more than 5% on the bounded benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-drafting-for-cpu-speculative-decoding-f433b36be308`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
