# 2-bit Draft with Residual FP16 Attention for Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-draft-with-residual-fp16-attention-for-speculative-decoding-25a05efba16d`
Run ID: `2-bit-draft-with-residual-fp16-attention-for-speculative-decoding-25a05efba16d-20260602T173049080016+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/42f8898fb57d

## What looked useful

Residual FP16 attention is useful only with an FP16 output head in this proxy. Group-size-128 mean acceptance improved from 0.3292 for int2_all_keep_lm_head to 0.4899 for int2_residual_fp16_attention_keep_lm_head, while int2_residual_fp16_attention without FP16 lm_head reached only 0.0481.

## Boundaries and scale limits

One-token acceptance proxy only; no packed int2 kernels, no measured serving speedup, no full speculative decoding loop, small prompt set, and GPT-2-small-class model scale rather than 7B+ deployment scale.

## Claim scope

On distilgpt2 over 64 deterministic prompt contexts, a 2-bit weight-only draft that keeps attention and lm_head FP16 has materially higher exact one-step speculative acceptance than a fully 2-bit transformer with lm_head FP16; quantizing everything except attention, including lm_head, collapses acceptance.

## Why it stopped

Proxy early falsification of the unqualified design: keeping only attention FP16 did not preserve draft acceptance; useful mechanism signal remains for the narrower FP16 attention plus FP16 lm_head variant.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should run a direct multi-token speculative decoding benchmark with FP16 attention plus FP16 lm_head and fully 2-bit controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct speculative decoding benchmark for int2 MLP with FP16 attention and output head
- Success threshold: Mean accepted tokens per proposal and end-to-end accepted tokens/sec exceed the fully 2-bit with FP16 lm_head control while remaining within 10 percent perplexity or one-step acceptance degradation of the FP16-attention-plus-lm_head proxy target.
- Stop condition: Stop if multi-token acceptance falls below 0.4 mean accepted-token overlap or if measured/simulated int2 throughput cannot offset verifier overhead relative to an FP16 draft baseline.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-draft-with-residual-fp16-attention-for-speculative-decoding-25a05efba16d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
