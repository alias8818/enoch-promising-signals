# Real-agent evidence ledger reliability on document-derived tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-agent-evidence-ledger-reliability-on-document-derived-b7e827943b`
Run ID: `real-agent-evidence-ledger-reliability-on-document-derived-b7e827943b-20260608T135023595816+0000`

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

- Parent run decision: Evidence Ledger Agent Reliability on CPU: enoch://control-plane/projects/evidence-ledger-agent-reliability-on-cpu-0a2382227de1/runs/evidence-ledger-agent-reliability-on-cpu-0a2382227de1-20260608T071443506500+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/f79dba4e738d

## What looked useful

A reproducible CPU-only Tier 1 harness shows that an evidence ledger gate can reject stale/draft document evidence and improve reliability on document-derived tasks without increasing abstentions.

## Boundaries and scale limits

Small generated Markdown corpus only; deterministic retrieval/extraction policy; no LLM-sampled natural traces, PDFs, web documents, human audit labels, noisy retrieval embeddings, long-horizon workflows, or production document systems.

## Claim scope

In a six-task controlled local document benchmark with stale/draft conflicting documents, a structured evidence ledger with source-status and value-entailment gating achieved 100% answer accuracy, 100% valid citation coverage, and 0% stale/decoy contamination versus 33% answer accuracy, 0% machine-checkable valid citation coverage, and 67% stale/decoy contamination for a plain first-retrieval document agent.

## Why it stopped

Tier 1 controlled direct test supports the mechanism but remains too small and deterministic for publication readiness.

## Recommended next action

Run a bounded deepen follow-up on natural LLM-agent document QA traces with independent citation-support labels before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural LLM-Agent Evidence Ledger Reliability on Document QA
- Success threshold: Ledger-gated traces improve verified answer correctness by >=20 percentage points and reduce unsupported/stale citations by >=30 percentage points versus plain traces, with abstention <=10% and task completion within 5 percentage points.
- Stop condition: Stop if the first 15 natural traces show <5 percentage points correctness improvement or if ledger gating causes >20% abstention/task failure.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-evidence-ledger-reliability-on-document-derived-b7e827943b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
