# Cross-layer KV sharing for long context

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `cross-layer-kv-sharing-for-long-context-4502a15954e7`
Run ID: `cross-layer-kv-sharing-for-long-context-4502a15954e7-20260525T112526913516+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/625d0a40f048

## What looked useful

Halving GPT-2 KV groups by sharing adjacent-layer K/V increased WikiText perplexity from 29.10 to 721.95 at 512 tokens and from 24.50 to 725.29 at 1024 tokens; adjacent-layer K/V cosine similarity was near zero.

## Boundaries and scale limits

Tested GPT-2 small only, not trained shared-KV architectures, fine-tuned adaptation, models larger than GPT-2, contexts beyond 1024 tokens, retrieval tasks, or production KV-cache kernels.

## Claim scope

Post-hoc fixed-group cross-layer KV sharing is not viable as a drop-in inference modification for GPT-2-small-class pretrained decoder-only models on WikiText chunks up to 1024 tokens.

## Why it stopped

Moderate proxy/direct evidence early-falsifies post-hoc KV sharing as a drop-in inference technique, but does not fully validate or refute trained shared-KV architectures.

## Recommended next action

Stop this no-paper post-hoc inference path; the only worthwhile bounded next step is a trained-from-scratch tiny shared-KV transformer baseline against a parameter-matched standard transformer.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train a tiny transformer with grouped shared KV from initialization
- Success threshold: At 50% KV-cache group reduction, the trained shared-KV model reaches validation loss no more than 10% worse than the standard baseline at the same parameter scale and token budget.
- Stop condition: Stop if the shared-KV model remains more than 25% worse in validation loss after the planned token budget or shows unstable training relative to the baseline.

## Evidence references

- Artifact root: `<local-path>/projects/cross-layer-kv-sharing-for-long-context-4502a15954e7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
