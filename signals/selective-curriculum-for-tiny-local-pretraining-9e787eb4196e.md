# Selective Curriculum for Tiny Local Pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `selective-curriculum-for-tiny-local-pretraining-9e787eb4196e`
Run ID: `selective-curriculum-for-tiny-local-pretraining-9e787eb4196e-20260610T120515716564+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/31c701dfcb0a

## What looked useful

Random sampling beat both cheap selective curricula at 20, 300, and 900 steps. At 900 steps, easy_to_hard was worse by +0.0359 validation loss and quality_top was worse by +0.0285 versus random, averaged over 3 paired seeds.

## Boundaries and scale limits

Tested only Wikitext-2 character-token pretraining with a sub-1M-parameter Transformer, 3 seeds, 300-step confirmation and 900-step persistence check. Not tested on BPE tokenization, GPT-2-small-class models, larger corpora, learned data-quality models, or downstream transfer tasks.

## Claim scope

For a tiny character-level Transformer trained on Wikitext-2 under equal token budgets, simple entropy-sorted and entropy/diversity-scored selective curricula did not improve held-out language-model loss over random block ordering.

## Why it stopped

Proxy-scale direct LM pretraining evidence consistently contradicted the simple selective-curriculum hypothesis; this is an early falsification for the tested heuristics, not a full-scale validation of all curriculum methods.

## Recommended next action

Stop this run as a scoped early negative; any next test should use a diversity-preserving selector or learned quality model with the same random-control protocol.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Diversity-preserving selective curriculum for tiny LM pretraining
- Success threshold: Mean held-out validation loss at least 0.01 below random over 3 paired seeds at 900 steps, with no seed worse than random by more than 0.005.
- Stop condition: Stop if the diversity-preserving selector fails to beat random by the success threshold or if exposure-diversity diagnostics show it collapses to a narrow subset of blocks.

## Evidence references

- Artifact root: `<local-path>/projects/selective-curriculum-for-tiny-local-pretraining-9e787eb4196e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
