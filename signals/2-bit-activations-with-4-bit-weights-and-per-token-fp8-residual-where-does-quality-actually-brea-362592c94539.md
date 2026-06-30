# 2-bit activations with 4-bit weights and per-token FP8 residual: where does quality actually break?

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-activations-with-4-bit-weights-and-per-token-fp8-residual-where-does-quality-actually-brea-362592c94539`
Run ID: `2-bit-activations-with-4-bit-weights-and-per-token-fp8-residual-where-does-quality-actually-brea-362592c94539-20260611T204700991877+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/083e54a74394

## What looked useful

A2W4 output NMSE ranged from 0.203 to 9.417 and failed worst on Student-t and outlier-channel activations. Adding per-token FP8 residual improved output NMSE by 14.7x to 504.0x and kept residual-path NMSE within 1.01x to 1.37x of W4-only, while residual top-1 logit flips remained close to W4-only at about 0.176 to 0.227.

## Boundaries and scale limits

No end-to-end language-model perplexity, benchmark accuracy, multi-layer accumulation, training stability, or kernel throughput validation. Tested hidden sizes up to 2048, output dimension up to 1024, 512 tokens, and three seeds per case.

## Claim scope

Synthetic one-layer CUDA proxy with controlled activation distributions: per-token FP8 residual repairs most 2-bit activation damage and leaves output error close to W4-only, but raw A2W4 breaks badly under heavy-tail and outlier-channel activations.

## Why it stopped

Proxy-only evidence supports the mechanism but does not validate end-to-end quality or efficiency.

## Recommended next action

Stop this run as a no-paper useful signal; run a bounded GPT-2-small-class end-to-end validation next if continuing the line.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small end-to-end validation for A2 plus FP8 residual with W4 weights
- Success threshold: Residual path reduces at least 70% of the perplexity delta between raw A2W4 and W4-only while keeping layerwise output NMSE within 1.5x W4-only on most layers.
- Stop condition: Stop if raw A2W4 and residual path both degrade perplexity similarly, if residual-path layer error grows monotonically beyond 2x W4-only in early blocks, or if implementation shows the residual representation is dominated by FP8 cost without a quality advantage over FP8 activations.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-activations-with-4-bit-weights-and-per-token-fp8-residual-where-does-quality-actually-brea`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
