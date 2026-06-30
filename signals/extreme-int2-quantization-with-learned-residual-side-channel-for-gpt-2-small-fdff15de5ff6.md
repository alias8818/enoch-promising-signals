# Extreme INT2 quantization with learned residual side-channel for GPT-2-small

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `extreme-int2-quantization-with-learned-residual-side-channel-for-gpt-2-small-fdff15de5ff6`
Run ID: `extreme-int2-quantization-with-learned-residual-side-channel-for-gpt-2-small-fdff15de5ff6-20260621T122333913919+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3f2726222032

## What looked useful

Low-rank residuals barely improve INT2. Rank-64 reaches about 3.96 effective bits/weight but still has 0.5473 global relative Frobenius error and 0.5369 synthetic output NRMSE, versus 0.1949 and 0.2126 for the INT4 reference.

## Boundaries and scale limits

No end-to-end perplexity, no real calibration data, no trained residual module, no full-model inference kernel, and only 12 of the GPT-2-small 2D tensors were probed. The SVD residual is an oracle low-rank proxy for a learned side-channel, not a deployed implementation.

## Claim scope

Early falsification of per-row symmetric INT2 plus low-rank residual side-channel on 12 actual GPT-2-small 2D weight tensors, using weight reconstruction and synthetic Gaussian activation-output metrics.

## Why it stopped

Proxy/early falsification: direct GPT-2-small weight-space evidence shows the low-rank side-channel remains much worse than INT4 even near a 4-bit effective budget, so it is not paper-ready or worth scaling as-is.

## Recommended next action

Stop this low-rank residual side-channel variant; only revisit INT2 residual quantization with a different activation-aware learned residual design and an end-to-end perplexity harness.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Activation-aware sparse residual side-channel for INT2 GPT-2-small
- Success threshold: At <=3.0 effective bits/weight, recover at least half of the INT2-to-INT4 perplexity gap and reduce synthetic activation-output NRMSE by at least 30% versus plain INT2 on the same tensors.
- Stop condition: Stop if the activation-aware residual does not beat the rank-64 low-rank residual at matched effective bits or fails to recover at least 25% of the INT2-to-INT4 perplexity gap on a small validation slice.

## Evidence references

- Artifact root: `<local-path>/projects/extreme-int2-quantization-with-learned-residual-side-channel-for-gpt-2-small-fdff15de5ff6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
