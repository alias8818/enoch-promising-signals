# Prompt-N-Gram Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `prompt-n-gram-speculative-decoding-on-cpu-413fd1a6e301`
Run ID: `prompt-n-gram-speculative-decoding-on-cpu-413fd1a6e301-20260528T161243416536+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9ad70054129c

## What looked useful

The mechanism is viable when prompts contain spans the target model will reuse: distilgpt2 repetitive prompts averaged 3.271x speedup with 0.777 acceptance, and gpt2 repetitive prompts averaged 2.357x speedup with 0.588 acceptance. Natural prompts were neutral for distilgpt2 and only modestly helpful for gpt2.

## Boundaries and scale limits

Five hand-written prompts, 32 generated tokens per prompt, greedy decoding only, PyTorch CPU execution, 4 CPU threads, distilgpt2 and gpt2 only; no production KV-cache serving engine, sampling, long-context trace set, batched workload, or larger model validation.

## Claim scope

On two small GPT-2-class CPU greedy-decoding benchmarks, prompt-local n-gram drafts reduce target forward passes and improve wall-clock decode speed for repetitive/template prompts, but are neutral or inconsistent for natural/open-ended prompts.

## Why it stopped

Evidence supports a narrow mechanism but not a publication-grade or broad CPU decoding claim; this was a bounded small-model benchmark, not full validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded step is a corpus-level CPU serving benchmark on real templated and natural prompts with a KV-cache inference engine.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Corpus-level CPU KV-cache benchmark for prompt n-gram speculative decoding
- Success threshold: >=1.2x geometric mean tokens/sec improvement on templated prompts and >=0.95x on natural controls, with no output mismatch for greedy decoding.
- Stop condition: Stop if templated prompt speedup is below 1.1x or natural controls regress below 0.9x after a correct KV-cache implementation.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-n-gram-speculative-decoding-on-cpu-413fd1a6e301`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
