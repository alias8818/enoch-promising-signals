# Real-encoder poisoned-peer consensus adapter test

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-encoder-poisoned-peer-consensus-adapter-test-f3bc6897ae`
Run ID: `real-encoder-poisoned-peer-consensus-adapter-test-f3bc6897ae-20260621T081233881059+0000`

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

- Parent run decision: CPU consensus embedding-adapter fine-tune with poisoned-peer test: enoch://control-plane/projects/cpu-consensus-embedding-adapter-fine-tune-with-poisoned-peer-test-a14094d3cf5c/runs/cpu-consensus-embedding-adapter-fine-tune-with-poisoned-peer-test-a14094d3cf5c-20260621T075602913070+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f1a51ae95934

## What looked useful

The mechanism is supported in the controlled minority-poison setting: consensus over independent peer memories rejects targeted poisoned memories while honest peers remain a strict majority, but fails sharply when poisoned peers reach 4/7 majority.

## Boundaries and scale limits

Synthetic task corpus, deterministic replicated poison templates, TF-IDF encoder rather than pretrained neural sentence embeddings, 40 seeds, 6 tasks, 7 peers, and no adaptive adversary or production agent loop.

## Claim scope

In a deterministic Tier 1 local replay-memory harness with seven peers, six tasks, exact poisoned-peer counts, and TF-IDF text encoding, consensus adapters recovered the correct answer with 100% accuracy when poisoned peers were a strict minority up to 3/7, while single-peer top-score retrieval fell to 50-66.7%.

## Why it stopped

No-paper useful signal: the Tier 1 direct harness supports the minority-poison consensus mechanism, but synthetic tasks and a TF-IDF encoder are not publication-grade evidence.

## Recommended next action

Run one bounded deepen follow-up using a pretrained sentence embedding encoder, a larger paraphrased replay corpus, and the same exact poisoned-peer-count protocol; stop if consensus does not beat single-peer retrieval at 2/7 and 3/7 poison.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained-encoder poisoned-peer consensus boundary test
- Success threshold: Consensus accuracy exceeds single-peer top-score retrieval by at least 20 percentage points at 2/7 and 3/7 poisoned peers, with less than 10% poison-selected rate in those minority-poison conditions.
- Stop condition: Stop as negative if consensus fails to beat single-peer retrieval at either 2/7 or 3/7 poisoned peers, or if poison-selected rate is at least 25% in a minority-poison condition.

## Evidence references

- Artifact root: `<local-path>/projects/real-encoder-poisoned-peer-consensus-adapter-test-f3bc6897ae`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
