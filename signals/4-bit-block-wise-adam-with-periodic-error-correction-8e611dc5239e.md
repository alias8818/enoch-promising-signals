# 4-bit Block-wise Adam with Periodic Error Correction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `4-bit-block-wise-adam-with-periodic-error-correction-8e611dc5239e`
Run ID: `4-bit-block-wise-adam-with-periodic-error-correction-8e611dc5239e-20260629T060220565029+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/515d21294efc

## What looked useful

The tested q4 Adam variants diverged to NaN across learning rates 1e-3 through 1e-5 and block sizes 32, 64, and 256. First-step diagnostics showed 62-64% of second-moment values quantized to zero despite nonzero gradients, inflating the worst pre-LR update from 31.62 to 117352.54. A stable tiny-LR q4 setting trained but was about 3.4x worse than standard Adam after 1000 steps, and periodic error correction did not improve mean loss while raising theoretical state memory to 65.6% of fp32 Adam.

## Boundaries and scale limits

No LLM-scale, real-corpus, packed-kernel, or long-horizon training was run. The result applies to the tested optimizer design, block sizes, learning-rate sweep, and small CUDA MLP task, not to all possible 4-bit Adam designs.

## Claim scope

Bounded GPU prototype on a synthetic teacher-student MLP regression task: naive linear 4-bit block-wise Adam second-moment quantization is unstable at normal Adam learning rates, and fp16 residual periodic error correction did not recover Adam-like behavior or preserve most memory savings.

## Why it stopped

Proxy early falsification, not full validation: the bounded implementation failed to preserve Adam-like stability at normal learning rates, and periodic fp16 residual correction was too late to prevent first-step denominator collapse.

## Recommended next action

Stop this naive design as no-paper evidence; if continuing, test a distinct second-moment quantizer that guarantees nonzero denominators, such as log-domain or floored 4-bit v-state, before any scale-up.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Nonzero 4-bit second-moment quantization for Adam
- Success threshold: No NaNs for lr >= 3e-4 with block size >= 64, mean final validation MSE <= 1.25x Adam32 after 1000 steps, and theoretical optimizer-state memory <= 25% of Adam32.
- Stop condition: Stop if first-step diagnostics still show more than 5% nonzero-gradient second-moment entries dequantizing to zero or if 3-seed validation loss remains above 2x Adam32 at the best stable learning rate.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-block-wise-adam-with-periodic-error-correction-8e611dc5239e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
