# Noisy held-out household replay with semantic retrieval baseline

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `noisy-held-out-household-replay-with-semantic-retrieval-ba-cd486b5695`
Run ID: `noisy-held-out-household-replay-with-semantic-retrieval-ba-cd486b5695-20260630T015714431265+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: LLM-agent layered memory replay on natural-language household traces: enoch://control-plane/projects/llm-agent-layered-memory-replay-on-natural-language-househ-098e82f6a1/runs/llm-agent-layered-memory-replay-on-natural-language-househ-098e82f6a1-20260629T224509471008+0000
- Parent run decision: Layered memory replay with paraphrased household traces and retrieval baselines: enoch://control-plane/projects/layered-memory-replay-with-paraphrased-household-traces-an-444bdfb33d/runs/layered-memory-replay-with-paraphrased-household-traces-an-444bdfb33d-20260630T010741918398+0000

## What looked useful

Flat semantic retrieval scored 0.423611 accuracy versus 0.430556 for lexical transcript search. Failure cases indicate wrong-household retrieval under typos and distractors. Structured household routing scored 1.0 accuracy but uses benchmark metadata, so it is a mechanism control rather than paper evidence.

## Boundaries and scale limits

Synthetic data only; no real household transcripts, embedding model, LLM generation, or non-oracle household identity extraction. CPU-only run completed in seconds and is not a full-scale validation.

## Claim scope

On a deterministic synthetic household replay benchmark with 12 households, 72 facts, and 432 held-out noisy queries, a flat synonym/character semantic retrieval proxy did not outperform lexical transcript search, while oracle household-routed structured memory solved the task.

## Why it stopped

No-paper useful signal: the flat semantic baseline was early-falsified by a bounded synthetic replay, and the positive layered result depends on oracle household routing.

## Recommended next action

Run a bounded deepen follow-up that adds non-oracle household/entity resolution plus a real embedding retriever and requires a clear lift over lexical transcript search on the same generated replay task.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Non-oracle household routing for noisy replay retrieval
- Success threshold: Entity-routed semantic retrieval accuracy at least 0.10 above lexical transcript search with no worse than 0.05 drop on typo_suffix queries relative to clean queries.
- Stop condition: Stop if entity-routed retrieval fails to beat lexical transcript search by 0.05 absolute accuracy or if most remaining errors are household identity confusions.

## Evidence references

- Artifact root: `<local-path>/projects/noisy-held-out-household-replay-with-semantic-retrieval-ba-cd486b5695`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
