# Proxy-Model Gradient Alignment Checks for Volunteer Verification

Status: `useful_signal`
Project ID: `proxy-model-gradient-alignment-checks-for-volunteer-verification-64faedf9ba57`
Run ID: `proxy-model-gradient-alignment-checks-for-volunteer-verification-64faedf9ba57-20260517T190400744727+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2d019a3fa381

## What looked useful

Proxy gradient alignment is strongly training-stage-sensitive: it separated synthetic bad volunteer batches perfectly with an undertrained proxy, degraded at intermediate training, and failed as a standalone verifier near convergence with 94.375% bad false positives at an optimistic honest p05 threshold.

## Boundaries and scale limits

Not tested on real volunteer traces, real federated updates, larger datasets, adversarial adaptation, independent threshold calibration, larger proxy architectures, or production-scale models.

## Claim scope

Small local sklearn-digits volunteer-verification simulation with a 64-hidden-unit MLP proxy, synthetic bad controls, and cosine alignment to a clean held-out reference gradient across proxy training stages.

## Why it stopped

Proxy/local evidence mixed: alignment works in an undertrained proxy but fails near convergence, so this is an early falsification of broad standalone volunteer verification rather than full validation.

## Recommended next action

Stop this run as a no-paper useful signal; next test a bounded deepen follow-up using independent calibration/test volunteers and undertrained probe checkpoints to see whether the early-stage signal survives non-leaky thresholding.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Independent-calibration undertrained proxy gradient verifier
- Success threshold: On held-out test volunteers, bad false-positive rate <= 0.10 at acceptable-volunteer true-positive rate >= 0.90 across at least two datasets or task splits.
- Stop condition: Stop if independent calibration produces bad false-positive rate > 0.25 at acceptable-volunteer true-positive rate 0.90 on either dataset/task split.

## Evidence references

- Artifact root: `<local-path>/projects/proxy-model-gradient-alignment-checks-for-volunteer-verification-64faedf9ba57`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
