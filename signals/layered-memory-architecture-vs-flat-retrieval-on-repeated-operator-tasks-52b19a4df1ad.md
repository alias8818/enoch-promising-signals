# Layered Memory Architecture vs Flat Retrieval on Repeated Operator Tasks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layered-memory-architecture-vs-flat-retrieval-on-repeated-operator-tasks-52b19a4df1ad`
Run ID: `layered-memory-architecture-vs-flat-retrieval-on-repeated-operator-tasks-52b19a4df1ad-20260630T080052947848+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/745fc4966091

## What looked useful

Layered memory appears useful when repeated task labels are shared across operators but the correct action is operator-specific; flat retrieval can be diluted by same-slot records from other operators, especially at high distractor ratios and wider top-k.

## Boundaries and scale limits

Synthetic records only; lexical Jaccard retrieval only; no embeddings, no LLM-in-the-loop answering, no real operator traces, and no long-term online memory drift.

## Claim scope

In a deterministic synthetic repeated-operator benchmark, operator-routed compressed layered memory improved mean answer accuracy over flat lexical top-k retrieval while reducing retrieved context tokens by more than 90%.

## Why it stopped

Closed as a useful proxy signal rather than a full validation because all evidence is synthetic and does not include real operator traces, embeddings, or LLM-in-the-loop behavior.

## Recommended next action

Run a bounded direct follow-up with realistic operator traces, embedding retrieval, and a small LLM answerer under matched context budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Embedding and LLM replay of layered versus flat memory on repeated operator traces
- Success threshold: Layered memory achieves at least 3 percentage points higher answer accuracy or at least 50% lower context tokens at statistically indistinguishable accuracy across three random seeds.
- Stop condition: Stop if layered memory fails to match flat retrieval accuracy within 1 percentage point while using comparable or greater context, or if realistic traces do not exhibit repeated operator-specific preferences.

## Evidence references

- Artifact root: `<local-path>/projects/layered-memory-architecture-vs-flat-retrieval-on-repeated-operator-tasks-52b19a4df1ad`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
