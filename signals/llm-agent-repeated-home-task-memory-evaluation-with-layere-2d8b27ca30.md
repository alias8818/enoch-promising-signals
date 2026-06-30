# LLM-agent repeated home-task memory evaluation with layered notes versus retrieval-only

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `llm-agent-repeated-home-task-memory-evaluation-with-layere-2d8b27ca30`
Run ID: `llm-agent-repeated-home-task-memory-evaluation-with-layere-2d8b27ca30-20260629T104650357775+0000`

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

- Parent run decision: Operator-Doctrine Memory: Do Layered Notes Beat Retrieval-Only on Repeated Home Tasks?: enoch://control-plane/projects/operator-doctrine-memory-do-layered-notes-beat-retrieval-only-on-repeated-home-tasks-6e3e13f1de30/runs/operator-doctrine-memory-do-layered-notes-beat-retrieval-only-on-repeated-home-tasks-6e3e13f1de30-20260629T101603777803+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1af9aa073b79

## What looked useful

Layered current-state memory achieved 1.0000 accuracy versus 0.8949 for retrieval-only top_k=20 and 0.9762 for retrieval-only top_k=50; retrieval-only errors were primarily stale answers from missing the latest fact.

## Boundaries and scale limits

Synthetic notes only; no real households, no LLM generation, no embedding retrieval, no noisy human notes, and no end-to-end memory-write evaluation. Main run covered 20 seeds, 64 homes, 20 visits per home, and 7,680 current-state queries.

## Claim scope

In a deterministic synthetic repeated-home benchmark with changing task facts, a layered current-state memory eliminated stale current-fact answers that remained in raw-note retrieval-only baselines up to top_k=50.

## Why it stopped

No-paper useful signal: the mechanism is supported in a synthetic proxy, but direct LLM-agent and real/noisy note evidence is required before a publication claim.

## Recommended next action

Run a bounded direct LLM-agent follow-up with realistic repeated home-task phrasing, embedding retrieval, imperfect note updates, and a success threshold on stale-answer reduction versus retrieval-only.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct LLM-agent repeated home-task memory benchmark with noisy layered notes
- Success threshold: Layered memory reduces stale-answer rate by at least 50% versus retrieval-only at matched context budget while losing no more than 2 percentage points of overall accuracy to note-update errors.
- Stop condition: Stop if layered note-update errors exceed retrieval-only stale errors, or if retrieval-only matches layered stale-answer rate within 2 percentage points at the same context budget.

## Evidence references

- Artifact root: `<local-path>/projects/llm-agent-repeated-home-task-memory-evaluation-with-layere-2d8b27ca30`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
