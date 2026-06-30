# Ternary GPT-2 with residual channels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ternary-gpt-2-with-residual-channels-7dee1546b5fe`
Run ID: `ternary-gpt-2-with-residual-channels-7dee1546b5fe-20260525T024151478602+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/d6ad506a8a39

## What looked useful

On the learnable increment_copy probe, dense reached val loss 0.2468, ternary-only 0.2561, and ternary-plus-residual 0.2555. Residual channels improved over ternary-only by only 0.00057 validation loss while using 1.91x estimated storage and running slower in this PyTorch CPU implementation.

## Boundaries and scale limits

No GPT-2-small-scale or real-text corpus training was run; results use one seed, tiny 2-layer 96-hidden models, synthetic tasks, analytical storage estimates, and no optimized ternary inference kernels.

## Claim scope

In a CPU-bounded tiny GPT-style Transformer on deterministic synthetic next-token tasks, ternary weights were trainable and retained near-dense quality on an easy learnable probe, but adding 12.5% dense residual output channels did not materially improve validation loss over ternary-only.

## Why it stopped

Bounded synthetic evidence shows trainability but does not support a meaningful residual-channel advantage over ternary-only; this is not full-scale validation.

## Recommended next action

Stop this run as no-paper useful signal; the only concrete next bounded action is a multi-seed residual-fraction ablation on a small real text corpus with parameter-matched dense and ternary controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-seed real-text residual-fraction ablation for ternary tiny GPT
- Success threshold: A residual-channel variant must improve mean validation loss over ternary-only by at least 0.02 with no overlapping seed-level confidence interval while keeping estimated storage below 35% of dense.
- Stop condition: Stop if no residual fraction beats ternary-only by 0.01 validation loss after the first two seeds or if dense and ternary-only do not both learn the real-text baseline task.

## Evidence references

- Artifact root: `<local-path>/projects/ternary-gpt-2-with-residual-channels-7dee1546b5fe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
