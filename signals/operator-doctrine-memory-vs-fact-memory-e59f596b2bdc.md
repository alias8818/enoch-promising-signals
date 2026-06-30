# Operator-Doctrine Memory vs Fact Memory

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `operator-doctrine-memory-vs-fact-memory-e59f596b2bdc`
Run ID: `operator-doctrine-memory-vs-fact-memory-e59f596b2bdc-20260629T062232103438+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/58869bd8e939

## What looked useful

Neutral fact memory had little effect on mixed retrieval, but adversarial policy-like fact memory sharply degraded mixed doctrine recall@1 from 0.703 at 1 fact/topic to 0.000 at 100 facts/topic; typed doctrine retrieval remained 1.000 recall@1 throughout.

## Boundaries and scale limits

Synthetic corpus, lexical retrieval only, oracle query routing, no LLM agent, no dense embeddings, no real operator memory data, and no downstream action-compliance measurement.

## Claim scope

In a synthetic TF-IDF retrieval benchmark with 12 operator-doctrine topics, mixed doctrine+fact memory is vulnerable to lexically overlapping fact memories displacing the relevant doctrine for doctrine queries; an oracle-routed typed doctrine store prevents that specific retrieval failure.

## Why it stopped

Stopped at useful synthetic retrieval evidence; this is a proxy mechanism result, not full validation of LLM agent memory behavior.

## Recommended next action

Run a bounded dense-embedding and small-agent follow-up using realistic memory traces to test whether type-aware doctrine retrieval improves downstream policy compliance over mixed retrieval.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Dense and Agentic Doctrine-vs-Fact Memory Retrieval Probe
- Success threshold: Type-aware retrieval improves doctrine recall@1 by at least 20 percentage points on policy-conflict queries and improves downstream compliance without reducing fact-query accuracy by more than 5 percentage points.
- Stop condition: Stop if dense retrieval mixed-memory doctrine recall@1 remains within 5 percentage points of type-aware retrieval and downstream compliance does not improve.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-vs-fact-memory-e59f596b2bdc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
