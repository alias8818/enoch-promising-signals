# Live CPU-Agent Evidence-Ledger Audit

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `live-cpu-agent-evidence-ledger-audit-40f15bb515`
Run ID: `live-cpu-agent-evidence-ledger-audit-40f15bb515-20260523T065404375967+0000`

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

- Parent run decision: Evidence Ledger Reduces Tool Hallucinations in CPU Agents: enoch://control-plane/projects/evidence-ledger-reduces-tool-hallucinations-in-cpu-agents-dda4497ae0be/runs/evidence-ledger-reduces-tool-hallucinations-in-cpu-agents-dda4497ae0be-20260523T053904416450+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/1a2919369805

## What looked useful

The before-state live audit failed 21/26 checks because closure artifacts were absent, while the same audit passed 26/26 checks after run notes, metrics, decision JSON, and legacy mirror were present. This gives a reproducible local quality-control harness for Enoch evidence-ledger closure but not a publishable research result.

## Boundaries and scale limits

Tested on one live CPU-agent project workspace only; not validated against a corpus of historical projects, concurrent controller writes, hostile malformed artifacts, or controller callback ingestion.

## Claim scope

A deterministic local audit can distinguish an incomplete evidence ledger from a closed evidence ledger for this live Enoch CPU-agent project by checking required artifacts, schema enums, follow-up depth, paper-gate consistency, command/result references, and .omx mirroring.

## Why it stopped

Tier 1 direct local evidence supports the audit mechanism for one live workspace, but it is a small engineering validation rather than publication-grade evidence.

## Recommended next action

Stop this branch as no-paper useful signal; the concrete next bounded test is to run the audit on at least 20 historical Enoch projects plus five intentionally corrupted fixtures and report false-positive and false-negative rates.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Corpus-Level Enoch Evidence-Ledger Audit Validation
- Success threshold: At least 95% agreement with human-reviewed labels and 0/5 corrupted fixtures incorrectly passing.
- Stop condition: Stop if any missing-decision or invalid-enum fixture passes, or if agreement on historical labeled projects is below 90%.

## Evidence references

- Artifact root: `<local-path>/projects/live-cpu-agent-evidence-ledger-audit-40f15bb515`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
