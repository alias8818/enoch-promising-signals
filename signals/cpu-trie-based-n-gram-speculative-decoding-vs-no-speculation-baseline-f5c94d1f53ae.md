# CPU trie-based n-gram speculative decoding vs no-speculation baseline

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-trie-based-n-gram-speculative-decoding-vs-no-speculation-baseline-f5c94d1f53ae`
Run ID: `cpu-trie-based-n-gram-speculative-decoding-vs-no-speculation-baseline-f5c94d1f53ae-20260628T014056049051+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/4cc4cbe143ac

## What looked useful

Mechanism appears workload-sensitive but useful under local repetition: best target-call reductions were 87.67% on repetitive protocol logs, 90.155% on code-like text, and 88.83% on prose-like text; random bytes had 0.0% reduction and a slight modeled slowdown.

## Boundaries and scale limits

No real transformer target model, no real batched verification kernel, no production serving loop, 80k train tokens and 20k held-out tokens per run, synthetic/local corpora only.

## Claim scope

Trace-driven byte-level proxy on four deterministic corpora shows trie n-gram speculation can reduce modeled target decode calls by about 88-90% on repetitive/code/prose-like streams, while providing no benefit on random streams.

## Why it stopped

Proxy-only evidence supports the mechanism under repetition but is insufficient for a paper or full validation; random-stream failure limits any broad claim.

## Recommended next action

Stop this run as no-paper useful-signal evidence; next run should integrate the drafter with a tiny real CPU language-model verifier and report real tokens/sec plus acceptance.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU target-model verification for trie n-gram speculative decoding
- Success threshold: At least 1.5x end-to-end tokens/sec improvement on repetitive/code-like workloads with identical decoded output under deterministic settings and no more than 10% slowdown on non-repetitive controls.
- Stop condition: Stop if real verifier integration shows less than 1.1x speedup on repetitive/code-like workloads or if trie overhead causes more than 10% slowdown on controls.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-trie-based-n-gram-speculative-decoding-vs-no-speculation-baseline-f5c94d1f53ae`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
