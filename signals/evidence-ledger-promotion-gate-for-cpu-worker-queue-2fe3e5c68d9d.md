# Evidence-ledger promotion gate for CPU worker queue

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-promotion-gate-for-cpu-worker-queue-2fe3e5c68d9d`
Run ID: `evidence-ledger-promotion-gate-for-cpu-worker-queue-2fe3e5c68d9d-20260620T225502839550+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/08f267be815c

## What looked useful

The verifier accepted the one explicitly supported useful-signal fixture and rejected seven malformed or overpromoted fixtures with 0 false accepts and 0 false rejects in this bounded suite.

## Boundaries and scale limits

Tested only 8 synthetic JSON ledger fixtures and one final project ledger; did not test production CPU worker queue integration, real LLM traces, human-labeled corpora, or natural-language semantic entailment.

## Claim scope

Bounded local synthetic-fixture validation of a deterministic evidence-ledger promotion gate for representative schema, reference, contradiction, duplicate-ID, and overpromotion failures.

## Why it stopped

The result is useful but synthetic/local only, so it is not a full validation of CPU worker queue promotion behavior.

## Recommended next action

Stop this run as no-paper useful signal; next concrete action is a bounded replay study on real worker ledgers with human-reviewed accept/reject labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay evidence-ledger promotion gate on real worker traces
- Success threshold: At least 30 real ledgers replayed with zero paper-positive overpromotions and less than 10% false rejection of human-labeled useful-signal ledgers.
- Stop condition: Stop if the gate accepts any human-labeled unsupported paper-positive claim or if missing structured fields make more than 25% of real ledgers unevaluable without schema migration.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-promotion-gate-for-cpu-worker-queue-2fe3e5c68d9d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
