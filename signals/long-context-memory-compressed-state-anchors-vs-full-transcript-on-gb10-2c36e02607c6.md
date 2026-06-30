# Long-Context Memory: Compressed State Anchors vs Full Transcript on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `long-context-memory-compressed-state-anchors-vs-full-transcript-on-gb10-2c36e02607c6`
Run ID: `long-context-memory-compressed-state-anchors-vs-full-transcript-on-gb10-2c36e02607c6-20260630T043049875518+0000`

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

Compressed state anchors are useful as working-memory state, but they are not a standalone substitute for full transcripts when arbitrary exact historical recall is required. A historical retrieval log or delta scheme is needed for temporal queries.

## Boundaries and scale limits

No LLM was run; token footprint is approximate compact serialization, not tokenizer-specific. Synthetic facts do not test natural language ambiguity, summarization error, model hallucination, or context-window effects.

## Claim scope

In a deterministic synthetic event-stream memory benchmark, compressed current state preserves current fact recall with very small footprint, while sparse full-state anchors trade exact temporal recall for footprint and dense anchors can exceed full-transcript footprint.

## Why it stopped

Proxy benchmark produced a clear useful signal but not direct LLM evidence or publication-grade validation.

## Recommended next action

Run a bounded model-in-the-loop follow-up that compares full transcript prompting against current-state-plus-retrieval prompting under tokenizer-measured context budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Model-in-loop compressed state plus retrieval vs full transcript memory benchmark
- Success threshold: At least 95% current QA accuracy, at least 90% temporal QA accuracy, and at least 50% prompt-token reduction versus full transcript on 5,000-turn synthetic conversations.
- Stop condition: Stop if state-plus-retrieval cannot exceed 80% temporal QA accuracy or if tokenizer-measured prompts are not at least 25% smaller than the full transcript baseline.

## Evidence references

- Artifact root: `<local-path>/projects/long-context-memory-compressed-state-anchors-vs-full-transcript-on-gb10-2c36e02607c6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
