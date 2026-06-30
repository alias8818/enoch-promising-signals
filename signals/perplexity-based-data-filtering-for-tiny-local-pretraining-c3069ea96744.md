# Perplexity-based data filtering for tiny local pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `perplexity-based-data-filtering-for-tiny-local-pretraining-c3069ea96744`
Run ID: `perplexity-based-data-filtering-for-tiny-local-pretraining-c3069ea96744-20260522T203135046009+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/72a1352c3750

## What looked useful

Low teacher-perplexity selection beat random in 3/3 seeds with mean final validation loss 7.4094 vs 7.4479 for random (mean delta -0.0385). High-perplexity selection was worse on average at 7.4729.

## Boundaries and scale limits

Single corpus, single teacher, 192 selected chunks per condition, sequence length 96, short training horizon, no downstream tasks, no deduplication controls, and no full-scale pretraining validation.

## Claim scope

On a small WikiText-2 local pretraining probe with a distilgpt2 teacher and a tiny 2-layer causal Transformer trained for 120 steps on equal-size selected chunks, lowest-teacher-perplexity filtering improved heldout validation loss versus random selection across three seeds.

## Why it stopped

No-paper closure: bounded local evidence supports a useful mechanism signal, but the scope is too small and short-horizon for publication-grade validation.

## Recommended next action

Run a medium confirmation on at least two corpora with larger selected-token budgets, repeated random baselines, threshold sweeps, and longer training to determine whether the low-PPL advantage persists beyond this toy probe.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium-scale low-perplexity filtering confirmation for tiny pretraining
- Success threshold: Low-PPL filtering improves final validation loss versus random by at least 0.03 mean loss on both corpora, wins at least 75% of seed-by-corpus comparisons, and does not rely on duplicate leakage.
- Stop condition: Stop if low-PPL filtering fails to beat random on either corpus, the effect falls below 0.01 mean validation-loss improvement, or duplicate/content artifacts explain the gain.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-based-data-filtering-for-tiny-local-pretraining-c3069ea96744`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
