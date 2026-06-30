# Falsifiability-Scored Evidence Ledgers for Agent Hallucination Reduction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `falsifiability-scored-evidence-ledgers-for-agent-hallucination-reduction-cba95c722129`
Run ID: `falsifiability-scored-evidence-ledgers-for-agent-hallucination-reduction-cba95c722129-20260525T210422029638+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f235eb42fe48

## What looked useful

Falsifiability scoring is not sufficient evidence for a standalone hallucination-reduction contribution unless future experiments show incremental value over source reliability, corroboration, and calibrated abstention controls.

## Boundaries and scale limits

Synthetic tasks only; no frontier LLM agent, no real retrieved corpus, no learned claim parser, no human factuality judgments, and source reliability labels are generator-provided.

## Claim scope

In a deterministic synthetic retrieval/QA environment with labeled support, contradictions, source reliability, and vague evidence, a falsifiability-scored evidence ledger reduces unsupported answers compared with relevance-only retrieval and a no-falsifiability ledger, but is dominated by a simpler reliability-weighted control that achieves the same zero hallucination rate with much higher coverage.

## Why it stopped

Proxy synthetic evidence was mixed: the method reduced hallucination versus weak relevance-only retrieval, but failed to improve over a stronger reliability-weighted control and lost substantial coverage, so this is not paper-ready or broadly validated.

## Recommended next action

Stop this run as a no-paper useful control result; a future bounded deepen test should evaluate falsifiability scoring on real or semi-real LLM-generated evidence with matched-coverage reliability controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Matched-Coverage Falsifiability Ledgers on LLM-Generated Evidence
- Success threshold: At matched coverage within 2 percentage points of the best reliability/corroboration control, falsifiability scoring reduces unsupported-answer rate by at least 20% relative with bootstrap confidence interval excluding zero.
- Stop condition: Stop if reliability/corroboration controls match or beat falsifiability scoring on unsupported-answer rate at equal or better coverage across two model/sample seeds.

## Evidence references

- Artifact root: `<local-path>/projects/falsifiability-scored-evidence-ledgers-for-agent-hallucination-reduction-cba95c722129`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
