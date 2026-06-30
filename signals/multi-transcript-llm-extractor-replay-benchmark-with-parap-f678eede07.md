# Multi-transcript LLM extractor replay benchmark with paraphrased held-out queries

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `multi-transcript-llm-extractor-replay-benchmark-with-parap-f678eede07`
Run ID: `multi-transcript-llm-extractor-replay-benchmark-with-parap-f678eede07-20260614T104058793881+0000`

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

- Parent run decision: Extractor-backed compressed state memory on real repeated-agent transcripts: enoch://control-plane/projects/extractor-backed-compressed-state-memory-on-real-repeated-dbeb15ff30/runs/extractor-backed-compressed-state-memory-on-real-repeated-dbeb15ff30-20260614T044802065894+0000
- Parent run decision: Held-out real transcript replay benchmark for extractor-backed compressed state memory: enoch://control-plane/projects/held-out-real-transcript-replay-benchmark-for-extractor-ba-67b4457e9a/runs/held-out-real-transcript-replay-benchmark-for-extractor-ba-67b4457e9a-20260614T095312131064+0000

## What looked useful

The proposed layered extractor proxy reached 100.0% held-out paraphrase accuracy across 14400 paraphrased queries, versus 17.8% for transcript BM25, 17.5% for flat extracted-memory BM25, 8.5% for current-slot surface memory, and 19.1% for the no-entity-guard ablation. The paired seed deltas were positive on all 40 seeds.

## Boundaries and scale limits

40 fixed seeds, 60 entities, 6 sessions, 6 slots, generated transcripts and generated paraphrases only; LLM extraction and semantic slot routing were proxied by deterministic logic, so this is not evidence for a deployed LLM extractor or natural transcript robustness.

## Claim scope

In a deterministic synthetic multi-transcript replay benchmark, an oracle-like layered current-fact extractor with paraphrase-aware slot normalization answered held-out paraphrased queries far more accurately than no-memory, raw transcript BM25, flat extracted-memory BM25, and entity-agnostic ablations.

## Why it stopped

Closed as no-paper useful signal because the local evidence supports the mechanism but relies on deterministic synthetic extraction/paraphrase routing rather than direct LLM extractor validation.

## Recommended next action

Run a bounded deepen follow-up that replaces the oracle proxy with a real LLM extractor on naturalistic transcripts and human-written paraphrases; stop if it does not beat transcript and flat-memory baselines on both extraction F1 and held-out replay accuracy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real LLM extractor replay benchmark on naturalistic paraphrased queries
- Success threshold: At least 80% extraction F1 and at least a 20 percentage point held-out replay accuracy gain over both transcript BM25 and flat extracted-memory BM25 across fixed seeds or folds.
- Stop condition: Stop if extraction F1 is below 70%, if replay accuracy gain over either real baseline is below 10 percentage points, or if errors are dominated by unresolved entity grounding failures.

## Evidence references

- Artifact root: `<local-path>/projects/multi-transcript-llm-extractor-replay-benchmark-with-parap-f678eede07`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
