# Tiny Agent Evidence-Ledger Contradiction Halting

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiny-agent-evidence-ledger-contradiction-halting-4e0be483bd53`
Run ID: `tiny-agent-evidence-ledger-contradiction-halting-4e0be483bd53-20260531T194811612004+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8d9c62e110b1

## What looked useful

Immediate contradiction halting on a ledger is brittle under retractions, producing 300 false positives on 300 retracted-conflict episodes. Adding a one-event deferred halt preserved recall and removed false positives in the scoped benchmark, with a work-savings tradeoff: 9.9% steps saved versus 23.1% for immediate typed halt and 34.7% for naive flip halt.

## Boundaries and scale limits

No natural-language extraction, LLM planning, real tool outputs, delayed retractions beyond one event, or production agent traces were tested. Runtime was CPU-only and synthetic; this does not validate broad agent reliability or paper-grade performance.

## Claim scope

In a deterministic synthetic tiny-agent evidence stream with structured claim/value/strength/retraction events, a typed ledger with a one-event deferred contradiction halt detected all planted persistent hard contradictions and avoided false halts on weak or immediately retracted conflicts across 1,200 generated episodes.

## Why it stopped

No-paper useful signal: this run supports the mechanism only on structured synthetic streams, not on real LLM-agent traces.

## Recommended next action

Run a bounded LLM/tool-agent follow-up that extracts structured claims from natural-language tool outputs and tests the deferred ledger against delayed retractions and semantic contradictions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-language tool trace test for deferred evidence-ledger halting
- Success threshold: On at least 100 labeled natural-language traces, deferred ledger halting achieves contradiction recall >= 0.90, false-halt rate <= 0.05, and no statistically obvious answer-correctness regression versus no-halt.
- Stop condition: Stop if claim extraction noise drives deferred ledger false-halt rate above 0.15 or contradiction recall below 0.75 on a 30-trace pilot.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-agent-evidence-ledger-contradiction-halting-4e0be483bd53`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
