# Principled Residual Channels for 2-bit Weight Quantization with Iso-Budget Baseline

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `principled-residual-channels-for-2-bit-weight-quantization-with-iso-budget-baseline-8b9a61126ad6`
Run ID: `principled-residual-channels-for-2-bit-weight-quantization-with-iso-budget-baseline-8b9a61126ad6-20260520T092209492583+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/0ab4599540f4

## What looked useful

Residual-energy channel selection consistently beat random at equal restored-channel count, but the residual-channel scheme was far worse than uniform 3-bit quantization at the near-iso-budget 1/16 residual setting.

## Boundaries and scale limits

No end-to-end model quality, perplexity, task accuracy, LLM transformer checkpoint, latency, or custom kernel evidence. Storage accounting excludes group scales and metadata. The Hugging Face tiny GPT-2 download stalled, so real-weight evidence is from a local VAE checkpoint rather than an LLM.

## Claim scope

CPU-only NumPy reconstruction/output-error probe on 12 synthetic matrices and 8 local F32 VAE weight matrices using 2-bit groupwise quantization, exact fp16-equivalent restored residual channels, and random/magnitude/uniform-bit controls.

## Why it stopped

Proxy/direct reconstruction evidence shows the mechanism is real but too weak: at 2.875 average weight bits, 1/16 exact residual channels had mean output relative MSE 0.2740 versus 0.0568 for uniform 3-bit.

## Recommended next action

Stop this paper path unless a cheaper residual representation or true mixed-bit baseline is proposed; the current fp16 residual-channel allocation is a proxy-level early falsification against near-iso-budget uniform 3-bit.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Cheap Residual Coding for Error-Selected 2-bit Channels
- Success threshold: At matched total storage including scales/metadata, the residual or mixed-bit scheme must reduce output relative MSE by at least 10% versus uniform 3-bit on real transformer weights, or match output error while improving measured memory bandwidth/latency.
- Stop condition: Stop if matched-storage residual coding remains worse than uniform 3-bit on both reconstruction/output metrics and any available task-level metric.

## Evidence references

- Artifact root: `<local-path>/projects/principled-residual-channels-for-2-bit-weight-quantization-with-iso-budget-baseline-8b9a61126ad6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
