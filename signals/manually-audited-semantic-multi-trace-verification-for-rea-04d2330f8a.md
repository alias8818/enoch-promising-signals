# Manually audited semantic multi-trace verification for real agent final claims

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `manually-audited-semantic-multi-trace-verification-for-rea-04d2330f8a`
Run ID: `manually-audited-semantic-multi-trace-verification-for-rea-04d2330f8a-20260517T173633445846+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Manually audited semantic multi-trace verification for real agent final claims: internal_generated:manually-audited-semantic-multi-trace-verification-for-rea-04d2330f8a

## What looked useful

On 15,624 fixed-seed claim checks from 856 completed local agent projects, semantic_multi_trace reached 1.0000 accuracy/F1 versus 0.7466 accuracy for decision_json_only, 0.4782 for quote_only_run_notes, and 0.5274 for accept_all. Bootstrap accuracy delta over decision_json_only was +0.2533 with 95% CI [0.2469, 0.2604].

## Boundaries and scale limits

The run used real local agent artifacts but controlled/generated labels and constrained claim grammars; it did not evaluate arbitrary natural-language final claims, independent human labels, LLM-judge baselines, production agent logs outside the local corpus, or cross-organization traces.

## Claim scope

Typed semantic multi-trace verification over 856 real local Enoch/Codex worker artifacts can validate or reject controlled final-claim families about decisions, statuses, artifact paths, follow-up flags, and JSON metrics more accurately than accept-all, quote-only, or decision-JSON-only baselines.

## Why it stopped

The bounded local corpus supports the typed multi-trace verification mechanism, but the evidence remains controlled-label and schema-constrained rather than publication-grade open semantic auditing of natural agent final answers.

## Recommended next action

Stop this run as useful no-paper evidence; the next concrete step is a bounded deepen study with naturally written real final claims and independent manual support labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Human-labeled natural final-claim audit for real agent traces
- Success threshold: On the human-labeled natural-claim set, multi-trace verification improves accuracy by >= 0.15 over the best non-semantic baseline, has precision >= 0.90 for unsupported-claim flags, recall >= 0.70, and the 95% bootstrap CI for accuracy improvement excludes zero.
- Stop condition: Stop if independent manual labels cannot be produced, if inter-annotator agreement is below 0.70 Cohen kappa after guideline refinement, or if multi-trace verification fails to beat the best non-semantic baseline by at least 0.05 accuracy in the first 200 labeled claims.

## Evidence references

- Artifact root: `<local-path>/projects/manually-audited-semantic-multi-trace-verification-for-rea-04d2330f8a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
