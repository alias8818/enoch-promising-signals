# GPT-2-Small Early-Exit Self-Speculation With KV-Cache Timing

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `gpt-2-small-early-exit-self-speculation-with-kv-cache-timi-1b4b9927c1`
Run ID: `gpt-2-small-early-exit-self-speculation-with-kv-cache-timi-1b4b9927c1-20260527T154050965267+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Self-Speculative Decoding via Early-Exit Draft on Shared Weights: enoch://control-plane/projects/self-speculative-decoding-via-early-exit-draft-on-shared-weights-8da54f3f587f/runs/self-speculative-decoding-via-early-exit-draft-on-shared-weights-8da54f3f587f-20260527T132654710640+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/6b0b50c36b43

## What looked useful

Naive GPT-2-small early-exit logit-lens drafting has too little acceptance to amortize KV-cache verification overhead: mean acceptance ranged from 2.9% to 5.3% for layers 4/6/8 and rose only to 15.8% at layer 11, while 64-token mean speed stayed between 0.195x and 0.229x of the cached baseline for layers 4/6/8 and 0.199x to 0.219x for layers 10/11. Some fp16 batched-verifier runs also diverged from single-token greedy outputs, adding a deployment exactness caveat.

## Boundaries and scale limits

Tier 1 controlled small direct test only: six prompts, short generations, one GPU, Hugging Face GPT-2-small kernels, no trained auxiliary heads, no custom fused serving kernels, no larger models, no sampling-mode acceptance, and only gamma 4.

## Claim scope

On this GB10 host with local GPT-2-small, fp16 GPU inference, six prompts, 64-token greedy decoding, gamma 4, and untrained logit-lens early exits at layers 4/6/8/10/11, early-exit self-speculation with KV-cache verification was consistently slower than cached full-model greedy decoding.

## Why it stopped

Tier 1 direct KV-cache timing produced consistent slowdowns rather than speedups; this is an early scoped falsification of the naive/untrained mechanism, not a full validation over larger models or trained heads.

## Recommended next action

Stop this naive early-exit logit-lens path as a speedup claim; the only bounded adjacent test worth running is to train or calibrate an auxiliary early-exit head and require both exact target equivalence and >1.05x wall-clock speedup over cached GPT-2-small greedy decoding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small trained early-exit head self-speculation timing
- Success threshold: Mean speedup greater than 1.05x over cached GPT-2-small greedy decoding with exact greedy match fraction 1.0 and mean drafted-token acceptance at least 60% on a held-out prompt set.
- Stop condition: Stop if trained/calibrated heads cannot reach 60% mean acceptance or if any exactness-preserving implementation remains below 1.0x wall-clock speedup after gamma and exit-layer tuning.

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-early-exit-self-speculation-with-kv-cache-timi-1b4b9927c1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
