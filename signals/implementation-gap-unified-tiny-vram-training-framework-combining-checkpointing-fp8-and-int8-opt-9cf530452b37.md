# implementation_gap: Unified Tiny-VRAM Training Framework Combining Checkpointing, FP8, and Int8 Optimizer

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `implementation-gap-unified-tiny-vram-training-framework-combining-checkpointing-fp8-and-int8-opt-9cf530452b37`
Run ID: `implementation-gap-unified-tiny-vram-training-framework-combining-checkpointing-fp8-and-int8-opt-9cf530452b37-20260610T051005835068+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/6d2ab989b5e9

## What looked useful

Blockwise int8 optimizer state reduced persistent optimizer bytes by about 75%; the full stack reduced peak allocation by 36.9% in a 69.6M-parameter probe and 57.1% in an activation-stress 168.9M-parameter probe. Per-tensor int8 state was unstable and should be avoided.

## Boundaries and scale limits

Synthetic repeated-token data only; 3-8 optimizer steps; no real corpus, no GPT-2-small-class baseline, no long-run stability or downstream quality metrics; FP8 tested as autograd saved-tensor storage rather than production FP8 compute kernels.

## Claim scope

On synthetic single-GPU GPT-style training probes up to 168.9M parameters on GB10, activation checkpointing plus blockwise int8 persistent AdamW state reduced measured CUDA peak allocation while preserving a short loss-decrease signal; FP8 saved-tensor hooks were functional but did not add measured peak reduction beyond checkpointing in the tested shapes.

## Why it stopped

Closed as a no-paper useful signal: the evidence is a short synthetic proxy, not a full validation.

## Recommended next action

Run a bounded real-data GPT-2-small-class confirmation with the blockwise int8 optimizer, checkpointing, and FP8 saved-tensor ablations; stop paper consideration until real loss curves and stability are measured.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-data confirmation of blockwise int8 optimizer plus checkpointed FP8 saved tensors
- Success threshold: At least 30% peak CUDA allocation reduction versus AdamW baseline and validation loss within 5% of baseline at the same step budget, with no divergence or NaNs.
- Stop condition: Stop if the full stack diverges, produces NaNs, or validation loss is more than 10% worse than baseline after the planned short run.

## Evidence references

- Artifact root: `<local-path>/projects/implementation-gap-unified-tiny-vram-training-framework-combining-checkpointing-fp8-and-int8-opt`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
