# Per-head INT8 KV cache halves CPU RAM without perplexity loss

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `per-head-int8-kv-cache-halves-cpu-ram-without-perplexity-loss-5ac970115787`
Run ID: `per-head-int8-kv-cache-halves-cpu-ram-without-perplexity-loss-5ac970115787-20260529T133333816632+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/5be7df449ccc

## What looked useful

Per-head INT8 KV cache uses essentially half of fp16 KV bytes but is sensitive to heavy-tailed/outlier KV values in synthetic attention. Per-token-head scaling is more robust but saved only 46.875% at head_dim 64 with fp32 scales.

## Boundaries and scale limits

No pretrained LM, tokenizer, real text corpus, or serving engine was available in this Python 3.14 CPU environment. Perplexity evidence is a synthetic logit-KL proxy only.

## Claim scope

Synthetic attention probe with 12 heads, head_dim 64, sequence lengths 256/1024/4096, five seeds, and normal/layernorm-like/outlier/student-t KV distributions. Directly supports near-50% KV byte savings for true per-head INT8 scales; does not directly validate real language-model perplexity.

## Why it stopped

No-paper closure: the run produced bounded synthetic evidence, but the original no-perplexity-loss claim was not directly validated and showed outlier sensitivity under proxy tests.

## Recommended next action

Run a direct pretrained small-LM perplexity comparison with fp16 KV vs per-head INT8 KV on a held-out text set; stop treating this run as more than a synthetic mechanism signal.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct small-LM perplexity test for per-head INT8 KV cache
- Success threshold: At context length at least 1024, measured KV-cache memory ratio <= 0.51 vs fp16, perplexity increase <= 0.1%, and no layer/head with token-level KL outliers above a predeclared tolerance.
- Stop condition: Stop if direct perplexity delta exceeds 0.5%, if memory ratio is above 0.55 after scale metadata is counted, or if implementation requires model/runtime changes that make fp16 and INT8 cache paths non-comparable.

## Evidence references

- Artifact root: `<local-path>/projects/per-head-int8-kv-cache-halves-cpu-ram-without-perplexity-loss-5ac970115787`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
