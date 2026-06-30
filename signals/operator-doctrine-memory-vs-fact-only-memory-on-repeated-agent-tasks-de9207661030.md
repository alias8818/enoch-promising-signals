# Operator-doctrine memory vs fact-only memory on repeated agent tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `operator-doctrine-memory-vs-fact-only-memory-on-repeated-agent-tasks-de9207661030`
Run ID: `operator-doctrine-memory-vs-fact-only-memory-on-repeated-agent-tasks-de9207661030-20260612T000138087322+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fd00523d3f50

## What looked useful

Doctrine memory improved transfer F1 by +0.0659 over fact-only memory (95% CI +0.0580 to +0.0739) and exact match by +0.1656 (95% CI +0.1455 to +0.1857), with wins in 95/100 seeds. Combined doctrine-plus-fallback improved transfer F1 by +0.0693 over fact-only.

## Boundaries and scale limits

CPU-only deterministic proxy; 100 seeds, 64 training episodes and 128 test episodes per seed. No live LLM, natural-language memory, human feedback, real repository tasks, or deployment-scale evaluation was performed.

## Claim scope

In a synthetic repeated-agent-task benchmark with stable hidden operator doctrine and changing task facts, a compact operator-doctrine memory outperformed nearest-neighbor fact-only episodic memory on held-out action prediction, especially on transfer-stressed cases.

## Why it stopped

This run produced a moderate synthetic useful signal, but it is not paper-ready because it did not test real LLM agents or natural-language memory formation.

## Recommended next action

Run a bounded live-agent follow-up using natural-language repeated file-system tasks and matched model/token/retrieval budgets for no-memory, fact-only memory, and operator-doctrine memory conditions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live-agent operator-doctrine memory benchmark on repeated file-system tasks
- Success threshold: Operator-doctrine memory improves paired task success by at least 10 percentage points or reduces policy violations by at least 30% versus fact-only memory, with confidence intervals excluding zero.
- Stop condition: Stop if doctrine memory fails to beat fact-only on both task success and policy-violation rate, or if gains disappear after controlling for memory token budget.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-vs-fact-only-memory-on-repeated-agent-tasks-de9207661030`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
