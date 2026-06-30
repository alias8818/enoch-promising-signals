# Long-Context Evidence Refresh Policy

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `long-context-evidence-refresh-policy-f4c6bda15afc`
Run ID: `long-context-evidence-refresh-policy-f4c6bda15afc-20260611T053201911434+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/eb94e1342f57

## What looked useful

Final 20-seed sweep showed hazard_risk_0.45_compact accuracy 0.9492 at refresh rate 0.8377 versus ttl_75_compact accuracy 0.9306 at refresh rate 0.8467; hazard_risk_0.25_compact reached 0.9747 accuracy at refresh rate 0.9089, close to ttl_25_compact accuracy 0.9751 at refresh rate 0.9433. Non-compacting variants had conflict rates above 0.49 and much lower accuracy.

## Boundaries and scale limits

No real LLM, real retriever, production traces, or real timestamped QA corpus were tested; answer behavior and fact-change distributions were simulated.

## Claim scope

In a deterministic synthetic long-context evidence-cache benchmark with mutable facts, entity-level compaction after refresh is the dominant mechanism for reducing stale-answer errors, and hazard-aware compact refresh gives a better accuracy/refresh tradeoff than compact fixed TTL at comparable refresh rates.

## Why it stopped

Closed as no-paper useful signal because the result is synthetic/proxy evidence and the hypothesis is mixed rather than publication-grade direct validation.

## Recommended next action

Run a bounded real-LLM deepen test using timestamped mutable QA items, comparing compact TTL and compact hazard-aware policies at matched refresh budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-LLM Timestamped QA Test for Evidence Refresh and Compaction
- Success threshold: At matched refresh rate within +/- 2 percentage points, compact hazard-aware refresh reduces stale-answer rate by at least 20% relative to the best compact TTL baseline with non-overlapping seed/bootstrap uncertainty.
- Stop condition: Stop if compact hazard-aware refresh fails to beat compact TTL on stale-answer rate at matched refresh budget, or if compaction alone explains the improvement.

## Evidence references

- Artifact root: `<local-path>/projects/long-context-evidence-refresh-policy-f4c6bda15afc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
