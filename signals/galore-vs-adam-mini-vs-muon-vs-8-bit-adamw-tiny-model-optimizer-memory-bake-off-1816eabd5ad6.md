# GaLore vs Adam-mini vs Muon vs 8-bit AdamW: tiny-model optimizer memory bake-off

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `galore-vs-adam-mini-vs-muon-vs-8-bit-adamw-tiny-model-optimizer-memory-bake-off-1816eabd5ad6`
Run ID: `galore-vs-adam-mini-vs-muon-vs-8-bit-adamw-tiny-model-optimizer-memory-bake-off-1816eabd5ad6-20260621T181803218381+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/842954d06f0a

## What looked useful

Optimizer-state compression was real: on the 5.27M-parameter preset, state bytes versus AdamW were 25.0% for 8-bit AdamW approx, 50.3% for Adam-mini approx, 5.3% for GaLore approx, and 50.0% for Muon approx. Peak CUDA delta versus AdamW was only 82.4%, 88.3%, 77.8%, and 88.3%, respectively, showing that tiny-model memory is not state-only.

## Boundaries and scale limits

Tested only 0.93M and 5.27M parameter models for 3 synthetic training steps on one GB10 GPU. Non-AdamW optimizers are local approximations, not package-identical production implementations. No convergence, validation, mixed-precision, checkpointing, or long-run stability evidence.

## Claim scope

On two synthetic tiny transformer-style CUDA runs, local transparent approximations of 8-bit AdamW, Adam-mini, GaLore, and Muon reduce optimizer state bytes versus AdamW, but end-to-end peak CUDA memory falls much less because non-optimizer memory dominates.

## Why it stopped

Closed as a no-paper useful signal: this proxy directly measured memory mechanics but does not validate exact optimizer implementations or training quality.

## Recommended next action

Run a bounded deepen experiment with real installable optimizer packages where available, mixed precision, a fixed small corpus, and 100-500 training steps reporting memory, tokens/sec, and validation loss.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-package tiny optimizer bake-off with validation curves
- Success threshold: A useful deepen result shows the same qualitative state-memory ranking and at least one optimizer with >=10% end-to-end peak CUDA memory reduction versus AdamW without worse validation loss after the bounded run.
- Stop condition: Stop if real packages cannot run reproducibly on GB10 after install attempts, or if all alternatives either save less than 10% peak CUDA memory or materially degrade validation loss in the bounded run.

## Evidence references

- Artifact root: `<local-path>/projects/galore-vs-adam-mini-vs-muon-vs-8-bit-adamw-tiny-model-optimizer-memory-bake-off-1816eabd5ad6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
