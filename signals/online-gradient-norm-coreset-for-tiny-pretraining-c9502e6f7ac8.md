# Online Gradient-Norm Coreset for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `online-gradient-norm-coreset-for-tiny-pretraining-c9502e6f7ac8`
Run ID: `online-gradient-norm-coreset-for-tiny-pretraining-c9502e6f7ac8-20260605T042201230706+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/05124460a93a

## What looked useful

The gradient-norm policy actively selected higher-score and higher-loss examples but finished worse than random by mean +0.00957 validation loss (+0.475%) and used about 1.44x wall time. A loss-topk control tied random, suggesting hard-example mining alone was not a reliable gain at this scale.

## Boundaries and scale limits

This does not test exact full-parameter per-example gradient norms, transformer/tokenized corpora, GPT-2-small-class scale, long schedules, or GPU compute-normalized throughput. It is an early bounded falsification of the simple raw top-k proxy formulation.

## Claim scope

In a bounded Tiny Shakespeare character-level GRU pretraining test with 300 updates, 3 seeds, candidate pool 32 selecting 8 examples, raw online top-k selection by an output-layer gradient-norm proxy did not improve held-out validation loss over random online sampling.

## Why it stopped

Proxy early falsification: the direct bounded tiny-pretraining test found no validation-loss advantage for raw online top-k gradient-norm coreset selection and measured material scoring overhead.

## Recommended next action

Stop this formulation as no-paper evidence; only revisit if a transformer/tokenized-corpus study can validate exact or better-calibrated gradient norms under matched scoring-overhead budgets.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/online-gradient-norm-coreset-for-tiny-pretraining-c9502e6f7ac8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
