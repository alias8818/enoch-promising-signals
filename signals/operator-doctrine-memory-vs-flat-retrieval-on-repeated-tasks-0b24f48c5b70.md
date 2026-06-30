# Operator-Doctrine Memory vs Flat Retrieval on Repeated Tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `operator-doctrine-memory-vs-flat-retrieval-on-repeated-tasks-0b24f48c5b70`
Run ID: `operator-doctrine-memory-vs-flat-retrieval-on-repeated-tasks-0b24f48c5b70-20260621T141957886789+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/14825ec65079

## What looked useful

Doctrine memory did not materially beat clean signal-only flat retrieval: average heldout F1 delta was +0.0037, far below the +0.05 probe threshold. It did consistently beat flat retrieval polluted by distractor features: average heldout F1 delta was +0.0276 with positive deltas in all seed/noise cells.

## Boundaries and scale limits

No natural-language tasks, LLM policy, embedding retrieval, human feedback, real incident traces, production memory maintenance, or tuned retrieval/reranking baselines. CPU-only local simulation completed in 18.10 seconds.

## Claim scope

Synthetic online benchmark of repeated operator checklist prediction from symbolic incident contexts. Doctrine memory was compared with flat nearest-neighbor episodic retrieval before each feedback update across 30 seeds, 4 noise levels, and 180000 predictions.

## Why it stopped

The bounded synthetic probe failed the pre-set +0.05 F1 threshold against the stronger clean flat retrieval baseline, so the broad claim is not supported; the positive distractor-robustness result is useful but not paper-ready.

## Recommended next action

Stop this run as no-paper useful signal; a bounded follow-up should test doctrine memory against embedding-based flat retrieval and tuned metadata-filtered retrieval on natural-language synthetic operator traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-language operator trace memory with tuned retrieval controls
- Success threshold: Doctrine memory improves heldout checklist F1 by at least 0.05 and reduces corrective feedback rate by at least 10% versus the best tuned retrieval baseline across at least 20 seeds or trace folds.
- Stop condition: Stop if doctrine memory fails to beat metadata-filtered/reranked retrieval by 0.02 F1 or if gains appear only against intentionally untuned distractor-polluted retrieval.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-vs-flat-retrieval-on-repeated-tasks-0b24f48c5b70`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
