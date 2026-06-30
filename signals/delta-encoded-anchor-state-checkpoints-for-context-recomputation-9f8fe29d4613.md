# Delta-Encoded Anchor State Checkpoints for Context Recomputation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `delta-encoded-anchor-state-checkpoints-for-context-recomputation-9f8fe29d4613`
Run ID: `delta-encoded-anchor-state-checkpoints-for-context-recomputation-9f8fe29d4613-20260602T225752720661+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/93566c73e35a

## What looked useful

Append-delta storage is an exact representation for online causal-transformer KV anchor checkpoints and gives the expected storage reduction from avoiding repeated prefix KV snapshots. In-memory reconstruction was 4.1x-5.1x faster than full-prefix replay in the local benchmark, but slower than cloning a full final checkpoint in some settings.

## Boundaries and scale limits

Random weights only; 2048-token context only; no production inference-engine integration; no trained generation quality check; no disk, network, paged-KV allocator, long-context, multi-query attention, 7B+, or serving-trace validation.

## Claim scope

In a bounded GB10 benchmark using a random-weight 24M-parameter GPT-2-style transformer at 2048 tokens, online append-delta KV anchor checkpoints reconstructed the online final anchor exactly and reduced checkpoint storage to 6.1%-22.2% of full-snapshot storage across anchor strides 64-256.

## Why it stopped

Closed as no-paper useful signal: local evidence supports the checkpoint representation mechanism, but this is not full validation of practical serving value.

## Recommended next action

Build a small inference-engine integration that restores append-delta reconstructed KV caches into generation on a trained small model and measures time-to-first-token, memory footprint, and output equivalence under realistic anchor-hit patterns.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end trained-model KV restore benchmark for append-delta anchor checkpoints
- Success threshold: At 2048-8192 token contexts on a trained small model, reconstructed-cache generation must match original-cache logits within fp tolerance and reduce checkpoint memory by at least 4x while improving mean time-to-first-token by at least 2x versus full-prefix replay.
- Stop condition: Stop if reconstructed KV cannot be restored without logit/token mismatch, or if reconstruction plus restore latency is not faster than full-prefix replay at two tested context lengths.

## Evidence references

- Artifact root: `<local-path>/projects/delta-encoded-anchor-state-checkpoints-for-context-recomputation-9f8fe29d4613`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
