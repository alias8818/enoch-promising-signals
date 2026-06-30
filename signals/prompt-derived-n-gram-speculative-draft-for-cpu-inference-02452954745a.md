# Prompt-Derived N-Gram Speculative Draft for CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `prompt-derived-n-gram-speculative-draft-for-cpu-inference-02452954745a`
Run ID: `prompt-derived-n-gram-speculative-draft-for-cpu-inference-02452954745a-20260604T022701073227+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/45d77e07dfa2

## What looked useful

Prompt-derived n-gram drafting appears mechanically viable for repetitive prompts and long contexts, but benefits are corpus/tokenization dependent. It is not paper-ready without real model-token traces and CPU serving latency measurements.

## Boundaries and scale limits

This run did not integrate with a real CPU LLM verifier, did not use BPE tokenizer output, did not measure end-to-end latency inside an inference engine, and used approximately 1 MB corpora with 192 stream samples per condition. Byte-token results are a stress/proxy check, not a deployable LLM-token result.

## Claim scope

On two small plain-text corpora using simulated speculative verification against held-out continuations, a prompt-only n-gram drafter can reduce estimated target calls when prompts are long and locally repetitive. The strongest word/punctuation-token result was Wikitext-2 stream sampling with 2048-token prompts, gamma 16, order 4 most-common lookup: 1.331x estimated speedup and 0.333 accepted draft tokens per target call. Tiny Shakespeare word/punctuation tokens showed only marginal improvement over a unigram prompt baseline.

## Why it stopped

Proxy evaluation supports the mechanism in some settings but is not direct/full validation of CPU inference speedup.

## Recommended next action

Stop this worker run as no-paper useful signal; the next bounded test should replay real BPE token traces from a small CPU-served language model and compare end-to-end latency against no-draft and prompt-unigram controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU LLM Trace Replay for Prompt N-Gram Drafting
- Success threshold: At least 1.15x median end-to-end tokens/sec improvement over no-draft and at least 0.10x over prompt-unigram on one repetitive prompt family, with no regression below 0.98x on a non-repetitive control.
- Stop condition: Stop as negative if prompt-ngram is below 1.05x median end-to-end improvement or loses to prompt-unigram after overhead on both prompt families.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-derived-n-gram-speculative-draft-for-cpu-inference-02452954745a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
