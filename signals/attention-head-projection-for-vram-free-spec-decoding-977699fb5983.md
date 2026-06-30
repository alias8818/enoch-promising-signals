# Attention-Head Projection for VRAM-Free Spec Decoding

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `attention-head-projection-for-vram-free-spec-decoding-977699fb5983`
Run ID: `attention-head-projection-for-vram-free-spec-decoding-977699fb5983-20260526T024931665527+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2d456810f23e

## What looked useful

Across 4,096 positions per model, the deployable all-head-summed zero-weight proposer had 0% prefix acceptance. GPT-2 small's best individual head reached only 5.37% immediate top-1 match, and even an oracle over all heads reached only 5.71% one-token and 0.22% two-token prefix match. This is an early falsification for raw head unembedding as a standalone speculative decoder.

## Boundaries and scale limits

This was a bounded trace/proxy evaluation on GPT-2-family models, not a full generation-loop speed benchmark. It did not test learned probes, CPU-resident projection tables, low-rank adapters, larger models, or regenerated greedy continuations for every prefix.

## Claim scope

For distilgpt2 and GPT-2 small on WikiText-2 validation, raw attention-head outputs projected through tied LM-head slices with no learned projection weights do not provide a useful VRAM-free speculative drafting signal.

## Why it stopped

Proxy/early falsification: the direct head-projection signal is far below useful speculative acceptance rates even under an oracle-over-heads diagnostic, so full serving integration is not warranted for this variant.

## Recommended next action

Stop this zero-learned head-projection path as no-paper negative evidence; if continuing, run a bounded adjacent test of tiny learned offset-specific probes with an explicit end-to-end acceptance and latency threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny Learned Head Probes for VRAM-Free Speculative Drafting
- Success threshold: On GPT-2 small or larger, a fixed deployable probe achieves at least 30% one-token acceptance and at least 10% two-token prefix acceptance with a measured end-to-end speedup over greedy target decoding and negligible added VRAM.
- Stop condition: Stop if held-out one-token acceptance stays below 15%, two-token prefix acceptance stays below 3%, or projection/transfer overhead eliminates any measured speedup.

## Evidence references

- Artifact root: `<local-path>/projects/attention-head-projection-for-vram-free-spec-decoding-977699fb5983`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
