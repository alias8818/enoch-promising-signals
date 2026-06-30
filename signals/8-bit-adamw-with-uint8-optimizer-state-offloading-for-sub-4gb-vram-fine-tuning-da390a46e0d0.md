# 8-bit AdamW with uint8 optimizer state offloading for sub-4GB VRAM fine-tuning

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `8-bit-adamw-with-uint8-optimizer-state-offloading-for-sub-4gb-vram-fine-tuning-da390a46e0d0`
Run ID: `8-bit-adamw-with-uint8-optimizer-state-offloading-for-sub-4gb-vram-fine-tuning-da390a46e0d0-20260608T005050641046+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/87067f92a14c

## What looked useful

Per-tensor uint8 moment scaling diverged, but 256-element blockwise uint8 scaling was stable: 0.2539 optimizer-state byte ratio, 0.00482 relative L2 parameter error after 25 deterministic steps, and synthetic eval accuracy 0.5483 versus 0.5498 for PyTorch AdamW.

## Boundaries and scale limits

No real LLM fine-tuning, no natural-language task metric, no hard 4GB VRAM cap, and no optimized throughput implementation were tested. Python CPU round-trip updates were about 4.4x slower than PyTorch AdamW on the small training probe.

## Claim scope

A short GB10 proxy experiment supports that blockwise uint8 CPU offloading of AdamW first/second moment state can reduce optimizer-state bytes to about 25.4% of PyTorch AdamW state while preserving deterministic update fidelity and small synthetic MLP training behavior.

## Why it stopped

Proxy/synthetic evidence supports the mechanism but is not direct/full validation for sub-4GB VRAM fine-tuning, so this run stops as no-paper useful signal.

## Recommended next action

Run a bounded real causal-LM fine-tuning test under a hard 4GB VRAM budget, comparing PyTorch AdamW, an established 8-bit optimizer if available, and the blockwise uint8 CPU-offload variant on memory, throughput, and validation loss.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hard-4GB mini causal-LM fine-tuning with blockwise uint8 AdamW offload
- Success threshold: Blockwise uint8 offload completes the same fine-tuning window under 4GB VRAM, reaches validation loss within 5% of the best baseline, and does not exceed a 3x step-time slowdown.
- Stop condition: Stop if the offload variant diverges, exceeds 4GB VRAM, cannot complete the fine-tuning window, or is slower than 3x baseline while providing no unique memory-budget success.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-adamw-with-uint8-optimizer-state-offloading-for-sub-4gb-vram-fine-tuning-da390a46e0d0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
