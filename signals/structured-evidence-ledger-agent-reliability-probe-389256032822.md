# Structured Evidence-Ledger Agent Reliability Probe

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `structured-evidence-ledger-agent-reliability-probe-389256032822`
Run ID: `structured-evidence-ledger-agent-reliability-probe-389256032822-20260621T141450097517+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/14825ec65079

## What looked useful

At extraction recall 0.9, ledger_guarded reached 0.9473 audit support at 0.664 coverage, while retrieval_first_seen reached 0.6198 audit support at full coverage. The bootstrap per-case audit-support delta for ledger minus retrieval was +0.3192 with 95% CI [0.3091, 0.3300]. Ledger failures were concentrated in missed-canonical/extracted-stale cases, disappearing at recall 1.0 in the synthetic setup.

## Boundaries and scale limits

This was a CPU-only deterministic proxy over 2,000 synthetic cases plus a 1,000-case recall sweep. It did not test a real LLM, live retrieval, natural-language extraction, long-horizon agent behavior, or human citation judgments.

## Claim scope

In a synthetic field-fact QA probe with missing evidence, conflicting stale evidence, distractor documents, and imperfect extraction recall, a structured evidence-ledger finalization policy reduced unsupported emitted claims versus all-claims and first-seen retrieval baselines, at the cost of lower answer coverage.

## Why it stopped

Proxy-only useful signal: the mechanism improved synthetic evidence audit reliability, but broad agent reliability remains unvalidated.

## Recommended next action

Run a bounded direct LLM-agent follow-up on a small real-document QA set comparing normal cited answers against ledger-gated finalization under matched retrieval budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct LLM Evidence-Ledger QA Reliability Test
- Success threshold: Ledger-gated agent reduces unsupported claim rate by >=25% versus baseline with >=60% coverage and no statistically significant drop in correct supported claims among answered fields.
- Stop condition: Stop if ledger gating fails to reduce unsupported claims by 10% on the first 100 audited questions, or if coverage falls below 40% with no clear retrieval/extraction fix.

## Evidence references

- Artifact root: `<local-path>/projects/structured-evidence-ledger-agent-reliability-probe-389256032822`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
