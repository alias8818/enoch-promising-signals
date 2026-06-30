# Sub-bit product quant with multi-granularity residual

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sub-bit-product-quant-with-multi-granularity-residual-0c1decc1c5e4`
Run ID: `sub-bit-product-quant-with-multi-granularity-residual-0c1decc1c5e4-20260628T205422044742+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ba6eef76f325

## What looked useful

The tested multi-granularity residual allocation was not a same-budget reconstruction win: MSE was 7.05% worse than standard 32-bit PQ on hierarchical data and 8.88% worse on isotropic data. Recall@10 was also worse on hierarchical data, but improved by 0.0102 absolute on isotropic data, suggesting ranking behavior may merit a separate bounded ablation.

## Boundaries and scale limits

No real embedding corpora, learned rotations/OPQ, hardware lookup kernels, large ANN indexes, or production latency measurements were tested. Runs used 2048 train/database vectors, 128 queries, 3 seeds, and two synthetic data regimes.

## Claim scope

Bounded synthetic 64-dimensional vector compression at 32 bits/vector, 0.5 bits/dim, comparing a fixed multi-granularity residual allocation against matched standard PQ and residual PQ baselines.

## Why it stopped

Proxy synthetic evidence is mixed and not paper-ready; the tested method fails the same-budget reconstruction criterion and only shows a small isolated recall signal.

## Recommended next action

Stop this run as a proxy/early falsification of the exact residual allocation; a separate bounded follow-up should test learned rotations and residual-bit allocation against PQ/OPQ/RVQ controls on a small real embedding corpus.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-embedding OPQ/RVQ ablation for sub-bit multi-granularity residual quantization
- Success threshold: At 0.5 bits/dim, multi-granularity residual coding improves recall@10 by at least 0.02 absolute over the best same-budget baseline while matching or improving reconstruction MSE.
- Stop condition: Stop if the method is worse than the best same-budget baseline on MSE and recall@10 on the first real embedding corpus after rotation/bit-allocation tuning.

## Evidence references

- Artifact root: `<local-path>/projects/sub-bit-product-quant-with-multi-granularity-residual-0c1decc1c5e4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
