# 4-bit KV Cache with Per-Head Residual Error Buffers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `4-bit-kv-cache-with-per-head-residual-error-buffers-fa55900c701e`
Run ID: `4-bit-kv-cache-with-per-head-residual-error-buffers-fa55900c701e-20260523T151554443367+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/94b8eb508186

## What looked useful

Synthetic recent-local attention at seq=2048 improved mean relative MSE by 278x with a 64-token residual window at 31.25% fp16 KV memory; seq=4096 improved 249x at 29.69% fp16 memory. Gaussian attention improved only 1.06x and random outlier values were mixed. A DistilGPT-2 real activation trace reduced mean relative MSE 2.46x to 5.23x for residual windows 8 to 64, but short prompts made larger windows consume 49% to 70% of fp16 KV memory.

## Boundaries and scale limits

No fused kernel, no generation or perplexity evaluation, no 7B+ model, no long-context real-model serving run, no throughput validation, and only a recent-token residual admission policy was tested.

## Claim scope

Bounded GPU mechanism evidence shows that a recent-token per-head fp16 residual error buffer can substantially reduce int4 KV attention-output error when attention concentrates on buffered recent tokens; a short DistilGPT-2 activation trace shows smaller but consistent reductions in next-token attention-output error.

## Why it stopped

No-paper closure: this run produced useful bounded mechanism evidence, but not publication-grade full-model quality, serving throughput, or robustness evidence.

## Recommended next action

Run a bounded direct model-quality follow-up on GPT-2-small or comparable real KV traces with 1k-4k token prompts, comparing recent-window residuals against outlier-aware residual admission and measuring next-token logit KL or perplexity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real long-context KV trace validation for int4 residual-buffer cache
- Success threshold: At a fixed KV memory budget below 40% of fp16, residual admission reduces next-token logit KL or perplexity degradation by at least 2x versus plain int4 KV and beats a pure recent-window policy on nonlocal or outlier-heavy prompts.
- Stop condition: Stop if matched-budget residual policies fail to improve logit KL or perplexity degradation by at least 1.25x versus plain int4 on real long-context traces, or if memory/latency overhead exceeds the stated budget.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-kv-cache-with-per-head-residual-error-buffers-fa55900c701e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
