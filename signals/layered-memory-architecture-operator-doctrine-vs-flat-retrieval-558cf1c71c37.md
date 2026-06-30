# Layered Memory Architecture: Operator Doctrine vs Flat Retrieval

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layered-memory-architecture-operator-doctrine-vs-flat-retrieval-558cf1c71c37`
Run ID: `layered-memory-architecture-operator-doctrine-vs-flat-retrieval-558cf1c71c37-20260621T080131655997+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bd2d277891e5

## What looked useful

Across 20 sweep runs, layered doctrine memory reached 1.000 mean accuracy and 0.000 doctrine violation rate; flat retrieval reached 0.3776 mean accuracy and 0.6224 doctrine violation rate. The useful mechanism signal is that explicit doctrine layering avoids conflict-induced flat-retrieval failures under noisy repeated sessions.

## Boundaries and scale limits

Synthetic symbolic benchmark only: no LLM generation, no embedding retrieval, no production operator traces, no latency/cost evaluation, and no validation against real multi-session agents.

## Claim scope

In a deterministic synthetic repeated-session memory proxy, separating standing operator doctrine into a privileged memory layer prevented stale/noisy transcript memories from overriding doctrine, outperforming flat retrieval on answer accuracy and doctrine violation rate.

## Why it stopped

Proxy-only synthetic evidence supports the mechanism but is not direct/full validation of agent memory architecture.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should replay naturalistic agent traces with an LLM and embedding flat-retrieval baseline before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Naturalistic LLM Replay Test for Layered Doctrine Memory
- Success threshold: Layered memory has at least 30% lower doctrine violation rate than flat retrieval and no more than 5 percentage point accuracy loss on held-out replay tasks.
- Stop condition: Stop if layered memory fails to reduce doctrine violations by at least 10% over flat retrieval on the first 50 held-out naturalistic tasks.

## Evidence references

- Artifact root: `<local-path>/projects/layered-memory-architecture-operator-doctrine-vs-flat-retrieval-558cf1c71c37`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
