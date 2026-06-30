# Speculative Decoding with Extreme Quantization Drafters

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-decoding-with-extreme-quantization-drafters-b981a096780e`
Run ID: `speculative-decoding-with-extreme-quantization-drafters-b981a096780e-20260603T194032749833+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/fd1189fd69cb

## What looked useful

Naive per-output-channel post-training quantization is an early falsification for extreme 4/3/2/1-bit drafters in this local probe: 4-bit mean acceptance was 0.2969 with best modeled speedup 0.9234, and 3-bit or lower acceptance was below 0.05 except 2-bit at 0.0413.

## Boundaries and scale limits

Small 82M-parameter target, 12 fixed prompts, 768 token positions per bit-depth, no trained drafter, no quantization-aware training, and no real low-bit inference kernels; speedup is analytic rather than measured serving throughput.

## Claim scope

On distilgpt2 with target-greedy contexts and emulated same-architecture post-training quantized drafters, 8-bit preserves speculative-decoding acceptance well, but naive 4-bit and lower quantization does not produce modeled speedup.

## Why it stopped

Controlled local mechanism evidence is sufficient for a useful negative signal but not for a full validation; throughput was modeled and extreme low-bit naive drafters failed the acceptance threshold.

## Recommended next action

Stop this no-paper run; the bounded next test is quantization-aware distillation or training of a 2-4 bit drafter, not further naive post-training quantization.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Quantization-aware distilled 4-bit speculative drafter probe
- Success threshold: Mean acceptance >= 0.75 and modeled gamma-4 speedup > 1.2 on held-out prompts; if real kernels are available, measured end-to-end speedup > 1.1.
- Stop condition: Stop if quantization-aware 4-bit acceptance remains below 0.55 after a bounded calibration/training run or if the modeled speedup stays <= 1.0.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-with-extreme-quantization-drafters-b981a096780e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
