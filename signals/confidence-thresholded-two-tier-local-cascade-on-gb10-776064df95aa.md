# Confidence-Thresholded Two-Tier Local Cascade on gb10

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `confidence-thresholded-two-tier-local-cascade-on-gb10-776064df95aa`
Run ID: `confidence-thresholded-two-tier-local-cascade-on-gb10-776064df95aa-20260610T073430945187+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/01fe695f76d4

## What looked useful

Calibrated two-tier routing produced useful operating points: at the 0.70 budget it averaged 0.8864 accuracy versus 0.8868 for large-only, exited 65.2% of examples at the small model, achieved 1.29x measured routed speedup, and beat random same-exit routing by about 2.7 accuracy points. Raw thresholds had much worse ECE despite sometimes lower expected cost.

## Boundaries and scale limits

Evidence is limited to CIFAR-10 image classification, simple CNN checkpoints trained in a prior project, PyTorch conditional microbatch inference, three seeds, and local GB10 timing. It does not validate LLM cascades, production serving runtimes, jointly trained cascades, or comparisons to early-exit/BranchyNet/MSDNet-style baselines.

## Claim scope

On GB10, using frozen CIFAR-10 small and large CNN checkpoints from a prior local run, a validation-selected calibrated confidence threshold can route a two-tier small-to-large cascade that retains large-model accuracy within about 0.05 percentage points at the 0.70 latency budget while measuring about 1.29x routed speedup versus large-only inference.

## Why it stopped

Useful bounded CIFAR-10 GB10 inference evidence was produced, but the run reused prior checkpoints and does not provide publication-grade novelty, target-domain breadth, or serving-system validation.

## Recommended next action

Stop this run as no-paper useful signal; next run should compare calibrated two-tier routing against a proper early-exit or optimized local-serving baseline under identical GB10 latency accounting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Matched GB10 Latency Comparison of Two-Tier Confidence Routing Versus Early-Exit Serving
- Success threshold: At matched accuracy within 0.2 percentage points of large-only, two-tier routing should achieve measured routed speedup no worse than 95% of the early-exit baseline speedup and retain ECE below 0.01.
- Stop condition: Stop if two-tier routing loses more than 0.5 accuracy points at comparable measured latency, or if routed Python/runtime overhead removes the speedup relative to large-only inference.

## Evidence references

- Artifact root: `<local-path>/projects/confidence-thresholded-two-tier-local-cascade-on-gb10-776064df95aa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
