# Real small-LM KV trace test for 2-bit residual block gates

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-small-lm-kv-trace-test-for-2-bit-residual-block-gates-f8490ab41d`
Run ID: `real-small-lm-kv-trace-test-for-2-bit-residual-block-gates-f8490ab41d-20260519T160407416563+0000`

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

- Internal Enoch project: Real small-LM KV trace test for 2-bit residual block gates: internal_generated:real-small-lm-kv-trace-test-for-2-bit-residual-block-gates-f8490ab41d

## What looked useful

KV-trace-conditioned gates beat random 2-bit and shuffled-trace controls within the gated family, but dense residuals and a simple fixed 2/3 residual gate were better on validation loss. Mean val loss: dense 2.3122, fixed_twothirds_2bit 2.3544, kv2bit 2.3999, shuffled_kv2bit 2.4163, random_2bit 2.4739.

## Boundaries and scale limits

This is a real small-LM Tier 2 test, not GPT-2-small-class token-level pretraining, long-context serving, or hardware-aware cache/skip validation. It does not rule out identity-biased, attention-only, or larger-scale gate families.

## Claim scope

A 4-layer, 4-head, 128-wide char-level causal Transformer trained on Tiny Shakespeare for 600 steps across seeds 0, 1, and 2. The tested KV-trace 2-bit residual block gate was active and trace-correlated, but did not match the dense residual baseline on validation loss.

## Why it stopped

Tier 2 direct small-LM evidence rejects the tested 2-bit KV-trace residual block gate as a dense-baseline replacement: kv2bit was +0.0877 validation loss and 9.15% relative perplexity worse than dense across 3 fixed seeds.

## Recommended next action

Stop paper work for this gate design; only pursue a bounded follow-up if it tests an identity-biased or attention-only compute-skip gate that must match dense validation loss within 1% while demonstrating real skip/cache savings.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Identity-biased KV trace gates with measured skip savings
- Success threshold: Across at least 3 fixed seeds, identity-biased KV gating must keep mean validation perplexity within 1% of dense and demonstrate at least 15% measured skip/cache-operation reduction, while beating shuffled/random controls.
- Stop condition: Stop if the identity-biased KV gate is more than 1% worse in mean perplexity than dense or shows less than 10% measured skip/cache-operation reduction after the planned training budget.

## Evidence references

- Artifact root: `<local-path>/projects/real-small-lm-kv-trace-test-for-2-bit-residual-block-gates-f8490ab41d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
