# N-Gram Speculative Decoding on CPU with Block Verification

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-decoding-on-cpu-with-block-verification-daaef003cb09`
Run ID: `n-gram-speculative-decoding-on-cpu-with-block-verification-daaef003cb09-20260607T103749414004+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/536a305805e4

## What looked useful

Block verification is mechanically sound and can cut target calls substantially, but for cheap CPU targets its overhead dominates. A derived break-even analysis found the best case needs roughly 7.39 microseconds of additional per-call target cost before speculative verification breaks even under a simple overhead model.

## Boundaries and scale limits

Single-process Python mechanism benchmark only; no transformer logits, KV-cache behavior, native implementation, stochastic sampling, real LLM serving, or production-scale CPU deployment was tested.

## Claim scope

On a local CPU word-level n-gram target over a 415k-word public-domain corpus, greedy n-gram speculative decoding with block verification exactly matched target-greedy output and reduced target invocations by up to 5.62x, but did not improve wall-clock speed in the cheap Python n-gram target; the best measured variant ran at 0.295x baseline speed.

## Why it stopped

No-paper useful signal: the mechanism was supported, but the local benchmark is a proxy and the measured Python n-gram implementation was slower than sequential decoding, so this is not direct publication-grade evidence.

## Recommended next action

Run a bounded native CPU follow-up using a small transformer or llama.cpp-class model to test whether real target-call cost and block verification produce end-to-end tokens/s improvement.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Native CPU Transformer Block Verification Benchmark
- Success threshold: At least 1.2x median end-to-end tokens/s improvement over sequential greedy decoding with exact output match on at least 10,000 generated tokens and no more than 10% extra memory.
- Stop condition: Stop if exactness fails, acceptance is too low to reduce target calls by 1.5x, or measured tokens/s remains below 1.0x baseline after testing at least three block sizes.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-decoding-on-cpu-with-block-verification-daaef003cb09`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
