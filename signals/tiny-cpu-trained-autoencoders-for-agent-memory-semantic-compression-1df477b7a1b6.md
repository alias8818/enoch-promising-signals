# Tiny CPU-Trained Autoencoders for Agent Memory Semantic Compression

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `tiny-cpu-trained-autoencoders-for-agent-memory-semantic-compression-1df477b7a1b6`
Run ID: `tiny-cpu-trained-autoencoders-for-agent-memory-semantic-compression-1df477b7a1b6-20260621T104323618591+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: qwen/qwen3.7-max: enoch://research-facility/provider/qwen/qwen3.7-max/eacd2fdc9cc6

## What looked useful

The cheap reconstruction-autoencoder version of the idea is not viable for this scoped retrieval task. Compression itself remains viable in the proxy because 32-dimensional SVD reached 1.0000 top-1, so future work should test query-aware or contrastive compression rather than plain reconstruction.

## Boundaries and scale limits

Synthetic structured records only; no private operator traces, no real LLM-agent replay corpus, no LLM embedding baseline, and no query-aware autoencoder objective. Runs were CPU-only and under 30 seconds total.

## Claim scope

On a 480-record synthetic repeated-agent memory retrieval benchmark, tiny reconstruction-only NumPy autoencoders at 8-64 latent dimensions did not preserve semantic retrieval identity, while matched SVD compression did.

## Why it stopped

Proxy early falsification: the tested tiny reconstruction autoencoders topped out at 0.0271 top-1 retrieval in the main run and 0.0250 after a small tuning check, versus 1.0000 for 32-dimensional SVD.

## Recommended next action

Stop this reconstruction-only autoencoder line as no-paper evidence; run a bounded query-aware contrastive or denoising autoencoder follow-up against SVD/PCA if continuing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Query-aware tiny autoencoder memory compression
- Success threshold: At 32 latent dimensions, query-aware autoencoder top-1 retrieval is at least 0.90 and within 0.05 absolute of SVD/PCA across three seeds, with clear improvement over reconstruction-only autoencoder.
- Stop condition: Stop if query-aware training remains below 0.50 top-1 at 32 dimensions on the synthetic benchmark or fails to beat reconstruction-only autoencoder by at least 0.20 absolute top-1.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-cpu-trained-autoencoders-for-agent-memory-semantic-compression-1df477b7a1b6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
