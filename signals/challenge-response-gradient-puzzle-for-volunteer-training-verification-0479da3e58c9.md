# Challenge-Response Gradient Puzzle for Volunteer Training Verification

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `challenge-response-gradient-puzzle-for-volunteer-training-verification-0479da3e58c9`
Run ID: `challenge-response-gradient-puzzle-for-volunteer-training-verification-0479da3e58c9-20260630T045102137536+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9c1f2304a1b1

## What looked useful

Luminance-matched distractors are necessary for this verifier class. At 7/8, the hardened variant passed low-noise trained solvers at 99.99% and luminance-only solvers at 0.06%, but wrong-gamma solvers still passed 31.23% and high-noise trained solvers only 40.73%.

## Boundaries and scale limits

10,000 synthetic sessions per variant with simulated solvers only; no real volunteers, no deployed UI, no accessibility cohort, and no VLM/browser adversary were tested.

## Claim scope

Synthetic Monte Carlo evidence for nonce-bound 4-choice gradient interpolation puzzles: the original design is defeated by luminance leakage; luminance-matched distractors reject random, replay, and luminance-only solvers but remain vulnerable to wrong-gamma interpolation and visual-noise sensitivity.

## Why it stopped

Proxy/early falsification of the original puzzle and limited synthetic support for a hardened variant; full volunteer-training verification was not directly tested.

## Recommended next action

Stop this run as a proxy-only useful signal; next run should perform a bounded human usability and adversarial solver pilot before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Human and adversarial pilot for luminance-matched gradient training verifier
- Success threshold: At least 95% trained-human pass rate and at most 1% untrained/adversarial pass rate at a fixed threshold, with no severe accessibility subgroup failure.
- Stop condition: Stop if trained-human pass rate is below 90%, any simple non-trained solver exceeds 5%, or accessibility/display effects dominate the score.

## Evidence references

- Artifact root: `<local-path>/projects/challenge-response-gradient-puzzle-for-volunteer-training-verification-0479da3e58c9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
