# N-Gram Suffix Speculation for CPU Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-suffix-speculation-for-cpu-decoding-b1fda7a496c1`
Run ID: `n-gram-suffix-speculation-for-cpu-decoding-b1fda7a496c1-20260525T141801033079+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/aea5c8197654

## What looked useful

Most-recent n-gram suffixes produced 1.43x to 1.64x simulated call reduction on byte traces, but only 1.02x to 1.07x on word/punctuation traces; tokenizer/workload granularity is the likely gating factor.

## Boundaries and scale limits

No real LLM tokenizer, no target-model logits, no llama.cpp or CPU inference integration, no end-to-end latency, no KV-cache/kernel overhead measurement, and only two public text corpora.

## Claim scope

Leakage-free trace simulation on Tiny Shakespeare and WikiText-2 raw, up to 250000 tokens per corpus/tokenization, shows n-gram suffix speculation can reduce conservative verifier-call counts on fine-grained byte tokens but provides only small gains on coarse word/punctuation tokens.

## Why it stopped

This run is a proxy trace simulation that supports the mechanism but does not validate real CPU decoding speed or broad workload utility.

## Recommended next action

Run a bounded direct follow-up inside a CPU LLM runtime with an actual BPE/SentencePiece tokenizer before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU Runtime Test of N-Gram Suffix Speculation
- Success threshold: At least 1.15x end-to-end tokens/sec on repetition-heavy prompts, no more than 3% slowdown on normal prompts, and n-gram overhead below 10% of saved verifier time.
- Stop condition: Stop if actual-tokenizer acceptance yields less than 1.05x verifier-call reduction or runtime overhead erases the simulated savings.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-speculation-for-cpu-decoding-b1fda7a496c1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
