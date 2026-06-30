# N-gram Suffix Array Drafting for CPU Speculative Decoding

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `n-gram-suffix-array-drafting-for-cpu-speculative-decoding-c9aee35364d5`
Run ID: `n-gram-suffix-array-drafting-for-cpu-speculative-decoding-c9aee35364d5-20260604T111702261967+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4f69b55a54be

## What looked useful

Suffix-array n-gram drafting is not favored as a CPU speculative decoding primitive in this bounded proxy: word/punctuation 8-token and 16-token contexts had 0 accepted draft tokens across 5000 queries, while byte-level gains reflected sub-token repetition and still made suffix-array lookup 3.19x to 1267.59x slower than hashing for identical draft quality.

## Boundaries and scale limits

Single 1.1 MB public corpus, simple tokenizers, offline held-out exact-match proxy, Python prototype, no live transformer verifier, no production BPE tokenizer, and no end-to-end speculative decoding latency measurement.

## Claim scope

On Tiny Shakespeare held-out continuation retrieval with regex word/punctuation and byte tokens, a prefix-sorted suffix-array-style n-gram index produced the same drafts as a hash n-gram index but had higher build time, higher memory use, and slower query latency; token-like contexts had near-zero exact draft acceptance at realistic context lengths.

## Why it stopped

Proxy early falsification: the tested suffix-array retrieval mechanism had no quality advantage over a hash n-gram baseline and was consistently slower/more memory-hungry, while the token-like exact-match signal was too sparse for useful 4-token drafts.

## Recommended next action

Stop pursuing suffix arrays as the first CPU draft index; run a bounded BPE decode-trace follow-up using hash/prompt-lookup n-gram drafting before considering any serving-scale experiment.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: BPE Prompt-Lookup N-gram Drafting on Real Decode Traces
- Success threshold: Hash n-gram lookup achieves at least 0.5 accepted BPE tokens per verifier step, at least 20% nonzero draft acceptance, and less than 10 microseconds mean CPU lookup latency without worse memory than suffix-array lookup.
- Stop condition: Stop if BPE exact-match acceptance is below 0.2 accepted tokens per verifier step or lookup overhead exceeds the estimated verifier-step savings on the bounded trace.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-array-drafting-for-cpu-speculative-decoding-c9aee35364d5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
