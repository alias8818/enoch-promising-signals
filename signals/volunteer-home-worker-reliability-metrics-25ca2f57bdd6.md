# Volunteer Home Worker Reliability Metrics

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `volunteer-home-worker-reliability-metrics-25ca2f57bdd6`
Run ID: `volunteer-home-worker-reliability-metrics-25ca2f57bdd6-20260609T114715031281+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/11af1c80a1bf

## What looked useful

Top-10% worker ranking improved future task success from about 25% overall to 71-73% in both dense and sparse synthetic regimes. Historical success was slightly best with 24 training attempts per worker; uptime and the task-aware composite were stronger in the 4-attempt sparse-history condition.

## Boundaries and scale limits

Synthetic-only evidence; no real BOINC/SETI@home/FTA trace was evaluated because the public FTA endpoint timed out from this worker. The simulator has hourly availability resolution, simplified task execution, and fixed metric weights.

## Claim scope

In a deterministic synthetic volunteer home compute simulator with 2,000 workers, 28 simulated days, and held-out future tasks, training-derived reliability metrics predict future task success substantially better than random ranking; simple historical success is best with dense task history, while uptime/task-aware metrics are best or close to best with sparse task history.

## Why it stopped

Synthetic proxy produced a useful mechanism signal but does not provide direct real-world validation or publication-grade evidence.

## Recommended next action

Stop this run as synthetic no-paper evidence; the concrete next action is to repeat the same held-out metric comparison on real FTA SETI@home traces or BOINC worker logs.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Validate volunteer worker reliability metrics on real availability traces
- Success threshold: Task-aware metric improves top-10% future task completion by at least 5 percentage points or 10% relative lift over the best simple baseline in sparse-history workers, without losing more than 2 percentage points in dense-history workers.
- Stop condition: Stop if real traces cannot be obtained or if task-aware ranking fails to beat the best simple baseline under both sparse-history and dense-history splits.

## Evidence references

- Artifact root: `<local-path>/projects/volunteer-home-worker-reliability-metrics-25ca2f57bdd6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
