# 2-bit per-head KV cache for longer local context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-per-head-kv-cache-for-longer-local-context-66929ef430ed`
Run ID: `2-bit-per-head-kv-cache-for-longer-local-context-66929ef430ed-20260604T075511797317+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/25e28f9bf1f5

## What looked useful

The memory-saving mechanism is arithmetically real, but simple 2-bit per-head KV quantization is not a reliable drop-in longer-context method under direct attention-fidelity tests. The best 2-bit tested scheme, per-head per-token min/scale, gives about 6.4x memory reduction but on normal KV has cosine about 0.82 and relative MSE about 0.5, and on outlier KV cosine falls to 0.26-0.43. Int8 per-token control remains essentially lossless at about 1.88x memory reduction.

## Boundaries and scale limits

No non-degenerate GPT-2-small-class perplexity benchmark, no packed 2-bit serving kernel, no trained/calibrated quantizer, and no long-context retrieval benchmark were run. The tiny-gpt2 sanity check is treated as weak API evidence only because the model architecture is too small to distinguish schemes.

## Claim scope

Bounded GPU tensor probes show that naive 2-bit per-head KV-cache quantization can reduce estimated KV memory by 6.4x to about 8.0x versus FP16, but it substantially degrades direct attention-output fidelity on normal and outlier synthetic KV distributions compared with an int8 per-token control.

## Why it stopped

Proxy/direct-attention early falsification of naive 2-bit per-head KV cache as a generic drop-in longer-context win; not a full real-model validation.

## Recommended next action

Stop this run as a no-paper useful signal; a bounded follow-up should test residual or mixed-precision protection for outlier/high-attention tokens on a non-degenerate GPT-2-small-class model.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual protected 2-bit KV cache on GPT-2-small-class text
- Success threshold: A residual or mixed-precision 2-bit variant achieves at least 4x estimated KV memory reduction versus FP16 with mean NLL delta under 0.05 and top-10 logit Jaccard at least 0.9 against FP16 on real text prefixes.
- Stop condition: Stop if naive and protected 2-bit variants both exceed mean NLL delta 0.10 or top-10 Jaccard below 0.8 while int8 remains near lossless.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-per-head-kv-cache-for-longer-local-context-66929ef430ed`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
