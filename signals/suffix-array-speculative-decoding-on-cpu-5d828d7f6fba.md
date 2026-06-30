# Suffix-Array Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-array-speculative-decoding-on-cpu-5d828d7f6fba`
Run ID: `suffix-array-speculative-decoding-on-cpu-5d828d7f6fba-20260524T163950037221+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/04976dd3018e

## What looked useful

Suffix-array copying works strongly on deliberately repetitive text, but natural-language and code token probes averaged only 0.410 and 0.444 accepted draft tokens per 4-token proposal, with small gains over a much faster n-gram baseline.

## Boundaries and scale limits

No target LM was run; regex tokens are only a tokenizer proxy; corpora were small/medium local slices; suffix-array implementation was pure Python rather than optimized C/Rust.

## Claim scope

Bounded CPU proxy test of suffix-array draft generation on 120k-byte repetitive, natural-language, and local Python-source corpora using exact held-out byte and regex-token continuation matches.

## Why it stopped

Proxy evidence did not show enough natural/code token acceptance to justify a paper claim; this is not a full validation because no target LM speculative verifier was run.

## Recommended next action

Stop this run as an early proxy negative; only deepen with a tokenizer-aligned real-LM code-completion serving test if the next worker can measure end-to-end accepted tokens and CPU decode speedup.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tokenizer-aligned real-LM suffix-array drafting for CPU code completion
- Success threshold: Suffix-array drafting averages >=1.5 accepted target tokens per proposal and improves end-to-end CPU tokens/s by >=10% over both greedy decoding and the n-gram draft baseline on the same code prompts.
- Stop condition: Stop if accepted target tokens remain below 1.0 per proposal or end-to-end tokens/s does not beat the n-gram baseline after tokenizer-aligned implementation.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-speculative-decoding-on-cpu-5d828d7f6fba`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
