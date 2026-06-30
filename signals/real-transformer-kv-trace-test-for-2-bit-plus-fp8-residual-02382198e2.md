# Real Transformer KV Trace Test for 2-Bit Plus FP8 Residual Cache

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-transformer-kv-trace-test-for-2-bit-plus-fp8-residual-02382198e2`
Run ID: `real-transformer-kv-trace-test-for-2-bit-plus-fp8-residual-02382198e2-20260523T055504445621+0000`

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

- Parent run decision: 2-Bit KV Cache with FP8 Residual Summary for Long Context: enoch://control-plane/projects/2-bit-kv-cache-with-fp8-residual-summary-for-long-context-08fee1860263/runs/2-bit-kv-cache-with-fp8-residual-summary-for-long-context-08fee1860263-20260523T024654422637+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8780efafda6d

## What looked useful

Sparse FP8 residuals reduce cache MSE monotonically and improve some top-5 overlap, but GPT-2 mean KL remains 0.042-0.151 for 4.0-2.5 nominal bits versus 0.000374 for dense FP8 cache. Dense FP8 residual over a 2-bit base reaches low drift at about 10 nominal bits, which is not a compelling compression win over dense FP8.

## Boundaries and scale limits

Single-prompt, 160-token cache and 48-token replay on GPT-2-class models only; nominal bit counts exclude sparse residual index overhead and no packed kernel, throughput, long-context, multi-prompt, or 7B+ validation was performed.

## Claim scope

Tier 1 direct replay test on real DistilGPT-2 and GPT-2 KV tensors: a simple groupwise 2-bit base plus sparse top-k FP8 residuals improves over 2-bit-only reconstruction but does not approach dense FP8-cache downstream drift at 2.5-4 nominal bits per element.

## Why it stopped

Controlled direct GPT-2-class cache replay found mechanism support but failed the practical low-bit threshold against a dense FP8 cache control.

## Recommended next action

Stop this simple sparse-residual formulation as no-paper evidence; the next bounded test should change the residual mechanism rather than merely scale this implementation.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Channelwise or attention-weighted residual selection for 2-bit KV cache
- Success threshold: On GPT-2-class direct replay, <=4 effective bits per element including metadata, mean KL no more than 2x dense FP8 cache, and mean top-5 overlap >=0.95 across at least 8 natural-language prompts.
- Stop condition: Stop if sensitivity-guided residual selection cannot beat the raw top-k residual baseline by at least 50% mean KL at matched effective bits on the first 8-prompt batch.

## Evidence references

- Artifact root: `<local-path>/projects/real-transformer-kv-trace-test-for-2-bit-plus-fp8-residual-02382198e2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
