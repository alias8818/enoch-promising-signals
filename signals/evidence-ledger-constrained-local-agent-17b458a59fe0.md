# Evidence-Ledger Constrained Local Agent

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-constrained-local-agent-17b458a59fe0`
Run ID: `evidence-ledger-constrained-local-agent-17b458a59fe0-20260607T192427792524+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/f3795769f29a

## What looked useful

The evidence-ledger mechanism reduced unsupported answer rate from 0.4000 to 0.0000 and improved accuracy from 0.6000 to 1.0000 on the main run; ten seeds reproduced the same aggregate rates.

## Boundaries and scale limits

Synthetic data only; no real local LLM generation, natural corpus, noisy parser, multi-hop evidence, or human-labeled benchmark was tested. The constrained agent used structured case fields as parsed query metadata.

## Claim scope

On a deterministic synthetic QA ledger with 512 evidence entries and 1,280 cases, an exact entity-attribute evidence-ledger constraint eliminated unsupported answers relative to an unconstrained nearest-evidence local baseline while preserving supported-answer accuracy.

## Why it stopped

No-paper closure: the result is a synthetic mechanism signal, not a full validation of an LLM local agent.

## Recommended next action

Run a bounded deepen follow-up with a real local instruct model, natural evidence snippets, and the same unsupported-claim metric before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Ledger-Constrained Local LLM on Natural Evidence QA
- Success threshold: Ledger-constrained local LLM has at least 50% lower unsupported answer rate than both baselines and at least 80% accuracy on answerable cases.
- Stop condition: Stop if the ledger-constrained condition cannot beat both baselines on unsupported answer rate or if abstention exceeds 50% on answerable cases.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-constrained-local-agent-17b458a59fe0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
