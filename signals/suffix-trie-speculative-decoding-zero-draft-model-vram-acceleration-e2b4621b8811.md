# Suffix-Trie Speculative Decoding: Zero-Draft-Model VRAM Acceleration

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-trie-speculative-decoding-zero-draft-model-vram-acceleration-e2b4621b8811`
Run ID: `suffix-trie-speculative-decoding-zero-draft-model-vram-acceleration-e2b4621b8811-20260628T042405638049+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/4b231f450f7e

## What looked useful

GPT-2 small gamma-8 suffix proposals reduced natural-prompt target rounds from 1024 to 455 tokens-equivalent rounds with 38.2% pooled draft-token acceptance, and repetitive prompts from 1024 to 162 rounds with 97.4% acceptance. GPU block verification for GPT-2 small cost about 2.49 ms for 8 tokens versus 2.11 ms for 1 token, supporting the target-round reduction mechanism.

## Boundaries and scale limits

Trace-simulated verification only; no online KV-cache speculative decoder, no serving scheduler, no learned-draft baseline, no sampling evaluation, no larger models, and no broad real-corpus benchmark.

## Claim scope

Bounded local trace result: a suffix-trie zero-draft proposer reduced simulated target verification rounds for distilgpt2 and GPT-2 small greedy decoding on 16 fixed prompts per model, especially on repeated contexts, while loading no draft model.

## Why it stopped

No-paper useful signal: the mechanism is supported by bounded trace and microbenchmark evidence, but end-to-end latency and cache-management overhead were only proxied, not directly validated.

## Recommended next action

Implement an online GPT-2-small KV-cache speculative decoder with cache crop/truncation and compare wall-clock tokens/s plus peak CUDA memory against one-token greedy decoding and a small learned-draft baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Online KV-cache suffix-trie speculative decoding benchmark
- Success threshold: At least 1.25x wall-clock tokens/s on repetitive prompts, no more than 10% slowdown on natural prompts, exact greedy-token match, and lower peak CUDA memory than the learned-draft speculative control.
- Stop condition: Stop if exact greedy-token equivalence fails, if cache-management overhead makes suffix-trie speculative slower than baseline on both prompt categories, or if learned-draft memory is not meaningfully higher in the tested setup.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-trie-speculative-decoding-zero-draft-model-vram-acceleration-e2b4621b8811`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
