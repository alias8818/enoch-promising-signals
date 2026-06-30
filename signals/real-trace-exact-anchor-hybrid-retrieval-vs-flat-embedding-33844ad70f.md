# Real-trace exact-anchor hybrid retrieval vs flat embedding retrieval

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-trace-exact-anchor-hybrid-retrieval-vs-flat-embedding-33844ad70f`
Run ID: `real-trace-exact-anchor-hybrid-retrieval-vs-flat-embedding-33844ad70f-20260620T180102224878+0000`

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

- Parent run decision: Exact-anchor suffix memory vs flat-vector retrieval: enoch://control-plane/projects/exact-anchor-suffix-memory-vs-flat-vector-retrieval-3bfa05a03872/runs/exact-anchor-suffix-memory-vs-flat-vector-retrieval-3bfa05a03872-20260620T170002623589+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/982c005a47ec

## What looked useful

Exact-anchor hybrid retrieval achieved 1.000 anchor recall@1 versus 0.000 for the flat anchor-blind embedding baseline, with 0.711 mean latency ratio, passing the predefined Tier 1 mechanism threshold but not the paper gate.

## Boundaries and scale limits

Small local corpus: 484 records, 20 replay tasks, 10 exact-anchor tasks, controlled distractors, deterministic anchor-blind hashed embedding surrogate rather than a production dense embedding model, no held-out private real trace corpus.

## Claim scope

In a deterministic Tier 1 controlled replay built from this project's real controller/scaffold trace text plus near-duplicate distractors, exact-anchor filtering before embedding ranking recovered all anchor-bearing target records that the local flat anchor-blind embedding baseline missed.

## Why it stopped

No-paper useful signal: the mechanism passed a bounded controlled direct test, but the evidence is not publication-grade because the dense baseline and distractor corpus are local surrogates.

## Recommended next action

Run a deepen follow-up on a deidentified held-out real trace corpus using a production dense embedding model and at least 200 natural anchor-bearing queries.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out real-trace exact-anchor hybrid retrieval with production dense embeddings
- Success threshold: Hybrid exact-anchor recall@1 >= flat dense recall@1 + 0.20, hybrid exact-anchor recall@1 >= 0.90, parser coverage >= 0.95 on anchor-bearing queries, and mean latency ratio <= 2.0.
- Stop condition: Stop if flat dense recall@1 is within 10 percentage points of hybrid, if anchor parser coverage is below 0.80 on real traces, or if hybrid mean latency exceeds 2.0x flat retrieval.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-exact-anchor-hybrid-retrieval-vs-flat-embedding-33844ad70f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
