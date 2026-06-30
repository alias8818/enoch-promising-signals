# Text-only noisy transcript extraction for layered memory versus tuned vector retrieval

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `text-only-noisy-transcript-extraction-for-layered-memory-v-703ad2f920`
Run ID: `text-only-noisy-transcript-extraction-for-layered-memory-v-703ad2f920-20260628T152914471019+0000`

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

- Parent run decision: Layered agent memory vs retrieval-only on repeated tasks: enoch://control-plane/projects/layered-agent-memory-vs-retrieval-only-on-repeated-tasks-690ac53a3116/runs/layered-agent-memory-vs-retrieval-only-on-repeated-tasks-690ac53a3116-20260628T144412116905+0000
- Parent run decision: Noisy transcript replay for layered memory versus tuned vector retrieval: enoch://control-plane/projects/noisy-transcript-replay-for-layered-memory-versus-tuned-ve-29034cedee/runs/noisy-transcript-replay-for-layered-memory-versus-tuned-ve-29034cedee-20260628T150254299052+0000

## What looked useful

Layered memory produced a 13.0 absolute accuracy point gain over tuned TF-IDF retrieval on noisy repeated-transcript durable fact recovery, while a clean-transcript oracle reached 0.650 accuracy, indicating extraction robustness is the main remaining bottleneck.

## Boundaries and scale limits

Synthetic generated transcripts only; hand-template fact extraction; TF-IDF retrieval rather than modern neural embeddings; no real ASR corpus, no human labels, no LLM extraction, no production memory stack.

## Claim scope

On a deterministic synthetic noisy-transcript benchmark with 96 users, 6 sessions, 2304 chunks, and 569 durable-memory queries, a text-only layered extraction memory achieved 0.494 accuracy versus 0.364 for an optimistic label-aware TF-IDF top-k retrieval sweep.

## Why it stopped

No-paper closure: bounded synthetic evidence supports the mechanism but is not broad, realistic, or baseline-complete enough for a publication-grade claim.

## Recommended next action

Run a bounded real-transcript follow-up with human-labeled durable facts and a modern embedding retrieval baseline before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real noisy transcript durable-memory extraction versus neural retrieval
- Success threshold: Layered memory beats the best tuned neural retrieval baseline by at least 5 absolute accuracy points with non-overlapping 95% bootstrap confidence intervals, while abstain rate remains below 15%.
- Stop condition: Stop if layered memory is within 2 absolute points of the neural retrieval baseline or if failures are dominated by template-specific extraction assumptions that do not transfer to real transcripts.

## Evidence references

- Artifact root: `<local-path>/projects/text-only-noisy-transcript-extraction-for-layered-memory-v-703ad2f920`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
