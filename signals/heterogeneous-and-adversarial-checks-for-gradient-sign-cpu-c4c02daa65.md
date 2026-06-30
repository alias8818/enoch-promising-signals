# Heterogeneous and adversarial checks for gradient-sign CPU puzzles

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `heterogeneous-and-adversarial-checks-for-gradient-sign-cpu-c4c02daa65`
Run ID: `heterogeneous-and-adversarial-checks-for-gradient-sign-cpu-c4c02daa65-20260527T065743268828+0000`

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

- Parent run decision: Gradient-Sign Puzzle for CPU Volunteer Verification: enoch://control-plane/projects/gradient-sign-puzzle-for-cpu-volunteer-verification-407b55a06267/runs/gradient-sign-puzzle-for-cpu-volunteer-verification-407b55a06267-20260525T182141104599+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/01c5be3baed4

## What looked useful

Local one-bit gradient signs are informative for clean CPU-style losses, but greedy sign updates stall on carry-heavy and heterogeneous arithmetic. Adversarial loss shaping reduced positive-gradient precision for clean improvement from 1.0 to about 0.87-0.89 without producing exact solves.

## Boundaries and scale limits

Synthetic 64-bit puzzle programs only; no real binaries, no larger bit widths, no SAT/SMT baselines, and no learned differentiable CPU surrogate. The run used one CPU process and short local budgets.

## Claim scope

A bounded CPU-worker Tier 1 benchmark of 64-bit synthetic CPU-style puzzles showed that one-bit gradient-sign search solves separable XOR/rotate puzzles and improves clean Hamming loss on add/rotate and heterogeneous mixed-arithmetic puzzles, but does not exactly solve heterogeneous puzzles within 2,048 or 8,192 evaluations.

## Why it stopped

No-paper useful signal: direct Tier 1 heterogeneous/adversarial tests did not meet the exact-solve threshold, though they showed locally informative gradients and adversarial sign degradation.

## Recommended next action

Run one bounded deepen test of carry-aware or beam-style multi-bit gradient-sign search against coordinate descent on the same 64-bit heterogeneous families; stop unless exact solve rate exceeds coordinate descent at matched evaluations.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Carry-aware beam updates for heterogeneous gradient-sign CPU puzzles
- Success threshold: At 8,192 evaluations, beam/carry-aware gradient-sign search achieves at least 20% exact solve rate on heterogeneous_mix and beats coordinate descent by at least 10 percentage points, while not degrading adversarial median clean loss.
- Stop condition: Stop as negative if exact solve rate remains below 5% or is not better than coordinate descent at matched evaluations on heterogeneous_mix.

## Evidence references

- Artifact root: `<local-path>/projects/heterogeneous-and-adversarial-checks-for-gradient-sign-cpu-c4c02daa65`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
