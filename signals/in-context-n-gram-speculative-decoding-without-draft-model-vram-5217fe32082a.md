# In-Context N-Gram Speculative Decoding Without Draft Model VRAM

Status: `useful_signal`
Project ID: `in-context-n-gram-speculative-decoding-without-draft-model-vram-5217fe32082a`
Run ID: `in-context-n-gram-speculative-decoding-without-draft-model-vram-5217fe32082a-20260515T093025517749+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/08bd9c0b18ff

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Proxy early validation only: small GPT-2-class runs support the n-gram proposal mechanism, but direct optimized serving evidence is missing.

## Recommended next action

Stop this run as a no-paper proxy result; deepen with a bounded KV-cache serving benchmark before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache benchmark for in-context n-gram speculative decoding
- Success threshold: At least 1.25x end-to-end decode tokens/sec versus ordinary KV-cache decoding on natural prompts, exact greedy output match, and less than 5% additional peak memory excluding the target model KV cache.
- Stop condition: Stop if natural-prompt acceptance is below 25% or end-to-end speedup is below 1.10x after a calibrated KV-cache implementation.

## Evidence references

- Artifact root: `<local-path>/projects/in-context-n-gram-speculative-decoding-without-draft-model-vram-5217fe32082a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
