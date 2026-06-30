# Layered memory replay with paraphrased household traces and retrieval baselines

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layered-memory-replay-with-paraphrased-household-traces-an-444bdfb33d`
Run ID: `layered-memory-replay-with-paraphrased-household-traces-an-444bdfb33d-20260630T010741918398+0000`

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

- Parent run decision: LLM-agent layered memory replay on natural-language household traces: enoch://control-plane/projects/llm-agent-layered-memory-replay-on-natural-language-househ-098e82f6a1/runs/llm-agent-layered-memory-replay-on-natural-language-househ-098e82f6a1-20260629T224509471008+0000
- Parent run decision: Layered Memory for Multi-Step Household Tasks: enoch://control-plane/projects/layered-memory-for-multi-step-household-tasks-b5f963b0da1a/runs/layered-memory-for-multi-step-household-tasks-b5f963b0da1a-20260629T221302309776+0000

## What looked useful

Layered memory reached 18/18 accuracy versus 11/18 for flat retrieval and 12/18 for transcript search, a +0.3889 and +0.3333 absolute accuracy gain respectively on the local synthetic benchmark.

## Boundaries and scale limits

Synthetic templated traces only; no real operator data, no embedding baseline, no LLM recall, no noisy extraction study, and no large held-out corpus. Results should not be interpreted as publication-grade validation for deployed household agents.

## Claim scope

On an 18-task synthetic household replay benchmark with manual paraphrases, deterministic layered memory with household-domain routing, synonym normalization, and latest-fact resolution outperformed no-memory, transcript-search, and flat lexical retrieval baselines.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic and locally scoped, not a full validation on real or large-scale traces.

## Recommended next action

Run a bounded deepen follow-up with a held-out noisy household trace corpus and a semantic embedding retrieval baseline before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Noisy held-out household replay with semantic retrieval baseline
- Success threshold: Layered memory improves absolute accuracy by at least 0.10 over the best retrieval baseline with no increase in cross-household leakage failures.
- Stop condition: Stop if layered memory fails to beat embedding retrieval by 0.05 absolute accuracy on the first 100 held-out tasks or shows any repeated cross-household leakage.

## Evidence references

- Artifact root: `<local-path>/projects/layered-memory-replay-with-paraphrased-household-traces-an-444bdfb33d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
