# Direct Local LLM Cascade Confidence Router Benchmark

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `direct-local-llm-cascade-confidence-router-benchmark-499591cc4f`
Run ID: `direct-local-llm-cascade-confidence-router-benchmark-499591cc4f-20260524T073222995351+0000`

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

- Parent run decision: Local Cascade Router with Tiny Confidence Oracle: enoch://control-plane/projects/local-cascade-router-with-tiny-confidence-oracle-bee70431d20c/runs/local-cascade-router-with-tiny-confidence-oracle-bee70431d20c-20260524T071643017596+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2f1443c8e737

## What looked useful

The predeclared calibrated router failed: held-out cascade accuracy was 0.600 versus direct-large accuracy 0.800, retaining only 0.750 of large-model accuracy despite reducing large calls by 0.875. Failure was driven by high-confidence cheap-model errors. A post-hoc conservative 0.95 threshold on the same holdout would have met the numeric tradeoff, so the mechanism is not a hard negative but requires pre-registered larger validation.

## Boundaries and scale limits

Small hand-built multiple-choice set; answer-letter logprob confidence only; no production traces, no public benchmark suite, no concurrent serving, no open-ended generation, and no larger fallback model than 3B.

## Claim scope

Tier 1 direct local benchmark of a calibrated confidence router from Qwen2.5-0.5B-Instruct to Qwen2.5-3B-Instruct on 60 deterministic multiple-choice questions with 20 calibration and 40 held-out examples.

## Why it stopped

The direct Tier 1 calibrated-router test failed the predeclared held-out accuracy-retention threshold; exploratory post-hoc threshold success is not publication-grade or primary validation.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded deepen follow-up with a larger public benchmark, separate calibration split, and pre-registered conservative threshold policy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pre-registered Conservative Confidence Router on Larger Local MCQ Benchmark
- Success threshold: Held-out cascade accuracy retention must be at least 95% of direct-large accuracy and large-model call reduction must be at least 30%, with the threshold selected only from the calibration split.
- Stop condition: Stop as negative if no pre-registered threshold on the calibration split satisfies the retention target, or if held-out retention falls below 95% even when large-call reduction is at least 30%.

## Evidence references

- Artifact root: `<local-path>/projects/direct-local-llm-cascade-confidence-router-benchmark-499591cc4f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
