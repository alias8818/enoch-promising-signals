# Suffix N-Gram Speculative Decoding vs No-Speculation Baseline on gb10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-n-gram-speculative-decoding-vs-no-speculation-baseline-on-gb10-701f02625d8b`
Run ID: `suffix-n-gram-speculative-decoding-vs-no-speculation-baseline-on-gb10-701f02625d8b-20260630T154442008134+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7e261507cbe2

## What looked useful

Copy-grounded run showed 4.40x mean tokens/s speedup and 80.9% target forward-call reduction, but exact output equality failed. A diagnostic rerun reproduced 4.65x speedup with failures on 3 of 4 prompts; conservative n-gram settings still failed on 2 of 4 prompts. One mismatch diverged after 28 generated tokens and prompt lookup continued to 80 tokens where baseline stopped at EOS after 37 tokens.

## Boundaries and scale limits

Single 360M-class model, four copy-grounded prompts, one weak natural-prompt control that immediately emitted EOS, max 80 new tokens, no production corpus, no larger model, and no alternate inference backend. Evidence is direct for this bounded local setup only.

## Claim scope

On a local NVIDIA GB10 using Transformers 4.57.6, PyTorch 2.12.0+cu130, and HuggingFaceTB/SmolLM2-360M-Instruct in CUDA bfloat16 greedy generation, suffix n-gram prompt lookup decoding reduced target forward calls and improved wall-clock throughput on small copy-grounded prompts, but did not reliably preserve no-speculation greedy output or stopping behavior.

## Why it stopped

Bounded local benchmark supports a speed mechanism on copy-overlap prompts, but the tested suffix n-gram prompt lookup path failed exact no-speculation baseline equivalence/stopping, so it is not a valid paper-positive acceleration result.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded correctness-first follow-up that isolates whether Transformers prompt lookup can be made token-equivalent and max-token/EOS compliant before measuring larger-model speed.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Correctness-gated suffix n-gram prompt lookup decoding on GB10
- Success threshold: All tested prompt-lookup outputs exactly match no-spec greedy baseline token IDs and stopping behavior; among copy-grounded prompts, mean throughput speedup is at least 1.5x with at least 30% target forward-call reduction.
- Stop condition: Stop if any exact-token, EOS, or max_new_tokens mismatch reproduces after the chosen fix/configuration, or if correctness holds but speedup is below 1.1x on copy-grounded prompts.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-n-gram-speculative-decoding-vs-no-speculation-baseline-on-gb10-701f02625d8b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
