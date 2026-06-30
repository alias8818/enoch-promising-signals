# Operator-Doctrine Memory vs Flat Retrieval on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `operator-doctrine-memory-vs-flat-retrieval-on-cpu-8a0a0cd61b76`
Run ID: `operator-doctrine-memory-vs-flat-retrieval-on-cpu-8a0a0cd61b76-20260620T163942579555+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/43a0ad0c6bd9

## What looked useful

Layered doctrine memory reached 300/300 correct current-doctrine answers; flat retrieval and transcript_search reached 0/300 under the primary synthetic stressor. This isolates a failure mode where obsolete but lexically strong traces outrank superseding doctrine.

## Boundaries and scale limits

Synthetic CPU-only rule-based retrieval; no real operator traces, no LLM generation, no embedding/hybrid retriever, no production memory pressure, and no large-scale validation.

## Claim scope

In a deterministic synthetic repeated-session operator-doctrine benchmark with obsolete rules and noisy metadata, a layered latest-doctrine memory answered current-policy queries correctly while flat lexical retrieval consistently selected obsolete or noisy evidence.

## Why it stopped

Proxy synthetic mechanism evidence only; not a full validation of real operator-doctrine memory systems.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded deepen follow-up using human-authored replay traces plus embedding/hybrid flat baselines before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Human-authored operator-doctrine replay benchmark with embedding flat baselines
- Success threshold: Layered doctrine memory improves current-policy exact-match accuracy by at least 10 percentage points over the best flat or hybrid baseline with no more than 10 percent latency overhead at the benchmark scale.
- Stop condition: Stop if the best flat or hybrid baseline matches layered memory within 5 accuracy points or if labeled human-authored replay data cannot be produced without private evidence.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-vs-flat-retrieval-on-cpu-8a0a0cd61b76`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
