# Semantic Evidence Sufficiency for Small-Agent Evidence Ledgers

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `semantic-evidence-sufficiency-for-small-agent-evidence-led-0e48aea068`
Run ID: `semantic-evidence-sufficiency-for-small-agent-evidence-led-0e48aea068-20260525T165021486292+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real Small-Agent Trace Validation for Evidence Ledgers: enoch://control-plane/projects/real-small-agent-trace-validation-for-evidence-ledgers-9b5be1df94/runs/real-small-agent-trace-validation-for-evidence-ledgers-9b5be1df94-20260525T164011029534+0000
- Parent run decision: Evidence Ledger for Small Agent Tool-Use Verification: enoch://control-plane/projects/evidence-ledger-for-small-agent-tool-use-verification-eb219bc87c40/runs/evidence-ledger-for-small-agent-tool-use-verification-eb219bc87c40-20260525T143821026652+0000

## What looked useful

The semantic rule achieved 0.9982 sufficiency accuracy but stopped at mean k=9.9731, essentially the same as fixed_k_10/lexical. The no-cohesion ablation was slightly better with 1.0000 accuracy and mean k=9.9580. Lower fixed-k baselines saved entries only by incurring high early-stop rates.

## Boundaries and scale limits

Evaluation used 600 shuffled HotpotQA examples, three fixed seeds, CPU-only pure-stdlib features, and a max ledger depth of 10. It did not test LLM answer correctness, learned embedding/NLI sufficiency models, production web retrieval, or examples whose gold support was not retrieved within top 10 BM25-ranked sentences.

## Claim scope

On HotpotQA dev-distractor evidence ledgers where BM25 sentence order contains all gold support facts within the top 10 entries, the tested cheap semantic sufficiency features do not materially reduce stopping length at high support-completion accuracy compared with fixed-k and lexical baselines.

## Why it stopped

Tier 2 direct evidence with fixed seeds, ablation, and real baselines did not support semantic sufficiency as an earlier stopping mechanism; this is a bounded negative/useful-signal result, not a full validation of all possible semantic sufficiency models.

## Recommended next action

Stop this mechanism as no-paper evidence; only revisit with a learned NLI/embedding sufficiency model evaluated on both support completion and downstream answer accuracy against the same baselines.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/semantic-evidence-sufficiency-for-small-agent-evidence-led-0e48aea068`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
