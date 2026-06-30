# Realistic Trace Noisy-Anchor Replay With Equal-Budget LLM Baseline

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `realistic-trace-noisy-anchor-replay-with-equal-budget-llm-c5cc88b5b7`
Run ID: `realistic-trace-noisy-anchor-replay-with-equal-budget-llm-c5cc88b5b7-20260613T214331996757+0000`

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

- Parent run decision: Anchor-Preserving Compressed Memory for Long-Context Agents: enoch://control-plane/projects/anchor-preserving-compressed-memory-for-long-context-agents-36f805127f4e/runs/anchor-preserving-compressed-memory-for-long-context-agents-36f805127f4e-20260613T204001598376+0000
- Parent run decision: Noisy Anchor Extraction Replay for Compressed Agent Memory: enoch://control-plane/projects/noisy-anchor-extraction-replay-for-compressed-agent-memory-53941c431f/runs/noisy-anchor-extraction-replay-for-compressed-agent-memory-53941c431f-20260613T211202106677+0000

## What looked useful

Layered noisy-anchor-aware replay reached 1.000 exact match and 0.000 distractor rate; removing noisy-anchor suppression dropped exact match to 0.704 and raised distractor rate to 0.294; equal-budget raw prompt exact match was 0.093.

## Boundaries and scale limits

Generated template traces only; deterministic shared answer extractor only; no real repeated-agent corpus; no live LLM answerer; CPU-only local run with 7,200 events and 1,200 queries.

## Claim scope

On a sanitized generated repeated-agent replay benchmark with 1,200 fixed-seed queries, scope/key/currentness layering plus noisy-anchor suppression improved exact fact recall under an equal 120-token replay budget versus raw-prompt, flat-retrieval, and no-anchor-filter controls.

## Why it stopped

Closed as no-paper useful signal because the run produced fixed-seed ablation evidence for the mechanism but did not satisfy the real equal-budget LLM baseline or real-trace requirements needed for publication-grade validation.

## Recommended next action

Run one bounded deepen evaluation on sanitized real repeated-agent traces with an actual equal-budget LLM answerer before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Trace Equal-Budget LLM Replay Validation
- Success threshold: Full layered replay beats equal-budget raw prompt by >=10 exact-match points and beats no-anchor-filter ablation by >=5 exact-match points with non-overlapping or bootstrap-supported 95% confidence intervals, while lowering distractor answer rate by >=5 points.
- Stop condition: Stop negative if the full method fails to beat either equal-budget raw prompt or no-anchor-filter ablation on exact match, or if distractor rate is not reduced by at least 5 points.

## Evidence references

- Artifact root: `<local-path>/projects/realistic-trace-noisy-anchor-replay-with-equal-budget-llm-c5cc88b5b7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
