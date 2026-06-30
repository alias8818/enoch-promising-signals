# N-Gram Speculative Decoding with Suffix Verification

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-decoding-with-suffix-verification-82652a9f883c`
Run ID: `n-gram-speculative-decoding-with-suffix-verification-82652a9f883c-20260522T183014511068+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2912fd585656

## What looked useful

Exact suffix verification made n-gram speculative decoding lossless in all tested cases. Target-call reduction was 0.0% on random IID synthetic traces, 63.2% on copied blocks with 5% mutation, 96.9% on periodic copy, and up to 90.6% on repeated distilgpt2 prompts.

## Boundaries and scale limits

Synthetic oracle traces plus sshleifer/tiny-gpt2 and distilgpt2 only; no 7B+ model, no production KV-cache serving engine, no natural trace corpus, no batching or sampling evaluation.

## Claim scope

In local synthetic traces and small GPT-2-family greedy decoding checks, n-gram suffix drafting with exact target verification preserves greedy output and reduces target calls when continuations repeat; it provides no benefit on random IID traces.

## Why it stopped

Current run produced a useful bounded mechanism signal but not publication-grade evidence; direct evidence is limited to synthetic traces and small GPT-2-family models.

## Recommended next action

Run a bounded deepen follow-up on real greedy decoding traces from a stronger model or existing inference logs, comparing suffix n-gram drafting against prompt lookup and standard speculative baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-Based N-Gram Suffix Speculation on Real LLM Outputs
- Success threshold: At least 25% mean target-call reduction on copy/code/long-context subsets, zero output mismatches, and no worse than 5% overhead on non-repetitive subsets.
- Stop condition: Stop if real traces show less than 10% mean target-call reduction on the intended copy-heavy subsets or any verified-output mismatch.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-decoding-with-suffix-verification-82652a9f883c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
