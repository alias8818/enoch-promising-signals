# Cross-Layer KV Cache Sharing with Adapters

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cross-layer-kv-cache-sharing-with-adapters-02f02cc35faf`
Run ID: `cross-layer-kv-cache-sharing-with-adapters-02f02cc35faf-20260604T054604596471+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ae31537fae7b

## What looked useful

Adapter-mediated cross-layer K/V sharing was viable in the toy setting: shared_adapters mean validation loss 0.2190 and accuracy 0.99998 versus baseline loss 0.2227 and accuracy 0.99990, with estimated fp16 KV cache 49152 bytes versus 98304 bytes per sequence. Raw sharing also learned but had worse mean loss 0.3335.

## Boundaries and scale limits

Synthetic delayed-copy only; 4 layers; short context length 64; 300 training steps; no pretrained LLM, natural-language corpus, long-context decoding benchmark, latency benchmark, or production cache implementation.

## Claim scope

On a 4-layer d_model=96 synthetic delayed-copy decoder probe, sharing K/V caches from even layers to adjacent odd layers through per-head linear adapters matched baseline copy accuracy across 3 seeds while reducing estimated fp16 decode KV cache bytes per sequence by 50%.

## Why it stopped

Closed as no-paper useful signal because evidence is synthetic and mechanism-level, not a direct natural-language or serving validation.

## Recommended next action

Run a bounded direct language-model follow-up on a small real text corpus with 8-12 layers, reporting perplexity, decode latency, and measured cache memory versus a parameter-matched baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small Real-Corpus Validation of Adapter-Mediated Cross-Layer KV Sharing
- Success threshold: Adapter sharing achieves validation perplexity within 3% of baseline and measured decode KV cache memory reduction of at least 40%, while raw sharing is worse or no better than adapters.
- Stop condition: Stop if adapter sharing is more than 10% worse in perplexity than baseline after matched training, or if measured decode memory reduction is below 30%.

## Evidence references

- Artifact root: `<local-path>/projects/cross-layer-kv-cache-sharing-with-adapters-02f02cc35faf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
