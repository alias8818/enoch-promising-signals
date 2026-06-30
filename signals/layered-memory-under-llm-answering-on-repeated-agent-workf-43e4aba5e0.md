# Layered Memory Under LLM Answering on Repeated Agent Workflows

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layered-memory-under-llm-answering-on-repeated-agent-workf-43e4aba5e0`
Run ID: `layered-memory-under-llm-answering-on-repeated-agent-workf-43e4aba5e0-20260619T035602048131+0000`

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

- Parent run decision: Layered Memory vs Flat Retrieval on Repeated Agent Tasks: enoch://control-plane/projects/layered-memory-vs-flat-retrieval-on-repeated-agent-tasks-70931faa820d/runs/layered-memory-vs-flat-retrieval-on-repeated-agent-tasks-70931faa820d-20260619T031742160535+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/02d6a3a11c2b

## What looked useful

Pooled across seeds 7-11, layered_memory reached 390/720 accuracy = 0.5417 versus flat_recent 196/720 = 0.2722 and no_memory 0/720 = 0.0. The layered-minus-flat lift was +0.2694, clearing the predefined +0.25 mechanism threshold in aggregate, with paired counts of 235 layered-only correct versus 41 flat-only correct. The effect varied by seed: 3/5 seeds individually cleared +0.25.

## Boundaries and scale limits

Five random seeds, 24 workflows per seed, 6 keys per workflow, 8 episodes per workflow, 720 questions per condition total. Synthetic MEMORY FACT transcripts, oracle memory updates, one small local LLM, exact single-token-style value recovery only; no real agent traces, non-oracle extraction, larger models, human evaluation, or downstream task completion.

## Claim scope

In a controlled synthetic repeated-agent-workflow QA benchmark with oracle-maintained current fact summaries and google/flan-t5-small answering, layered memory consisting of stable facts plus a short recent transcript improved exact current-value answer accuracy over a flat recent-transcript memory under the same constrained context setting.

## Why it stopped

Tier 1 controlled direct evidence supports the mechanism but remains synthetic and oracle-memory; it is useful no-paper evidence rather than publication-grade validation.

## Recommended next action

Run a bounded deepen test with non-oracle memory extraction on semi-real or generated agent traces, preserving the same flat-recency control and requiring the layered advantage to survive extraction/update errors.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Non-oracle layered memory on semi-real repeated agent traces
- Success threshold: Layered memory beats flat recent memory by at least +0.15 exact QA accuracy in aggregate, clears flat in at least 4/5 seeds or trace batches, and retains extraction F1 >= 0.80 on current facts.
- Stop condition: Stop as negative/no-paper if layered memory lift is below +0.10 aggregate, if fewer than 3/5 batches beat flat recent memory, or if extraction F1 below 0.70 explains most of the loss.

## Evidence references

- Artifact root: `<local-path>/projects/layered-memory-under-llm-answering-on-repeated-agent-workf-43e4aba5e0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
