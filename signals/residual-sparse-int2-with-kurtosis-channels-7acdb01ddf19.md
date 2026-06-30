# Residual-Sparse INT2 with Kurtosis Channels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `residual-sparse-int2-with-kurtosis-channels-7acdb01ddf19`
Run ID: `residual-sparse-int2-with-kurtosis-channels-7acdb01ddf19-20260604T224611111258+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/56ed13c59bd9

## What looked useful

Kurtosis-selected residual columns nearly matched oracle residual-energy selection only in the deliberately heavy-tailed synthetic mechanism test. On GPT-2-small activation probes, kurtosis ranked last in 18 of 24 layer/budget conditions and was usually worse than abs-mean, variance, random, and oracle selectors.

## Boundaries and scale limits

No end-to-end perplexity, packed INT2 kernel, serving latency, GPT-2-medium/large, or corpus-scale calibration validation was run. GPT-2 evidence used a small local text calibration set.

## Claim scope

Bounded local probe of residual-sparse INT2 output reconstruction error on synthetic heavy-tail/smooth activations and GPT-2-small layer 0, 5, and 11 attention/MLP projections.

## Why it stopped

Proxy/local early falsification: the original kurtosis-channel hypothesis was not robust on direct GPT-2-small projection reconstruction metrics, though a controlled synthetic mechanism was observed.

## Recommended next action

Stop kurtosis-only validation; run a bounded branch test of abs-mean or calibration residual-energy selectors on GPT-2-small perplexity at matched memory budgets.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Calibration residual-energy selectors for residual-sparse INT2
- Success threshold: At least 10% relative reduction in output NMSE versus random residual columns and no perplexity regression versus the strongest non-oracle baseline at the same effective bit budget.
- Stop condition: Stop if abs-mean/residual-energy selectors fail to beat random by at least 5% relative output NMSE on a majority of tested layers or if perplexity is worse than the strongest simple baseline.

## Evidence references

- Artifact root: `<local-path>/projects/residual-sparse-int2-with-kurtosis-channels-7acdb01ddf19`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
