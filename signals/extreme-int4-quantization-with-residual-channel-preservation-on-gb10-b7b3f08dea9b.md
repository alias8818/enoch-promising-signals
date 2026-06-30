# Extreme INT4 Quantization with Residual Channel Preservation on GB10

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `extreme-int4-quantization-with-residual-channel-preservation-on-gb10-b7b3f08dea9b`
Run ID: `extreme-int4-quantization-with-residual-channel-preservation-on-gb10-b7b3f08dea9b-20260608T205306297139+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/91e7721ea839

## What looked useful

Pure INT4 increased GPT-2 small WikiText-2 proxy loss by +0.4196. Preserving the top 5% output channels by quantization error reduced the loss delta to +0.2934, recovering about 30.1% of the pure-INT4 loss damage at a modeled 0.2998x FP16 storage ratio. Error selection beat magnitude and random controls at every tested preservation fraction.

## Boundaries and scale limits

Evaluated 6,711 WikiText-2 validation tokens on GPT-2 small only. The implementation dequantizes weights into normal PyTorch tensors, so storage ratios are modeled and no packed INT4 kernel throughput, resident memory footprint, 7B-class behavior, or broad benchmark robustness was validated.

## Claim scope

On a bounded GPT-2 small WikiText-2 proxy, symmetric per-output-channel INT4 weight quantization with error-selected FP16 residual output channels reduced loss and logit drift versus pure INT4 and random/magnitude preservation controls.

## Why it stopped

Stopped after producing a reproducible bounded useful signal; evidence is proxy-only and not sufficient for a paper or full GB10 quantized-inference claim.

## Recommended next action

Run a bounded follow-up with activation-aware channel selection, a held-out WikiText/short-task evaluation of at least 100k tokens, repeated random controls, and a measured packed INT4 plus residual runtime path before considering paper writing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-Aware Residual Channel Selection for Packed INT4 GPT-2 Inference on GB10
- Success threshold: At 5% or fewer preserved weights and no more than 0.35x FP16 measured storage, activation-aware residual selection recovers at least 40% of pure-INT4 loss damage and improves measured throughput or memory residency versus FP16 on GB10.
- Stop condition: Stop if packed runtime cannot beat FP16 memory residency, or if activation-aware residual selection fails to outperform repeated random controls by at least 10% relative recovery of INT4 loss damage.

## Evidence references

- Artifact root: `<local-path>/projects/extreme-int4-quantization-with-residual-channel-preservation-on-gb10-b7b3f08dea9b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
