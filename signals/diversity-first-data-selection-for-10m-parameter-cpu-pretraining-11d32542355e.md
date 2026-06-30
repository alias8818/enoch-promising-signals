# Diversity-First Data Selection for 10M-Parameter CPU Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `diversity-first-data-selection-for-10m-parameter-cpu-pretraining-11d32542355e`
Run ID: `diversity-first-data-selection-for-10m-parameter-cpu-pretraining-11d32542355e-20260608T052943209728+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/c21b4dafbe61

## What looked useful

Diversity-first selection consistently increased rare-domain selected documents by 39-43 over random and improved rare-domain validation NLL by 0.013-0.019, but balanced validation NLL was mixed and near zero versus random.

## Boundaries and scale limits

Not a real-text or transformer validation; does not test tokenizer effects, document quality filtering, long training, larger models, or datacenter-scale pretraining.

## Claim scope

Synthetic 8-domain imbalanced-pool next-token pretraining with a 10M-parameter CPU embedding LM and exact full-softmax validation across three seeds.

## Why it stopped

The bounded synthetic proxy supports rare-domain protection but does not support the broad claim that diversity-first selection improves overall balanced pretraining loss.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should use a small real text corpus and a transformer-like 10M-parameter baseline with tail-domain metrics pre-registered.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-text 10M-parameter diversity-first selection with tail-domain metrics
- Success threshold: Diversity-first improves tail-domain NLL by at least 0.01 versus random in all seeds and does not worsen balanced-average NLL by more than 0.002 on average.
- Stop condition: Stop if diversity-first fails the tail-domain threshold in two seeds or worsens balanced-average NLL by more than 0.005 on average.

## Evidence references

- Artifact root: `<local-path>/projects/diversity-first-data-selection-for-10m-parameter-cpu-pretraining-11d32542355e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
