# Layer-skip speculative decoding with confidence scoring

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `layer-skip-speculative-decoding-with-confidence-scoring-bb3dfbd2c68b`
Run ID: `layer-skip-speculative-decoding-with-confidence-scoring-bb3dfbd2c68b-20260608T230001550810+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/0547e56fa3bc

## What looked useful

The calibrated run reached 100% full-model validation accuracy. The only gate meeting the local success threshold was depth 7 of 8 residual layers at confidence threshold 0.35, with 100% accept rate, 0% accepted disagreement, and 1.125x estimated layer-count speedup. Depth 6 could reach 1.167x estimated speedup but accepted 6.06% disagreements, or zero disagreement at only 1.052x speedup.

## Boundaries and scale limits

Synthetic finite token table, residual MLP rather than transformer, fixed-context classification rather than autoregressive KV-cache decoding, and toy NumPy timing rather than production LLM latency.

## Claim scope

In a small NumPy residual next-token proxy, confidence-thresholded intermediate logits can safely skip only the final residual layer while preserving full-depth predictions; more aggressive layer skipping did not meet the combined speed and disagreement threshold.

## Why it stopped

No-paper closure: this is a bounded toy/proxy useful signal, not direct transformer or production speculative-decoding evidence.

## Recommended next action

Run the same confidence-gated layer-skip test on a compact transformer with real autoregressive decoding and compare against full-depth decoding, no-confidence early exit, entropy, and logit-margin gates.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Confidence-gated layer skipping in a compact autoregressive transformer
- Success threshold: At least one nontrivial gate skips one or more final transformer layers with accepted disagreement <=1%, accept rate >=5%, and measured decode speedup >=1.10x on a held-out prompt set.
- Stop condition: Stop if all gates either exceed 1% accepted disagreement at >=1.10x speedup or fall below 1.10x measured speedup when disagreement is kept <=1%.

## Evidence references

- Artifact root: `<local-path>/projects/layer-skip-speculative-decoding-with-confidence-scoring-bb3dfbd2c68b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
