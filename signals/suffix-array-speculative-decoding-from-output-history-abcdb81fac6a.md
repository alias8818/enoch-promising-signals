# Suffix-Array Speculative Decoding from Output History

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-array-speculative-decoding-from-output-history-abcdb81fac6a`
Run ID: `suffix-array-speculative-decoding-from-output-history-abcdb81fac6a-20260527T131851587807+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/6b0b50c36b43

## What looked useful

The mechanism exists but is weak as a standalone method: default min-context 4, draft length 8 gave 1.044x natural-text proxy speedup versus 1.035x block-shuffle and 1.00003x token-shuffle. The best swept setting, min-context 2 and draft length 16, reached 1.153x natural but block-shuffle still reached 1.129x and token-shuffle triggered often, indicating reliance on short common phrases.

## Boundaries and scale limits

This was a CPU-only corpus replay proxy over word tokens, not a live LLM speculative decoding benchmark. It did not measure tokenizer effects, model probability acceptance, GPU scheduling, KV-cache overhead, batching, or wall-clock serving throughput.

## Claim scope

On four public-domain book corpora under oracle replay, online output-history suffix drafting produces reproducible exact-token acceptance above token-shuffle controls, but only small idealized verifier-call gains and modest improvement over 64-token block-shuffle controls.

## Why it stopped

Proxy evidence supports a detectable recurrence mechanism but early-falsifies the stronger standalone decoding claim: gains are small, much of the signal survives block shuffling, and no live model throughput evidence was produced.

## Recommended next action

Stop this run as a no-paper proxy result; only continue with a bounded live LLM serving test if integrating the heuristic is cheap enough to measure real wall-clock overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live Small-LLM Output-History Drafting Benchmark
- Success threshold: At least 5% end-to-end tokens/sec improvement on repetition-heavy prompts and no more than 1% slowdown on normal prompts, with acceptance attributable to contexts of length at least 4.
- Stop condition: Stop if lookup plus verification overhead erases the proxy gain, if accepted tokens per verifier call stays below 1.03 on live outputs, or if gains only appear for contexts shorter than 4 tokens.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-speculative-decoding-from-output-history-abcdb81fac6a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
