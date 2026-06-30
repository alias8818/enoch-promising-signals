# Prompt N-Gram Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `prompt-n-gram-speculative-decoding-on-cpu-a5f03701d003`
Run ID: `prompt-n-gram-speculative-decoding-on-cpu-a5f03701d003-20260609T033740857364+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/0b02e3d6188e

## What looked useful

Prompt n-gram lookup is cheap on CPU, but natural-continuation acceptance is too sparse for a compelling standalone CPU decoding speedup. The best latest-match configuration was prompt_len=2048, ngram_order=2, draft_len=16 with 1.04165x mean and 1.02811x median upper-bound target-call speedup over 20,800 trace cases; first-match control was similar at 1.03940x mean over 11,700 cases.

## Boundaries and scale limits

This is not an end-to-end CPU LLM serving benchmark. It uses held-out natural prose as an oracle target, simple regex tokenization, and target-call accounting rather than measured model latency. It does not cover copy-heavy RAG, code, templated outputs, or production BPE tokenizers.

## Claim scope

In a CPU-only trace benchmark over four public-domain prose books using regex tokens, prompt-only n-gram speculative drafting produces at best a 1.04165x mean upper-bound target-call reduction for 256-token natural continuations, before real model verification overhead.

## Why it stopped

Proxy trace evidence, not full serving validation, shows the mechanism has too low an acceptance ceiling on natural prose to justify paper writing or larger general-purpose CPU experiments.

## Recommended next action

Stop this project as an early negative for general natural-continuation CPU speedup; only revisit with a direct CPU LLM serving benchmark on explicitly copy-heavy workloads.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Prompt N-Gram Speculation for Copy-Heavy CPU LLM Workloads
- Success threshold: At least 1.15x end-to-end median tokens/s improvement on a copy-heavy workload with no regression above 5% on the natural-continuation control.
- Stop condition: Stop if accepted draft tokens remain below 5% of drafted tokens or end-to-end speedup is below 1.05x after CPU verification overhead is included.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-n-gram-speculative-decoding-on-cpu-a5f03701d003`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
