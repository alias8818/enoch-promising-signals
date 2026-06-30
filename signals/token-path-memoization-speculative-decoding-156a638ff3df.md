# Token-Path Memoization Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `token-path-memoization-speculative-decoding-156a638ff3df`
Run ID: `token-path-memoization-speculative-decoding-156a638ff3df-20260527T042913041689+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/48a9fd9eca41

## What looked useful

Exact path memoization gives very large target-call reductions on repeated templated traces, moderate reductions on character-level natural text, and negligible reductions on natural word/punctuation tokens. The shuffled controls show gains require real repeated path structure rather than token frequency alone.

## Boundaries and scale limits

No transformer runtime, BPE tokenizer, live serving traces, KV-cache overhead, batching, stochastic sampling, or end-to-end latency was measured. Results should not be treated as full speculative-decoding validation.

## Claim scope

Trace-level deterministic acceptance test for exact token-path memoization on a 300k-character Tiny Shakespeare slice plus a repeated-template synthetic corpus, using word/punctuation and character tokenizations.

## Why it stopped

Closed as a no-paper useful signal: this was a trace-level proxy and early falsification of broad exact-path memoization usefulness on natural word-level text, not a full serving validation.

## Recommended next action

Run a bounded deepen test with BPE tokenization and actual small-transformer speculative verification, including cache lookup/memory overhead and a no-memo baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: BPE Small-Model Token-Path Memoization Speculative Decoding
- Success threshold: At least 10% end-to-end tokens/sec improvement over the best local baseline on a request-like repeated corpus, with less than 3% regression on natural text and measured cache overhead below the saved verification time.
- Stop condition: Stop if BPE exact-path acceptance gives less than 5% target-call reduction on repeated/request-like traces or if cache overhead eliminates throughput gains in the small-model benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/token-path-memoization-speculative-decoding-156a638ff3df`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
