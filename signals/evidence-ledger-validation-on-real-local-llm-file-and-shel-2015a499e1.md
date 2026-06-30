# Evidence-ledger validation on real local LLM file and shell tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-validation-on-real-local-llm-file-and-shel-2015a499e1`
Run ID: `evidence-ledger-validation-on-real-local-llm-file-and-shel-2015a499e1-20260604T000502449737+0000`

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

- Parent run decision: Evidence-ledger guardrails for small local tool-use agents: enoch://control-plane/projects/evidence-ledger-guardrails-for-small-local-tool-use-agents-4afbbc87d5dd/runs/evidence-ledger-guardrails-for-small-local-tool-use-agents-4afbbc87d5dd-20260603T191720320164+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/61f117a7314a

## What looked useful

The mechanism is useful for catching unsupported or corrupted local-task claims: answer mismatches, missing citations, and stdout hash tampering were rejected. The main failure mode is protocol/schema fragility: the local LLM emitted citation instead of citations in every parseable output, and one SHA-256 task confused the command stdout file hash with the ledger stdout hash.

## Boundaries and scale limits

Single model, single small fixture suite, prepared evidence packets rather than model-selected tool calls, no constrained decoding, no open-ended repository tasks, and no multi-run robustness statistics.

## Claim scope

On an 8-task controlled local file/shell fixture suite using cached Qwen/Qwen2.5-0.5B-Instruct, an evidence-ledger validator rejected all 24 corrupted controls and supported 7/8 correct answers when citation/citations key aliasing was allowed, but accepted 0/8 under the strict requested citations schema.

## Why it stopped

Tier 1 direct evidence produced a useful mechanism signal but also a strict-schema failure, so it is no-paper evidence rather than paper-positive validation.

## Recommended next action

Run a bounded deepen follow-up with constrained JSON schema/tool-call formatting and model-selected commands on 25-50 local file/shell tasks; stop if strict-schema supported rate remains below 80% or corrupted-control rejection falls below 95%.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Constrained-schema evidence ledger on model-selected local shell commands
- Success threshold: Strict-schema supported-answer rate >= 80% and corrupted-control rejection rate >= 95% with no unresolved parser exceptions.
- Stop condition: Stop as negative/no-paper if strict-schema supported-answer rate is < 80%, corrupted-control rejection is < 95%, or the model cannot reliably emit parseable ledger JSON after constrained prompting.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-validation-on-real-local-llm-file-and-shel-2015a499e1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
