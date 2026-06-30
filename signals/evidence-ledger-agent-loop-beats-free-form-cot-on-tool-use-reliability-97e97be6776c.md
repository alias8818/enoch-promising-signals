# Evidence-Ledger Agent Loop Beats Free-Form CoT on Tool-Use Reliability

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-loop-beats-free-form-cot-on-tool-use-reliability-97e97be6776c`
Run ID: `evidence-ledger-agent-loop-beats-free-form-cot-on-tool-use-reliability-97e97be6776c-20260629T160230499071+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/65a9515b260a

## What looked useful

Across five 10,000-task seeds, free-form success averaged 0.71988 while the evidence-ledger loop averaged 0.99926, for mean absolute lift 0.27938 with 4.6 mean regressions per 10,000 tasks.

## Boundaries and scale limits

50,000 synthetic tasks across 5 seeds; no real LLM, no natural-language prompt comparison, no real external tool APIs, and repairability is part of the synthetic generator.

## Claim scope

In a deterministic synthetic tool-use benchmark with verifier-visible failures, an evidence-ledger validate-and-retry loop improved final-answer correctness versus accepting a free-form first final answer.

## Why it stopped

Synthetic mechanism evidence is useful but insufficient for a paper-ready claim about real LLM tool-use reliability.

## Recommended next action

Run a bounded direct LLM tool-use benchmark using the same task interface and compare free-form CoT prompts against evidence-ledger loop prompts with blind final-answer scoring.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct LLM evidence-ledger versus free-form tool-use benchmark
- Success threshold: Ledger loop improves final-answer correctness by at least 5 percentage points and reduces unsupported final answers by at least 30% without increasing total tool calls by more than 2x.
- Stop condition: Stop if ledger validation fails to improve correctness on both models or if gains disappear when retry budget is controlled.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-loop-beats-free-form-cot-on-tool-use-reliability-97e97be6776c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
