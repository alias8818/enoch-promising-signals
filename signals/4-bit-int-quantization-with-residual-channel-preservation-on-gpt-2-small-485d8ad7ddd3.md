# 4-bit INT Quantization with Residual Channel Preservation on GPT-2-small

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `4-bit-int-quantization-with-residual-channel-preservation-on-gpt-2-small-485d8ad7ddd3`
Run ID: `4-bit-int-quantization-with-residual-channel-preservation-on-gpt-2-small-485d8ad7ddd3-20260608T043727392039+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/7841a987ac2c

## What looked useful

Plain INT4 increased WikiText-2 validation NLL from 3.5745 to 3.9918. Preserving top-norm channels reduced NLL to 3.9412 at 2% and 3.9284 at 4%, outperforming random preservation at the same budgets, but 4% preservation still left +0.3539 NLL versus FP32.

## Boundaries and scale limits

Tested only GPT-2-small, WikiText-2 validation, dequantized simulated INT4 weights, weight-norm channel selection, and no packed INT4 kernel or wall-clock serving efficiency claim.

## Claim scope

On GPT-2-small with simulated per-output-channel INT4 post-training quantization of projection/linear weights, preserving the top 2-4% output channels by weight L2 norm in full precision reduces WikiText-2 validation perplexity damage versus plain INT4 and versus random channel preservation at matching budgets.

## Why it stopped

Bounded direct evidence supports the mechanism but the recovered perplexity is too partial and the implementation is simulated rather than deployment-realistic, so this is not a paper-ready positive result.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should compare activation-calibrated residual channel selection against weight-norm and random controls on GPT-2-small with layerwise budget ablations.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-calibrated residual channel preservation for GPT-2-small INT4 quantization
- Success threshold: Activation-calibrated preservation improves NLL recovery by at least 0.03 over weight-norm preservation at the same budget while remaining consistently better than random across calibration seeds.
- Stop condition: Stop if activation-calibrated selection does not beat weight-norm selection by at least 0.01 NLL recovery at both 2% and 4% budgets, or if gains are seed-unstable.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-int-quantization-with-residual-channel-preservation-on-gpt-2-small-485d8ad7ddd3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
