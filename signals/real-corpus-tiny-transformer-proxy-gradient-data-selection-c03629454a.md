# Real-Corpus Tiny-Transformer Proxy-Gradient Data Selection

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `real-corpus-tiny-transformer-proxy-gradient-data-selection-c03629454a`
Run ID: `real-corpus-tiny-transformer-proxy-gradient-data-selection-c03629454a-20260527T021813432882+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Proxy-Gradient Data Selection for Tiny Pretraining: enoch://control-plane/projects/proxy-gradient-data-selection-for-tiny-pretraining-59d297f9250d/runs/proxy-gradient-data-selection-for-tiny-pretraining-59d297f9250d-20260524T203645855286+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/94333ccb4b8d

## What looked useful

Across seven seeds, proxy-gradient top selection had mean validation loss 2.70854 versus 2.67559 for random candidates, a +0.03295 worse paired difference; top selection beat random in 0/7 seeds.

## Boundaries and scale limits

Tiny byte-level transformer only; WikiText-2 only; short training horizon; microbatch-level gradient scores rather than exact per-example influence; not evidence about GPT-2-small-class or large-scale data selection.

## Claim scope

In a controlled small direct test on WikiText-2 byte-level language modeling with a 2-layer tiny transformer, proxy-gradient top selection did not improve target validation loss over random candidate selection at matched token and optimization budgets.

## Why it stopped

Proxy-gradient top selection failed to beat random in the seven-seed real-corpus tiny-transformer test, so the mechanism is unsupported at the required Tier 1 direct validation level and is not paper-ready.

## Recommended next action

Stop this follow-up as an early direct falsification of the small-scale threshold; only revisit with a medium confirmation that changes the scoring granularity and tokenizer/model scale.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-tiny-transformer-proxy-gradient-data-selection-c03629454a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
