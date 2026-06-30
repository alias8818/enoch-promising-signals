# Tiny agent evidence ledger loop

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-agent-evidence-ledger-loop-d32568392f5e`
Run ID: `tiny-agent-evidence-ledger-loop-d32568392f5e-20260530T082540923162+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/241613175b74

## What looked useful

Across 240 main seed/condition comparisons, the filtered evidence ledger improved accuracy over the best raw-memory baseline by 0.2244 mean absolute accuracy points with 95% bootstrap CI [0.2141, 0.2340]. A harder stress run retained a 0.1340 mean accuracy gain over 180 comparisons, but naive contradiction downweighting underperformed an unfiltered ledger and sometimes hurt citation precision.

## Boundaries and scale limits

Synthetic Python simulation only; no LLM, no natural-language extraction, no public benchmark, no human citation grading, and all runs completed locally in under one minute each.

## Claim scope

In a synthetic tiny iterative agent loop where agents receive identical noisy observations, a persistent structured evidence ledger improves answer accuracy over limited context-only and fixed-size raw-memory baselines.

## Why it stopped

Synthetic mechanism evidence supports persistence but is proxy-only and not direct validation of real LLM agents.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded follow-up that embeds the ledger in an actual small LLM/tool agent on an evidence-grounded QA benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence ledger loop in a small LLM fact-checking agent
- Success threshold: Ledger agent improves answer accuracy by at least 5 absolute percentage points over the strongest matched baseline without reducing citation faithfulness by more than 2 points.
- Stop condition: Stop if ledger extraction/parsing overhead prevents matched evaluation, or if accuracy improvement is under 2 absolute points with overlapping confidence intervals after at least 200 evaluated tasks.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-agent-evidence-ledger-loop-d32568392f5e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
