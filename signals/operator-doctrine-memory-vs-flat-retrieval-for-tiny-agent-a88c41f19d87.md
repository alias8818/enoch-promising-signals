# Operator-Doctrine Memory vs Flat Retrieval for Tiny Agent

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `operator-doctrine-memory-vs-flat-retrieval-for-tiny-agent-a88c41f19d87`
Run ID: `operator-doctrine-memory-vs-flat-retrieval-for-tiny-agent-a88c41f19d87-20260619T082032420365+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8977943e21b7

## What looked useful

Main sweep: layered_doctrine_memory mean accuracy 1.0000 vs flat_retrieval 0.9657, with flat degrading to 0.9216 at noise 0.60 while layered stayed 1.0000. Boundary run with one stable mention: layered 0.9414 vs flat 0.6114, but layered dropped to 0.8359 at noise 0.90, showing the mechanism needs enough stable signal.

## Boundaries and scale limits

No real operator data, no LLM inference, no embedding model, no learned doctrine extractor, and no production tiny-agent loop. Main sweep used 60 synthetic operators, 16 sessions, 8 seeds, and 57,600 decisions per strategy; stress boundary used 24 operators, 4 seeds, and 6,912 decisions per strategy.

## Claim scope

Synthetic repeated-session operator-doctrine recovery with explicit preference labels: a hand-coded layered doctrine memory outperformed flat top-k retrieval under controlled contradictory exception and stale-note noise.

## Why it stopped

Closed as no-paper useful signal: synthetic mechanism evidence supports a bounded advantage but is not production or publication-grade validation.

## Recommended next action

Run a medium confirmation with realistic human-authored replay traces, an LLM or embedding retrieval baseline, and an extractor that must infer doctrine without synthetic event labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium realistic replay confirmation for doctrine memory
- Success threshold: Layered doctrine memory improves adherence accuracy by at least 5 percentage points over flat retrieval and reduces conflict-induced failures by at least 25% on held-out realistic replay tasks.
- Stop condition: Stop if inferred doctrine extraction fails to beat flat retrieval by 2 percentage points or if failure cases show the advantage depends on synthetic-label leakage.

## Evidence references

- Artifact root: `<local-path>/projects/operator-doctrine-memory-vs-flat-retrieval-for-tiny-agent-a88c41f19d87`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
