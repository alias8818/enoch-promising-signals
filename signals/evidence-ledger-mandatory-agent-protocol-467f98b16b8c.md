# Evidence-Ledger Mandatory Agent Protocol

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-mandatory-agent-protocol-467f98b16b8c`
Run ID: `evidence-ledger-mandatory-agent-protocol-467f98b16b8c-20260611T150217624475+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fd9129181108

## What looked useful

Mandatory ledger enforcement prevented unsupported accepted claims in the bounded benchmark. Strict model-formatted citations were brittle, but protocol-side citation repair recovered many supported answers without accepting unsupported ones.

## Boundaries and scale limits

Synthetic single-hop QA only; one small instruction model; lexical support verifier; no long-horizon agents, tool traces, semantic entailment, natural corpora, adversarial paraphrase, or human factuality ratings.

## Claim scope

On a 480-task synthetic evidence-grounded QA benchmark using google/flan-t5-small, a mandatory evidence-ledger verifier with deterministic citation repair reduced accepted unsupported claims from a 0.6917 baseline mean to 0.0000, while accepting a mean 0.6083 of tasks.

## Why it stopped

Evidence is a bounded synthetic protocol test, not full validation of mandatory evidence ledgers for real agents.

## Recommended next action

Stop this run as no-paper useful signal; next bounded work should test the same protocol on a real multi-document QA or agent trace benchmark with semantic entailment verification.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger enforcement on real multi-document QA
- Success threshold: Accepted unsupported claim rate is reduced by at least 50% relative to baseline, repaired ledger accepted answer rate is at least 50%, and verifier false rejections are below 25% on answerable examples.
- Stop condition: Stop if the ledger protocol cannot reduce accepted unsupported claims by 25% or if accepted answer rate falls below 30% after verifier calibration.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-mandatory-agent-protocol-467f98b16b8c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
