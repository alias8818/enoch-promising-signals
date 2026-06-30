# Operator-Doctrine Memory vs Flat Retrieval on Repeated Agent Tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `operator-doctrine-memory-vs-flat-retrieval-on-repeated-agent-tasks-a85a3b4d9e55`
Run ID: `operator-doctrine-memory-vs-flat-retrieval-on-repeated-agent-tasks-a85a3b4d9e55-20260630T044100284911+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/258725c218cc

## What looked useful

Doctrine memory's observed advantage is compression/context efficiency rather than accuracy over a strong structured retrieval control. Naive text retrieval failed badly, but structured retrieval eliminated the accuracy gap.

## Boundaries and scale limits

Synthetic proxy only; no real LLM agent, production task traces, embedding retrieval, delayed feedback, or human-authored doctrine evaluation. CPU-only local run: 30 seeds, 360 episodes per seed.

## Claim scope

On a deterministic synthetic repeated-operations benchmark with immediate feedback and hand-written feature extraction, compact conflict-count doctrine memory matches structured flat retrieval accuracy while using less active context, and both strongly outperform naive lexical flat retrieval.

## Why it stopped

Synthetic proxy evidence is useful but insufficient for a positive paper claim, and the strongest structured retrieval baseline matches doctrine accuracy.

## Recommended next action

Stop this run as no-paper useful signal; next run should test real LLM-agent traces with embedding retrieval and fixed context budgets before making any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-agent trace harness for doctrine memory versus embedding retrieval under context budgets
- Success threshold: Doctrine must match or exceed embedding retrieval accuracy within 1 percentage point while reducing retrieved context tokens by at least 40%, or improve accuracy by at least 5 percentage points at equal token budget.
- Stop condition: Stop if doctrine loses more than 3 percentage points of accuracy versus embedding retrieval at equal budget or fails to reduce context tokens by at least 20%.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-vs-flat-retrieval-on-repeated-agent-tasks-a85a3b4d9e55`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
