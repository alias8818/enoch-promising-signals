# Blockwise INT3 with FP4 per-block residual channel

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `blockwise-int3-with-fp4-per-block-residual-channel-6e28a0c4602d`
Run ID: `blockwise-int3-with-fp4-per-block-residual-channel-6e28a0c4602d-20260629T234820305465+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1ff1ce5b8c3a

## What looked useful

The residual-channel mechanism is measurable but weak: it helps INT3 slightly, with larger gains only at smaller block widths that raise storage overhead, and it does not close most of the gap to INT4.

## Boundaries and scale limits

No real model weights, perplexity, accuracy, finetuning, hardware packing, CUDA kernel throughput, or exact vendor FP4 behavior were tested. The result is a bounded proxy, not a full validation.

## Claim scope

Synthetic numpy reconstruction-only evidence for 1024x1024 matrices shows that one selected FP4-like residual column per 64x64 INT3 block consistently reduces relative L2 error versus INT3-only, but only by 0.99% to 2.54% across tested distributions and remains far from INT4 reconstruction quality.

## Why it stopped

Synthetic reconstruction evidence is useful but insufficient and does not support a paper-positive claim; the strong version of the hypothesis is not supported by this proxy.

## Recommended next action

Stop this run as a proxy early falsification of the strong claim; only pursue a bounded follow-up if testing real transformer weights with perplexity or task accuracy is available.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-weight perplexity test for INT3 plus one FP4 residual channel
- Success threshold: At comparable storage below INT4, INT3+FP4 residual must recover at least half of the INT3-to-INT4 perplexity or accuracy gap on a real model while preserving a clear bits-per-weight advantage.
- Stop condition: Stop if real-model metrics show less than 10% recovery of the INT3-to-INT4 downstream quality gap or if storage overhead approaches INT4 without quality parity.

## Evidence references

- Artifact root: `<local-path>/projects/blockwise-int3-with-fp4-per-block-residual-channel-6e28a0c4602d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
