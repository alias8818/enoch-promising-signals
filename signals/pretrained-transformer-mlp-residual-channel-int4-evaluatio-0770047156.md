# Pretrained transformer MLP residual-channel INT4 evaluation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `pretrained-transformer-mlp-residual-channel-int4-evaluatio-0770047156`
Run ID: `pretrained-transformer-mlp-residual-channel-int4-evaluatio-0770047156-20260629T103621978280+0000`

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

- Parent run decision: Sensitivity-aware residual channels for INT4 MLP blocks: enoch://control-plane/projects/sensitivity-aware-residual-channels-for-int4-mlp-blocks-a09ec09e492e/runs/sensitivity-aware-residual-channels-for-int4-mlp-blocks-a09ec09e492e-20260629T083317034180+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.7-code: enoch://research-facility/provider/moonshotai/kimi-k2.7-code/85c96a57ff49

## What looked useful

Across 3 seeds, preserving 2, 4, 8, and 16 of 128 residual output channels reduced mean relative L2 error versus all-INT4 by 2.32%, 3.25%, 4.78%, and 7.30%, respectively, and beat random preserved-channel controls by 1.82%, 2.13%, 2.76%, and 3.35%.

## Boundaries and scale limits

Only Pythia-14M was tested; activations were synthetic proxies rather than real text hidden states; no perplexity, downstream task, larger-model, GPU, packed-kernel latency, or memory-bandwidth benchmark was run.

## Claim scope

On cached pretrained Pythia-14M MLP weights, using synthetic normalized hidden-state inputs transformed by real layernorm parameters, preserving the highest-energy MLP residual output channels in FP16/FP32 while rowwise-INT4 quantizing the remaining MLP weights consistently reduces MLP output reconstruction error versus all-INT4 and random preserved-channel controls.

## Why it stopped

Closed as no-paper useful signal because the proxy reconstruction evidence supports the mechanism but does not validate real activations, language modeling quality, larger models, or INT4 kernel performance.

## Recommended next action

Run a direct real-text forward/perplexity evaluation on a cached small language model using the same residual-channel selection policy, with all-INT4 and random-channel controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-text perplexity test for residual-channel MLP INT4 preservation
- Success threshold: At 8/128 or comparable <=6.25% preserved residual channels, reduce perplexity degradation versus all-INT4 by at least 10% relative and beat random-channel preservation on every tested seed/model layer group.
- Stop condition: Stop if real-text activation calibration fails to beat random preserved-channel controls or if perplexity degradation is not improved at equal effective bit budget.

## Evidence references

- Artifact root: `<local-path>/projects/pretrained-transformer-mlp-residual-channel-int4-evaluatio-0770047156`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
