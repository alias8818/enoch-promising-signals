# Prompt-Suffix N-Gram Speculative CPU Decode

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `prompt-suffix-n-gram-speculative-cpu-decode-6b9580f7aaba`
Run ID: `prompt-suffix-n-gram-speculative-cpu-decode-6b9580f7aaba-20260607T162038927520+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/7e3b211a9fba

## What looked useful

Across two seeds, copy-heavy synthetic prompts reached roughly 70%-91% target-call reduction depending on n-gram/draft length, while Gutenberg prose stayed around 0%-4%. Shuffled-prompt controls removed nearly all long n-gram gains, supporting ordered prompt-local reuse as the mechanism.

## Boundaries and scale limits

No real transformer verifier, logits, tokenizer-specific production behavior, KV-cache effects, or CPU wall-clock target-model throughput were measured. Evidence is bounded to synthetic repeated/structured prompts and public-domain prose trace proxies.

## Claim scope

Proxy trace-verification evidence shows prompt-suffix n-gram speculation can greatly reduce target verification calls only when continuations reuse ordered spans from the prompt; it provides little to no benefit on ordinary Gutenberg prose chunks.

## Why it stopped

Proxy evidence is useful but not publication-grade; it supports a situational mechanism and early-falsifies a broad natural-prose speedup claim without real model wall-clock validation.

## Recommended next action

Run a bounded real CPU causal-LM benchmark with prompt-lookup speculation on repeated/structured prompts and natural-prose controls; stop paper consideration unless wall-clock tokens/sec improves on copy-heavy prompts without meaningful regression on natural prose.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU LM Prompt-Lookup Speculative Decode Benchmark
- Success threshold: At least 1.3x wall-clock tokens/sec improvement on repeated/structured prompts, less than 5% slowdown on natural prose, and acceptance/call-reduction metrics consistent with the proxy mechanism.
- Stop condition: Stop as negative if real CPU wall-clock speedup is below 1.1x on copy-heavy prompts or if natural-prose controls regress by 5% or more after overhead is included.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-suffix-n-gram-speculative-cpu-decode-6b9580f7aaba`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
