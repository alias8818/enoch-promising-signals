# Corpus-Controlled CPU Benchmark for Exact Context-Ngram Drafting

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `corpus-controlled-cpu-benchmark-for-exact-context-ngram-dr-7ad07139c5`
Run ID: `corpus-controlled-cpu-benchmark-for-exact-context-ngram-dr-7ad07139c5-20260523T202643256512+0000`

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

- Parent run decision: Context-Ngram Speculative Decoding CPU: enoch://control-plane/projects/context-ngram-speculative-decoding-cpu-a6de05d8db60/runs/context-ngram-speculative-decoding-cpu-a6de05d8db60-20260523T144434496393+0000
- Parent run decision: Real CPU Decoder Validation for Context-Ngram Drafting: enoch://control-plane/projects/real-cpu-decoder-validation-for-context-ngram-drafting-7d61778323/runs/real-cpu-decoder-validation-for-context-ngram-drafting-7d61778323-20260523T201641060729+0000

## What looked useful

Exact context n-gram drafting strongly beat prefix bigram on the repeated controlled corpus and collapsed under shuffled-prefix control, supporting the ordered-repetition mechanism. On real WikiText-2, however, prefix bigram beat the best exact n-gram setting, so the broad practical superiority claim is not supported.

## Boundaries and scale limits

This is not a real target-LM speculative-decoding benchmark. It measures held-out corpus continuation matches with 512-token prefixes, 16-token drafts, 800 sampled positions per corpus/seed, and three seeds. The exact n-gram implementation is simple Python and not an optimized serving implementation.

## Claim scope

Fixed-seed CPU corpus-continuation benchmark with prefix-only exact context n-gram drafting on WikiText-2 validation text, a repeated-chunk controlled corpus, and a shuffled-prefix control.

## Why it stopped

Tier 2 evidence is mixed: exact n-gram mechanism is supported on repetition-heavy controlled data, but it fails to beat the real prefix-bigram baseline on WikiText-2, so the claim is not paper-ready.

## Recommended next action

Stop this run as no-paper useful signal; if continuing, run a bounded real-verifier GPT-2-small CPU benchmark on the same contexts with repetition-stratified analysis.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Verifier CPU Benchmark for Repetition-Gated Exact Context Drafting
- Success threshold: On high-repetition strata, hybrid or gated exact-context drafting must improve accepted tokens per CPU second by at least 15% over prefix_bigram without degrading low-repetition strata by more than 5%.
- Stop condition: Stop if the real-verifier benchmark shows no accepted-token or latency advantage over prefix_bigram on the high-repetition stratum, or if gating overhead erases the measured draft benefit.

## Evidence references

- Artifact root: `<local-path>/projects/corpus-controlled-cpu-benchmark-for-exact-context-ngram-dr-7ad07139c5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
