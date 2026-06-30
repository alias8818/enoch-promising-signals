# Activation-aware 4-bit weight quantization for 1-3B models on GB10

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `activation-aware-4-bit-weight-quantization-for-1-3b-models-on-gb10-e58ca6a3faf3`
Run ID: `activation-aware-4-bit-weight-quantization-for-1-3b-models-on-gb10-e58ca6a3faf3-20260611T015139381568+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d5a821022275

## What looked useful

Activation-aware scaling gave consistent layer-level reconstruction gains on a 1B-class transformer: 22.20% mean output-MSE improvement versus RTN at group size 128 and 23.86% at group size 64, with 12/12 positive layers in both runs. True activation statistics beat shuffled activation controls by about 30% mean output MSE.

## Boundaries and scale limits

No whole-model quantized perplexity or downstream accuracy was measured; no packed int4 GB10 kernel was implemented; calibration used short built-in text prompts with 512 activation rows per sampled layer; model-family robustness beyond Pythia-1B was not tested.

## Claim scope

On 12 selected Linear layers from EleutherAI/pythia-1b-deduped, using short-prompt calibration activations on GB10, activation-aware per-input-channel scaling before symmetric groupwise int4 quantization reduced layer output reconstruction MSE versus RTN and versus shuffled activation controls.

## Why it stopped

Closed as no-paper useful signal because the current evidence supports the layer reconstruction mechanism but lacks end-to-end model quality and real int4 kernel throughput.

## Recommended next action

Run a bounded full-model follow-up that quantizes all Pythia-1B linear layers, evaluates perplexity on a fixed public corpus, and tests a packed or fused int4 GB10 inference path before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end Pythia-1B activation-aware int4 perplexity and GB10 packed-kernel validation
- Success threshold: Activation-aware int4 improves perplexity degradation by at least 20% relative to RTN at the same group size and preserves or improves GB10 tokens/sec or memory pressure compared with a credible fp16/RTN baseline.
- Stop condition: Stop if full-model perplexity gains are absent versus RTN, if the packed/fused int4 path is slower than fp16 without meaningful memory benefit, or if calibration sensitivity makes the effect non-reproducible.

## Evidence references

- Artifact root: `<local-path>/projects/activation-aware-4-bit-weight-quantization-for-1-3b-models-on-gb10-e58ca6a3faf3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
