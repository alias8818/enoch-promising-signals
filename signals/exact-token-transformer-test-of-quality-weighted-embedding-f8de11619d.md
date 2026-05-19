# Exact-token transformer test of quality-weighted embedding diversity sampling

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-token-transformer-test-of-quality-weighted-embedding-f8de11619d`
Run ID: `exact-token-transformer-test-of-quality-weighted-embedding-f8de11619d-20260518T202105561819+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/62eeb01088ca

## What looked useful

QWED reached 0.7181 mean validation accuracy versus random 0.6713, quality-only 0.6952, and diversity-only 0.6410 at exactly 4,608 training tokens per run. It beat random in 4/5 seeds, quality-only in 3/5, and diversity-only in 5/5, but had worse mean validation loss than random/diversity.

## Boundaries and scale limits

Synthetic data only; tiny Transformer encoder; 5 seeds; 4,608 selected training tokens per method and seed; no real text embeddings, no real quality estimator, no large language-model pretraining or finetuning validation.

## Claim scope

In a controlled synthetic exact-token small-transformer classification test, quality-weighted embedding diversity selection improved mean validation accuracy over random, quality-only, and diversity-only controls while preserving full cluster coverage and high selected-label cleanliness.

## Why it stopped

No-paper closure: this is a useful small direct synthetic signal, but the evidence is loss-mixed and not publication-grade.

## Recommended next action

Run a bounded real-text exact-token follow-up with frozen sentence embeddings and predeclared quality scores; stop paper escalation unless QWED beats the best baseline by at least 2 percentage points in mean task score without worse mean validation loss.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-text exact-token QWED selection with loss guardrail
- Success threshold: QWED improves mean validation or test task score by at least 2 percentage points over the strongest baseline and does not have worse mean validation loss than that strongest baseline under the exact same token budget.
- Stop condition: Stop if QWED fails to beat the strongest baseline by 2 percentage points, loses on validation loss, or the advantage appears only in synthetic or quality-leakage settings.

## Evidence references

- Artifact root: `<local-path>/projects/exact-token-transformer-test-of-quality-weighted-embedding-f8de11619d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
