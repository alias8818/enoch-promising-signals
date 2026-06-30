# Self-Speculative Early-Exit with Shared KV Cache Reuse

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `self-speculative-early-exit-with-shared-kv-cache-reuse-85aba3adf192`
Run ID: `self-speculative-early-exit-with-shared-kv-cache-reuse-85aba3adf192-20260529T001703302037+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f12390d6958e

## What looked useful

Speculative batching can create latency headroom, but the median proxy case required about 87.6% independent per-token early-exit acceptance to break even, and no-reuse batched verification was as fast or faster in 18 of 72 cases. Shared KV reuse is therefore not supported as a standalone paper-ready mechanism by this run.

## Boundaries and scale limits

No trained language model acceptance was measured; transformer layers were proxied by dense matrix layers; no GPU kernels, real KV-cache layout, tokenizer behavior, sampling policy, or production serving stack was tested.

## Claim scope

CPU NumPy proxy benchmark of self-speculative early-exit scheduling with shared lower-layer/KV reuse versus sequential full-depth decoding and a no-reuse batched-verifier control.

## Why it stopped

No-paper useful signal from a bounded proxy: the result identifies high acceptance thresholds and mixed shared-KV-specific benefit, but it is not a full validation on a trained LM or serving stack.

## Recommended next action

Run a bounded GPT-2-small-class early-exit acceptance probe and compare full decoding, no-reuse speculative verification, and shared-KV speculative verification before considering larger-scale serving work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small early-exit acceptance and verifier-control benchmark
- Success threshold: At one useful exit depth and draft length, observed acceptance must exceed the measured break-even threshold with at least 1.2x end-to-end latency speedup over full sequential decoding and shared-KV must beat no-reuse verification by at least 10%.
- Stop condition: Stop if all practical exit depths fall below break-even acceptance or if shared-KV verification fails to beat no-reuse batched verification in end-to-end latency.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-early-exit-with-shared-kv-cache-reuse-85aba3adf192`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
