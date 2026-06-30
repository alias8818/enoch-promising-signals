# Early-Exit Speculative Decoding for VRAM-Free Drafting

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `early-exit-speculative-decoding-for-vram-free-drafting-53993551f2cf`
Run ID: `early-exit-speculative-decoding-for-vram-free-drafting-53993551f2cf-20260522T164338990947+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/a993b80fdf91

## What looked useful

Intermediate layers were not reliable enough to serve as practical draft heads without training. Best distilgpt2 layer 4/6 reached 0.645 raw top-1 agreement, mean accepted run length 1.67, and optimistic speedup upper bound 0.979; GPT-2-small layer 9/12 reached only 0.285 raw agreement and mean accepted run length 0.376. Confidence gating helped only the late distilgpt2 layer and did not provide enough cheap persistent drafts.

## Boundaries and scale limits

Tested distilgpt2 for 640 generated-token positions and gpt2 for 288 generated-token positions on a compact built-in prompt suite. Actual block speculative decoding wall-clock speedup, larger corpora, modern 7B+ LMs, and trained/calibrated early-exit heads were not tested.

## Claim scope

Bounded early falsification for strict no-training, no-separate-draft-model early-exit speculative drafting on GPT-2-class causal LMs using existing intermediate hidden states plus the base LM head.

## Why it stopped

Proxy and small-model direct metrics did not meet the success threshold: no tested layer achieved both high agreement and persistent accepted runs at a cheap depth, and optimistic practical speedup was below or not meaningfully above baseline.

## Recommended next action

Stop this strict no-training VRAM-free drafting hypothesis as an early proxy falsification; if continuing, run a bounded adjacent test with a calibrated early-exit head and an actual block verifier.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated Early-Exit Head With Block Verification
- Success threshold: At least 1.1x measured wall-clock speedup versus greedy decoding, mean accepted block length above 2, no more than 1% token divergence under greedy-equivalent verification, and less than 5% additional VRAM over the base model.
- Stop condition: Stop if calibrated agreement remains below 70% at layers costing half the model or less, or if measured wall-clock speedup remains at or below 1.0x after implementing block verification.

## Evidence references

- Artifact root: `<local-path>/projects/early-exit-speculative-decoding-for-vram-free-drafting-53993551f2cf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
