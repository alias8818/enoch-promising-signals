# Evidence-ledger for small agent multi-hop QA

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-for-small-agent-multi-hop-qa-59fc5f6063a2`
Run ID: `evidence-ledger-for-small-agent-multi-hop-qa-59fc5f6063a2-20260601T022411276615+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4c0f43dccae5

## What looked useful

Across five 1,000-case confirmation seeds at 4 hops with a 60-word raw context, raw exact accuracy was 0.8936 and ledger exact accuracy was 0.8976, but raw verified exact was 0.0000 versus ledger verified exact 0.8944. The mechanism improves retained auditable support, not answer-only accuracy.

## Boundaries and scale limits

Synthetic data only; deterministic controlled extraction; no LLM generation, no real multi-hop QA dataset, no human provenance grading, and no end-to-end agent/tool loop. Results are local CPU proxy evidence, not publication-grade validation.

## Claim scope

In a controlled synthetic relation-chain multi-hop QA probe with distractors and tight raw-context budgets, a compact evidence ledger preserved complete supporting evidence and enabled verified exact answers far more often than a rolling raw-snippet context, while answer-only accuracy was nearly unchanged.

## Why it stopped

Closed as a no-paper useful signal because the run used synthetic controlled extraction and cannot validate real LLM agent behavior; it supports a mechanism worth direct evaluation, not a paper-positive claim.

## Recommended next action

Run a bounded direct follow-up with a small instruction-tuned model on a real multi-hop QA dataset, grading both exact answer and complete cited evidence under matched retrieval and token budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real small-model multi-hop QA evidence-ledger evaluation
- Success threshold: Ledger improves verified exact rate by at least 10 percentage points over rolling raw context while exact answer accuracy changes by no worse than -2 percentage points on the same examples.
- Stop condition: Stop if citation extraction/grading cannot be made reliable for the chosen dataset, or if the ledger fails to improve verified exact rate by at least 5 percentage points in an initial 100-example pilot.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-small-agent-multi-hop-qa-59fc5f6063a2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
