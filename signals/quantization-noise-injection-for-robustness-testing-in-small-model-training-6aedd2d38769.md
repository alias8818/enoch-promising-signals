# Quantization Noise Injection for Robustness Testing in Small Model Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantization-noise-injection-for-robustness-testing-in-small-model-training-6aedd2d38769`
Run ID: `quantization-noise-injection-for-robustness-testing-in-small-model-training-6aedd2d38769-20260607T234515265877+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/3b3ec81cde58

## What looked useful

Naive quantization-noise injection slightly improved mean int4 fake-quantized accuracy (+0.00249) but the paired 95% CI crossed zero; it consistently reduced clean, int8, and input-corruption accuracy while increasing train loss and runtime.

## Boundaries and scale limits

No transformer or GPT-2-small-class model, no language modeling corpus, no real quantized kernels, no deployment calibration, and no long training. Evidence is limited to 20 paired seeds on a synthetic small classification task.

## Claim scope

Bounded CPU-only NumPy MLP experiment on a synthetic noisy two-class spiral task: always-on 4-bit-scaled quantization-noise injection during training did not improve general robustness and only showed a weak, statistically uncertain int4 fake-quantization benefit.

## Why it stopped

Proxy early falsification of the broad robustness claim: the small reproducible test did not support general robustness improvement from naive always-on quantization-noise injection.

## Recommended next action

Stop this run as a no-paper useful signal; before any scale-up, run a bounded schedule/amplitude study that requires int4 robustness gains without clean or corruption-robustness regression.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Quantization-noise schedule and amplitude sweep for preserving clean robustness
- Success threshold: At least one schedule improves int4 accuracy by >=0.005 mean paired delta with 95% CI above zero while clean and input-noise sigma 0.30 deltas remain within +/-0.0015 and have no clear negative CI.
- Stop condition: Stop if all schedules either fail to improve int4 accuracy with CI above zero or improve int4 only by degrading clean/input-corruption robustness beyond the threshold.

## Evidence references

- Artifact root: `<local-path>/projects/quantization-noise-injection-for-robustness-testing-in-small-model-training-6aedd2d38769`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
