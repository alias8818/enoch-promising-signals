# Hierarchical Chunk KV Merging for Eight-Thousand-Token Local Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hierarchical-chunk-kv-merging-for-eight-thousand-token-local-context-ea9d4e147efb`
Run ID: `hierarchical-chunk-kv-merging-for-eight-thousand-token-local-context-ea9d4e147efb-20260607T130422465378+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/94ace52d2eee

## What looked useful

Bulk old-context attention mass can be preserved by weighted chunk centroids, but this is insufficient for local-context fidelity: rare high-salience old keys with high exact attention mass are averaged away and produce large value errors even with smaller chunks and more representatives.

## Boundaries and scale limits

No trained transformer, real text task, perplexity, generation, or production KV-cache kernel was evaluated. Timing is directional because the implementation uses offline Python/PyTorch chunk compression and includes warmup effects.

## Claim scope

Synthetic 8k attention benchmark: query-independent per-chunk KV mean/k-means merging with log-count weights preserves outputs on smooth clustered and diffuse random old contexts at about 8x-14x compression, but fails a rare old-key retrieval stress case.

## Why it stopped

Proxy early falsification of query-independent hierarchical chunk KV merging as a general 8k local-context replacement: synthetic smooth-context results were positive, but the direct rare-retrieval proxy failed with mean needle MSE around 1.9-2.1 and max absolute errors around 3-5 while exact attention assigned about 0.477 mass to the old needle.

## Recommended next action

Stop this run as a no-paper useful signal; test a salience-protected or query-aware residual KV merge that keeps rare high-match old keys exact before considering model-level validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Salience-Protected Residual KV Merge for Rare Old-Key Retrieval
- Success threshold: At 8x or better compression, preserve clustered/random cosine >= 0.99 and reduce needle output MSE by at least 10x versus kmeans_r8 while keeping max absolute error below 1.0 across three seeds.
- Stop condition: Stop if residual exact slots cannot reduce needle MSE below 0.2 at 8x compression or if preserving retrieval requires compression below 2x.

## Evidence references

- Artifact root: `<local-path>/projects/hierarchical-chunk-kv-merging-for-eight-thousand-token-local-context-ea9d4e147efb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
