# Local PoW-Gradient Puzzle for Volunteer Cheating Detection

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `local-pow-gradient-puzzle-for-volunteer-cheating-detection-5bcec97af01c`
Run ID: `local-pow-gradient-puzzle-for-volunteer-cheating-detection-5bcec97af01c-20260607T132108644794+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/db9f9c4c51eb

## What looked useful

In 800 confirmation submissions at 12-bit difficulty, every tested strategy achieved 100% PoW acceptance, while quality metrics diverged sharply: random gradients had mean cosine -0.001 and median relative L2 error 1.411, zero gradients had median relative L2 error 1.000, sign-flipped gradients had cosine -1.000 and median relative L2 error 2.000, and stale replay had mean cosine 0.510. The PoW check imposed nonce-search cost but provided no cheating-discrimination signal.

## Boundaries and scale limits

Synthetic logistic-regression gradients only; no large-model volunteer network, no real heterogeneous worker traces, no adaptive economic adversary, and no protocol variant with hidden verifier-side canaries or recomputation checks. The result is protocol-level for PoW-only byte binding, not a full validation of all PoW-assisted training-integrity designs.

## Claim scope

For a local verifier that accepts gradients solely by checking a worker- and round-bound SHA-256 proof-of-work over submitted gradient bytes, PoW acceptance does not distinguish honest gradients from fabricated, zero, sign-flipped, scaled, replayed, or copied gradients in a deterministic synthetic logistic-regression simulation.

## Why it stopped

Early protocol-level falsification: the tested PoW-only mechanism accepts arbitrary gradient bytes after nonce search, so it cannot detect cheating without an additional correctness signal.

## Recommended next action

Stop treating PoW-only gradient-byte binding as a cheating detector; the next bounded test should add a verifier-side correctness-coupled challenge and require fabricated/replayed/copied gradients to have lower acceptance or materially higher cost than honest gradients.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Verifier-Coupled Gradient Puzzle With Hidden Canary Checks
- Success threshold: At fixed honest false-rejection rate below 5%, at least random, zero, sign-flip, stale replay, and naive copy-peer adversaries must have pass rates below 20% or require at least 5x honest-equivalent compute to pass.
- Stop condition: Stop if adversaries can satisfy the coupled puzzle over arbitrary or copied gradients with pass rate within 10 percentage points of honest workers at comparable cost.

## Evidence references

- Artifact root: `<local-path>/projects/local-pow-gradient-puzzle-for-volunteer-cheating-detection-5bcec97af01c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
