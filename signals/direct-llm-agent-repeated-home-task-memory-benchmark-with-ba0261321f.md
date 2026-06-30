# Direct LLM-agent repeated home-task memory benchmark with noisy layered notes

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `direct-llm-agent-repeated-home-task-memory-benchmark-with-ba0261321f`
Run ID: `direct-llm-agent-repeated-home-task-memory-benchmark-with-ba0261321f-20260629T112703916283+0000`

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

- Parent run decision: LLM-agent repeated home-task memory evaluation with layered notes versus retrieval-only: enoch://control-plane/projects/llm-agent-repeated-home-task-memory-evaluation-with-layere-2d8b27ca30/runs/llm-agent-repeated-home-task-memory-evaluation-with-layere-2d8b27ca30-20260629T104650357775+0000
- Parent run decision: Operator-Doctrine Memory: Do Layered Notes Beat Retrieval-Only on Repeated Home Tasks?: enoch://control-plane/projects/operator-doctrine-memory-do-layered-notes-beat-retrieval-only-on-repeated-home-tasks-6e3e13f1de30/runs/operator-doctrine-memory-do-layered-notes-beat-retrieval-only-on-repeated-home-tasks-6e3e13f1de30-20260629T101603777803+0000

## What looked useful

Oldest-first layered notes caused severe recency failure in repeated-update cases: flan-t5-base achieved 0% on three-update cells and predicted the first stale update in 96.7% of those cases. Reordering notes newest-first raised flan-t5-base three-update accuracy to 70%, but high-noise repeated cases still reached only 30%.

## Boundaries and scale limits

Synthetic notes only; two small local FLAN-T5 models only; exact-answer metric only; no real user memory logs, no long-lived agent sessions, no frontier LLMs, and no tool-augmented memory retrieval.

## Claim scope

Bounded synthetic benchmark of direct LLM answering over repeated household-task notes with distractor household notes, using google/flan-t5-small and google/flan-t5-base on 60-case grids.

## Why it stopped

No-paper closure: bounded local evidence is useful but not publication-grade and only tests synthetic proxy notes on small local models.

## Recommended next action

Run a bounded deepen follow-up comparing newest-first chunking and structured recency-index retrieval against direct prompting on paraphrased synthetic notes plus a small human-authored household-note set.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Recency-index retrieval versus direct prompting for noisy household memory notes
- Success threshold: Structured recency-index retrieval or newest-first chunking achieves at least 80% exact/latest-answer accuracy and at least 30 percentage points improvement over oldest-first direct prompting on high-noise repeated-update cases.
- Stop condition: Stop if all mitigation variants remain below 60% exact/latest-answer accuracy on high-noise repeated-update cases or if direct prompting on a stronger model already exceeds 90%, making the small-model failure non-general for the intended target.

## Evidence references

- Artifact root: `<local-path>/projects/direct-llm-agent-repeated-home-task-memory-benchmark-with-ba0261321f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
