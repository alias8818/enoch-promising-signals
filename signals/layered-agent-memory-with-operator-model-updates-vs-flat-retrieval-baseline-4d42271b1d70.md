# Layered agent memory with operator-model updates vs flat retrieval baseline

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `layered-agent-memory-with-operator-model-updates-vs-flat-retrieval-baseline-4d42271b1d70`
Run ID: `layered-agent-memory-with-operator-model-updates-vs-flat-retrieval-baseline-4d42271b1d70-20260630T173353857188+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3a52a3160c0f

## What looked useful

Layered operator-model memory reached 1.000 accuracy with one state lookup. Flat retrieval reached 0.189 at k=3, 0.284 at k=10, 0.449 at k=30, and 0.614 at k=100 under paraphrased/conflicting updates; a no-paraphrase control reached 1.000 by k=30, indicating the failure is tied to paraphrased update retrieval rather than a broken baseline.

## Boundaries and scale limits

Synthetic traces only; no real operator logs, dense embedding retriever, LLM extraction, production agent loop, or long-horizon memory-maintenance cost was tested. Main CPU-only run used 30 seeds, 3000 events per seed, and 1200 queries per seed.

## Claim scope

In a deterministic synthetic operator-preference benchmark with conflicting updates and paraphrased wording, resolving updates into a layered operator model answered current-preference queries more accurately and with less query context than flat lexical retrieval over raw events.

## Why it stopped

No-paper closure: this is a synthetic/proxy mechanism result, not direct real-agent or publication-grade validation.

## Recommended next action

Run a bounded deepen follow-up replacing lexical retrieval with dense or hybrid retrieval plus LLM extraction on the same generator and a small hand-authored agent trace set.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Dense-retrieval and LLM-extraction check for layered operator memory
- Success threshold: Layered memory beats the strongest flat dense/hybrid baseline by at least 10 percentage points in current-preference accuracy at matched or lower context budget across synthetic and hand-authored traces.
- Stop condition: Stop if dense/hybrid flat retrieval closes the gap to under 5 percentage points or if layered update normalization fails on ambiguous/noisy updates.

## Evidence references

- Artifact root: `<local-path>/projects/layered-agent-memory-with-operator-model-updates-vs-flat-retrieval-baseline-4d42271b1d70`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
