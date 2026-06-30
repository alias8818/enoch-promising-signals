# Sub-2-bit Embedding via Product Quantization + Residual Codebook

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sub-2-bit-embedding-via-product-quantization-residual-codebook-817eff2e5484`
Run ID: `sub-2-bit-embedding-via-product-quantization-residual-codebook-817eff2e5484-20260628T171511168772+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ca36c73b2e4f

## What looked useful

Residual vector codebooks consistently improved PQ reconstruction. At 1.375 index bits/dimension, PQ M16 K32 plus residual K256 beat 2-bit scalar NMSE on Gaussian, clustered-low-rank, and smooth-token-like synthetic tables, but recall@10 lagged the 2-bit scalar baseline on two of three distributions.

## Boundaries and scale limits

Evidence is synthetic and offline-only: no real pretrained embedding table, no downstream model perplexity or retrieval task, no optimized decode kernel, and small-table codebook overhead can push total storage above 2 bits per dimension for larger codebooks.

## Claim scope

On synthetic 64-dimensional embedding tables, product quantization plus one residual full-vector codebook can improve held-out reconstruction below 2 index bits per dimension, often beating a 2-bit scalar quantization baseline on normalized MSE; nearest-neighbor preservation is mixed.

## Why it stopped

Synthetic proxy evidence supports reconstruction but not robust neighbor preservation, so this is not a full validation or paper-positive result.

## Recommended next action

Stop this run as no-paper useful signal; next run should test pretrained GPT-2-small-class embedding matrices with downstream logits or perplexity and neighbor-preservation controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Test sub-2-bit PQ plus residual codebook on real pretrained embedding matrices
- Success threshold: At less than 2 total bits per dimension after codebook amortization, PQ plus residual should beat matched baselines on downstream logits or perplexity proxy and not lose more than 10 percent relative recall@10 versus the best matched baseline.
- Stop condition: Stop as negative if reconstruction gains do not translate to downstream logits/perplexity improvement or if codebook overhead prevents sub-2-bit total storage at realistic vocabulary sizes.

## Evidence references

- Artifact root: `<local-path>/projects/sub-2-bit-embedding-via-product-quantization-residual-codebook-817eff2e5484`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
