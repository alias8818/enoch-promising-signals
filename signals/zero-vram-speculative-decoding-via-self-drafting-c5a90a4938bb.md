# Zero-VRAM Speculative Decoding via Self-Drafting

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `zero-vram-speculative-decoding-via-self-drafting-c5a90a4938bb`
Run ID: `zero-vram-speculative-decoding-via-self-drafting-c5a90a4938bb-20260613T215958374733+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/61ea5cfee158

## What looked useful

The best truncated-context self-draft setting reached 259.05 mean tokens/s versus 641.75 mean tokens/s for cached greedy, despite 1.0 mean acceptance, and used slightly higher peak CUDA allocation (205.35 MiB versus 195.72 MiB). The added draft and verification forwards outweighed fewer verification rounds.

## Boundaries and scale limits

This run did not test LayerSkip-style early exits, large Llama-class models, long contexts, batched serving, sampling, or production KV-cache repair/reuse. The result should not be generalized to trained early-exit self-speculative decoding.

## Claim scope

On GB10 with distilgpt2, greedy decoding, four short prompts, and draft windows 16-128, truncated-context self-drafting with the same target model uses no second model weights but does not speed up cached greedy decoding.

## Why it stopped

Proxy/direct local early falsification: the tested no-extra-model truncated-context self-drafting mechanism was slower than cached greedy under favorable high-acceptance settings, so it is not viable as a practical speedup path without a materially cheaper draft computation.

## Recommended next action

Stop this truncated-context path as a no-paper early negative; if continuing, implement a bounded early-exit or layer-skip self-draft variant with correct KV reuse and require greater than 1.1x cached-greedy throughput.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Early-Exit Zero-Extra-Weight Self-Speculation on GB10
- Success threshold: Mean throughput at least 1.1x cached greedy with exact greedy output agreement and no second model-weight residency.
- Stop condition: Stop if early-exit acceptance is below 0.5, outputs diverge after verification, or mean throughput remains below cached greedy after two draft lengths.

## Evidence references

- Artifact root: `<local-path>/projects/zero-vram-speculative-decoding-via-self-drafting-c5a90a4938bb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
