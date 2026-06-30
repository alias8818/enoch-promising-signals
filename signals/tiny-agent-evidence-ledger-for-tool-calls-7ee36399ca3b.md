# Tiny Agent Evidence Ledger for Tool Calls

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-agent-evidence-ledger-for-tool-calls-7ee36399ca3b`
Run ID: `tiny-agent-evidence-ledger-for-tool-calls-7ee36399ca3b-20260604T065304736695+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ede08e12091f

## What looked useful

The evidence-ledger mechanism achieved 100% accuracy and 0% false accepts on 800 invalid synthetic claims, while accept-all and tool-called baselines accepted all invalid claims.

## Boundaries and scale limits

Only 1,000 synthetic structured scenarios were tested. No real LLM transcripts, natural-language extraction, multi-step reasoning chains, concurrency, adversarial tool output, or durable cryptographic append-only storage were evaluated.

## Claim scope

For structured synthetic tool-call traces with explicit subject/predicate/value claims, a tiny cited-evidence ledger rejected missing, unknown, contradictory, and wrong-subject evidence claims while accepting supported claims.

## Why it stopped

Closed as no-paper useful signal because the result is synthetic and structured; it supports the mechanism but is not direct full validation.

## Recommended next action

Run a bounded replay study on real or realistically generated agent transcripts with natural-language claim extraction before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay Evidence Ledger on Natural-Language Agent Traces
- Success threshold: At least 80% reduction in false accepts versus citation-only or tool-called baselines, with false rejects on supported claims below 10% on the labeled transcript set.
- Stop condition: Stop if claim extraction or evidence alignment cannot produce labels for at least 100 transcripts, or if false rejects exceed 20% after simple schema improvements.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-agent-evidence-ledger-for-tool-calls-7ee36399ca3b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
