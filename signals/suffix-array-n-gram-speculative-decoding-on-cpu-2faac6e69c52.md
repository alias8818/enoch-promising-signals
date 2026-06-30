# Suffix-Array N-Gram Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-array-n-gram-speculative-decoding-on-cpu-2faac6e69c52`
Run ID: `suffix-array-n-gram-speculative-decoding-on-cpu-2faac6e69c52-20260604T145134445848+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/7c5b6c075e7f

## What looked useful

Suffix arrays are compact, about 7.5-12% of the estimated hash n-gram index size, and can be lookup-competitive at larger sparse real-text contexts, but exact continuation acceptance on Tiny Shakespeare was near zero beyond 3-token contexts. On repetition-heavy synthetic text, accepted drafts were nontrivial but hash n-gram lookup was about 7-9x faster and accepted slightly more tokens.

## Boundaries and scale limits

No LLM target model, no tokenizer-specific serving path, no KV-cache integration, no batched decoding, and corpus prefixes capped at about 184k tokens. Speculative acceptance is proxied by exact held-out continuation agreement.

## Claim scope

Single-thread CPU benchmark of suffix-array versus hash n-gram retrieval for exact-match draft continuations on one synthetic repeated corpus and Tiny Shakespeare token IDs.

## Why it stopped

Early proxy falsification: the mechanism is compact but did not show useful exact-match acceptance on real held-out text, and synthetic positive cases were slower than a hash n-gram baseline.

## Recommended next action

Stop this as no-paper evidence; only revisit with a direct prompt-local LLM serving benchmark that measures accepted speculative tokens and end-to-end latency against no-speculation and hash n-gram baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Prompt-local suffix-array drafting in a small LLM serving loop
- Success threshold: At least 10% end-to-end median decode latency reduction versus no speculation on a repeated long-prompt workload, while matching or beating hash n-gram memory by at least 4x and not losing more than 5% latency versus hash n-gram drafting.
- Stop condition: Stop if accepted speculative tokens remain below 0.2 per decode step or if index build plus lookup overhead eliminates latency gains on the small-model repeated-prompt benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-array-n-gram-speculative-decoding-on-cpu-2faac6e69c52`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
