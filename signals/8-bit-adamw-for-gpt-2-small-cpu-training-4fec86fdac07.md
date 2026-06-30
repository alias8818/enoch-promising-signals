# 8-bit AdamW for GPT-2-small CPU training

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `8-bit-adamw-for-gpt-2-small-cpu-training-4fec86fdac07`
Run ID: `8-bit-adamw-for-gpt-2-small-cpu-training-4fec86fdac07-20260604T231641054895+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/e621841cbccf

## What looked useful

Naive absmax int8 quantization of AdamW moments saves memory but is not a viable drop-in CPU training optimizer in this bounded test: GPT-2-small-shaped optimizer state fell from 949.4 MiB to 237.8 MiB, optimizer-only step time rose from 0.421 s to 3.148 s, and tiny-proxy training loss exploded from 85.22 to 11156.59 while fp32 AdamW fell to 28.61. A diagnostic found 33.0% of second-moment entries quantized to exact zero after one update.

## Boundaries and scale limits

No full GPT-2-small forward/backward training on a real corpus was run. The target-scale evidence is optimizer-only with synthetic gradients; the loss evidence is from a tiny synthetic-data transformer proxy. Optimized native CPU kernels and more sophisticated 8-bit variance quantizers were not tested.

## Claim scope

For the inspectable blockwise linear int8-moment AdamW implementation tested here, GPT-2-small-shaped optimizer state shrinks by about 4x on CPU, but optimizer-only steps are substantially slower and a tiny GPT-style training proxy diverges.

## Why it stopped

Bounded direct/proxy evidence falsified the straightforward implementation: memory improved, but CPU update overhead and tiny-model divergence make it unsuitable as tested. This is an early falsification, not a full validation of all 8-bit AdamW designs.

## Recommended next action

Stop this run as a no-paper negative/useful signal for naive linear 8-bit AdamW; the next bounded action is to test a safer second-moment quantizer before any GPT-2-small-scale training attempt.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CPU 8-bit AdamW with protected variance quantization
- Success threshold: All three required evidence checks pass in one bounded CPU run under 15 minutes.
- Stop condition: Stop if the safer quantizer still diverges on the tiny training proxy, shows more than 1% second-moment zero-collapse, or exceeds 2x optimizer-step overhead on GPT-2-small-shaped tensors.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-adamw-for-gpt-2-small-cpu-training-4fec86fdac07`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
