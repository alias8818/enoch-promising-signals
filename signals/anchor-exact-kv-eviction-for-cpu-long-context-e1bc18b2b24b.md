# Anchor-Exact KV Eviction for CPU Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-exact-kv-eviction-for-cpu-long-context-e1bc18b2b24b`
Run ID: `anchor-exact-kv-eviction-for-cpu-long-context-e1bc18b2b24b-20260603T205143764848+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/8eb4dc190ee9

## What looked useful

Across 60 replicated rows, anchor-exact matched the full-attention oracle on retained-anchor retrieval with mean MSE 6.34e-14 and cosine 1.000 while retaining about 15.99% of KV on average. It failed on old non-anchor retrieval, with mean MSE 1.652 versus sliding-window 0.739, and was roughly tied with sliding on diffuse attention.

## Boundaries and scale limits

No real language model, tokenizer, multi-layer cache interaction, quantized KV cache, production scheduler, or task-quality benchmark was tested. Sequence lengths were limited to 8192 with 64-dimensional synthetic K/V and 128 evaluated queries per run.

## Claim scope

Synthetic single-layer attention simulator: anchor-plus-recent KV retention preserves full-attention outputs when long-range evidence is exactly on retained anchors under a same-budget comparison to sliding-window eviction.

## Why it stopped

Synthetic proxy evidence is complete and supports only a narrow mechanism; it is not direct model-quality evidence and is not paper-ready.

## Recommended next action

Run a bounded direct LM follow-up on a small decoder-only model with long-context retrieval tasks, comparing full KV, same-budget sliding, and anchor-exact caches using fixed and saliency-derived anchors.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-LM Anchor-Exact KV Eviction on Long-Context Retrieval
- Success threshold: At the same retained-KV budget, anchor-exact must improve retrieval accuracy or target-token log probability by at least 10% relative over sliding-window eviction on cases where measured anchor recall is at least 95%, without a CPU latency regression larger than 20%.
- Stop condition: Stop if anchor target recall is below 80% for practical anchor selection or if same-budget anchor-exact does not outperform sliding-window on retained-anchor retrieval prompts.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-exact-kv-eviction-for-cpu-long-context-e1bc18b2b24b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
