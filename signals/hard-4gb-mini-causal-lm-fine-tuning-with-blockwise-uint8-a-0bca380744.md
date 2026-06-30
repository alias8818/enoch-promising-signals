# Hard-4GB mini causal-LM fine-tuning with blockwise uint8 AdamW offload

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `hard-4gb-mini-causal-lm-fine-tuning-with-blockwise-uint8-a-0bca380744`
Run ID: `hard-4gb-mini-causal-lm-fine-tuning-with-blockwise-uint8-a-0bca380744-20260608T051412680520+0000`

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

- Parent run decision: 8-bit AdamW with uint8 optimizer state offloading for sub-4GB VRAM fine-tuning: enoch://control-plane/projects/8-bit-adamw-with-uint8-optimizer-state-offloading-for-sub-4gb-vram-fine-tuning-da390a46e0d0/runs/8-bit-adamw-with-uint8-optimizer-state-offloading-for-sub-4gb-vram-fine-tuning-da390a46e0d0-20260608T005050641046+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/87067f92a14c

## What looked useful

Blockwise uint8 AdamW moment storage was not immediately destructive for mini causal-LM fine-tuning and materially reduced optimizer-state bytes, but this remains no-paper bounded mechanism evidence.

## Boundaries and scale limits

Not tested on real text, pretrained weights, GPT-2-small-class scale, a strict 4 GiB memory cap, or long-run convergence. The simple CPU/offload implementation was about 3.1x slower than fp32 AdamW in the controlled run.

## Claim scope

A 3.44M-parameter decoder-only causal LM on a deterministic synthetic token stream can train for 80 steps with CPU/offload-style blockwise uint8 AdamW moments, matching fp32 AdamW final loss within the Tier-1 threshold while reducing optimizer-state storage by about 4x.

## Why it stopped

Tier-1 controlled small direct test completed and produced useful mechanism support, but not full hard-4GB validation or publication-grade evidence.

## Recommended next action

Run a bounded GPT-2-small-class or memory-capped pretrained causal-LM fine-tune with a real dataset, identical fp32 AdamW baseline, and measured <=4 GiB memory budget before considering paper readiness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Memory-capped GPT-2-small-class blockwise uint8 AdamW offload fine-tune
- Success threshold: Candidate stays within <=4 GiB measured memory, completes the planned fine-tune segment without NaN/divergence, reaches final validation loss within 1.25x of fp32 AdamW when the baseline can run, and keeps optimizer-state storage at least 2.5x smaller than fp32 AdamW.
- Stop condition: Stop if the candidate exceeds the 4 GiB budget, diverges/NaNs, is more than 1.25x worse than baseline final validation loss after the planned segment, or offload overhead makes the bounded run impractical under documented resource limits.

## Evidence references

- Artifact root: `<local-path>/projects/hard-4gb-mini-causal-lm-fine-tuning-with-blockwise-uint8-a-0bca380744`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
