# Evidence Ledger Schema Stress Test on CPU Agent Suite

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-schema-stress-test-on-cpu-agent-suite-4ba7ab32641f`
Run ID: `evidence-ledger-schema-stress-test-on-cpu-agent-suite-4ba7ab32641f-20260613T201202030674+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9bc227371e8f

## What looked useful

The hardened verifier matched expected outcomes on 62/62 generated stress cases, including fixed trap cases and 50 seeded mutations, with zero mismatches and an 8.029 second total runtime.

## Boundaries and scale limits

Synthetic ledgers only; largest generated valid case had 1000 claims and 2000 evidence entries; no real agent traces, external corpus, production database workload, or semantic truth validation.

## Claim scope

Dependency-free local schema and reference-integrity validation for synthetic evidence-ledger JSON cases on a CPU worker.

## Why it stopped

Useful bounded synthetic signal only; insufficient direct/full evidence for a paper-scale agent-suite schema claim.

## Recommended next action

Stop this no-paper run; run a bounded follow-up on real agent trace ledgers with human-labeled expected validity if direct evidence is needed.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Agent Trace Evidence-Ledger Validation
- Success threshold: At least 95% agreement with human-labeled validity on a minimum of 100 real or replayed trace ledgers, with all critical unsupported-reference cases rejected.
- Stop condition: Stop if agreement is below 90% or if critical unsupported-reference cases are accepted after one bounded schema/verifier revision.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-schema-stress-test-on-cpu-agent-suite-4ba7ab32641f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
