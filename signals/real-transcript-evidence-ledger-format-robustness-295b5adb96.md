# Real Transcript Evidence-Ledger Format Robustness

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-transcript-evidence-ledger-format-robustness-295b5adb96`
Run ID: `real-transcript-evidence-ledger-format-robustness-295b5adb96-20260619T232855801719+0000`

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

- Parent run decision: Evidence Ledger Format Robustness on CPU Agent Tasks: enoch://control-plane/projects/evidence-ledger-format-robustness-on-cpu-agent-tasks-bffa24a48a89/runs/evidence-ledger-format-robustness-on-cpu-agent-tasks-bffa24a48a89-20260619T231252956198+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d95f05653d68

## What looked useful

The scaffold is viable as a concrete evidence-ledger robustness harness: controlled fixtures reached 1.000 valid accept rate, 1.000 invalid reject rate, and 1.000 overall pass rate, but evidence remains too narrow for paper readiness.

## Boundaries and scale limits

Tier 1 only: 10 deterministic fixtures over one short real transcript-format excerpt; no large transcript corpus, noisy ASR, adversarial LLM ledger generation, or deep semantic entailment validation.

## Claim scope

A no-dependency verifier accepted all valid controlled transcript-ledger fixture variants and rejected all invalid controlled fixture variants covering format, reference, quote-grounding, speaker, duplicate-id, and simple claim/evidence term-alignment failures.

## Why it stopped

Tier 1 controlled direct test met its local success threshold, but the evidence is small-fixture mechanism support rather than broad validation or publication-grade evidence.

## Recommended next action

Run a bounded deepen follow-up with at least 50 independently curated real transcript ledger cases across multiple transcript sources and formatting variants before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-source real transcript evidence-ledger robustness suite
- Success threshold: valid_accept_rate >= 0.95 and invalid_reject_rate >= 0.95 with no uncaught quote-drift or missing-reference cases
- Stop condition: Stop if valid_accept_rate or invalid_reject_rate falls below 0.90 after fixture defects are corrected, or if failures require semantic entailment beyond explicit transcript-grounding checks.

## Evidence references

- Artifact root: `<local-path>/projects/real-transcript-evidence-ledger-format-robustness-295b5adb96`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
