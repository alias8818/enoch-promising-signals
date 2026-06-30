# Real transformer activation-outlier channel isolation for INT2 projection weights

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-transformer-activation-outlier-channel-isolation-for-65d885f4dc`
Run ID: `real-transformer-activation-outlier-channel-isolation-for-65d885f4dc-20260628T130232081037+0000`

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

- Parent run decision: Activation Outlier Isolation Channels for INT2 Weight Quantization: enoch://control-plane/projects/activation-outlier-isolation-channels-for-int2-weight-quantization-a49e8d9cd7e8/runs/activation-outlier-isolation-channels-for-int2-weight-quantization-a49e8d9cd7e8-20260628T115456475280+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.2: enoch://research-facility/provider/hf:zai-org/GLM-5.2/c4557f400578

## What looked useful

Activation RMS selection reduced mean relative projection NMSE to 0.7093 at 1% preserved channels and 0.4892 at 10%, while random preservation stayed at 0.9899 and 0.8773 respectively; weight-row-norm selection was weaker at 0.8768 and 0.7708.

## Boundaries and scale limits

Tested one small GPT-2-family pretrained model, 24 natural-language prompts, direct layer-output NMSE only. Did not test full-model perplexity, generation quality, larger 7B+ models, learned calibration sets, or production mixed-precision kernels.

## Claim scope

For distilgpt2 projection layers, preserving a small fraction of activation-outlier input channels in full precision substantially reduces signed symmetric INT2 projection output reconstruction error versus full INT2, random channel preservation, and usually weight-row-norm selection.

## Why it stopped

No-paper useful signal: this run directly supports the layer-output mechanism but does not validate full-model quality or deployment tradeoffs.

## Recommended next action

Run a bounded in-place full-model evaluation on distilgpt2 or GPT-2-small comparing full INT2, activation-preserved INT2, random-preserved INT2, and weight-only-preserved INT2 on language-model loss/perplexity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Full-model perplexity test for activation-preserved INT2 projection channels
- Success threshold: At 1% to 5% preserved input channels, activation-based preservation recovers at least 50% of the full-INT2 loss increase and beats both random and weight-row-norm controls on the same evaluation set.
- Stop condition: Stop if activation-based preservation fails to beat both controls at 5% preserved channels or if the implementation cannot reproduce the projection-level error reduction in full-model loss.

## Evidence references

- Artifact root: `<local-path>/projects/real-transformer-activation-outlier-channel-isolation-for-65d885f4dc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
