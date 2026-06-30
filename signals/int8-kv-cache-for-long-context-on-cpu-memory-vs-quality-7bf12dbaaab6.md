# INT8 KV Cache for Long Context on CPU: Memory vs Quality

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int8-kv-cache-for-long-context-on-cpu-memory-vs-quality-7bf12dbaaab6`
Run ID: `int8-kv-cache-for-long-context-on-cpu-memory-vs-quality-7bf12dbaaab6-20260619T023231499095+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/2fb0acef370f

## What looked useful

Quantization granularity is the main practical signal: per-token/vector INT8 produced no proxy threshold failures, whereas per-head/global INT8 produced 9 failures, all on outlier contexts, despite slightly better memory savings.

## Boundaries and scale limits

No full language model, no perplexity or generation-quality evaluation, no real prompt corpus, no fused CPU inference kernel, no batching/serving latency measurement, and max tested synthetic context length was 8192 tokens with 8 heads and head_dim 64.

## Claim scope

Synthetic CPU attention-only proxy for long-context KV-cache quantization. Per-token/vector INT8 KV cache preserved attention-output fidelity across 36 bounded cases while reducing stored KV bytes by 73.44% versus FP32; per-head/global INT8 showed outlier-context top-1 attention failures.

## Why it stopped

No-paper closure: this is useful attention-proxy evidence, not full-model validation of long-context CPU quality.

## Recommended next action

Run a bounded direct small-language-model CPU evaluation comparing FP32/FP16/per-token INT8/per-head INT8 KV caches on perplexity, needle retrieval, and generation consistency before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-LM direct evaluation of per-token INT8 KV cache on CPU
- Success threshold: Per-token/vector INT8 reduces KV-cache storage by at least 65% versus FP32 and at least 40% versus FP16 while keeping perplexity degradation below 2% versus FP16 and long-context retrieval accuracy within 1 percentage point on the bounded prompt set.
- Stop condition: Stop as negative if per-token/vector INT8 exceeds 5% perplexity degradation versus FP16 or loses more than 5 percentage points retrieval accuracy on the bounded direct model test.

## Evidence references

- Artifact root: `<local-path>/projects/int8-kv-cache-for-long-context-on-cpu-memory-vs-quality-7bf12dbaaab6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
