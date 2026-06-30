# Byzantine-robust aggregator benchmark under realistic volunteer failure modes

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `byzantine-robust-aggregator-benchmark-under-realistic-volunteer-failure-modes-0457f08eeeb1`
Run ID: `byzantine-robust-aggregator-benchmark-under-realistic-volunteer-failure-modes-0457f08eeeb1-20260619T154302040995+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8d7f05af6eeb

## What looked useful

Median-style robust aggregators handled static Byzantine sign-flip attacks, but several became unstable when Byzantine updates were combined with volunteer dropout, stale updates, and non-IID data. Krum was the most stable under the two mixed volunteer scenarios, while being worse in clean and static-Byzantine settings.

## Boundaries and scale limits

No real volunteer traces, no real federated dataset, no deep model, no production asynchronous protocol, and no large-scale multi-node validation. CUDA was available but this was a small local benchmark.

## Claim scope

Synthetic logistic-regression federated benchmark with 80 clients, 6 seeds, 90 rounds, 20% Byzantine clients, and controlled volunteer dropout, staleness, and non-IID client data.

## Why it stopped

Synthetic bounded evidence is useful but insufficient for a paper; the result is a scoped benchmark signal, not full validation under real volunteer systems.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should replay realistic availability/staleness traces on a real federated dataset and check whether Krum's mixed-failure stability persists.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-driven volunteer Byzantine aggregation on a real federated dataset
- Success threshold: Krum or a trace-aware variant must reduce final loss by at least 25% versus the next best robust aggregator in mixed volunteer+Byzantine scenarios without losing more than 10% relative accuracy in clean or Byzantine-only controls.
- Stop condition: Stop if Krum's advantage disappears after learning-rate tuning, if all robust aggregators converge similarly under traces, or if runtime cost dominates the stability benefit for the tested client counts.

## Evidence references

- Artifact root: `<local-path>/projects/byzantine-robust-aggregator-benchmark-under-realistic-volunteer-failure-modes-0457f08eeeb1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
