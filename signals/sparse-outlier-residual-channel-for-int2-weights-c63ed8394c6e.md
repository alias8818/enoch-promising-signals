# Sparse Outlier Residual Channel for INT2 Weights

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sparse-outlier-residual-channel-for-int2-weights-c63ed8394c6e`
Run ID: `sparse-outlier-residual-channel-for-int2-weights-c63ed8394c6e-20260525T233640882957+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/23d032b8c77b

## What looked useful

Unstructured top-error residuals improved output relative MSE by about 9-34% versus INT2, strongest on heavy-tailed/outlier cases, but at 2.93 bits/weight remained 1.95x to 7.39x worse than INT3. At 3.95 bits/weight they still remained 1.64x to 6.57x worse than INT3. Whole-column residuals were cheaper but much weaker.

## Boundaries and scale limits

No pretrained transformer weights, perplexity, hardware kernels, or serving throughput were tested. Results are limited to synthetic Gaussian, Laplace, Student-t, mixture-outlier, and channel-outlier matrices with groupwise quantization.

## Claim scope

Bounded NumPy linear-layer proxy with synthetic 512 x 512 weight matrices: INT2 plus sparse residuals reduces quantization output error versus INT2 and random residual controls, but does not approach dense INT3 accuracy under explicit bits/weight accounting.

## Why it stopped

Proxy/early falsification of the practical storage-efficiency claim: sparse residuals help, but not enough to compete with INT3 in this controlled test.

## Recommended next action

Stop this proxy as no-paper useful evidence; next bounded test should use pretrained transformer layers with activation-aware residual placement and compare against INT2, random residuals, and dense INT3 at no more than about 3 bits/weight.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-aware INT2 sparse residuals on pretrained transformer layers
- Success threshold: At <=3.0 effective bits/weight, INT2 plus residual should reduce at least 80% of the INT2-to-INT3 output-error gap on most tested layers or show a corresponding perplexity gap closure, while beating random residual controls.
- Stop condition: Stop if activation-aware residuals remain more than 1.5x worse than INT3 output error at comparable bits/weight or if metadata/runtime overhead erases the storage benefit.

## Evidence references

- Artifact root: `<local-path>/projects/sparse-outlier-residual-channel-for-int2-weights-c63ed8394c6e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
