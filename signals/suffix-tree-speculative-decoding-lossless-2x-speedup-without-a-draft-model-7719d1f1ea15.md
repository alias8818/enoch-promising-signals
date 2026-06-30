# Suffix-Tree Speculative Decoding: Lossless 2x Speedup Without a Draft Model

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-speculative-decoding-lossless-2x-speedup-without-a-draft-model-7719d1f1ea15`
Run ID: `suffix-tree-speculative-decoding-lossless-2x-speedup-without-a-draft-model-7719d1f1ea15-20260621T012133575490+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/57393c8e9a2b

## What looked useful

Lossless suffix-history proposals are mechanically viable for greedy decoding and produced 1.94x forward-call speedup on tiny-gpt2 64-token runs and 3.25x mean speedup on distilgpt2 64-token runs, with exact output equality. The broad 2x speedup claim is not paper-ready because evidence is small-scale and serving latency is only proxied.

## Boundaries and scale limits

Small local prompt suite, small GPT-2-class models, deterministic greedy only, full-context harness rather than production KV-cache serving, no sampling, no large-model or broad-corpus validation.

## Claim scope

Bounded greedy-decoding probe: suffix-history proposals verified by the target model preserved exact greedy outputs and reduced target forward calls on tiny GPT-2 and distilgpt2 small prompt suites.

## Why it stopped

The run produced a proxy/early bounded validation of the mechanism but not full validation of the broad lossless 2x speedup claim.

## Recommended next action

Stop this run as no-paper useful signal; next bounded step is a cached KV implementation tested on a larger prompt corpus with exact-match, tokens/sec, latency, memory, and acceptance-rate metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cached suffix-history verification for lossless greedy decoding
- Success threshold: On at least 200 prompts, exact match in 100% of greedy decodes, median tokens/sec >=1.5x overall, >=2.0x on high-repetition/template subset, and memory overhead <=20% versus cached greedy baseline.
- Stop condition: Stop if exactness fails, median tokens/sec is <1.2x overall after cache optimization, or memory overhead exceeds 20% without a clear mitigation.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculative-decoding-lossless-2x-speedup-without-a-draft-model-7719d1f1ea15`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
