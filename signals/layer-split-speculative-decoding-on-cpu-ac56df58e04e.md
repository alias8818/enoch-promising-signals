# Layer-Split Speculative Decoding on CPU

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `layer-split-speculative-decoding-on-cpu-ac56df58e04e`
Run ID: `layer-split-speculative-decoding-on-cpu-ac56df58e04e-20260524T163020852557+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/04976dd3018e

## What looked useful

The distilgpt2 probe showed zero all-accepted draft blocks and observed advancement of only 1.33 to 1.5 tokens versus 2.11 to 3.96 tokens required for CPU break-even. A two-layer tiny model was positive but degenerate and not representative.

## Boundaries and scale limits

Evidence is limited to greedy decoding, GPT-2 class models, six prompts for distilgpt2, short prefixes, PyTorch CPU kernels, and per-step break-even measurement rather than a production quantized end-to-end decoder.

## Claim scope

On a CPU worker, unmodified GPT-2 layer-prefix drafts using the original LM head did not beat cached target decoding for distilgpt2 across splits 1/6 and 3/6 with draft lengths 2 and 4.

## Why it stopped

Proxy/early falsification: a real six-layer GPT-2 probe fell well below CPU break-even because early-layer draft agreement was too low, though larger quantized engines or trained split heads were not directly tested.

## Recommended next action

Stop this unmodified layer-prefix approach; only revisit with a bounded follow-up that trains or calibrates an intermediate draft head and requires end-to-end speedup over a cached CPU baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated Intermediate Head for CPU Layer-Split Speculation
- Success threshold: At least 1.15x end-to-end tokens/sec over cached target decoding on the same CPU for one split and draft length, with no degradation in exact greedy output.
- Stop condition: Stop if calibrated-head mean advancement remains below measured break-even for all tested splits/draft lengths or if head overhead erases the speedup.

## Evidence references

- Artifact root: `<local-path>/projects/layer-split-speculative-decoding-on-cpu-ac56df58e04e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
