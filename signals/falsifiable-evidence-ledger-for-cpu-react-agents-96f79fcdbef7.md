# Falsifiable Evidence Ledger for CPU ReAct Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `falsifiable-evidence-ledger-for-cpu-react-agents-96f79fcdbef7`
Run ID: `falsifiable-evidence-ledger-for-cpu-react-agents-96f79fcdbef7-20260528T231903427362+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/57b4ce2850fe

## What looked useful

The ledger mechanism creates falsifiable handles for claim support, citation existence, payload integrity, and observation freshness that a plain transcript audit missed in four of six injected failure classes; CPU overhead was about 11.1 microseconds per validation and serialized traces were about 2.6x larger.

## Boundaries and scale limits

Synthetic generator rather than live LLM agent; built-in task oracles; simple plain-transcript baseline; no real tool APIs, adversarial natural-language paraphrases, human audit study, or production ReAct integration.

## Claim scope

In a deterministic synthetic CPU ReAct trace harness with arithmetic and lookup tasks, a structured evidence ledger with cited evidence IDs and SHA-256 observation payload checks detected injected wrong-final, missing-citation, nonexistent-citation, tampered-observation, stale-observation, and missing-observation failures at 100% rate with 0% false positives across 21,000 traces.

## Why it stopped

Closed as no-paper useful signal because the current evidence is synthetic trace mutation evidence, not direct live-agent validation.

## Recommended next action

Run a bounded live-agent deepen test with a local CPU ReAct loop, real tool observations, naturally occurring failures, and a stronger schema-only baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live CPU ReAct Evidence Ledger Against Schema-Only Tool Traces
- Success threshold: Ledger improves invalid-failure detection by at least 20 percentage points over schema-only traces with false positive rate under 5% and median validation latency under 5 milliseconds per task.
- Stop condition: Stop if ledger detection is within 5 percentage points of schema-only baseline, false positives exceed 10%, or median validation latency exceeds 25 milliseconds per task.

## Evidence references

- Artifact root: `<local-path>/projects/falsifiable-evidence-ledger-for-cpu-react-agents-96f79fcdbef7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
