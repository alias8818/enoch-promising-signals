# N-gram draft verification for tiny model inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-draft-verification-for-tiny-model-inference-16a39483c3e3`
Run ID: `n-gram-draft-verification-for-tiny-model-inference-16a39483c3e3-20260601T000151558887+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/6290d1416720

## What looked useful

Plain corpus n-gram drafting is implementable for exact greedy verification, but acceptance was too low to create practical speedup for tiny cached LM inference in this setting. Best exact config was order 5 max draft 4 with 7.66% acceptance, 1.09% mean call reduction, and 1.0075x mean wall speedup across 24 prompts.

## Boundaries and scale limits

Small local benchmark only: one tiny/small causal LM, WikiText-2 text, greedy decoding, no continuous batching, no quantization, no custom serving kernels, and no high-repetition code/log domain.

## Claim scope

On a bounded GB10 CUDA test using distilgpt2, WikiText-2 train n-gram tables, and WikiText-2 validation prompts, cached n-gram speculative verification preserved exact greedy outputs for order 4 and 5 configs but produced only about 1% model-call reduction and no meaningful wall-time gain over cached greedy decoding.

## Why it stopped

Direct local cached-inference evidence showed exactness but only noise-level speed changes and about 1% model-call reduction, so the result is a bounded useful negative signal rather than full validation.

## Recommended next action

Stop this broad plain-corpus n-gram draft idea as no-paper evidence; the only bounded next test worth running is a separate prompt-local or retrieval-local n-gram cache benchmark on highly repetitive code/log completions with a >=15% exact wall-time speedup threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Prompt-local n-gram draft verification on repetitive completion workloads
- Success threshold: >=15% mean wall-time speedup and >=10% p50 wall-time speedup over cached greedy decoding with 100% exact greedy output equality on at least two high-repetition workloads.
- Stop condition: Stop if exact prompt-local/retrieval-local drafting stays below 5% call reduction or below 1.05x mean wall-time speedup after a warmup-controlled 100-prompt benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-draft-verification-for-tiny-model-inference-16a39483c3e3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
