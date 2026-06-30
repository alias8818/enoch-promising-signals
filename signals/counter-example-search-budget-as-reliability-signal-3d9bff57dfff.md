# Counter-Example Search Budget as Reliability Signal

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `counter-example-search-budget-as-reliability-signal-3d9bff57dfff`
Run ID: `counter-example-search-budget-as-reliability-signal-3d9bff57dfff-20260611T011530890699+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/cd48ab272cb1

## What looked useful

Uniform search survival reduced miss-weighted mean exact failure rate from 0.046901 at budget 1 to 0.000105 at budget 4096, with mean absolute miss calibration error 0.00769. A biased-away-rare control had much worse calibration error 0.13234 and left 10 faulty candidates with at least 50% survival at budget 4096, showing budget must be reported with the search distribution or coverage model.

## Boundaries and scale limits

Synthetic finite-domain proxy only; no LLM-generated programs, theorem-prover traces, large software systems, or production fuzzing engines were tested. CPU-only run used 32 candidates, budgets up to 4096, and 300 repeated searches per candidate/budget/strategy.

## Claim scope

On finite synthetic Boolean and arithmetic candidate tasks with exact enumerated failure rates, uniform counter-example search survival budget is a useful calibrated reliability signal; the signal is search-distribution-dependent and degrades under biased search that avoids rare failure regions.

## Why it stopped

Synthetic proxy evidence supports the mechanism under matched search and falsifies distribution-agnostic budget reliability, but it is not direct/full validation.

## Recommended next action

Stop this worker run as no-paper useful signal; next bounded test should evaluate survival-budget calibration on real LLM-generated candidate programs with property-based or fuzzing counter-example search and held-out failure-rate estimates.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrate counter-example search budget on LLM-generated candidate programs
- Success threshold: Survival budget plus coverage/search-distribution features should improve held-out failure-rate ranking or calibration over unit-test pass count alone by at least 20% relative error reduction on a predeclared metric.
- Stop condition: Stop if budget survival is not monotonic with held-out failure rate on real generated candidates, or if coverage features fail to explain calibration failures better than unit-test pass count.

## Evidence references

- Artifact root: `<local-path>/projects/counter-example-search-budget-as-reliability-signal-3d9bff57dfff`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
