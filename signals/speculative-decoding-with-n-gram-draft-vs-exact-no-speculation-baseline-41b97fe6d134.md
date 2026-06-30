# Speculative Decoding with N-Gram Draft vs Exact No-Speculation Baseline

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-decoding-with-n-gram-draft-vs-exact-no-speculation-baseline-41b97fe6d134`
Run ID: `speculative-decoding-with-n-gram-draft-vs-exact-no-speculation-baseline-41b97fe6d134-20260630T073701921277+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/745fc4966091

## What looked useful

N-gram drafting can create a real batching opportunity: gamma=4 achieved 0.334 target batches/token and 2.99x ideal target-forward batch speedup with 0.753 acceptance, but wall time was 0.36x baseline because the toy target was already cheap and speculation added Python overhead.

## Boundaries and scale limits

This was a CPU-only n-gram proxy, not a real Transformer serving benchmark. It does not measure KV-cache behavior, GPU kernel efficiency, tokenizer-level drafting, or production batch scheduling. Main run emitted 20,480 tokens per method.

## Claim scope

Exact word-level n-gram target language model on public text: lower-order n-gram draft speculative decoding reduced target forward batches per emitted token from 1.0 to 0.25-0.57 across gamma 1-12 while preserving exact accept/reject correction.

## Why it stopped

Proxy result supports the mechanism but is not direct/full validation; paper-level evidence would require a real Transformer exact no-speculation baseline versus n-gram speculative decoding on the same hardware.

## Recommended next action

Stop this CPU proxy as no-paper useful signal; run a separate cache-aware small Transformer benchmark before making any serving-speed claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cache-aware Transformer benchmark for n-gram speculative decoding
- Success threshold: At least 1.2x wall-clock tokens/s improvement over cache-aware no-speculation baseline with no distribution sanity regression and at least 10,000 emitted tokens.
- Stop condition: Stop if gamma/draft-order sweeps fail to exceed 1.0x wall-clock speedup or if acceptance stays below 0.4 after reasonable n-gram smoothing/tokenization choices.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-with-n-gram-draft-vs-exact-no-speculation-baseline-41b97fe6d134`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
