# Live/local LLM citation-ledger validation on labeled QA cases

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `live-local-llm-citation-ledger-validation-on-labeled-qa-ca-b8356537f9`
Run ID: `live-local-llm-citation-ledger-validation-on-labeled-qa-ca-b8356537f9-20260630T092842013950+0000`

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

- Parent run decision: Evidence-Ledger Agent Reliability Harness on GB10: enoch://control-plane/projects/evidence-ledger-agent-reliability-harness-on-gb10-2663c06beb40/runs/evidence-ledger-agent-reliability-harness-on-gb10-2663c06beb40-20260630T084812042004+0000
- Parent run decision: Live-LLM evidence-ledger reliability harness: enoch://control-plane/projects/live-llm-evidence-ledger-reliability-harness-7de012d4d0/runs/live-llm-evidence-ledger-reliability-harness-7de012d4d0-20260630T090822181912+0000

## What looked useful

The stronger 1.5B local model reached 11/12 answer accuracy in both answer-only and ledger conditions, but only 2/12 ledger outputs jointly passed answer correctness, citation support coverage, citation precision, and quote grounding. Ledger validation is useful diagnostically, but current small-model outputs are not reliable enough for a paper claim.

## Boundaries and scale limits

Synthetic controlled cases only; two small models (0.5B and 1.5B); no public benchmark, retrieval pipeline, human adjudication, semantic entailment validation, or 7B+ model.

## Claim scope

On a 12-case controlled labeled QA corpus, two small local Qwen2.5 instruction models can emit parseable citation-ledger JSON, but deterministic ledger validation exposes provenance failures that answer accuracy alone misses.

## Why it stopped

Small controlled local validation produced a reproducible diagnostic signal but did not reach reliable citation-ledger validity; this is not full validation or publication-grade evidence.

## Recommended next action

Run a bounded deepen test on a public QA/provenance dataset with at least 100 labeled cases and one stronger local 7B-class model; stop this run as no-paper useful-signal evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Public-provenance QA citation-ledger validation with stronger local models
- Success threshold: At least 80% joint answer+citation+quote validity on the ledger condition, answer accuracy no worse than answer-only by more than 3 percentage points, and at least 95% parseable JSON.
- Stop condition: Stop as negative if joint validity remains below 50% after prompt/schema tuning or if answer accuracy drops more than 10 percentage points versus answer-only.

## Evidence references

- Artifact root: `<local-path>/projects/live-local-llm-citation-ledger-validation-on-labeled-qa-ca-b8356537f9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
