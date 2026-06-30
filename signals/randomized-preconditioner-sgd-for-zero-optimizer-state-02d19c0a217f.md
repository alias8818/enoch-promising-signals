# Randomized Preconditioner SGD for Zero Optimizer State

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `randomized-preconditioner-sgd-for-zero-optimizer-state-02d19c0a217f`
Run ID: `randomized-preconditioner-sgd-for-zero-optimizer-state-02d19c0a217f-20260525T132711600176+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/7cb06f40219f

## What looked useful

Across 3 seeds, condition numbers 1e2/1e4/1e6, and a learning-rate/randomness grid, best random-lognormal diagonal SGD tied or slightly underperformed tuned SGD on every task, while Bernoulli random diagonals were consistently worse and had more divergence. Adam and oracle diagonal controls improved strongly on high-condition-number tasks, confirming that useful curvature information matters but independent stateless randomness did not supply it.

## Boundaries and scale limits

No GPT-2-small, LLM, distributed, mixed-precision, or long-horizon training was run. The result does not rule out structured zero-state methods using side information, block structure, deterministic transforms, or current-batch curvature estimates.

## Claim scope

For independent fresh random diagonal preconditioners with zero optimizer state, bounded convex quadratic and synthetic ill-conditioned linear-regression tests show no meaningful improvement over tuned SGD; randomization mostly behaves like multiplicative gradient noise.

## Why it stopped

Proxy/early falsification: bounded direct optimization tests found no meaningful advantage over tuned SGD for the tested zero-state random preconditioner, and larger model training would not be justified without a stronger small-scale mechanism signal.

## Recommended next action

Stop this independent-random-diagonal variant as a no-paper useful negative signal; only reopen with a materially different structured zero-state mechanism and first require it to beat tuned SGD on the saved quadratic/regression harness.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/randomized-preconditioner-sgd-for-zero-optimizer-state-02d19c0a217f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
