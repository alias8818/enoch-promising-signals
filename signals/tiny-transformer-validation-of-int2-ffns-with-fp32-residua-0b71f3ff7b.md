# Tiny-transformer validation of INT2 FFNs with FP32 residual adapters

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiny-transformer-validation-of-int2-ffns-with-fp32-residua-0b71f3ff7b`
Run ID: `tiny-transformer-validation-of-int2-ffns-with-fp32-residua-0b71f3ff7b-20260603T200034177409+0000`

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

- Parent run decision: INT2 FFN with Parallel FP32 Residual Adapters: enoch://control-plane/projects/int2-ffn-with-parallel-fp32-residual-adapters-486872bdae11/runs/int2-ffn-with-parallel-fp32-residual-adapters-486872bdae11-20260603T134912680474+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/5bfc35e4763c

## What looked useful

Across seeds 7, 8, and 9, INT2-only eval loss exceeded dense by 0.07542 mean while INT2+adapter exceeded dense by 0.04998 mean, showing consistent loss-gap narrowing. INT2+adapter accuracy exceeded INT2-only by only 0.01092 mean, below the +0.05 success threshold, with 0 of 3 seeds passing.

## Boundaries and scale limits

Not a fully trainable transformer, not a real text corpus, not GPT-2-small-class, and not packed INT2 hardware. The intended tinygrad fully trainable transformer path was blocked by missing clang and an unusably slow Python backend.

## Claim scope

In a three-seed controlled NumPy tiny causal sequence model with frozen causal attention features and a trainable FFN residual branch, INT2 FFNs with a small FP32 residual adapter partially reduced INT2-only loss degradation but did not meet the preregistered accuracy repair threshold.

## Why it stopped

No-paper useful signal: the controlled Tier 1 test was executed and failed the stated success threshold, while showing partial adapter loss repair that warrants a stricter fully trainable follow-up.

## Recommended next action

Run a bounded deepen follow-up on a supported fully trainable tiny transformer stack with the same dense/INT2/INT2+adapter threshold before considering larger-scale validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fully trainable tiny-transformer INT2 FFN adapter threshold test
- Success threshold: Across at least three seeds, INT2+adapter eval loss <= dense eval loss + 0.25 and INT2+adapter eval accuracy >= INT2-only eval accuracy + 0.05, with at least two seeds individually passing and mean metrics passing.
- Stop condition: Stop as negative if the fully trainable implementation again produces mean accuracy repair below +0.05 or if dense training itself fails to learn the controlled task.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-transformer-validation-of-int2-ffns-with-fp32-residua-0b71f3ff7b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
