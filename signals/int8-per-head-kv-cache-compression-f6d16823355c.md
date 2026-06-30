# INT8 Per-Head KV Cache Compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int8-per-head-kv-cache-compression-f6d16823355c`
Run ID: `int8-per-head-kv-cache-compression-f6d16823355c-20260607T012100709404+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ef1d873df424

## What looked useful

Per-head scaling is a better granularity than a single global cache scale and can preserve logits in small real-model probes, but practical serving value depends on fused implementation and outlier-robust quantization.

## Boundaries and scale limits

No full perplexity/task evaluation, no fused INT8 attention kernel, no production KV traces, no multi-request serving benchmark, and only a small GPT-2-family model was directly probed.

## Claim scope

Bounded GPU probes show that per-head symmetric INT8 KV-cache quantization gives about 2x KV storage reduction and small next-token logit perturbation on distilgpt2 at 512 and 1024 token prefixes, while synthetic outlier caches expose substantial error and a naive dequantize-then-attend path is slower than fp16.

## Why it stopped

No-paper closure: bounded evidence supports the mechanism but also shows naive serving is slower than fp16 and robustness/full-quality evidence is missing.

## Recommended next action

Run a bounded follow-up that evaluates perplexity and generation quality on a small public corpus with cache quantization applied during autoregressive decoding, and include an outlier-aware variant before considering kernel work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Autoregressive Quality Probe for Outlier-Aware INT8 Per-Head KV Cache
- Success threshold: Per-head or outlier-aware INT8 cache achieves at least 1.95x KV storage reduction, less than or equal to 1 percent perplexity regression versus fp16 on the bounded corpus, and no systematic top-k instability across decode steps.
- Stop condition: Stop if perplexity regression exceeds 3 percent, top-k instability is systematic, or outlier handling erases the practical memory benefit below 1.8x.

## Evidence references

- Artifact root: `<local-path>/projects/int8-per-head-kv-cache-compression-f6d16823355c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
