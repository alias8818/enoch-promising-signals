# Real noisy transcript durable-memory extraction versus neural retrieval

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `real-noisy-transcript-durable-memory-extraction-versus-neu-fae6b0d9fc`
Run ID: `real-noisy-transcript-durable-memory-extraction-versus-neu-fae6b0d9fc-20260628T155512159372+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Text-only noisy transcript extraction for layered memory versus tuned vector retrieval: enoch://control-plane/projects/text-only-noisy-transcript-extraction-for-layered-memory-v-703ad2f920/runs/text-only-noisy-transcript-extraction-for-layered-memory-v-703ad2f920-20260628T152914471019+0000
- Parent run decision: Noisy transcript replay for layered memory versus tuned vector retrieval: enoch://control-plane/projects/noisy-transcript-replay-for-layered-memory-versus-tuned-ve-29034cedee/runs/noisy-transcript-replay-for-layered-memory-versus-tuned-ve-29034cedee-20260628T150254299052+0000

## What looked useful

Durable extraction achieved 395/473 accuracy (0.8351) versus neural retrieval 255/473 (0.5391); bootstrap extraction-minus-retrieval delta p05/p50/p95 was 0.2583/0.2970/0.3270.

## Boundaries and scale limits

Synthetic transcripts, templated facts, compact all-MiniLM-L6-v2 retrieval baseline, no real ASR transcripts, no LLM extraction model, no production memory store, and no multi-seed or human-labeled corpus validation.

## Claim scope

On a reproducible synthetic noisy repeated-transcript benchmark with 120 cases and 473 latest-fact queries, rule-based durable memory extraction outperformed sentence-transformer top-3 retrieval for current user fact recovery.

## Why it stopped

Direct local synthetic evidence supports the scoped mechanism but is not publication-grade because the data and extractor are templated proxies rather than real noisy transcripts and learned extraction systems.

## Recommended next action

Stop this run as no-paper useful signal; next, run the same harness on a small real or ASR-noisy transcript corpus with an LLM extraction baseline and multiple retrieval top-k settings.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real ASR transcript memory extraction versus neural retrieval
- Success threshold: Durable extraction beats the best retrieval-only configuration by at least 10 absolute accuracy points with bootstrap p05 delta above 0 on human-labeled latest-fact queries.
- Stop condition: Stop if durable extraction does not beat the best retrieval-only setting by 5 absolute points or if human labels show the synthetic task assumptions do not transfer.

## Evidence references

- Artifact root: `<local-path>/projects/real-noisy-transcript-durable-memory-extraction-versus-neu-fae6b0d9fc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
