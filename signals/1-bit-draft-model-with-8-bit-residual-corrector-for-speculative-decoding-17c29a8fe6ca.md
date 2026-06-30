# 1-bit Draft Model with 8-bit Residual Corrector for Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `1-bit-draft-model-with-8-bit-residual-corrector-for-speculative-decoding-17c29a8fe6ca`
Run ID: `1-bit-draft-model-with-8-bit-residual-corrector-for-speculative-decoding-17c29a8fe6ca-20260608T025600308691+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/e2b1eb0a4bf6

## What looked useful

Across five seeds, 1-bit plus int8 residual improved mean one-step acceptance from 0.5868 to 0.7177 and reduced mean KL from 0.5784 to 0.2592 versus 1-bit-only, while remaining below the dense draft acceptance of 0.7601.

## Boundaries and scale limits

No natural-language corpus, transformer architecture, autoregressive rollout, KV-cache behavior, fused quantized kernel, or real serving latency was tested. Timing is a dequantized PyTorch proxy only.

## Claim scope

In a synthetic 64-token bigram next-token teacher setting, an int8 residual corrector trained on teacher-minus-1-bit-draft logits consistently improves 1-bit draft proposal quality for speculative decoding acceptance proxies.

## Why it stopped

Closed as no-paper useful signal because the current result is synthetic/proxy evidence for proposal quality, not direct full validation of natural-language speculative decoding or latency.

## Recommended next action

Run a bounded deepen test on a tiny transformer language model with a real speculative decoding loop and a parameter/storage-matched dense or int8 draft baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny Transformer Speculative Decoding Test for 1-bit Draft plus Int8 Residual
- Success threshold: Corrected draft improves accepted tokens per target call by at least 20% over 1-bit-only and is not worse than the storage-matched dense/int8 control by more than 10% on acceptance, with no quality regression in sampled continuations.
- Stop condition: Stop if corrected acceptance gain over 1-bit-only is below 10%, if residual overhead erases target-call savings in wall-clock latency, or if generated-token quality diverges from the teacher control.

## Evidence references

- Artifact root: `<local-path>/projects/1-bit-draft-model-with-8-bit-residual-corrector-for-speculative-decoding-17c29a8fe6ca`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
