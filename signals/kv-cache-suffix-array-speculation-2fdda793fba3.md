# KV-Cache Suffix-Array Speculation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-suffix-array-speculation-2fdda793fba3`
Run ID: `kv-cache-suffix-array-speculation-2fdda793fba3-20260519T200127097182+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b619b6e6d9ae

## What looked useful

Suffix-array copying produced strong acceptance on repeated code controls and nonzero streaming-cache acceptance on local/code corpora, but static-prior results were weak on less repetitive data and essentially matched by a simple n-gram continuation baseline.

## Boundaries and scale limits

No real LLM tokenizer, no transformer KV-cache integration, no GPU/serving wall-clock benchmark, no dynamic suffix-array maintenance cost, inputs limited to at most 160k bytes and 12k evaluated positions per dataset.

## Claim scope

Bounded byte-token proxy: suffix-array lookup can draft exact future bytes from repeated prior contexts on synthetic repeated code, local project artifacts, and Python stdlib prefixes, including a causal streaming-cache proxy.

## Why it stopped

No-paper proxy closure: the mechanism is useful under repetition but this run does not validate real KV-cache serving speedup or superiority over simpler baselines.

## Recommended next action

Run a bounded real-tokenizer small-transformer follow-up that measures end-to-end speculative decoding tokens/sec against dynamic n-gram/cache-copy baselines, including index update overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tokenizer-level suffix-cache speculation in a small transformer loop
- Success threshold: At least 10% end-to-end tokens/sec improvement over the best simple dynamic lookup baseline on a repeated-context dataset, with no more than 5% regression on ordinary text/code and acceptance distributions explaining the gain.
- Stop condition: Stop if suffix-index overhead erases throughput gains, if acceptance is not better than dynamic n-gram/cache-copy baselines, or if gains only appear on the synthetic positive control.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-suffix-array-speculation-2fdda793fba3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
