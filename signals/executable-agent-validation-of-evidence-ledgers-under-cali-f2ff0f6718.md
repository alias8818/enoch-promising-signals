# Executable-agent validation of evidence ledgers under calibrated abstention

Status: `useful_signal`
Project ID: `executable-agent-validation-of-evidence-ledgers-under-cali-f2ff0f6718`
Run ID: `executable-agent-validation-of-evidence-ledgers-under-cali-f2ff0f6718-20260518T143205558744+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f96907f28b2e

## What looked useful

Primary run: executable validator coverage 0.7125, selective accuracy 1.0, false accept rate 0.0, insufficient abstain rate 1.0. Across 10 final replicated seeds: 10/10 passed, mean coverage 0.71875, minimum coverage 0.675, maximum false accept rate 0.0. Calibrated non-executing baseline had 0.0 mean safe coverage; permissive heuristic false-accepted 0.5788 on average.

## Boundaries and scale limits

Tested only generated numeric ledgers with deterministic claim functions: 240 held-out ledgers in the primary run and 10 replicated seeds of 240 test ledgers each. Not tested on natural LLM-authored ledgers, real research artifacts, multi-file provenance, adversarial sandboxing, or external benchmarks.

## Claim scope

In synthetic tabular evidence ledgers with typed executable claims, hash/schema checks plus calibrated abstention achieved safe useful coverage while a non-executing heuristic baseline could only meet the same false-acceptance target by abstaining on all examples.

## Why it stopped

No-paper closure: Tier 1 controlled direct evidence supports the mechanism, but the evidence remains synthetic and narrow rather than publication-grade.

## Recommended next action

Run a medium direct benchmark using LLM-authored evidence ledgers over real public datasets, preserving the executable validator and calibrated abstention policy, before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium benchmark of executable validation on LLM-authored public-data evidence ledgers
- Success threshold: False accept rate <= 0.02, coverage >= 0.55, selective accuracy >= 0.90, and safe coverage at least 0.20 higher than both baselines on the held-out test split.
- Stop condition: Stop if executable validation cannot keep false accepts <= 0.02 at coverage >= 0.55, or if baselines match safe coverage within 0.05.

## Evidence references

- Artifact root: `<local-path>/projects/executable-agent-validation-of-evidence-ledgers-under-cali-f2ff0f6718`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
