# Lossy State Compression with Exact Position Anchors

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `lossy-state-compression-with-exact-position-anchors-19db28626e33`
Run ID: `lossy-state-compression-with-exact-position-anchors-19db28626e33-20260525T095402178368+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3646626a8185

## What looked useful

Across 4096-state, 512-query, 5-seed sweeps, exact-position compression improved top-1 agreement over full-state PCA by 0.0758 to 0.9332 depending on rank and positional weight, with exact-position mean rank near 1.0 whenever positional signal was active.

## Boundaries and scale limits

No real transformer, learned compressor, KV-cache implementation, language-model perplexity, generation, or long-context benchmark was run. Baselines were limited to naive full-state PCA versus content-only PCA with exact positions on 4096-state synthetic sequences.

## Claim scope

Synthetic transformer-KV-like retrieval proxy with random content states, deterministic sinusoidal position coordinates, and PCA lossy compression. Exact/recomputed positions plus lossy content PCA preserved retrieval substantially better than naive full-state PCA at the same lossy content rank.

## Why it stopped

Closed as no-paper useful signal: the proxy supports the mechanism but is synthetic and not direct evidence for real model state compression.

## Recommended next action

Run a bounded real-model KV-cache follow-up on a GPT-2-small-class or similar small transformer comparing dense cache, naive lossy cache, and content-lossy cache with exact RoPE/position reconstruction on long-context retrieval and perplexity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model KV cache test for exact position anchored lossy compression
- Success threshold: Exact-position anchored compression should reduce quality loss by at least 25% relative to naive full-state lossy compression at the same storage budget, without more than 10% decode-time overhead on the tested small model.
- Stop condition: Stop if the exact-position anchored method fails to beat a matched-storage naive or stronger compression baseline on both retrieval accuracy and perplexity/NLL in the small-model setting.

## Evidence references

- Artifact root: `<local-path>/projects/lossy-state-compression-with-exact-position-anchors-19db28626e33`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
