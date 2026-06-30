# Per-layer int8 KV eviction for long-context GPT-2-small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `per-layer-int8-kv-eviction-for-long-context-gpt-2-small-4a9da6ba6b19`
Run ID: `per-layer-int8-kv-eviction-for-long-context-gpt-2-small-4a9da6ba6b19-20260530T062743365441+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/7f71c05face3

## What looked useful

Int8 quantization of retained KV tensors adds negligible NLL beyond float eviction, while eviction dominates degradation. A 256-token early-heavy per-layer allocation beat uniform and late-heavy at 384 and 768 tokens, but all 128-token policies and 256-token policies at 768 tokens remain far from full-cache quality. Modeled cache storage falls 83-96%, but measured throughput is slower for int8 variants due to per-step quantize/dequantize overhead.

## Boundaries and scale limits

Pretrained GPT-2-small only; maximum tested context 768 tokens because GPT-2-small has a 1024-token learned position limit; 3 chunks at 384 tokens and 2 chunks at 768 tokens; no fused int8 attention kernel; no batched serving or true long-context model validation.

## Claim scope

Bounded GPT-2-small inference test up to 768 tokens on WikiText chunks: int8 KV storage is quality-benign relative to eviction error, but sink-plus-recent eviction with 128-256 token per-layer budgets causes substantial next-token loss under stronger context pressure and naive dequantization does not improve latency.

## Why it stopped

Direct bounded evidence shows the current per-layer int8 eviction mechanism is not viable as a paper result: cache storage shrinks, but eviction causes large quality loss at 768 tokens and the naive int8 path is slower than full float cache.

## Recommended next action

Stop this run as no-paper useful signal; a bounded follow-up should test profiled early-heavy or learned per-layer budgets at 256-384 retained tokens on more GPT-2-small sequences with a delta-NLL success threshold before any kernel or serving work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Profiled per-layer GPT-2-small KV budgets under 1024-token contexts
- Success threshold: Best profiled int8 policy reaches delta NLL <= 0.05 versus full float cache at >=80% modeled KV-cache storage reduction on the near-1024-token evaluation set.
- Stop condition: Stop if the best 256-384 token profiled policy exceeds +0.10 delta NLL or if int8 overhead remains slower than float eviction without a plausible fused-kernel path.

## Evidence references

- Artifact root: `<local-path>/projects/per-layer-int8-kv-eviction-for-long-context-gpt-2-small-4a9da6ba6b19`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
