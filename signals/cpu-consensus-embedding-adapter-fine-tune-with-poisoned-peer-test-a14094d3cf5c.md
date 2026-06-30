# CPU consensus embedding-adapter fine-tune with poisoned-peer test

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cpu-consensus-embedding-adapter-fine-tune-with-poisoned-peer-test-a14094d3cf5c`
Run ID: `cpu-consensus-embedding-adapter-fine-tune-with-poisoned-peer-test-a14094d3cf5c-20260621T075602913070+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f1a51ae95934

## What looked useful

The poisoned peer alone achieved 1.000 triggered attack success with 0.9926 clean Recall@1, showing the attack was learnable. Mean consensus reduced attack success to 0.0208, while median and trimmed-mean consensus reached 0.0000 attack success with about 0.998 clean Recall@1.

## Boundaries and scale limits

Evidence is synthetic only: 64-dimensional normalized embeddings, 12 classes, closed-form ridge adapters, 8 random seeds, one poisoned peer out of five, no real corpus, no neural encoder fine-tuning, and no adaptive attacker.

## Claim scope

In a small synthetic CPU retrieval setting with 5 linear embedding-adapter peers and 1 triggered poisoned peer, coordinate-median and 20% trimmed-mean consensus suppressed the poisoned adapter's backdoor while preserving clean Recall@1.

## Why it stopped

Closed as no-paper useful signal because the evidence is a small synthetic mechanism test, not direct real-embedding or publication-grade validation.

## Recommended next action

Run a bounded deepen test on a real small text retrieval corpus with a frozen sentence encoder plus trainable adapter, comparing median/trimmed consensus against mean under 1-of-5 and 2-of-5 poisoned peers.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-encoder poisoned-peer consensus adapter test
- Success threshold: Median or trimmed consensus reduces triggered attack success by at least 80% relative to mean consensus while losing no more than 2 absolute percentage points of clean retrieval quality.
- Stop condition: Stop if robust consensus fails to reduce attack success on the real-encoder setup, or if clean retrieval loss exceeds 2 absolute percentage points in both robust aggregators.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-consensus-embedding-adapter-fine-tune-with-poisoned-peer-test-a14094d3cf5c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
