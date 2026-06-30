# Suffix-Array Drafting for CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-array-drafting-for-cpu-inference-3bf47d98c944`
Run ID: `suffix-array-drafting-for-cpu-inference-3bf47d98c944-20260524T220546002860+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e971ea2dbc86

## What looked useful

Variable-length repeat-copy drafting produced nontrivial exact continuation proposals, reaching 0.4924 top-1 accuracy and 1.1238 accepted bytes/query. Suffix arrays did not improve that signal over occurrence-matched hash backoff and had about 6x higher mean lookup latency.

## Boundaries and scale limits

Byte-token corpus only; exact future-token proxy only; no neural target-model speculative acceptance; no BPE tokenizer; no C/C++ optimized suffix-array or compressed-index implementation; no live CPU LLM runtime integration.

## Claim scope

On Tiny Shakespeare byte-token exact-continuation drafting with 180k train tokens and 5k held-out query positions, suffix-array variable-context drafting matches hash-backoff accepted-token signal but is slower in this Python CPU prototype.

## Why it stopped

Proxy/local evidence supports repeat-copy drafting but early-falsifies suffix arrays as a superior CPU drafting novelty versus a simpler hash-backoff baseline; this is not a full LLM validation.

## Recommended next action

Stop this project as no-paper useful signal; any next test should use BPE-tokenized inference traces and compare an optimized suffix-array-family index against occurrence-matched hash backoff on actual speculative acceptance and memory.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: BPE trace speculative acceptance for repeat-copy drafting indexes
- Success threshold: Suffix-array-family index must improve accepted tokens per second by at least 10% or reduce index memory by at least 2x at statistically indistinguishable acceptance versus hash backoff.
- Stop condition: Stop if suffix-array-family indexing matches hash-backoff acceptance but is slower and not at least 2x smaller in memory on BPE traces.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-drafting-for-cpu-inference-3bf47d98c944`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
