# Local Compressed-State Distillation Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `local-compressed-state-distillation-pretraining-de588f68c223`
Run ID: `local-compressed-state-distillation-pretraining-de588f68c223-20260620T032902441734+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a49c4c28f6c4

## What looked useful

Compressed-state KD produced a small mean validation-loss improvement over baseline (-0.003531) and logit KD (-0.001698) across three seeds, but did not improve next-token accuracy and is not paper-ready.

## Boundaries and scale limits

Synthetic data only; teacher and students are sub-million-parameter toy transformers; no real corpus, GPT-2-small-class baseline, downstream task, learned compression, long run, or full-hidden-state KD control was tested.

## Claim scope

On a tiny synthetic next-token pretraining probe with latent affine sequence rules, a small student trained with logit KD plus a 16-dimensional random projection of teacher hidden states achieved slightly lower validation loss than baseline LM training across three seeds and lower mean validation loss than logit-only KD.

## Why it stopped

Closed as no-paper useful signal because the result is a toy/synthetic mechanism probe with a small loss-only gain, not direct publication-grade evidence for compressed-state distillation pretraining.

## Recommended next action

Run a bounded real-text deepen test on a small public corpus with matched student parameters, logit KD, compressed-state KD, full-hidden-state KD, and multiple code dimensions; stop if compressed-state KD does not beat logit KD by at least 0.01 validation loss in two of three seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-text bounded test of compressed-state KD versus logit and full-state KD
- Success threshold: Compressed-state KD beats logit-only KD by at least 0.01 validation loss in at least two of three seeds while using no more than one third of the full hidden-state target dimensionality.
- Stop condition: Stop as negative if compressed-state KD fails to beat logit-only KD by 0.01 validation loss in two of three seeds or if gains appear only at full-state-equivalent bandwidth.

## Evidence references

- Artifact root: `<local-path>/projects/local-compressed-state-distillation-pretraining-de588f68c223`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
