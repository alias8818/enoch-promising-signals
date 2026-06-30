# Agent memory architecture: layered operator-doctrine vs flat retrieval

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `agent-memory-architecture-layered-operator-doctrine-vs-flat-retrieval-3531b9e27832`
Run ID: `agent-memory-architecture-layered-operator-doctrine-vs-flat-retrieval-3531b9e27832-20260621T125842067808+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3f2726222032

## What looked useful

Layered doctrine memory achieved 1.0000 joint accuracy versus 0.3833 for flat retrieval. Flat retrieval failures were concentrated in stale or crowded-out doctrine selection while preferences remained easy to retrieve.

## Boundaries and scale limits

120 synthetic cases from one deterministic generator seed; symbolic metadata and deterministic extraction; no LLM-in-the-loop agent, embedding retriever, real operator doctrine corpus, or live repeated-task traces.

## Claim scope

In a deterministic synthetic replay benchmark with explicit doctrine updates, user preferences, and noisy conflicting memories, typed layered doctrine memory outperformed flat top-k retrieval on joint policy-plus-preference accuracy.

## Why it stopped

Closed as no-paper useful signal because the evidence is a synthetic mechanism probe rather than direct real-agent validation.

## Recommended next action

Run a bounded LLM-in-the-loop replay benchmark using the same strategy matrix, with a tuned flat retrieval baseline and held-out realistic doctrine-update traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: LLM-in-the-loop layered doctrine memory replay benchmark
- Success threshold: Layered doctrine memory improves joint task accuracy by at least 10 percentage points over tuned flat retrieval with no increase in severe doctrine-violation rate.
- Stop condition: Stop if the tuned flat retrieval baseline matches layered memory within 5 percentage points on joint accuracy or if most failures are prompt/model compliance errors unrelated to memory architecture.

## Evidence references

- Artifact root: `<local-path>/projects/agent-memory-architecture-layered-operator-doctrine-vs-flat-retrieval-3531b9e27832`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
