# Self-Speculative Decoding via Layer-Pipelined Early Exit

Status: `useful_signal`
Project ID: `self-speculative-decoding-via-layer-pipelined-early-exit-3a34fb6b1278`
Run ID: `self-speculative-decoding-via-layer-pipelined-early-exit-3a34fb6b1278-20260518T101733422273+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/6dcd20e5834b

## What looked useful

Across distilgpt2 and gpt2, best serial modeled speedup stayed below 1.0, while ideal perfect-overlap pipeline speedup reached 1.71x and 1.66x respectively at gamma 1; acceptance and pipeline benefit declined as gamma increased.

## Boundaries and scale limits

Direct evidence is limited to small GPT-style pretrained models, short prompt sets, greedy decoding, and modeled layer work. No fused KV-cache serving implementation, CUDA stream overlap, large model, long-context, or broad prompt-distribution validation was run.

## Claim scope

Pretrained distilgpt2 and GPT-2-small greedy decoding probes show intermediate exits can draft exact final tokens, but serial self-speculation is below break-even; only an optimistic perfect-overlap layer-pipeline cost model shows a narrow speedup region for small gamma.

## Why it stopped

Proxy/early falsification: the direct small-model probe rejects the stronger serial-speedup claim, and the remaining positive claim depends on unimplemented real pipeline overlap rather than full validation.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded action is a direct KV-cache layer-pipelined implementation measuring exact greedy wall-clock speedup versus a tuned baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Measure real KV-cache layer-pipelined early-exit self-speculation
- Success threshold: At least 1.2x median wall-clock tokens/s over tuned greedy decoding with exact greedy outputs on GPT-2-small-class or larger models, plus overlap traces showing the pipeline is real.
- Stop condition: Stop if the best measured exact-output speedup is below 1.05x after tuned KV-cache baseline comparison, or if overlap traces show the implementation is effectively serial.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-decoding-via-layer-pipelined-early-exit-3a34fb6b1278`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
