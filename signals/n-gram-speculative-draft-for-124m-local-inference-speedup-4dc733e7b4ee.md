# N-gram speculative draft for 124M local inference speedup

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-speculative-draft-for-124m-local-inference-speedup-4dc733e7b4ee`
Run ID: `n-gram-speculative-draft-for-124m-local-inference-speedup-4dc733e7b4ee-20260605T002431072492+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/e4701a56048d

## What looked useful

Prompt n-gram speculative drafting can materially reduce target forwards for a 124M local model when prompts/generated text contain repeated n-grams. The realistic cached float32 run reduced target forwards by 63.99% with 79.24% draft acceptance and exact greedy equivalence. The fp16 cached run diverged on 9/32 prompts, identifying precision-sensitive exactness as the main practical risk.

## Boundaries and scale limits

Single model, single GPU host, small prompt suite, greedy-only, Python/Hugging Face prototype. Larger models, sampling, batching, long-context serving, quantized inference, production kernels, and broad prompt distributions were not validated. Cached fp16 speculative decoding was fast but not exact in this run.

## Claim scope

Bounded local evidence: GPT-2 124M on NVIDIA GB10, greedy decoding, WikiText prompts, 32 prompts x 128 generated tokens, prompt n-gram drafting with max_ngram=8 and max_draft=8, KV-cache verification in float32 exactly matched cached greedy output and improved mean decode throughput from 306.20 to 773.09 generated tokens/s (2.52x).

## Why it stopped

Useful bounded local evidence was produced, but small scale and non-exact cached fp16 behavior prevent a paper-ready speedup claim.

## Recommended next action

Stop this run as no-paper useful signal; next concrete step is a bounded deterministic cached fp16/bf16 verifier study before any larger serving benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Deterministic cached fp16/bf16 n-gram speculative verification for GPT-2-small-class inference
- Success threshold: Zero exact-match divergences and at least 1.5x mean throughput speedup versus cached greedy fp16/bf16 baseline on the bounded prompt suite.
- Stop condition: Stop if any verifier policy still produces exact-match divergences after deterministic settings are applied, or if exact mode falls below 1.2x mean speedup.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-speculative-draft-for-124m-local-inference-speedup-4dc733e7b4ee`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
