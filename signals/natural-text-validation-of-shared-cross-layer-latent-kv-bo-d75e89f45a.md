# Natural-text validation of shared cross-layer latent KV bottlenecks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `natural-text-validation-of-shared-cross-layer-latent-kv-bo-d75e89f45a`
Run ID: `natural-text-validation-of-shared-cross-layer-latent-kv-bo-d75e89f45a-20260531T160400919537+0000`

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

- Parent run decision: Cross-Layer Latent KV Bottleneck for Home Inference: enoch://control-plane/projects/cross-layer-latent-kv-bottleneck-for-home-inference-32ceaf8c6fa4/runs/cross-layer-latent-kv-bottleneck-for-home-inference-32ceaf8c6fa4-20260531T121457841771+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9589fd5d43ed

## What looked useful

The Tier 1 direct activation probe supports a shared cross-layer latent KV bottleneck mechanism on natural text: rank-32 shared basis energy was 0.9323, shared/per-layer fraction was 0.9878, and shared-random gap was 0.6799. A matched shuffled-token control was nearly identical, bounding the claim to generic GPT-2 KV geometry rather than natural syntax specificity.

## Boundaries and scale limits

Single pretrained GPT-2 small model, one natural-text dataset split, 64 short chunks, post-hoc SVD activation compressibility only. No K/V intervention, no perplexity measurement under compressed K/V, no training of a bottlenecked architecture, and shuffled-token controls show the metric is not natural-order-specific.

## Claim scope

On 64 WikiText-2 validation chunks of 128 tokens, pretrained GPT-2 small KV activations admit a per-input shared cross-layer rank-32 temporal basis that captures 93.23% mean KV energy and 98.78% of the per-layer SVD upper-bound energy.

## Why it stopped

No-paper useful signal: the controlled Tier 1 activation test supports compressibility but does not validate functional inference quality or natural-syntax specificity.

## Recommended next action

Run a bounded functional intervention: replace GPT-2 K/V with rank-32 shared cross-layer reconstructed K/V during evaluation and compare WikiText-2 NLL against full K/V, per-layer compressed K/V, first-layer-basis transfer, random basis, and shuffled-token controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Functional NLL test of shared cross-layer KV bottleneck reconstruction
- Success threshold: Shared rank-32 reconstructed K/V adds no more than 10% relative NLL degradation versus full K/V and retains at least 95% of the NLL benefit of per-layer rank-32 compression on the same chunks.
- Stop condition: Stop if shared rank-32 K/V causes more than 25% relative NLL degradation or performs no better than first-layer-basis transfer/random controls on two independent 64-chunk WikiText-2 samples.

## Evidence references

- Artifact root: `<local-path>/projects/natural-text-validation-of-shared-cross-layer-latent-kv-bo-d75e89f45a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
