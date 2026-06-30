# Tiny Draft Speculative Decoding for Home GPUs

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `tiny-draft-speculative-decoding-for-home-gpus-d05f0025ac61`
Run ID: `tiny-draft-speculative-decoding-for-home-gpus-d05f0025ac61-20260527T130613588708+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/127bf6091a35

## What looked useful

A readily available tiny GPT-2-family draft model is not enough to speed up stock home-GPU speculative decoding; exact float32 assisted generation is slower than baseline, and the fp16 assisted path is both slower and not token-exact against fp16 cached greedy output in this benchmark.

## Boundaries and scale limits

Only GPT-2-family small models were tested. The run did not test 7B+ targets, quantized kernels, custom fused verification, target-trained drafts, sampling workloads, batching, or long-form serving.

## Claim scope

On this GB10 host, stock Transformers assisted generation with distilgpt2 as draft for gpt2 does not improve deterministic greedy throughput; the exact float32 path is 0.57x to 0.61x of warmed greedy baseline across six prompts and 64 generated tokens.

## Why it stopped

The direct local test failed the predeclared positive threshold: best exact calibrated setting was 0.61x baseline throughput, not a speedup.

## Recommended next action

Stop this run as a bounded negative/useful-signal result; only reopen with a different draft/target pairing or implementation that can first demonstrate token-exact >=1.10x warmed-greedy speedup in a small local benchmark.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/tiny-draft-speculative-decoding-for-home-gpus-d05f0025ac61`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
