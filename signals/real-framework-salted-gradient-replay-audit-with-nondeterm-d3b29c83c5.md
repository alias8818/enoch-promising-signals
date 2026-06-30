# Real framework salted-gradient replay audit with nondeterminism controls

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-framework-salted-gradient-replay-audit-with-nondeterm-d3b29c83c5`
Run ID: `real-framework-salted-gradient-replay-audit-with-nondeterm-d3b29c83c5-20260620T110452106261+0000`

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

- Parent run decision: Deterministic Gradient Replay Audit for Volunteer Submissions: enoch://control-plane/projects/deterministic-gradient-replay-audit-for-volunteer-submissions-d29fd7a12865/runs/deterministic-gradient-replay-audit-for-volunteer-submissions-d29fd7a12865-20260620T104431943061+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/addb2b44e416

## What looked useful

The Tier 1 audit supports the mechanism: deterministic controls remove replay noise for baseline and fixed-salt controls, making different-salt gradients distinguishable across every tested step. An OS-entropy negative control also fails replay, showing nondeterminism must be controlled before attributing mismatches to salting.

## Boundaries and scale limits

Tested only CPU PyTorch, synthetic data, a tiny MLP, SGD, 32 steps, one process, and explicit per-parameter salt injection. Not tested: CUDA, AMP, distributed training, dataloader workers, dropout-heavy models, larger models, real datasets, cross-host replay, or adversaries that know the salt.

## Claim scope

In a small CPU PyTorch autograd MLP with deterministic framework controls, no-salt and same-salt replays produce exact per-step gradient digest matches, while different per-run gradient salts are rejected by digest and strict allclose replay checks.

## Why it stopped

Tier 1 direct test completed and produced useful mechanism evidence, but evidence is CPU-only and too narrow for publication readiness.

## Recommended next action

Run a bounded CUDA-enabled deepen test on a small CNN or transformer with deterministic controls, AMP off/on ablation, dataloader worker controls, and the same digest/allclose replay threshold before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CUDA salted-gradient replay audit with AMP and dataloader controls
- Success threshold: No-salt and same-salt controls must replay with 100% digest match or a predeclared tolerance justified by CUDA/AMP precision; different-salt runs must be rejected for at least 99% of audited steps and have max_abs_delta above the replay threshold.
- Stop condition: Stop as negative if deterministic/no-salt controls cannot replay under documented settings, or if different-salt gradients are not distinguishable from controlled replay noise.

## Evidence references

- Artifact root: `<local-path>/projects/real-framework-salted-gradient-replay-audit-with-nondeterm-d3b29c83c5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
