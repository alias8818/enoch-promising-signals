# INT3 with top-k outlier channels kept in FP16 (GPT-2-small)

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `int3-with-top-k-outlier-channels-kept-in-fp16-gpt-2-small-425492126a60`
Run ID: `int3-with-top-k-outlier-channels-kept-in-fp16-gpt-2-small-425492126a60-20260621T033001993755+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ad6e7f5c06bf

## What looked useful

Naive INT3 severely degraded GPT-2-small perplexity. Reference PPL was 50.26; INT3 PPL ranged from 1481.68 with 0% kept channels to 315.00 with 20% kept channels. Keeping outlier channels helped monotonically but remained 6.27x worse than reference at only 2.85x estimated Conv1D-weight compression.

## Boundaries and scale limits

CPU-only quality probe; no custom INT3 runtime kernel, no activation-aware calibration, no GPTQ/AWQ-style error compensation, no full validation split, and no larger model family tested. Storage compression is estimated for Conv1D weights excluding bias.

## Claim scope

Bounded GPT-2-small post-training probe: symmetric weight-only INT3 quantization of GPT-2 Conv1D weights with max-abs top-k output channels left unquantized, evaluated on 8192 WikiText-2 validation tokens.

## Why it stopped

Bounded direct quality test found a large perplexity regression for every tested keep fraction, so the naive max-abs top-k outlier-channel INT3 hypothesis is unsupported; this is an early bounded falsification rather than a full validation of all INT3 methods.

## Recommended next action

Stop this naive scheme as no-paper evidence; only revisit with a bounded activation-aware INT3 recipe such as GPTQ/AWQ-style compensation and a predefined perplexity tolerance.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-aware INT3 outlier-channel preservation for GPT-2-small
- Success threshold: Perplexity no more than 25% above the unquantized reference while preserving at least 3x estimated Conv1D-weight compression excluding bias.
- Stop condition: Stop if activation-aware INT3 remains more than 2x reference perplexity at every tested kept-channel fraction up to 20%, or if the method cannot maintain at least 3x estimated compression.

## Evidence references

- Artifact root: `<local-path>/projects/int3-with-top-k-outlier-channels-kept-in-fp16-gpt-2-small-425492126a60`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
