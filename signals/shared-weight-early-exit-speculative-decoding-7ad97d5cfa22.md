# Shared-Weight Early-Exit Speculative Decoding

Status: `useful_signal`
Project ID: `shared-weight-early-exit-speculative-decoding-7ad97d5cfa22`
Run ID: `shared-weight-early-exit-speculative-decoding-7ad97d5cfa22-20260515T201443058312+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f8aa642cf3d5

## What looked useful

Early exits that are cheap enough to matter are poorly aligned with the final GPT-2 distribution, while near-final exits have better acceptance but are too expensive. Best observed optimistic latency proxy was 0.7928x for gamma=1 layer 11; draft-temperature softening to 2.0 reached only 0.6232x for gamma=2 layer 11.

## Boundaries and scale limits

This is a bounded GPT-2-small direct test plus speed proxies, not a 7B+ production serving benchmark. Wall-clock serving speed was proxied by an optimistic verifier-latency model and a conservative linear-FLOP model rather than measured inside a paged-KV inference engine.

## Claim scope

Pure no-training shared-weight early-exit speculative decoding was tested on GPT-2-small using intermediate layers 3, 6, 9, and 11 as draft distributions projected through the existing final norm and tied LM head on WikiText-2 validation contexts. Within this scope, the mechanism did not reach speculative decoding break-even under gamma 1, 2, or 4.

## Why it stopped

Proxy/early falsification: bounded GPT-2-small direct acceptance tests and favorable speed proxies stayed below break-even, so the result is not paper-positive and not worth scaling as-is.

## Recommended next action

Stop this pure shared-weight/no-training variant as an early negative; only revisit with a trained or explicitly calibrated auxiliary exit and require measured throughput above 1.0x on a real inference path.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Calibrated Auxiliary Early-Exit Draft for Speculative Decoding
- Success threshold: At least 1.10x measured tokens/second over ordinary GPT-2-small decoding on 128+ WikiText-style prompts with exact speculative correction and no degradation of target distribution.
- Stop condition: Terminate if layer 6-9 calibrated exits cannot achieve at least 0.70 token acceptance for gamma 2 or if measured throughput remains at or below 1.0x after KV-cache implementation.

## Evidence references

- Artifact root: `<local-path>/projects/shared-weight-early-exit-speculative-decoding-7ad97d5cfa22`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
