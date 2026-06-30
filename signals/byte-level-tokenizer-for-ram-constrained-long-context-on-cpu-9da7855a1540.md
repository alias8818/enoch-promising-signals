# Byte-level tokenizer for RAM-constrained long context on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `byte-level-tokenizer-for-ram-constrained-long-context-on-cpu-9da7855a1540`
Run ID: `byte-level-tokenizer-for-ram-constrained-long-context-on-cpu-9da7855a1540-20260608T174925315709+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/1d3749dd7343

## What looked useful

Byte tokenization saves about 27-44 MiB of tokenizer load RSS and encodes much faster, but expands sequence length by 3.16x-5.80x versus cl100k_base. For standard transformer KV-cache inference, embedding/vocab savings are exhausted after about 167-703 BPE-equivalent tokens depending on model/corpus, causing multi-GiB net RAM increases at 32k context.

## Boundaries and scale limits

No full model was trained or served; corpora were synthetic and small; KV-cache results are analytical rather than measured in a serving runtime; quality, latency under decode, sliding-window attention, KV quantization details, and non-transformer architectures were not validated.

## Claim scope

Measured on five 1 MiB synthetic text/code/JSON/Unicode corpora with raw byte tokenization versus tiktoken GPT-2 and cl100k_base BPE; transformer long-context RAM conclusion is based on measured token expansion plus explicit KV-cache memory formulas for GPT-2-small-like, 1B-like, and LLaMA-7B-like fp16 KV configurations.

## Why it stopped

Proxy/local evidence early-falsifies byte tokenization alone as a RAM-saving strategy for standard long-context transformer CPU inference; this is not a full model-serving validation.

## Recommended next action

Stop as no-paper useful signal unless pursuing a bounded follow-up that directly measures byte-level models with compressed or non-KV per-token state.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU serving comparison for byte tokens with compressed per-position state
- Success threshold: At matched task quality, byte-level compressed-state serving uses at least 20% less peak RSS than the BPE baseline at 16k and 32k effective text contexts without more than 25% throughput loss.
- Stop condition: Stop if byte-level sequence expansion causes peak RSS to exceed the BPE baseline by more than 10% at 16k context, or if matched quality cannot be reached in the bounded small-model setup.

## Evidence references

- Artifact root: `<local-path>/projects/byte-level-tokenizer-for-ram-constrained-long-context-on-cpu-9da7855a1540`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
