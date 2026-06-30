# Tiny Transformer Validation of N-Gram Anchor Sparse Attention

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-transformer-validation-of-n-gram-anchor-sparse-attent-19a8ed4043`
Run ID: `tiny-transformer-validation-of-n-gram-anchor-sparse-attent-19a8ed4043-20260604T155221013941+0000`

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

- Parent run decision: Sparse Anchor Attention via N-Grams: enoch://control-plane/projects/sparse-anchor-attention-via-n-grams-010b635aff5f/runs/sparse-anchor-attention-via-n-grams-010b635aff5f-20260604T101514832957+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/2322373383a0

## What looked useful

Corrected 3-seed direct test: n-gram-anchor sparse mean validation accuracy 0.9974, local-only 0.0153, dense same-budget 0.0254; anchor edge fraction 0.2603. The mechanism is supported for designed n-gram keyed retrieval but is not paper-ready.

## Boundaries and scale limits

Synthetic tiny-scale CPU experiment only; no natural-language corpus, no GPT-2-small-class baseline, no tuned dense convergence baseline, no GPU/kernel throughput validation, and no robustness sweep over longer contexts or alternative anchor definitions.

## Claim scope

On a synthetic repeated-bigram key/value retrieval task with sequence length 64 and a 112,448-parameter tiny transformer, local-plus-n-gram-anchor sparse attention solved the task across 3 seeds while using about 26% of dense causal attention edges and strongly outperforming a local-only sparse mask with nearly identical edge count.

## Why it stopped

Tier 1 direct mechanism threshold was met, but evidence remains synthetic/tiny and same-budget dense did not converge, so this is useful no-paper evidence rather than publication-grade validation.

## Recommended next action

Run a bounded medium follow-up with a tuned dense baseline and a mixed retrieval/language-modeling dataset before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium Tuned Baseline Test for N-Gram Anchor Sparse Attention
- Success threshold: N-gram-anchor sparse reaches at least 95% of tuned dense validation quality, beats local-only by at least 10 percentage points on retrieval accuracy or a meaningful perplexity margin, and uses at most 35% of dense causal edges across all seeds.
- Stop condition: Stop if tuned dense learns the task but n-gram-anchor sparse fails either the 95% dense-quality threshold or the local-only improvement threshold in two independent seeds.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-transformer-validation-of-n-gram-anchor-sparse-attent-19a8ed4043`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
