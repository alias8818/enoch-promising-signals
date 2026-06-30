# Ternary weights with learned residual scalars on GPT-2-small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ternary-weights-with-learned-residual-scalars-on-gpt-2-small-b4598cc4a4b6`
Run ID: `ternary-weights-with-learned-residual-scalars-on-gpt-2-small-b4598cc4a4b6-20260607T124057789643+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/26d63467276c

## What looked useful

Two-stage learned residual scalars reduced weighted projection relative MSE from 0.236 to 0.079 at the best loss point and improved KL versus one-stage ternary, but best residual loss still rose by 4.40 nats and perplexity was 81x dense.

## Boundaries and scale limits

CPU-only early probe; no backprop-trained scalars, no activation-aware calibration, no standard full validation corpus, no retraining, embeddings and LM head excluded.

## Claim scope

Post-training replacement of GPT-2-small transformer projection matrices with global learned scalar ternary plus residual ternary approximations improves weight reconstruction versus one-stage ternary but remains functionally non-viable on an 8-prompt short-context language-model probe.

## Why it stopped

Proxy/early falsification: direct GPT-2-small projection replacement was tested, but only on short prompts and without training; the simplest residual-scalar ternary design remains far from dense behavior.

## Recommended next action

Stop this simple post-training global-scalar path as no-paper; the only bounded next test worth running is activation-aware or per-channel residual scalar calibration with a predeclared loss-delta threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-aware per-channel residual scalars for ternary GPT-2-small projections
- Success threshold: Residual calibrated variant achieves loss_delta < 1.0 nat and token KL < 1.0 while retaining a clear storage/computation advantage over dense and outperforming one-stage ternary.
- Stop condition: Stop if activation-aware calibration cannot get below loss_delta 2.0 nats on the bounded validation subset or if storage accounting eliminates the compression advantage.

## Evidence references

- Artifact root: `<local-path>/projects/ternary-weights-with-learned-residual-scalars-on-gpt-2-small-b4598cc4a4b6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
