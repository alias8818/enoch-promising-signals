# 4-bit GaLore for GPT-2-Small Pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `4-bit-galore-for-gpt-2-small-pretraining-62276e650b75`
Run ID: `4-bit-galore-for-gpt-2-small-pretraining-62276e650b75-20260525T141801478002+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/51320b64bd65

## What looked useful

GaLore fp32 reduced optimizer-state storage from 176.60 MiB to 2.98 MiB and stayed finite, while blockwise int4 GaLore reduced state to 0.98 MiB but diverged to NaN at lr 0.002 and to 2.35e18 loss at lr 0.0005. The memory mechanism works, but quantizing both Adam moments to int4 was numerically unstable in this GPT-style probe.

## Boundaries and scale limits

Not full GPT-2-small, not real text pretraining, not thousands of steps, and not a production fused 4-bit optimizer. The result supports only an early falsification of naive/blockwise int4 Adam-moment GaLore stability, not a universal impossibility claim.

## Claim scope

Bounded local GPT-style synthetic pretraining probe: a 23.1M-parameter causal decoder on GB10 compared AdamW, fp32 GaLore AdamW, and blockwise signed-int4 GaLore AdamW for 20 CUDA training steps.

## Why it stopped

Early falsification by proxy/local direct optimizer test: blockwise signed-int4 GaLore moment state was unstable while fp32 GaLore remained finite under matched conditions.

## Recommended next action

Stop this run as a scoped negative/useful signal; do not write a paper claiming successful 4-bit GaLore pretraining from these results.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stabilized mixed-precision GaLore moments for GPT-style training
- Success threshold: No non-finite losses or explosive loss growth over 200 steps, final training loss within 5 percent of fp32 GaLore on the synthetic harness, and at least 2x optimizer-state memory reduction versus fp32 GaLore.
- Stop condition: Stop if all mixed-precision variants either diverge before 200 steps or require second-moment precision that eliminates the optimizer-state memory advantage versus fp32 GaLore.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-galore-for-gpt-2-small-pretraining-62276e650b75`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
