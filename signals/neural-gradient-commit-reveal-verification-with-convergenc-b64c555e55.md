# Neural-gradient commit-reveal verification with convergence impact

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `neural-gradient-commit-reveal-verification-with-convergenc-b64c555e55`
Run ID: `neural-gradient-commit-reveal-verification-with-convergenc-b64c555e55-20260629T013811884914+0000`

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

- Parent run decision: Commit-Reveal Gradient Verification for Volunteer CPU Workers: enoch://control-plane/projects/commit-reveal-gradient-verification-for-volunteer-cpu-workers-c9a34d5f9ede/runs/commit-reveal-gradient-verification-for-volunteer-cpu-workers-c9a34d5f9ede-20260628T233344862110+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/4b5657fb2df5

## What looked useful

Commit-reveal is useful as a gradient transport/integrity check, not as a standalone Byzantine-gradient correctness mechanism. Post-commit tampering was fully detected in the toy run, while committed poison passed verification and destroyed convergence.

## Boundaries and scale limits

Synthetic Gaussian classification data, small MLP, 8 seeds, 60 epochs, single-process CPU NumPy simulation, no real network latency, no large model, no non-IID production data, no collusion study, and no gradient-correctness proof.

## Claim scope

In a deterministic toy 2-layer MLP with 8 synchronous workers, full-gradient SHA-256 commit/reveal verification preserved convergence under post-commit gradient substitution by rejecting altered reveals, but did not protect against a worker that committed a poisoned gradient from the start.

## Why it stopped

Toy evidence supports only the post-commit integrity mechanism and directly falsifies commit-reveal-alone robustness against committed poisoned gradients.

## Recommended next action

Stop this run as no-paper useful evidence; next bounded test should combine commit-reveal with robust aggregation or a gradient-validity layer and measure whether committed poisoned gradients are rejected without harming clean convergence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Commit-reveal plus robust aggregation against committed poisoned gradients
- Success threshold: Recover at least 90% final test accuracy under committed-poison attack while keeping clean accuracy within 1 percentage point of the clean baseline and detecting or neutralizing at least 95% of poisoned updates.
- Stop condition: Stop if the added layer cannot distinguish committed poison from honest gradients in the toy setting or reduces clean accuracy by more than 1 percentage point.

## Evidence references

- Artifact root: `<local-path>/projects/neural-gradient-commit-reveal-verification-with-convergenc-b64c555e55`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
