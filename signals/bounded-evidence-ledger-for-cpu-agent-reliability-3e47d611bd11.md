# Bounded Evidence Ledger for CPU Agent Reliability

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `bounded-evidence-ledger-for-cpu-agent-reliability-3e47d611bd11`
Run ID: `bounded-evidence-ledger-for-cpu-agent-reliability-3e47d611bd11-20260613T163959110169+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/5b5177f0394d

## What looked useful

The verifier accepted all 8 supported claims and rejected all 4 planted unsupported-claim traps with 0 false accepts and 0 false rejects in a bounded local CPU run.

## Boundaries and scale limits

Synthetic local corpus only: 12 labeled claims, 8 supported claims, 4 planted traps, exact string assertions only, no real LLM-agent transcript replay, no semantic entailment checking, no human adjudication.

## Claim scope

A deterministic local verifier can catch missing references, absent assertion text, unreferenced assertions, and source-hash mismatches in an exact-assertion evidence ledger for CPU-agent reliability summaries.

## Why it stopped

No-paper proxy result: the exact-ledger mechanism worked on a synthetic bounded corpus, but broad CPU-agent reliability claims require direct transcript evidence.

## Recommended next action

Run a bounded direct follow-up on 30 to 50 real agent transcript summaries comparing ledger-gated versus ungated unsupported-claim false accept rates.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Transcript Ledger-Gating False-Accept Test
- Success threshold: Ledger-gated summaries reduce unsupported-claim false accept rate by at least 50 percent relative to ungated summaries while keeping supported-claim false reject rate at or below 10 percent.
- Stop condition: Stop if ledger gating fails to reduce unsupported-claim false accepts by at least 25 percent on the first 20 adjudicated summaries or if supported-claim false rejects exceed 20 percent.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-evidence-ledger-for-cpu-agent-reliability-3e47d611bd11`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
