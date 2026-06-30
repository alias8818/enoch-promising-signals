# Noisy local-LLM ingestion for evidence ledger memory

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `noisy-local-llm-ingestion-for-evidence-ledger-memory-64d54c1030`
Run ID: `noisy-local-llm-ingestion-for-evidence-ledger-memory-64d54c1030-20260527T031043820163+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Multi-seed evidence ledger versus stronger retrieval baselines for small local LLM memory: enoch://control-plane/projects/multi-seed-evidence-ledger-versus-stronger-retrieval-basel-2219348c89/runs/multi-seed-evidence-ledger-versus-stronger-retrieval-basel-2219348c89-20260524T185753516729+0000
- Parent run decision: Evidence ledger versus retrieval memory in a small local LLM agent: enoch://control-plane/projects/evidence-ledger-versus-retrieval-memory-in-a-small-local-l-0fa10d7f29/runs/evidence-ledger-versus-retrieval-memory-in-a-small-local-l-0fa10d7f29-20260524T154159930796+0000

## What looked useful

Ledger abstention is useful as a false-memory/provenance safety control under noisy ingestion, while temporal decay is essential for mutable facts. The tested ledger is not a general recall win: confidence/latest remained stronger for all-key current-fact accuracy.

## Boundaries and scale limits

240000 generated documents across conditions; extraction errors were simulated rather than produced by a real local LLM; no human-labeled real corpus or downstream agent task was evaluated.

## Claim scope

In a controlled longitudinal fact-memory simulation with fixed seeds, evidence-ledger ingestion with contradiction-aware abstention reduced false current-fact answers and improved provenance precision under high extractor noise, but did not improve full-coverage current-fact accuracy over a confidence/latest baseline.

## Why it stopped

Bounded validation produced a mixed useful signal rather than publication-grade support: simulated noisy ingestion showed lower false-memory rate but worse full-coverage accuracy than a simple confidence/latest baseline.

## Recommended next action

Stop paper work for this run; run one bounded real-local-model follow-up on labeled documents before making any broader claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real local-model extraction test for evidence-ledger false-memory control
- Success threshold: Ledger reduces error_rate_all by at least 20% versus confidence/latest at matched or no worse than 10% relative accuracy_all loss, with provenance_precision at least 5 percentage points higher.
- Stop condition: Stop if real-model extraction noise is below 10% wrong current values, if JSON extraction reliability prevents valid parsing after two prompt formats, or if ledger loses more than 10% relative accuracy_all without at least 20% error reduction.

## Evidence references

- Artifact root: `<local-path>/projects/noisy-local-llm-ingestion-for-evidence-ledger-memory-64d54c1030`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
