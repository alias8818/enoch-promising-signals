# 8-bit Adam Optimizer State Reduction for CPU Training Stability

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `8-bit-adam-optimizer-state-reduction-for-cpu-training-stability-eac6e2f67370`
Run ID: `8-bit-adam-optimizer-state-reduction-for-cpu-training-stability-eac6e2f67370-20260610T141048903018+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/7ed7bd294395

## What looked useful

The stability-critical detail is second-moment quantization: rounding positive v values to zero can make Adam updates explode, while a minimal nonzero-v floor stabilized this bounded CPU task without increasing state bytes.

## Boundaries and scale limits

Synthetic data, small MLP, 300 steps, three seeds, NumPy prototype, theoretical optimizer-state bytes rather than end-to-end trainer RSS savings, and no real language-model or optimized CPU-kernel validation.

## Claim scope

On a NumPy CPU synthetic MLP classification task with 1,191,946 parameters, naive per-tensor 8-bit Adam moment storage reduced optimizer-state bytes by 75% but diverged after one completed step in all three seeds; adding a minimum nonzero bucket for positive second moments preserved the same state reduction and completed all three 300-step runs with final loss comparable to FP32 Adam.

## Why it stopped

Proxy/synthetic CPU evidence is not full validation: it early-falsifies naive 8-bit Adam state and identifies a stabilizing mechanism, but does not establish real-workload training stability or performance.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should validate the nonzero-v 8-bit Adam variant on a real small transformer or real tabular/vision workload with validation loss and measured RSS.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Validate nonzero-v 8-bit Adam state on a real small CPU training workload
- Success threshold: Nonzero-v 8-bit Adam completes all seeds, validation loss is within 5% of FP32 Adam, measured optimizer/training memory is materially lower, and no divergence or non-finite updates occur.
- Stop condition: Stop if nonzero-v 8-bit Adam diverges in at least two seeds, validation loss is more than 10% worse than FP32 Adam, or measured memory savings are not visible outside theoretical state accounting.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-adam-optimizer-state-reduction-for-cpu-training-stability-eac6e2f67370`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
