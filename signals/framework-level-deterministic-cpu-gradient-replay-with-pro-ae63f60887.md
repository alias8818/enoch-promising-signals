# Framework-level deterministic CPU gradient replay with process restarts

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `framework-level-deterministic-cpu-gradient-replay-with-pro-ae63f60887`
Run ID: `framework-level-deterministic-cpu-gradient-replay-with-pro-ae63f60887-20260610T152729884910+0000`

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

- Parent run decision: Deterministic-Replay Gradient Verification on CPU: enoch://control-plane/projects/deterministic-replay-gradient-verification-on-cpu-d87145400ce6/runs/deterministic-replay-gradient-verification-on-cpu-d87145400ce6-20260610T144111964244+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b0deda3113ea

## What looked useful

The direct Tier 1 test matched uninterrupted training exactly for per-step gradient hashes, sampled-batch hashes, optimizer state, and final model parameters with RNG restoration; an otherwise identical no-RNG control diverged at step 0 for all 48 steps.

## Boundaries and scale limits

Only 48 synthetic-data training steps, a tiny MLP, single-process CPU execution, deterministic algorithms enabled, and one intra/inter-op thread were tested. Larger models, real data loaders, multi-threaded kernels, distributed execution, GPU, mixed precision, long horizons, and crash-atomic checkpointing remain untested.

## Claim scope

In PyTorch 2.12.0+cpu on a single-thread CPU worker, a tiny dropout MLP with random batch sampling and AdamW replayed exactly across four fresh Python process restarts when checkpoints included model state, optimizer state, step, records, and CPU RNG state.

## Why it stopped

Tier 1 mechanism support was achieved, but the evidence is a small controlled direct test and is not paper-positive.

## Recommended next action

Run a bounded deepen test that adds PyTorch DataLoader workers and multi-threaded CPU execution while keeping exact baseline-vs-restart gradient and parameter hashing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Deterministic CPU replay across process restarts with DataLoader workers and threaded kernels
- Success threshold: Zero gradient, batch/order, optimizer, and final-parameter mismatches across all tested seeds and chunk schedules, with negative controls diverging before or at the first restart boundary.
- Stop condition: Stop if any restored-RNG replay mismatches under deterministic settings after verifying the mismatch is not a harness bug, or if the test exceeds 15 CPU-worker minutes without checkpointed partial metrics.

## Evidence references

- Artifact root: `<local-path>/projects/framework-level-deterministic-cpu-gradient-replay-with-pro-ae63f60887`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
