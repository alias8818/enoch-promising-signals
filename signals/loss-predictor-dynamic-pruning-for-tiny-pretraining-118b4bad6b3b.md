# Loss-Predictor Dynamic Pruning for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `loss-predictor-dynamic-pruning-for-tiny-pretraining-118b4bad6b3b`
Run ID: `loss-predictor-dynamic-pruning-for-tiny-pretraining-118b4bad6b3b-20260528T065532121320+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/06d174cb09bf

## What looked useful

The loss predictor selected high-current-loss examples, but high loss was dominated by irreducible noise. Candidate streams contained about 19.9% noise, while predictor-prune selected about 69.6% noise, producing 3.0967 mean validation loss versus 1.6916 for dense at the same model-trained token count.

## Boundaries and scale limits

This is a bounded proxy using a tiny model, synthetic corpus, 240-step runs, and three seeds. It does not rule out larger models, real corpora, token-level pruning, predictor targets based on reducible loss or gradient value, or filtering policies that avoid irreducible-noise examples.

## Claim scope

Raw predicted-loss top-k sequence pruning before the model forward pass was tested on a tiny GPT-style next-token LM over a synthetic mixed-regime corpus with easy, learnable, and intentionally unlearnable high-entropy sequences. In this scope, it failed to preserve validation loss at the same model-trained token count as dense training.

## Why it stopped

Proxy/early falsification: the tested raw predicted-loss selector over-sampled unlearnable noise and substantially worsened validation loss, so the result is not a full-scale validation and not paper-positive.

## Recommended next action

Stop this raw-loss top-k pruning line as tested; a bounded follow-up should replace raw loss with a reducible-loss or learning-progress target and require no quality regression versus dense at matched model-trained tokens.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Reducible-loss predictor pruning for tiny LM pretraining
- Success threshold: At equal model-trained tokens, validation loss is no worse than 2% above dense while training on no more than 50% of candidate examples, and selected unlearnable-noise fraction is no more than 2x its candidate fraction.
- Stop condition: Stop if reducible-loss selection still enriches unlearnable noise above 2x or remains more than 2% worse than dense validation loss after three seeds.

## Evidence references

- Artifact root: `<local-path>/projects/loss-predictor-dynamic-pruning-for-tiny-pretraining-118b4bad6b3b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
