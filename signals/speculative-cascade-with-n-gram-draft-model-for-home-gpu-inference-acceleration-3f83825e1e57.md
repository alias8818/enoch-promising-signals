# Speculative Cascade with N-gram Draft Model for Home GPU Inference Acceleration

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-cascade-with-n-gram-draft-model-for-home-gpu-inference-acceleration-3f83825e1e57`
Run ID: `speculative-cascade-with-n-gram-draft-model-for-home-gpu-inference-acceleration-3f83825e1e57-20260607T105540141771+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/2fe9114ac6a6

## What looked useful

N-gram drafting produced exact fp32 speedups of 1.51x on repetition-biased prompts and 1.27x on lower-repetition controls, with 24-37% target-forward reduction. fp16 favorable prompts were exact at 1.52x, but fp16 control prompts had output mismatches, making the broad home-GPU exact-decoding claim unresolved and not paper-ready.

## Boundaries and scale limits

Only short 64-token generations, GPT-2, manually constructed prompts, single-process decoding, and fp32/fp16 PyTorch Transformers were tested. No 7B+ quantized model, production serving engine, long-context workload, sampling mode, continuous batching, or broad corpus validation was run.

## Claim scope

Bounded GPT-2-small class greedy decoding on a GB10 GPU: an exact n-gram draft verifier reduced target forwards and improved wall-clock throughput on 24-prompt synthetic sets when numerical exactness was preserved, with stronger gains on repetition-biased prompts.

## Why it stopped

Bounded local evidence supports the mechanism, but fp16 exactness failures on lower-repetition controls prevent a reliable home-GPU acceleration claim; this is not a full validation.

## Recommended next action

Stop this run as no-paper useful signal; next run should test an fp16-safe acceptance guard that preserves exact outputs on the control set while retaining at least 1.15x speedup.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: FP16-safe n-gram speculative decoding with acceptance-margin guard
- Success threshold: Pass if fp16 control exact_match_all is true and aggregate speedup is >= 1.15x on control prompts, while favorable prompts remain exact with >= 1.25x speedup.
- Stop condition: Stop as negative if exactness still fails on any fp16 control prompt or if guard overhead/rejections reduce control speedup below 1.05x.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-cascade-with-n-gram-draft-model-for-home-gpu-inference-acceleration-3f83825e1e57`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
