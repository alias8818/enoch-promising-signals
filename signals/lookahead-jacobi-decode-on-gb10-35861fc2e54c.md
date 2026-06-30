# Lookahead Jacobi Decode on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `lookahead-jacobi-decode-on-gb10-35861fc2e54c`
Run ID: `lookahead-jacobi-decode-on-gb10-35861fc2e54c-20260614T055759614148+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/915e27ae2b3e

## What looked useful

Verified multi-token accepts are real in this bounded probe, but naive un-fused Jacobi/lookahead decoding spends 3.43x-4.71x as many model forwards as greedy KV and averaged only 0.41x-0.49x greedy throughput on distilgpt2. The path worth testing next is fused/batched verification, not separate full-forward Python loops.

## Boundaries and scale limits

Direct tests used distilgpt2, 4 prompts, 24 generated tokens, greedy decoding, and a research Python harness. Production fused lookahead, FlashAttention-compatible packing, long contexts, sampled decoding, and 1B+/7B+ bandwidth-bound models were not tested.

## Claim scope

On GB10 with distilgpt2, a naive same-model Jacobi n-gram pool can preserve exact greedy outputs and reduce decoding iterations by 2.25x-3.0x, but separate full-forward lookahead and verification calls make it slower than KV-cache greedy on normal prompts.

## Why it stopped

Bounded direct probe found a useful mechanism signal but a negative performance result for the naive implementation; this is not full validation of production lookahead decoding.

## Recommended next action

Stop this run as no-paper useful evidence; next implement a packed single-forward lookahead/verification prototype and require exact greedy match plus >1.2x tokens/s on non-degenerate prompts before scaling.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Packed single-forward lookahead verification on a small causal LM
- Success threshold: >=1.2x mean tokens/s versus greedy KV with exact greedy-match on all prompts and no result driven solely by repeated whitespace or repeated-token continuations.
- Stop condition: Stop if packed/fused verification still averages <1.0x greedy KV throughput or exactness fails on any prompt.

## Evidence references

- Artifact root: `<local-path>/projects/lookahead-jacobi-decode-on-gb10-35861fc2e54c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
