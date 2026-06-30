# Home CPU Long-Context Inference via Selective KV Pruning

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `home-cpu-long-context-inference-via-selective-kv-pruning-91908f5ed964`
Run ID: `home-cpu-long-context-inference-via-selective-kv-pruning-91908f5ed964-20260608T043303522696+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/4965522b9dfe

## What looked useful

Selective pruning beat recency on cosine similarity in 24/24 paired trials at 12.5%, 25%, and 50% keep. Mean cosine gains over recency were +0.232, +0.146, and +0.061. Compacted attention-only speedups for selective pruning were 25.2x, 14.2x, and 3.2x; including naive select/gather they were 2.17x, 1.62x, and 0.68x.

## Boundaries and scale limits

No real LLM, tokenizer, quantized KV cache, multi-head/multi-layer decoder, perplexity, retrieval task, or end-to-end tokens/sec measurement was run. Naive per-token gather/copy overhead can erase speedups unless pruning compacts the cache periodically and amortizes selection.

## Claim scope

In a synthetic NumPy CPU single-token attention proxy at context length 16,384 and head dimension 128, warmup-attention salience pruning preserved full-attention output direction better than recency or random pruning while reducing compacted KV attention time and KV bytes touched.

## Why it stopped

Proxy evidence supports the mechanism but is not direct/full validation of home CPU long-context LLM inference.

## Recommended next action

Stop this run as no-paper useful signal; next concrete action is a bounded real-decoder follow-up that implements periodic salience KV compaction and measures tokens/sec plus quality against full KV and recency pruning.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU Decoder Test of Periodic Salience KV Compaction
- Success threshold: At 25% KV keep, salience pruning achieves at least 1.3x end-to-end decode tokens/sec over full KV and beats recency pruning on quality at matched keep ratio without more than 5% relative perplexity degradation from full KV.
- Stop condition: Stop if salience pruning is not faster than full KV after amortized compaction or if it does not beat recency pruning on quality at matched keep ratio.

## Evidence references

- Artifact root: `<local-path>/projects/home-cpu-long-context-inference-via-selective-kv-pruning-91908f5ed964`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
