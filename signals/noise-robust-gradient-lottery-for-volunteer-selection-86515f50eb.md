# Noise-robust gradient lottery for volunteer selection

Status: `useful_signal`
Project ID: `noise-robust-gradient-lottery-for-volunteer-selection-86515f50eb`
Run ID: `noise-robust-gradient-lottery-for-volunteer-selection-86515f50eb-20260519T060534315722+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f1d01a04c256

## What looked useful

Robust lottery improved mean final loss vs noisy_topk by 10.69% at noise_sigma=1.5 and 19.69% at noise_sigma=2.0, with higher oracle overlap and selected utility from noise_sigma=1.0 upward. It missed the >=5% final-loss threshold at noise_sigma=1.0 with a 3.53% improvement, while broad one-shot noisy_lottery was consistently worse than noisy_topk.

## Boundaries and scale limits

160 volunteers, 24-dimensional linear regression, 48 examples per volunteer, 20 training rounds, 40 random seeds; score noise is simulated, and robust_lottery uses 4 score probes per volunteer without a cost-matched deterministic robust top-k baseline.

## Claim scope

Controlled small direct test on synthetic heterogeneous linear-regression volunteer shards: robust_lottery improved volunteer-selection diagnostics and final loss versus one-shot noisy_topk at high gradient-score noise, but not at every noise level in the stated threshold.

## Why it stopped

No-paper useful signal: the controlled direct test supports the mechanism only under higher score noise and fails the stated >=5% improvement threshold at noise_sigma=1.0, so it is not paper-positive or broadly validated.

## Recommended next action

Stop the paper path for this run; if deepening, run a cost-matched boundary-noise test comparing robust_lottery to 4-probe deterministic robust_topk and one-shot baselines on noise_sigma 1.0-1.25.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cost-matched robust lottery versus robust top-k at boundary score noise
- Success threshold: robust_lottery beats cost-matched robust_topk by at least 3% mean final loss or lower variance at two of three boundary noise levels, while remaining at least 5% better than one-shot noisy_topk.
- Stop condition: Stop as negative if robust_lottery does not beat cost-matched robust_topk at boundary noise, because the current signal would then be explained by repeated score measurement rather than lottery selection.

## Evidence references

- Artifact root: `<local-path>/projects/noise-robust-gradient-lottery-for-volunteer-selection-86515f50eb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
