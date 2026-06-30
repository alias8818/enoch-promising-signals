# Multi-corpus GPT-2 KV residual decode robustness test

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `multi-corpus-gpt-2-kv-residual-decode-robustness-test-0c0ea680bd`
Run ID: `multi-corpus-gpt-2-kv-residual-decode-robustness-test-0c0ea680bd-20260523T194442920991+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Quantized KV Cache with Per-Head Residual Channels: enoch://control-plane/projects/quantized-kv-cache-with-per-head-residual-channels-007da086960e/runs/quantized-kv-cache-with-per-head-residual-channels-007da086960e-20260523T190843160160+0000
- Parent run decision: Held-out end-to-end GPT-2 KV residual decode test: enoch://control-plane/projects/held-out-end-to-end-gpt-2-kv-residual-decode-test-0adb2a0ea3/runs/held-out-end-to-end-gpt-2-kv-residual-decode-test-0adb2a0ea3-20260523T192913400832+0000

## What looked useful

Small single-layer Gaussian KV-cache perturbations produced near-zero aggregate NLL deltas (+0.0009 to +0.0019), while matched residual-stream perturbations were materially worse at mid/late layers, especially block 5 scale 0.03 (+0.0720 NLL, about 51.8x matched KV). No-op cache clone was exactly zero delta, and EOS-only plus zero-all-KV controls raised NLL by +2.6802 and +2.1631 respectively, confirming the metric is sensitive to context/cache removal.

## Boundaries and scale limits

No external benchmark corpora, no larger GPT-2 or 7B+ models, no long-context serving traces, no quantized/runtime cache implementation, no real hardware fault injection, and no generation-level human or task evaluation.

## Claim scope

GPT-2-small fp16 on GB10, six fixed synthetic corpus-style prompt sets, 48 prompt/continuation examples, fixed seeds 17/29/43, Gaussian single-layer KV-cache and residual-stream perturbations at scales 0.01 and 0.03, scored by held-out continuation NLL delta versus clean cache decode.

## Why it stopped

Tier 2 local evidence supports a bounded mechanism signal but relies on synthetic corpus-style prompts and GPT-2-small only, so it is not publication-grade robustness evidence.

## Recommended next action

Stop this run as a no-paper useful signal; run one bounded deepen follow-up on real benchmark corpora with logit KL, continuation NLL, and sampled-generation stability before considering any paper gate.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Benchmark-corpus GPT-2 KV perturbation robustness with logit and generation metrics
- Success threshold: Across real corpora and fixed seeds, small KV perturbations have mean NLL delta below 10 percent of matched residual perturbations and below +0.01 absolute NLL, while context-removal or zero/all-layer KV controls exceed +1.0 NLL delta.
- Stop condition: Stop as unsupported if benchmark-corpus KV perturbations exceed +0.05 mean NLL delta, exceed 50 percent of matched residual perturbation impact, or show unstable/non-reproducible direction across seeds and corpora.

## Evidence references

- Artifact root: `<local-path>/projects/multi-corpus-gpt-2-kv-residual-decode-robustness-test-0c0ea680bd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
