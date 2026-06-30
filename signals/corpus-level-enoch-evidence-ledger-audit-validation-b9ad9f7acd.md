# Corpus-Level Enoch Evidence-Ledger Audit Validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `corpus-level-enoch-evidence-ledger-audit-validation-b9ad9f7acd`
Run ID: `corpus-level-enoch-evidence-ledger-audit-validation-b9ad9f7acd-20260523T065852826763+0000`

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

- Parent run decision: Live CPU-Agent Evidence-Ledger Audit: enoch://control-plane/projects/live-cpu-agent-evidence-ledger-audit-40f15bb515/runs/live-cpu-agent-evidence-ledger-audit-40f15bb515-20260523T065404375967+0000
- Parent run decision: Evidence Ledger Reduces Tool Hallucinations in CPU Agents: enoch://control-plane/projects/evidence-ledger-reduces-tool-hallucinations-in-cpu-agents-dda4497ae0be/runs/evidence-ledger-reduces-tool-hallucinations-in-cpu-agents-dda4497ae0be-20260523T053904416450+0000

## What looked useful

The full audit improved injected-fault recall from 0.3333 to 1.0000 at 0.0000 clean false-positive rate; ablations showed distinct coverage from hash checks, referenced-evidence checks, and run-note/decision consistency checks. Natural unmodified audit flagged 54 of 192 projects for triage.

## Boundaries and scale limits

Labels are fixed-seed injected mutations over real artifacts, not independently adjudicated natural defects. Clean false positives are measured on projects that pass the full audit, not the entire unfiltered corpus. Human and LLM audit behavior were not tested.

## Claim scope

On 192 local Enoch project artifacts with three fixed seeds and 2520 labeled injected ledger faults, a cross-linked corpus evidence-ledger audit detected all injected faults while a completeness/schema baseline detected only missing/invalid decision artifacts.

## Why it stopped

Tier 2 injected-fault evidence supports the mechanism but is not publication-grade because natural corpus flags and human/LLM audit impact were not independently validated.

## Recommended next action

Stop as no-paper useful signal; next bounded test should blindly adjudicate natural corpus flags and matched clean controls under transcript-only, schema-baseline, and ledger-assisted review.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Blinded Natural-Corpus Adjudication of Enoch Evidence-Ledger Audit Flags
- Success threshold: At least 25 percentage-point higher confirmed defect detection for ledger-assisted review over schema baseline, with clean-control false-positive rate no higher than 5%.
- Stop condition: Stop if fewer than 20 natural flags can be adjudicated, if clean-control false positives exceed 5%, or if ledger-assisted recall improves by less than 10 percentage points over schema baseline.

## Evidence references

- Artifact root: `<local-path>/projects/corpus-level-enoch-evidence-ledger-audit-validation-b9ad9f7acd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
