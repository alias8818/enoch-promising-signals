# Tiny-Draft Speculative Decoding with N-Gram Suffix Baseline

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiny-draft-speculative-decoding-with-n-gram-suffix-baseline-863953f7a292`
Run ID: `tiny-draft-speculative-decoding-with-n-gram-suffix-baseline-863953f7a292-20260619T215857384208+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/690b94d997f1

## What looked useful

Tiny draft speculation is not a broad replacement for n-gram/suffix lookup. It may be worth testing only for workloads with stable templated continuations where training history matches deployment format.

## Boundaries and scale limits

No real LLM verifier, no GPU latency measurement, no batching/KV-cache/tree-attention effects, no optimized suffix automaton, and only one small public prose corpus plus two synthetic repetitive controls.

## Claim scope

In a CPU-only known-target-stream exact-prefix simulation, a tiny count-based n-gram draft beats suffix lookup on templated repetitive logs, ties it on copy-like repetition, and does not improve heldout prose.

## Why it stopped

No-paper useful signal: this was a proxy proposer-quality probe with mixed results, not full speculative-decoding validation.

## Recommended next action

Run a bounded direct GPT-2-small verifier experiment with an optimized suffix/trie baseline on real high-overlap summarization or code-edit prompts; stop if tiny draft fails to improve end-to-end latency by at least 15% on two tasks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Small-Model Verifier Test for Tiny N-Gram Draft vs Optimized Suffix Lookup
- Success threshold: Tiny draft achieves at least 15% lower end-to-end latency than optimized suffix lookup on two real high-overlap task families with no output-quality regression.
- Stop condition: Stop if tiny draft is within 5% of suffix lookup latency or worse on the first two real task families, or if proposer overhead erases verifier-call savings.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-draft-speculative-decoding-with-n-gram-suffix-baseline-863953f7a292`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
