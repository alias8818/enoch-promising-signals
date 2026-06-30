# ChunkKV: Prefix/Suffix Exact + Middle Compressed Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `chunkkv-prefix-suffix-exact-middle-compressed-context-50ccc583c5ad`
Run ID: `chunkkv-prefix-suffix-exact-middle-compressed-context-50ccc583c5ad-20260621T073505039464+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/37227f7a15f9

## What looked useful

Uniform middle KV chunk averaging removes addressable exact middle tokens. In 200-trial sweeps, prefix/suffix needles retained 1.000 hit rate and 1.000 value cosine, while middle needles at 3.37x-3.95x compression had 0.000 hit rate and near-zero value cosine despite full attention cosine 1.000.

## Boundaries and scale limits

No trained transformer, no real language task, no learned compressor, no multi-layer dynamics, and no GPU/model-serving benchmark. Results are CPU-only NumPy proxy evidence, not full architecture validation.

## Claim scope

Synthetic single-attention retrieval proxy for a 4096-token cache with exact first/last 512 KV entries and uniformly averaged middle KV chunks. Endpoint retrieval is preserved, but exact middle retrieval is not preserved by mean or mean-rescaled-key chunk compression.

## Why it stopped

Proxy/early falsification: exact prefix/suffix retention worked, but simple middle chunk compression failed exact middle retrieval under the direct synthetic attention mechanism tested.

## Recommended next action

Stop this simple ChunkKV variant as a no-paper proxy falsification; only continue with a bounded learned or salience-preserving middle compressor test that must retain exact middle retrieval.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Salience-preserving middle ChunkKV retrieval probe
- Success threshold: At >=3x compression on the 4096-token synthetic probe, middle-needle argmax hit rate >=0.90 and mean value cosine >=0.90 while prefix/suffix hit rate remains 1.00.
- Stop condition: Stop if middle-needle hit rate remains below 0.50 or mean value cosine remains below 0.70 at >=3x compression after adding salience-preserving exemplars.

## Evidence references

- Artifact root: `<local-path>/projects/chunkkv-prefix-suffix-exact-middle-compressed-context-50ccc583c5ad`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
