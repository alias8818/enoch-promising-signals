# Adaptive layer-skip self-speculative decoding on GB10

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `adaptive-layer-skip-self-speculative-decoding-on-gb10-082e6ecec741`
Run ID: `adaptive-layer-skip-self-speculative-decoding-on-gb10-082e6ecec741-20260619T133952885798+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/999e8a3b4411

## What looked useful

Exact self-speculative verification worked, but acceptance was only 3.5% to 8.6% across tested layer exits/adaptive thresholds, producing 0.225x to 0.347x of the KV-cache greedy baseline throughput.

## Boundaries and scale limits

Six fixed prompts, 32 generated tokens per prompt, openai-community/gpt2 in float16 through Hugging Face/PyTorch CUDA. No trained early-exit heads, no production fused inference backend, and no long-context or large-model validation.

## Claim scope

On the local GB10 worker, raw intermediate-layer logits from an unmodified GPT-2-small-class model preserve exact greedy output under self-speculative verification but do not improve throughput for the tested short-generation workload.

## Why it stopped

Early proxy falsification: raw GPT-2 layer exits were exact after verification but had too little token acceptance to offset added draft compute, so the tested mechanism is not a GB10 speedup.

## Recommended next action

Stop this raw-layer-exit variant; only continue with a bounded follow-up that trains or calibrates early-exit draft heads and requires a clear acceptance/throughput threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated early-exit heads for GB10 self-speculative decoding
- Success threshold: Exact greedy match with at least 55% draft-token acceptance and at least 1.10x end-to-end tokens/s versus the full-depth KV-cache baseline on a 6+ prompt, 32+ token benchmark.
- Stop condition: Stop if trained/calibrated exits remain below 30% acceptance or below 0.9x baseline throughput after one bounded training/calibration pass.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-layer-skip-self-speculative-decoding-on-gb10-082e6ecec741`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
