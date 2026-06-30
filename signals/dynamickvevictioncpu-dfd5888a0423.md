# DynamicKVEvictionCPU

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `dynamickvevictioncpu-dfd5888a0423`
Run ID: `dynamickvevictioncpu-dfd5888a0423-20260523T155635699729+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/d1f0bf117fed

## What looked useful

Across 4 synthetic workloads, 3 cache capacities, and 7 seeds, the dynamic policy never beat the best non-dynamic baseline by retained attention mass. Its best delta versus the best baseline was -0.0302 and worst was -0.2423, failing the +0.0200 success threshold. The failure mode is stale cumulative heavy-hitter preservation rather than excessive CPU overhead.

## Boundaries and scale limits

No real transformer weights, no real inference engine, no perplexity/task-quality metric, and no production KV memory movement were tested. The result is an early proxy falsification of this implemented dynamic heuristic, not a proof that all dynamic KV eviction is non-viable.

## Claim scope

Synthetic CPU-policy simulation of a dynamic KV eviction heuristic using sink tokens, recent tokens, cumulative heavy-hitter scores, and adaptive heavy/recent budget allocation across recency, needle, mixed, and phase-shift attention traces.

## Why it stopped

Proxy early falsification: the implemented dynamic heavy/recent KV eviction policy underperformed simple sliding or sink+recent baselines on every tested synthetic workload and cache budget.

## Recommended next action

Stop this line as no-paper proxy evidence; the concrete next bounded test is to evaluate an age-aware or predictor-based dynamic policy on real small-transformer attention traces before any larger CPU inference implementation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Age-aware dynamic KV eviction on real small-transformer attention traces
- Success threshold: Age-aware dynamic policy improves retained attention mass by at least 0.02 over the best fixed baseline on real model traces for at least two constrained cache budgets without more than 2x heavy_recent policy overhead.
- Stop condition: Stop if age-aware dynamic fails to beat the best fixed baseline by 0.02 on real traces or if policy overhead exceeds 2x heavy_recent without a compensating retained-mass gain.

## Evidence references

- Artifact root: `<local-path>/projects/dynamickvevictioncpu-dfd5888a0423`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
