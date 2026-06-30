# Semantic Operator Doctrine vs Flat Vector Retrieval

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `semantic-operator-doctrine-vs-flat-vector-retrieval-8c51e776c7d1`
Run ID: `semantic-operator-doctrine-vs-flat-vector-retrieval-8c51e776c7d1-20260621T054202341389+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/7933f37160e7

## What looked useful

Clean labels: flat_vector top1=0.0139, recall@5=0.0806, MRR=0.0710; doctrine-aware variants top1=1.0000, recall@5=1.0000, MRR=1.0000. With 20% doctrine and 20% action label corruption, doctrine-aware top1 remained about 0.68 and recall@5 about 0.77-0.78.

## Boundaries and scale limits

Synthetic-only corpus; TF-IDF baseline rather than modern neural embeddings; generated doctrine/action labels rather than extracted labels; no private operator traces, human relevance judgments, serving latency, or index-update evaluation.

## Claim scope

In a deterministic synthetic replay benchmark with 1,080 generated memories and 360 generated tasks, doctrine-aware retrieval using structured tenant/doctrine/action context substantially outperformed flat TF-IDF retrieval under lexical distractors.

## Why it stopped

Proxy-only useful signal; not publication-grade evidence for real semantic retrieval or real operator traces.

## Recommended next action

Run a bounded direct-evidence follow-up using a real or human-labeled repeated-agent trace corpus, modern embedding retrieval as the flat baseline, and a doctrine metadata extraction pipeline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Doctrine-aware retrieval on human-labeled repeated-agent traces
- Success threshold: Doctrine-aware retrieval improves recall@5 and MRR by at least 15% relative over the flat embedding baseline on clean metadata and remains at least 5% relative better when metadata labels have realistic extraction noise.
- Stop condition: Stop if doctrine-aware retrieval fails to beat the flat embedding baseline on recall@5 or MRR, or if metadata extraction noise eliminates the retrieval advantage.

## Evidence references

- Artifact root: `<local-path>/projects/semantic-operator-doctrine-vs-flat-vector-retrieval-8c51e776c7d1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
