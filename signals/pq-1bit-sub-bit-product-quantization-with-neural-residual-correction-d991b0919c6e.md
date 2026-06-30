# PQ-1bit: Sub-Bit Product Quantization with Neural Residual Correction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `pq-1bit-sub-bit-product-quantization-with-neural-residual-correction-d991b0919c6e`
Run ID: `pq-1bit-sub-bit-product-quantization-with-neural-residual-correction-d991b0919c6e-20260628T071052084196+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5c84415f6acd

## What looked useful

Across three medium seeds on a nonlinear manifold, PQ+MLP reduced held-out MSE by 53.85% versus binary PQ and improved recall@10 from 0.3032 to 0.3212. On Gaussian controls, PQ+MLP worsened MSE by 0.82% and did not improve recall@10. Shuffled residual training stayed near baseline, supporting a real code/residual mechanism.

## Boundaries and scale limits

Three synthetic medium seeds only; no real embedding corpus, no OPQ/PQ production baseline suite, no latency-optimized ANN serving path, and decoder parameters are amortized rather than included in per-vector bit rate.

## Claim scope

Synthetic 64-dimensional vector reconstruction at 0.25 bits/dimension shows neural residual correction helps when vectors have shared nonlinear latent structure across product-quantization subspaces, but not when residuals are independent Gaussian noise.

## Why it stopped

Current evidence is useful but synthetic/proxy-only and therefore not sufficient for a paper or broad validation.

## Recommended next action

Run a bounded real-embedding validation on a public vector dataset with matched PQ/OPQ baselines, decoder-parameter accounting, and recall/latency metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-embedding validation of sub-bit PQ with neural residual correction
- Success threshold: At least 20% reconstruction MSE reduction and at least 5% relative recall@10 improvement over the strongest matched-memory non-neural baseline, with less than 25% query latency overhead.
- Stop condition: Stop if the neural residual decoder fails to beat matched OPQ/PQ recall by 2% relative on the first real dataset or if decoder latency overhead exceeds 50% in the bounded prototype.

## Evidence references

- Artifact root: `<local-path>/projects/pq-1bit-sub-bit-product-quantization-with-neural-residual-correction-d991b0919c6e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
