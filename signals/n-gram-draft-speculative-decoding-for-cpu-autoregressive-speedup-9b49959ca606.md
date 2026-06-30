# N-gram draft speculative decoding for CPU autoregressive speedup

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `n-gram-draft-speculative-decoding-for-cpu-autoregressive-speedup-9b49959ca606`
Run ID: `n-gram-draft-speculative-decoding-for-cpu-autoregressive-speedup-9b49959ca606-20260525T155941043016+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/a571a18fae2a

## What looked useful

Exact n-gram drafting had a poor precision/coverage tradeoff: short n-grams drafted often but were mostly wrong, long n-grams were more precise but almost never fired, and measured CPU verifier cost erased the small ideal iteration reduction.

## Boundaries and scale limits

This run did not use a real LLM, real BPE tokenizer, llama.cpp prompt-lookup implementation, or production serving traces. It tests exact n-gram trace acceptance plus a small CPU verifier-cost proxy only.

## Claim scope

On a dependency-free CPU proxy using tiny Shakespeare word/punctuation tokens, static and online-history exact n-gram draft policies did not produce autoregressive decoding speedup; best measured cost-model result was 0.9996x and the best idealized verifier-call ceiling was only 1.0784x.

## Why it stopped

Proxy/early falsification rather than full validation: the tested n-gram draft policies lacked enough accepted-token headroom on this trace, and the measured CPU verifier proxy did not provide batch-cost savings.

## Recommended next action

Stop this proxy line as no-paper evidence; if continuing, run a bounded llama.cpp prompt-lookup speculative decoding test on a small CPU model and a deliberately repetitive workload to obtain direct model evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct llama.cpp prompt-lookup speculative decoding on repetitive CPU workloads
- Success threshold: At least 1.15x wall-clock tokens/sec improvement on a high-repetition workload with no regression below 0.98x on natural prose, measured over three repeated CPU runs.
- Stop condition: Stop if accepted tokens per generated token remain below 0.15 or wall-clock speedup remains below 1.05x for all tested draft lengths.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-draft-speculative-decoding-for-cpu-autoregressive-speedup-9b49959ca606`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
