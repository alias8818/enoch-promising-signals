# Entropy-Routed Quantization Cascade

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `entropy-routed-quantization-cascade-be1da45d8235`
Run ID: `entropy-routed-quantization-cascade-be1da45d8235-20260601T074844412674+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/5734810fcadd

## What looked useful

Across two GPT-style models and four matched mixed-precision budgets, low-entropy high-precision routing beat random and high-entropy high-precision routing; entropy correlated negatively with per-token precision benefit.

## Boundaries and scale limits

Only final hidden states before the LM head were quantized; no intermediate-layer, KV-cache, weight, benchmark-corpus, generation-quality, or runtime-throughput validation was performed.

## Claim scope

In a bounded final-hidden-state quantization probe on distilgpt2 and gpt2, entropy is a useful routing signal, but the observed best direction is assigning high precision to low-entropy token positions rather than high-entropy positions.

## Why it stopped

Closed as no-paper useful signal: the local proxy supports entropy as a routing signal but is not a full validation of an end-to-end quantization cascade.

## Recommended next action

Run a bounded deepen test that applies low-entropy versus high-entropy routing to KV-cache or residual-stream quantization on a standard validation slice with perplexity and runtime counters.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Low-Entropy Routing for KV-Cache Quantization
- Success threshold: Low-entropy routing must reduce KL-to-baseline or perplexity degradation by at least 10% versus random routing at the same average bit budget in both tested models without erasing expected memory savings.
- Stop condition: Stop if low-entropy routing fails to beat random routing on either model or if routing overhead eliminates the practical memory/latency benefit.

## Evidence references

- Artifact root: `<local-path>/projects/entropy-routed-quantization-cascade-be1da45d8235`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
