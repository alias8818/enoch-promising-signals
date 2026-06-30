# Verifier versus token-loss curation on model-generated GSM8K traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `verifier-versus-token-loss-curation-on-model-generated-gsm-36edb4c442`
Run ID: `verifier-versus-token-loss-curation-on-model-generated-gsm-36edb4c442-20260629T095549329733+0000`

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

- Parent run decision: Real-trace prefix verifier versus token-loss curation: enoch://control-plane/projects/real-trace-prefix-verifier-versus-token-loss-curation-3b7c767fc2/runs/real-trace-prefix-verifier-versus-token-loss-curation-3b7c767fc2-20260629T084412212920+0000
- Parent run decision: Early-token reasoning quality scorer for post-training data curation: enoch://control-plane/projects/early-reasoning-quality-token-loss-curation-20260628/runs/early-reasoning-quality-token-loss-curation-20260628-20260629T062713910921+0000

## What looked useful

Token loss was directionally correlated with correctness in aggregate, but it frequently selected fluent wrong traces over available correct traces. Exact-answer verification is a much cleaner high-precision curation filter for this bounded GSM8K trace setting.

## Boundaries and scale limits

Single 0.5B instruct generator/scorer, 60 GSM8K test problems, four samples per problem, one prompt format, no downstream fine-tuning comparison, and final-answer parsing sensitivity for markerless outputs.

## Claim scope

On 240 locally generated GSM8K test traces from Qwen/Qwen2.5-0.5B-Instruct, exact-answer verifier curation retained correct traces with 100% precision and 61.7% permissive-parser problem coverage, while same-model average-token-loss top-1 selection achieved 36.7% precision; under strict explicit-answer-marker parsing the corresponding coverages were 30.0% and 15.0%.

## Why it stopped

Bounded local evidence supports the mechanism but does not provide paper-grade downstream or robustness evidence.

## Recommended next action

Run a bounded downstream training test: fine-tune a small model on equal-size verifier-selected versus token-loss-selected trace sets with strict answer markers, then compare held-out GSM8K accuracy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Downstream GSM8K fine-tuning comparison for verifier-selected versus loss-selected traces
- Success threshold: Verifier-selected fine-tuning improves held-out exact-answer accuracy by at least 3 absolute percentage points over token-loss-selected fine-tuning at matched data size and training budget.
- Stop condition: Stop if strict verifier coverage remains below 25% after prompt repair or if matched fine-tuning shows less than 1 percentage point advantage across two seeds.

## Evidence references

- Artifact root: `<local-path>/projects/verifier-versus-token-loss-curation-on-model-generated-gsm-36edb4c442`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
