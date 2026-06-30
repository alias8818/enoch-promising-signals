# Evidence Ledger Constrained Agent

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-constrained-agent-8fd94bb76acc`
Run ID: `evidence-ledger-constrained-agent-8fd94bb76acc-20260608T142935155064+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/e6366c2e2979

## What looked useful

Across 10 synthetic runs, the ledger-constrained agent had mean unsupported rate 0.000 while the unconstrained agent had mean unsupported rate 0.365; the main seed showed 0.000 versus 0.341 unsupported rate. The mechanism appears useful for abstention and injection/fallback suppression, but the setup is too synthetic for a paper claim.

## Boundaries and scale limits

Proxy-only evidence: no real LLM generation, no real retrieval corpus, no natural-language evidence extraction, no long-horizon tool planning, and no human support judgments. The main direct run used 1,200 paired synthetic cases; robustness used 10 seeds x 1,200 paired cases.

## Claim scope

In a deterministic synthetic document-QA benchmark with structured evidence records, exact entity/attribute support checks, answerable questions, unanswerable questions, distractors, and injection-like tool noise, requiring a verified evidence ledger eliminated unsupported answers relative to an unconstrained fallback-answering agent.

## Why it stopped

Closed as no-paper useful signal because the current result is a deterministic synthetic proxy rather than direct LLM-agent validation.

## Recommended next action

Run a bounded deepen follow-up with a small real instruction model on a real or semi-real citation QA dataset, preserving ledger traces and judging cited evidence support.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model evidence-ledger QA with support judgments
- Success threshold: At least 25 percentage-point unsupported-rate reduction with no more than 20 percentage-point answerable accuracy loss on a minimum 300-question real or semi-real QA set.
- Stop condition: Stop if unsupported-rate reduction is under 10 percentage points or if answerable accuracy drops by more than 30 percentage points after prompt and parser fixes.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-constrained-agent-8fd94bb76acc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
