# Self-Speculative Layer-Skip Decoding on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `self-speculative-layer-skip-decoding-on-cpu-fe323590d23c`
Run ID: `self-speculative-layer-skip-decoding-on-cpu-fe323590d23c-20260530T053301099076+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c14bdb765dcf

## What looked useful

Layer-skipped self-speculative decoding can be CPU-faster in a bounded proxy, but the speedup partly comes from batched full verification rather than acceptance alone; real Transformer validation is required before any paper claim.

## Boundaries and scale limits

Synthetic residual decoder only; no trained language model, no attention/KV-cache path, no perplexity or text-quality measurement, and CPU BLAS timing variability was not exhaustively controlled.

## Claim scope

In a deterministic NumPy residual decoder proxy on CPU, a 3-of-12-layer skipped draft with batched verification improved greedy decoding wall-clock throughput versus dense one-token full decoding, reaching 2.02x mean speedup on held-out 2048-token traces at 0.766 mean acceptance.

## Why it stopped

No-paper useful signal: proxy evidence supports the mechanism direction but is not direct/full evidence for real language models.

## Recommended next action

Run a bounded CPU experiment on a small real Transformer with KV-cache-aware dense decoding, exact greedy self-spec verification, and a batched-verification-only control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Transformer CPU Self-Spec Verification
- Success threshold: At least 1.25x mean tokens/sec improvement over dense greedy with identical greedy output and at least 0.6 draft-token acceptance on a real small Transformer.
- Stop condition: Stop as negative if exact-output self-spec is under 1.0x mean speedup or if acceptance stays below 0.4 after reasonable draft-depth/chunk sweeps.

## Evidence references

- Artifact root: `<local-path>/projects/self-speculative-layer-skip-decoding-on-cpu-fe323590d23c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
