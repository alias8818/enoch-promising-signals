# INT4 Residual Channel Quantization for Home AI Memory Reduction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int4-residual-channel-quantization-for-home-ai-memory-reduction-978f6f8a7540`
Run ID: `int4-residual-channel-quantization-for-home-ai-memory-reduction-978f6f8a7540-20260613T235323878682+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/55c904e84fe4

## What looked useful

Residual-channel INT4 improved mean output NMSE versus plain INT4 by 15.1% at 4.260 bits/param, 25.3% at 4.511 bits/param, and 42.7% at 5.013 bits/param. However, ordinary per-channel INT5 at 5.009 bits/param improved mean output NMSE by 72.7%, dominating the similar-storage 25% residual variant across all tested scenarios. The only attractive niche was the outlier-channel scenario, where 6.25% residual channels reduced INT4 output NMSE by 55.9% while staying at 4.260 bits/param.

## Boundaries and scale limits

No real model perplexity, activation-trace calibration, packed-kernel latency, allocator-level memory, KV-cache, or end-to-end home inference measurements were run. The evidence is a bounded synthetic/proxy matrix test over 1024x1024 to 4096x4096 shapes, four distributions, and three seeds.

## Claim scope

Synthetic transformer-like linear matrices on GB10/CUDA show that INT4 plus residual INT4 codes for selected high-error output channels consistently reduces plain INT4 reconstruction and activation-output error, with the strongest benefit when quantization error is concentrated in outlier channels.

## Why it stopped

Synthetic proxy evidence supports the residual-channel mechanism but early-falsifies the broader claim that it is a generally superior home-AI memory-reduction format, because a simple same-storage INT5 baseline produced substantially lower output error.

## Recommended next action

Stop this run as no-paper useful-signal evidence; if pursued, run a bounded real-checkpoint activation/perplexity follow-up focused on outlier-channel layers and compare against same-budget INT5 and mixed-precision outlier baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-checkpoint outlier-channel residual INT4 validation
- Success threshold: At less than or equal to 4.35 effective bits/parameter, residual-channel INT4 must reduce plain INT4 perplexity degradation or activation-output NMSE by at least 30% and be within 10% relative error of the best same-budget baseline on at least one real checkpoint.
- Stop condition: Stop if same-budget INT5 or mixed-precision outlier-channel quantization dominates residual-channel INT4 on all tested real checkpoints, or if residual metadata pushes effective storage above 4.35 bits/parameter for the small-residual setting.

## Evidence references

- Artifact root: `<local-path>/projects/int4-residual-channel-quantization-for-home-ai-memory-reduction-978f6f8a7540`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
