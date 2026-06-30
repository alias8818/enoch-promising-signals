# N-Gram Suffix Cache Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-suffix-cache-speculative-decoding-on-cpu-69c3a809a5de`
Run ID: `n-gram-suffix-cache-speculative-decoding-on-cpu-69c3a809a5de-20260528T204930436478+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9412444b7082

## What looked useful

The mechanism is domain-sensitive. Repeated contract-like synthetic text reached 80.0% target-call reduction and 1.84x modeled speedup at draft-token cost 0.25, while synthetic logs were marginal at 1.06x, Python stdlib was 0.90x, Alice was 0.80x, and Tiny Shakespeare was 0.80x. Longer drafts improved call reduction but often worsened modeled speedup due to rejected draft work.

## Boundaries and scale limits

Tested with regex-tokenized traces up to 120k tokens per corpus, five corpora including two synthetic repetitive corpora, and a Python simulator. No real transformer verifier, BPE tokenizer, or production CPU backend was measured.

## Claim scope

Leak-free trace simulation shows that an n-gram suffix cache can reduce target-model calls on highly repetitive generated streams, but it does not support a broad CPU speculative-decoding speedup claim across prose and code-like traces under a conservative verifier-cost model.

## Why it stopped

Trace-only evidence is mixed and does not validate real CPU wall-clock speedup; this is an early bounded proxy result rather than full validation.

## Recommended next action

Stop this run as no-paper useful signal; the concrete next action is a bounded direct CPU verifier experiment in llama.cpp or an equivalent backend, requiring at least 15% wall-clock tok/s improvement over greedy decoding on two non-synthetic repetitive structured corpora.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU verifier test for suffix-cache drafts on repetitive structured outputs
- Success threshold: At least 15% wall-clock tok/s improvement over greedy decoding on two non-synthetic structured repetitive corpora, with no more than 5% slowdown on a generic prose control.
- Stop condition: Stop if the integrated verifier shows less than 5% wall-clock speedup on the first structured corpus or more than 10% slowdown on the prose control after 1000 generated tokens per condition.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-cache-speculative-decoding-on-cpu-69c3a809a5de`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
