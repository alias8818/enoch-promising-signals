# Sub-Network Early-Exit Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sub-network-early-exit-speculative-decoding-217a9bc7d4d6`
Run ID: `sub-network-early-exit-speculative-decoding-217a9bc7d4d6-20260524T215744673812+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/1f1cc68664d7

## What looked useful

Intermediate exits preserve exact greedy output under verification, but acceptance is too low and draft overhead too high: best main run wall speedup was 0.359x versus greedy, and the later-exit draft-8 sensitivity run reached only 0.312x despite 57.8% verifier-call reduction.

## Boundaries and scale limits

Tested only GPT-2 small, greedy decoding, 8 prompts, 24 generated tokens per prompt, intermediate exits up to layer 11, and non-production PyTorch forwards without auxiliary early-exit training or optimized KV-cache/fused kernels.

## Claim scope

For a naive GPT-2-small implementation that uses untrained intermediate transformer layers with the final tied LM head as early-exit drafters, exact greedy speculative decoding works but does not speed up generation on the local GB10 GPU probe.

## Why it stopped

Bounded model-backed proxy/direct probe falsified the practical speedup hypothesis for untrained GPT-2 intermediate exits; this is not a full validation of trained sub-network exits or production kernels.

## Recommended next action

Stop this naive early-exit version; the only bounded next test worth running is to train lightweight early-exit/distillation heads and require both high acceptance and measured speedup against a KV-cache baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Distilled GPT-2 Early-Exit Heads for Speculative Drafting
- Success threshold: At least one trained exit must preserve exact greedy output under verification, achieve mean acceptance >= 0.65 on held-out prompts, and deliver >= 1.15x wall-clock speedup versus the KV-cache greedy baseline for 256+ generated tokens per prompt.
- Stop condition: Stop if trained exits remain below 0.45 mean acceptance or below 1.0x wall-clock speedup after a bounded training run and kernel-neutral evaluation.

## Evidence references

- Artifact root: `<local-path>/projects/sub-network-early-exit-speculative-decoding-217a9bc7d4d6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
