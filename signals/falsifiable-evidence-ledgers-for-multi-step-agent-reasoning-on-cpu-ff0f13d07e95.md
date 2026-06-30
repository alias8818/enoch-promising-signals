# Falsifiable Evidence Ledgers for Multi-Step Agent Reasoning on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `falsifiable-evidence-ledgers-for-multi-step-agent-reasoning-on-cpu-ff0f13d07e95`
Run ID: `falsifiable-evidence-ledgers-for-multi-step-agent-reasoning-on-cpu-ff0f13d07e95-20260525T104450954178+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/74ba39470e6c

## What looked useful

Ledger verification achieved 0.64512 recall across all injected faults versus 0.166 for final-answer-only checking, with 0.0 clean false positives and 0.96863 localization accuracy among detected step-local faults. Recall was 1.0 for arithmetic corruption, unsupported evidence, and missing dependencies, but only 0.0578 for wrong fact binding and 0.1678 for dependency transcription.

## Boundaries and scale limits

Tested 5,000 clean synthetic tasks and 50,000 injected-fault trials with deterministic rule-based ledgers; no real LLM agents, natural-language evidence, adversarial coherent ledger rewriting, or full-scale agent workloads were tested.

## Claim scope

Synthetic CPU-only arithmetic DAG tasks show that minimal structured evidence ledgers detect explicit computational and structural faults better than final-answer-only checking, but they do not reliably detect semantically valid wrong fact or dependency substitutions.

## Why it stopped

Closed as no-paper useful signal because the local synthetic test supports the mechanism for explicit ledger-invariant faults but falsifies sufficiency of a minimal evidence/dependency ledger for semantic substitution faults.

## Recommended next action

Run a bounded deepen follow-up that adds semantic role-binding contracts to the ledger schema and tests whether wrong fact/dependency substitutions become detectable without raising clean false positives above 1%.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Role-Bound Evidence Contracts for Falsifiable Reasoning Ledgers
- Success threshold: Wrong fact binding and dependency transcription recall both exceed 0.9, aggregate ledger recall exceeds 0.9, and clean false positive rate remains below 0.01.
- Stop condition: Stop if role binding fails to lift wrong fact binding or dependency transcription recall above 0.5, or if clean false positives exceed 0.05 after schema tuning.

## Evidence references

- Artifact root: `<local-path>/projects/falsifiable-evidence-ledgers-for-multi-step-agent-reasoning-on-cpu-ff0f13d07e95`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
