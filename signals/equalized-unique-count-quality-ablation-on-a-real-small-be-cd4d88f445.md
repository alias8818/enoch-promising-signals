# Equalized unique-count quality ablation on a real small benchmark

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `equalized-unique-count-quality-ablation-on-a-real-small-be-cd4d88f445`
Run ID: `equalized-unique-count-quality-ablation-on-a-real-small-be-cd4d88f445-20260629T091053551100+0000`

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

- Parent run decision: Dataset quality benchmark for generalized understanding beyond scale: enoch://control-plane/projects/frontier-dataset-quality-generalized-understanding-benchmark-20260628/runs/frontier-dataset-quality-generalized-understanding-benchmark-20260628-20260629T064245391541+0000
- Parent run decision: Factorized quality ablation with equalized unique-example count: enoch://control-plane/projects/factorized-quality-ablation-with-equalized-unique-example-14a9eb3fb4/runs/factorized-quality-ablation-with-equalized-unique-example-14a9eb3fb4-20260629T085446323130+0000

## What looked useful

Moderate temperature produced more unique answers and better raw/oracle metrics than low temperature, but its equalized unique pass@1/pass@2 advantage over low temperature was small with bootstrap intervals crossing zero; high temperature produced still more unique answers but worse equalized quality than moderate temperature.

## Boundaries and scale limits

Small fixed-order benchmark slice, one small model, one seed schedule, numeric-answer extraction only, finite candidate pools, and no stronger-model or multi-benchmark replication.

## Claim scope

On 30 GSM8K test problems using cached Qwen/Qwen2.5-0.5B-Instruct with 12 stochastic samples per problem for three temperature settings, raw and unique-oracle quality differences are partly confounded by the number of unique extracted numeric answers; equalized unique pass@1/pass@2 substantially shrinks the temp_0_7 versus temp_0_2 advantage.

## Why it stopped

Current run provides useful small-benchmark evidence but is not paper-ready because it uses only 30 problems and one small model.

## Recommended next action

Run a bounded deepen follow-up on 100-200 GSM8K examples with Qwen2.5-1.5B or Qwen2.5-3B, preserving the same equalized unique-count metrics and bootstrap intervals.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Equalized unique-count ablation with a stronger small model on 100-200 GSM8K problems
- Success threshold: The moderate-temperature raw/oracle advantage over low temperature shrinks by at least 50% under equalized unique pass@1/pass@2, with paired bootstrap intervals excluding a raw-sized equalized effect.
- Stop condition: Stop if stronger-model generation cannot complete within a bounded local run or if equalized unique pass@1/pass@2 preserves the raw advantage within 20%, indicating unique-count equalization is not explaining the effect.

## Evidence references

- Artifact root: `<local-path>/projects/equalized-unique-count-quality-ablation-on-a-real-small-be-cd4d88f445`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
