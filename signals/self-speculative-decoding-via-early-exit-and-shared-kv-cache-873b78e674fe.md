# Self-Speculative Decoding via Early Exit and Shared KV Cache

Status: `useful_signal`
Project ID: `self-speculative-decoding-via-early-exit-and-shared-kv-cache-873b78e674fe`
Run ID: `self-speculative-decoding-via-early-exit-and-shared-kv-cache-873b78e674fe-20260516T165828812822+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/651118c6a43c

## What looked useful

Layer 10 of 12 was best but reached only 38.94% exact greedy-token agreement; layers 2/4/6/8 reached 7.64%/10.76%/15.54%/24.55%. A 90% early-confidence gate at layer 10 covered 20.85% of tokens with 74.38% precision, but the exit is too late and still too error-prone for reliable drafting.

## Boundaries and scale limits

Offline agreement proxy only; tested GPT-2 small on 16,512 Wikitext-2 positions. No online speculative decoder, shared-KV kernel, trained intermediate head, larger model, or multi-corpus robustness evaluation was run.

## Claim scope

Untrained early exits in GPT-2 small, projected through the final layer norm and tied LM head, do not provide enough greedy-token agreement on Wikitext-2 to justify self-speculative decoding with a shared KV cache.

## Why it stopped

Proxy early falsification: direct early-exit agreement was too low for the naive untrained method, and full validation would require a trained/calibrated head plus an online shared-KV decoder.

## Recommended next action

Stop this run as a proxy early falsification; the concrete next bounded test is to train or calibrate an intermediate GPT-2 head and measure online shared-KV speculative decoding against greedy decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train a calibrated GPT-2 intermediate head for self-speculative decoding
- Success threshold: Layer 6 or earlier reaches at least 65% held-out greedy-token agreement and the online decoder achieves at least 1.15x tokens/s over greedy decoding with no detected quality drift on the prompt suite.
- Stop condition: Stop if trained layer-6-or-earlier agreement remains below 55% or online decoding is slower than greedy after shared-KV reuse is implemented.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-via-early-exit-and-shared-kv-cache-873b78e674fe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
