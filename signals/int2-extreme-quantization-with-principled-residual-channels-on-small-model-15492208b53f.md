# INT2 Extreme Quantization with Principled Residual Channels on Small Model

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `int2-extreme-quantization-with-principled-residual-channels-on-small-model-15492208b53f`
Run ID: `int2-extreme-quantization-with-principled-residual-channels-on-small-model-15492208b53f-20260610T080621885234+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/016e72d87fd6

## What looked useful

Residual hidden channels recovered some accuracy after INT2 quantization, but the activation/weight quantization-sensitivity selector did not reliably outperform equal-budget controls; raw quantization-error ranking was stronger at 12% and 25% budgets.

## Boundaries and scale limits

Does not test transformers, language-model perplexity, pretrained checkpoints, real datasets, layerwise residual allocation, packed INT2 inference throughput, or GPT-2-small-class models.

## Claim scope

Bounded synthetic teacher-student small MLP evidence: post-training INT2 min-max quantization with full-precision residual hidden channels on a 64-input, 256-hidden GELU classifier over three seeds.

## Why it stopped

The bounded direct test did not support the principled sensitivity selector; this is not a full transformer validation, but it is an early negative signal against the proposed selector.

## Recommended next action

Stop this run as a no-paper useful signal; a bounded follow-up should test raw quantization-error versus sensitivity residual-channel selection on a real small pretrained language model.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual-channel INT2 selection on a real small pretrained language model
- Success threshold: A selector is useful only if it reduces perplexity or accuracy loss versus random by at least 20% of the all-INT2 degradation and also beats raw quantization-error selection at two or more residual budgets.
- Stop condition: Stop if sensitivity selection fails to beat raw quantization-error selection on two calibration splits or if residual channels recover less than 10% of the all-INT2 degradation at 12% residual budget.

## Evidence references

- Artifact root: `<local-path>/projects/int2-extreme-quantization-with-principled-residual-channels-on-small-model-15492208b53f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
