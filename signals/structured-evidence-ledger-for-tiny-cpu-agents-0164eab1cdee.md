# Structured Evidence Ledger for Tiny CPU Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `structured-evidence-ledger-for-tiny-cpu-agents-0164eab1cdee`
Run ID: `structured-evidence-ledger-for-tiny-cpu-agents-0164eab1cdee-20260523T230648696549+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/12311a2acc01

## What looked useful

Structured ledger accuracy exceeded rolling notes by +0.028 to +0.322 absolute across 512-8192 byte budgets, with matching provenance gains, at 20x-63x naive ingestion overhead but only 20 MB max RSS and 27.69 s total wall-clock.

## Boundaries and scale limits

Synthetic regex-extracted archive snippets only; 50 paired seeds; no real LLM extraction, real tool traces, adversarial language, or production agent loop was tested.

## Claim scope

In a deterministic synthetic sequential-evidence benchmark, a structured fact/source ledger under 512-8192 byte memory budgets improves final answer and provenance accuracy over unstructured rolling notes for tiny CPU-bound agents.

## Why it stopped

Closed as no-paper useful signal because the mechanism is supported only by synthetic/proxy evidence, not by real agent or LLM traces.

## Recommended next action

Run a bounded deepen study with a real tiny CPU LLM or noisy extractor on natural task traces, scoring extraction errors end-to-end against rolling notes and compact-summary baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Structured Evidence Ledger with Noisy Tiny-LLM Extraction
- Success threshold: Structured ledger improves provenance-correct answer accuracy by at least 10 absolute percentage points over both baselines at one or more sub-8KB memory budgets without more than 3x optimized ingestion overhead.
- Stop condition: Stop if ledger gains are below 5 absolute percentage points over the best baseline or if extraction errors erase provenance gains in two independent task sets.

## Evidence references

- Artifact root: `<local-path>/projects/structured-evidence-ledger-for-tiny-cpu-agents-0164eab1cdee`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
