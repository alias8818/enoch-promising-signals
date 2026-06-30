# Ledger-Constrained Local LLM on Natural Evidence QA

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ledger-constrained-local-llm-on-natural-evidence-qa-785ab88a54`
Run ID: `ledger-constrained-local-llm-on-natural-evidence-qa-785ab88a54-20260607T232455234248+0000`

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

- Parent run decision: Evidence-Ledger Constrained Local Agent: enoch://control-plane/projects/evidence-ledger-constrained-local-agent-17b458a59fe0/runs/evidence-ledger-constrained-local-agent-17b458a59fe0-20260607T192427792524+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/f3795769f29a

## What looked useful

Ledger prompting did not improve an easy answerable fixture because both baseline and ledger scored 24/24. On a harder abstention/distractor fixture, ledger scored 15/16 versus baseline 14/16, a +6.25 percentage point gain that fixed one no-support case but missed the predeclared +8 point threshold and increased mean latency from 1.19s to 1.70s per item.

## Boundaries and scale limits

Local hand-built fixtures only; public WikiQA dataset fetch hung; no broad Natural Questions/WikiQA benchmark validation; llama.cpp binary had no usable GPU support so inference was CPU-mapped through a persistent local server.

## Claim scope

Small controlled direct evidence-ID QA tests using a local Phi-4-mini instruct GGUF model through llama.cpp server: 24 answerable natural-language evidence items and 16 abstention/distractor items.

## Why it stopped

Tier 1 controlled direct evidence did not meet the stated success threshold: ledger gain was 0 points on the answerable fixture and +6.25 points on the challenge fixture, below the required +8 points.

## Recommended next action

Stop the paper path for this run; if continuing, run the same baseline-vs-ledger protocol on at least 100 public answerable and unanswerable evidence-QA items with a fair NONE option.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Public Benchmark Ledger Prompt Test for Evidence QA Abstention
- Success threshold: Ledger accuracy is at least 8 percentage points higher than the fair baseline, with no parse-failure increase above 2 percentage points and mean latency less than 2x baseline.
- Stop condition: Stop as negative if ledger improvement is under 8 percentage points, if gains are driven by parser artifacts, or if public dataset access cannot be made reproducible.

## Evidence references

- Artifact root: `<local-path>/projects/ledger-constrained-local-llm-on-natural-evidence-qa-785ab88a54`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
